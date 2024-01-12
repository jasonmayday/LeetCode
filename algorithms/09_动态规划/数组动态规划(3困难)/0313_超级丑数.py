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

"""方法一：动态规划"""
class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        dp = [0] * (n + 1)  # dp[i] 表示第 ii 个超级丑数
        m = len(primes)
        pointers = [0] * m  # 创建与数组 primes 相同长度的数组 pointers，表示下一个超级丑数是当前指针指向的超级丑数乘以对应的质因数。
        nums = [1] * m

        for i in range(1, n + 1):
            min_num = min(nums)
            dp[i] = min_num
            for j in range(m):
                if nums[j] == min_num:
                    pointers[j] += 1
                    nums[j] = dp[pointers[j]] * primes[j]
        return dp[n]

"""方法一：动态规划"""
class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        m = len(primes)
        dp = [float('inf')] * (n)   # dp[i] 代表第 i+1 个丑数
        dp[0] = 1                   # 最小的超级丑数是 1
        indexes = [0] * m           # indexes代表每个质因子现在应该跟哪个丑数相乘

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