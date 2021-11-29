"""
https://leetcode-cn.com/problems/number-of-equivalent-domino-pairs/

给你一个由一些多米诺骨牌组成的列表 dominoes。

如果其中某一张多米诺骨牌可以通过旋转 0 度或 180 度得到另一张多米诺骨牌，我们就认为这两张牌是等价的。

形式上，dominoes[i] = [a, b] 和 dominoes[j] = [c, d] 等价的前提是 a==c 且 b==d，或是 a==d 且 b==c。

在 0 <= i < j < dominoes.length 的前提下，找出满足 dominoes[i] 和 dominoes[j] 等价的骨牌对 (i, j) 的数量。

示例：
    输入：dominoes = [[1,2],[2,1],[3,4],[5,6]]
    输出：1

提示：
    1 <= dominoes.length <= 40000
    1 <= dominoes[i][j] <= 9

"""
from typing import List
import collections

'''用字典存储特定多米诺骨牌的个数'''
class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        dict = collections.defaultdict(int)
        res = 0
        for i, j in dominoes:
            res += dict [(i, j)]
            if i != j:
                res += dict [(j, i)]
            dict [(i, j)] += 1
        return res


'''用一个两位数代表每一张多米诺骨牌，用数组来存储骨牌的状态'''
class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        num = [0] * 100             # 无需使用哈希表统计元素数量，而直接使用长度为 100100 的数组即可。
        res = 0
        for x, y in dominoes:
            if x <= y:              # e.g. [1,2]
                val = x * 10 + y    # 12
            if x > y:               # e.g. [2,1]
                val = y * 10 + x    # 12
            res += num[val]
            num[val] += 1
        return res
    
if __name__ == "__main__":
    dominoes = [[1,2],[2,1],[3,4],[5,6]]
    sol = Solution()
    result = sol.numEquivDominoPairs(dominoes)
    print(result)