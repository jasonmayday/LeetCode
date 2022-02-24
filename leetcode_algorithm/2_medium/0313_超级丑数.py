"""
https://leetcode-cn.com/problems/super-ugly-number/

超级丑数 是一个正整数，并满足其所有质因数都出现在质数数组 primes 中。

给你一个整数 n 和一个整数数组 primes ，返回第 n 个 超级丑数 。

题目数据保证第 n 个 超级丑数 在 32-bit 带符号整数范围内。

示例 1：
    输入：n = 12, primes = [2,7,13,19]
    输出：32
    解释：给定长度为 4 的质数数组 primes = [2,7,13,19]，前 12 个超级丑数序列为：[1,2,4,7,8,13,14,16,19,26,28,32] 。

示例 2：
    输入：n = 1, primes = [2,3,5]
    输出：1
    解释：1 不含质因数，因此它的所有质因数都在质数数组 primes = [2,3,5] 中。

提示：
    1 <= n <= 10^6
    1 <= primes.length <= 100
    2 <= primes[i] <= 1000
    题目数据 保证 primes[i] 是一个质数
    primes 中的所有值都 互不相同 ，且按 递增顺序 排列

"""
from typing import List

class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        m = len(primes)
        # dp[i] 代表第i+1个丑数
        dp = [inf] * n
        dp[0] = 1
        # indexes代表每个质因子现在应该跟哪个丑数相乘
        indexes = [0] * m

        for i in range(1, n):
            # 哪个质因子相乘的丑数将会变化
            changeIndex = 0
            for j in range(m):
                # 如果当前质因子乘它的丑数小于当前的丑数，更新当前丑数并更新变化坐标
                if primes[j] * dp[indexes[j]] < dp[i]:
                    changeIndex = j
                    dp[i] = primes[j] * dp[indexes[j]]
                # 如果相等直接变化，这样可以去重复
                elif primes[j] * dp[indexes[j]] == dp[i]:
                    indexes[j] += 1
            # 变化的坐标+1
            indexes[changeIndex] += 1
        return dp[-1]


if __name__ == "__main__":
    n = 12
    primes = [2,7,13,19]
    sol = Solution()
    result = sol.nthSuperUglyNumber(n, primes)
    print (result)