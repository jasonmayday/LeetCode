"""
https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

给定一个整数数组prices，其中第  prices[i] 表示第 i 天的股票价格 。​

设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）:

    卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。

注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

示例 1:
    输入: prices = [1,2,3,0,2]
    输出: 3
    解释: 对应的交易状态为: [买入, 卖出, 冷冻期, 买入, 卖出]

示例 2:
    输入: prices = [1]
    输出: 0

提示：
    1 <= prices.length <= 5000
    0 <= prices[i] <= 1000

"""
from typing import List

""" 方法一：动态规划
    三种不同的状态：
    状态0. f[i][0]: 手上持有股票的最大收益
    状态1. f[i][1]: 手上不持有股票，并且处于冷冻期中的累计最大收益
    状态2. f[i][2]: 手上不持有股票，并且不在冷冻期中的累计最大收益 """

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        n = len(prices)

        # 初始化dp，假设第 0 天买入
        # [[-1, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
        dp = [[-prices[0], 0, 0]] + [[0] * 3 for _ in range(n - 1)]

        for i in range(1, n):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][2] - prices[i])  # 比较：[前一天手上持有股票(状态0)] and [前一天状态2，当天买入变为状态0]
            dp[i][1] = dp[i - 1][0] + prices[i]                     # 必然是前一天卖出了才导致今天冷冻，从前一天的状态转移0 到 今天的状态1
            dp[i][2] = max(dp[i - 1][1], dp[i - 1][2])              # 比较：[前一天不在冷冻期(状态2)] and [前一天在冷冻期且今天解冻(状态1到状态2)]

        return max(dp[n - 1][1], dp[n - 1][2])  # 最后一定是手里没有股票赚的钱最多，因此最后返回 dp1 和 dp2 的最大值

if __name__ == "__main__":
    prices = [1,2,3,0,2]
    sol = Solution()
    result = sol.maxProfit(prices)
    print (result)
