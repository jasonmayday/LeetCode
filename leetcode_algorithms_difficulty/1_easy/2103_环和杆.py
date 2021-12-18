"""
https://leetcode-cn.com/problems/rings-and-rods/

总计有 n 个环，环的颜色可以是红、绿、蓝中的一种。这些环分布穿在 10 根编号为 0 到 9 的杆上。

给你一个长度为 2n 的字符串 rings ，表示这 n 个环在杆上的分布。rings 中每两个字符形成一个 颜色位置对 ，用于描述每个环：
    第 i 对中的 第一个 字符表示第 i 个环的 颜色（'R'、'G'、'B'）。
    第 i 对中的 第二个 字符表示第 i 个环的 位置，也就是位于哪根杆上（'0' 到 '9'）。

例如，"R3G2B1" 表示：共有 n == 3 个环，红色的环在编号为 3 的杆上，绿色的环在编号为 2 的杆上，蓝色的环在编号为 1 的杆上。

找出所有集齐 全部三种颜色 环的杆，并返回这种杆的数量。

示例 1：
    输入：rings = "B0B6G0R6R0R6G9"
    输出：1
    解释：
        - 编号 0 的杆上有 3 个环，集齐全部颜色：红、绿、蓝。
        - 编号 6 的杆上有 3 个环，但只有红、蓝两种颜色。
        - 编号 9 的杆上只有 1 个绿色环。
        因此，集齐全部三种颜色环的杆的数目为 1 。

示例 2：
    输入：rings = "B0R0G0R9R0B0G0"
    输出：1
    解释：
        - 编号 0 的杆上有 6 个环，集齐全部颜色：红、绿、蓝。
        - 编号 9 的杆上只有 1 个红色环。
        因此，集齐全部三种颜色环的杆的数目为 1 。

示例 3：
    输入：rings = "G4"
    输出：0
    解释：
        只给了一个环，因此，不存在集齐全部三种颜色环的杆。

提示：
    rings.length == 2 * n
    1 <= n <= 100
    如 i 是 偶数 ，则 rings[i] 的值可以取 'R'、'G' 或 'B'（下标从 0 开始计数）
    如 i 是 奇数 ，则 rings[i] 的值可以取 '0' 到 '9' 中的一个数字（下标从 0 开始计数）

"""
from collections import defaultdict

"""解法：维护每根杆的状态"""
class Solution:
    def countPoints(self, rings: str) -> int:
        n = len(rings)
        status = [0] * 10           # 状态数组
        for i in range(0, n, 2):    # 遍历颜色位置对维护状态数组
            pos = int(rings[i+1])   # pos为环的位置，为每个圆环颜色的下一位
            if rings[i] == 'R':
                status[pos] |= 1
            elif rings[i] == 'G':
                status[pos] |= 2
            elif rings[i] == 'B':
                status[pos] |= 4
        res = 0
        for i in range(10):         # 统计集齐三色环的杆的数量
            if status[i] == 7:
                res += 1
        return res

"""解法：字典"""
class Solution:
    def countPoints(self, rings: str) -> int:
        dict = {}   # 存放 {杆: (环)} {pos: ring} 的字典
        n = len(rings)
        for i in range(0, n, 2):
            ring = rings[i]             # 环
            pos = int(rings[i+1])       # 杆的位置
            if pos in dict:             # 如果有环在杆上
                dict[pos].add(ring)     # 把 {pos: ring} 加入字典
            else:                       # 如果还没有环在当前杆上
                dict[pos] = set(ring)   # 创建一个值为set类的字典值，用于过滤之后出现的重复颜色元素
        count = 0
        for pos, ring in dict.items():
            if len(ring) == 3:
                count += 1
        return count

class Solution:
    def countPoints(self, rings: str) -> int:
        dic = defaultdict(set)
        for i in range(len(rings))[::2]:
            dic[rings[i+1]].add(rings[i])
        return sum([1 for i in dic.values() if len(i)==3])

if __name__ == "__main__":
    rings = "B0B6G0R6R0R6G9"
    sol = Solution()
    result = sol.countPoints(rings)
    print (result)  