"""
https://leetcode-cn.com/problems/x-of-a-kind-in-a-deck-of-cards/

给定一副牌，每张牌上都写着一个整数。

此时，你需要选定一个数字 X，使我们可以将整副牌按下述规则分成 1 组或更多组：
    每组都有 X 张牌。
    组内所有的牌上都写着相同的整数。

仅当你可选的 X >= 2 时返回 true。

示例 1：
    输入：[1,2,3,4,4,3,2,1]
    输出：true
    解释：可行的分组是 [1,1]，[2,2]，[3,3]，[4,4]

示例 2：
    输入：[1,1,1,2,2,2,3,3]
    输出：false
    解释：没有满足要求的分组。

示例 3：
    输入：[1]
    输出：false
    解释：没有满足要求的分组。

示例 4：
    输入：[1,1]
    输出：true
    解释：可行的分组是 [1,1]

示例 5：
    输入：[1,1,2,2,2,2]
    输出：true
    解释：可行的分组是 [1,1]，[2,2]，[2,2]

提示：
    1 <= deck.length <= 10000
    0 <= deck[i] < 10000
    
"""
from math import gcd
from collections import Counter
from functools import reduce

class Solution:
    def hasGroupsSizeX(self, deck):
        vals = Counter(deck).values()   # Counter统计字符串（数字）种类及数量，返回字典
        return reduce(gcd, vals) >= 2   # math.gcd求两个数的最大公约数，返回整数
                                        # functools.reduce 逐次对上次函数结果与当前序列元素应用函数；
                                        # reduce(function, sequence)
                                        # 例如 reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) 计算为((((1+2)+3)+4)+5)
                                        
class Solution:
    def hasGroupsSizeX(self, deck):
        def gcd(a, b):
            if b == 0: return a
            return gcd(b, a % b)
        return reduce(gcd, Counter(deck).values()) > 1

if __name__ == "__main__":
    deck = [1,1,2,2,2,2]
    sol = Solution()
    result = sol.hasGroupsSizeX(deck)
    print (result)