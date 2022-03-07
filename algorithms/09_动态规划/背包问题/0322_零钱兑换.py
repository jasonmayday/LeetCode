"""
https://leetcode-cn.com/problems/coin-change/

给你一个整数数组 coins ，表示不同面额的硬币；以及一个整数 amount ，表示总金额。

计算并返回可以凑成总金额所需的 最少的硬币个数 。如果没有任何一种硬币组合能组成总金额，返回 -1 。

你可以认为每种硬币的数量是无限的。

示例 1：
    输入：coins = [1, 2, 5], amount = 11
    输出：3
    解释：11 = 5 + 5 + 1

示例 2：
    输入：coins = [2], amount = 3
    输出：-1

示例 3：
    输入：coins = [1], amount = 0
    输出：0

提示：
    1 <= coins.length <= 12
    1 <= coins[i] <= 2^31 - 1
    0 <= amount <= 10^4

"""
from typing import List

""" 动态规划 """
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1]*(amount + 1)
        dp[0] = 0   # dp[j]：凑足总额为j所需钱币的最少个数为dp[j]
        for coin in coins:
            for j in range(coin, amount + 1):
                dp[j] = min(dp[j], dp[j - coin] + 1)
        return dp[amount] if dp[amount] < amount + 1 else -1
'''
F(0) = 1
F(1) = 1
F(2) = 1
F(3) = 2
F(4) = 2
F(5) = 2

'''
if __name__ == "__main__":
    coins = [1, 2, 5]
    amount = 11
    sol = Solution()
    result = sol.coinChange(coins, amount)
    print (result)