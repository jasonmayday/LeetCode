"""
假设你是一位很棒的家长，想要给你的孩子们一些小饼干。但是，每个孩子最多只能给一块饼干。

对每个孩子 i，都有一个胃口值 g[i]，这是能让孩子们满足胃口的饼干的最小尺寸；并且每块饼干 j，都有一个尺寸 s[j] 。
如果 s[j] >= g[i]，我们可以将这个饼干 j 分配给孩子 i ，这个孩子会得到满足。
你的目标是尽可能满足越多数量的孩子，并输出这个最大数值。

示例 1:
    输入: g = [1,2,3], s = [1,1]
    输出: 1
    解释: 
    你有三个孩子和两块小饼干，3个孩子的胃口值分别是：1,2,3。
    虽然你有两块小饼干，由于他们的尺寸都是1，你只能让胃口值是1的孩子满足。
    所以你应该输出1。

示例 2:
    输入: g = [1,2], s = [1,2,3]
    输出: 2
    解释: 
    你有两个孩子和三块小饼干，2个孩子的胃口值分别是1,2。
    你拥有的饼干数量和尺寸都足以让所有孩子满足。
    所以你应该输出2.

提示：
    1 <= g.length <= 3 * 10^4
    0 <= s.length <= 3 * 10^4
    1 <= g[i], s[j] <= 2^31 - 1

"""
from typing import List

""" 贪心算法 """
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()    # 把 greed, size 排序，从前往后遍历
        s.sort()
        count = 0   # 用来保存分了几个人
        greed = 0
        cookie = 0   
        
        while greed < len(g) and cookie < len(s):
            if g[greed] <= s[cookie]:
                count += 1      # 可以满足胃口，把小饼干喂给小朋友，计数值+1
                greed += 1      # 就继续往后遍历 小朋友
                cookie += 1     # 接续遍历 饼干
            else:
                cookie += 1     # 不满足胃口，查看下一块小饼干
        return count

""" 贪心算法 """
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        res = 0
        for i in range(len(s)):
            if res < len(g) and s[i] >= g[res]:  # 小饼干先喂饱小胃口
                res += 1
        return res

''' 双指针 '''
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        r_g = len(g) - 1    # 两个指针分别指向两个列表的末尾
        r_s = len(s) - 1
        count = 0
        while r_g >= 0 and r_s >= 0:    # 循环条件
            if s[r_s] >= g[r_g]:        # 两个指针分别指向两个列表的末尾如果满足`s[r_s] >= g[r_g]`，则都向前移动
                count += 1
                r_g -= 1
                r_s -= 1
            else:           # 否则只需要移动g的指针
                r_g -= 1
        return count

if __name__ == "__main__":
    greed = [1,2]
    size = [1,2,3]
    sol = Solution()
    result = sol.findContentChildren(greed, size)
    print(result)