"""
https://leetcode-cn.com/problems/the-number-of-weak-characters-in-the-game/

你正在参加一个多角色游戏，每个角色都有两个主要属性：攻击 和 防御 。给你一个二维整数数组 properties ，其中 properties[i] = [attacki, defensei] 表示游戏中第 i 个角色的属性。

如果存在一个其他角色的攻击和防御等级 都严格高于 该角色的攻击和防御等级，则认为该角色为 弱角色 。更正式地，如果认为角色 i 弱于 存在的另一个角色 j ，那么 attackj > attacki 且 defensej > defensei 。

返回 弱角色 的数量。

示例 1：
    输入：properties = [[5,5],[6,3],[3,6]]
    输出：0
    解释：不存在攻击和防御都严格高于其他角色的角色。

示例 2：
    输入：properties = [[2,2],[3,3]]
    输出：1
    解释：第一个角色是弱角色，因为第二个角色的攻击和防御严格大于该角色。

示例 3：
    输入：properties = [[1,5],[10,4],[4,3]]
    输出：1
    解释：第三个角色是弱角色，因为第二个角色的攻击和防御严格大于该角色。

提示：
    2 <= properties.length <= 10^5
    properties[i].length == 2
    1 <= attacki, defensei <= 10^5

"""
from typing import List

""" 排序 + 指针 """
class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key = lambda x: (x[0], -x[1]))  # 攻击力按小到大排，然后防御力按大到小排
        res = 0                                         # [[1,6], [1,5], [4,3], [9,4]]
        max_defense = -1
        for attack, defense in properties[::-1]:    # 然后遍历的时候再倒过来，这时候，变成攻击力大到小，防御力小到大. [[9, 4], [4, 3], [1, 5], [1, 6]]
            if max_defense > defense:               # 防御力从小到大反方向排序，意味着如果出现攻击力相同的，比如 [1, 5], [1, 6]]，就直接可以省略判断攻击力是否相等，这时只需要比较 defense
                res += 1                            # 遍历过程中，如果当前最大的 defense 大于 右边的 defense，答案加一
            max_defense = max(max_defense, defense)
        return res
    
""" 单调栈 """
class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key = lambda x: (x[0], -x[1]))  # 攻击力按小到大排，然后防御力按大到小排
        ans = 0                                         # [[1,6], [1,5], [4,3], [9,4]]
        stack = []
        for attack, defense in properties:          # 按照角色攻击值 从低到高 依次遍历每个元素
            while stack and stack[-1] < defense:    # 遍历时如果发现栈顶的角色 p 的防御值小于当前的角色 q 的防御值
                stack.pop()
                ans += 1                            # 则可以认为找到攻击值和防御值都严格大于 p 的角色 q
            stack.append(defense)
        return ans

if __name__ == "__main__":
    properties = [[1,5],[1,6],[9,4],[4,3]]
    sol = Solution()
    result = sol.numberOfWeakCharacters(properties)
    print(result)