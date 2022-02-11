"""
https://leetcode-cn.com/problems/simplified-fractions/

给你一个整数 n ，请你返回所有 0 到 1 之间（不包括 0 和 1）满足分母小于等于  n 的 最简 分数 。分数可以以 任意 顺序返回。

示例 1：
    输入：n = 2
    输出：["1/2"]
    解释："1/2" 是唯一一个分母小于等于 2 的最简分数。

示例 2：
    输入：n = 3
    输出：["1/2","1/3","2/3"]

示例 3：
    输入：n = 4
    输出：["1/2","1/3","1/4","2/3","3/4"]
    解释："2/4" 不是最简分数，因为它可以化简为 "1/2" 。

示例 4：
    输入：n = 1
    输出：[]

提示：
    1 <= n <= 100

"""
from typing import List
from math import gcd

""" nu: numerator   分子
    ————————————————————
    de: denominator 分母
"""


""" 解法1: gcd 最大公约数函数 """
class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        return [f"{nu}/{de}" for de in range(2, n + 1) for nu in range(1, de) if gcd(de, nu) == 1]


class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        res = []
        for fenmu in range(2, n + 1):
            for fenzi in range(1, fenmu):
                if gcd(fenzi, fenmu) == 1:
                    res.append(str(fenzi) + '/' + str(fenmu))
        return res


""" 解法2: 根据数值大小和集合去重"""
class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        res = []
        values = set()   
        for fenmu in range(2, n + 1):
            for fenzi in range(1, fenmu):
                value = fenzi / fenmu
                if value not in values:  # 如果按照分母和分子都从小到大遍历, 每次最先遇到的都是最简形式, 因为假如不是最简的话一定有一个更小的分母分子组合有相同数值在之前被遍历
                    values.add(value)    # 所以可以将每个分数值存入集合中, 然后从小到大遍历并判断该分数是否已经存在即可, 没存在的话加入最终结果中, 否则不加
                    res.append(str(fenzi) + '/' + str(fenmu))
        return res

if __name__ == "__main__":
    n = 4
    sol = Solution()
    result = sol.simplifiedFractions(n)
    print(result) 