'''
https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/

给定一个数组 prices ，它的第 i 个元素 prices[i] 表示一支给定股票第 i 天的价格。

你只能选择 某一天 买入这只股票，并选择在 未来的某一个不同的日子 卖出该股票。设计一个算法来计算你所能获取的最大利润。

返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 0 。

示例 1：
    输入：[7,1,5,3,6,4]
    输出：5
    解释：在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
    注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格；同时，你不能在买入前卖出股票。

示例 2：
    输入：prices = [7,6,4,3,1]
    输出：0
    解释：在这种情况下, 没有交易完成, 所以最大利润为 0。
 

提示：
    1 <= prices.length <= 10^5
    0 <= prices[i] <= 10^4

'''
from typing import List

"""遍历一遍数组，计算每次 到当天为止 的最小股票价格和最大利润。"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprice = float('inf')
        maxprofit = 0
        for price in prices:
            minprice = min(minprice, price)
            maxprofit = max(maxprofit, price - minprice)
        return maxprofit

"""动态规划
   dp[i] 表示前 i 天的最大利润，因为我们始终要使利润最大化，则：
   dp[i] = max(dp[i-1], prices[i]-minprice)
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 0: 
            return 0    # 边界条件
        dp = [0] * n    # 创建动态规划计算表
        minprice = prices[0] 

        for i in range(1, n):
            minprice = min(minprice, prices[i])
            dp[i] = max(dp[i - 1], prices[i] - minprice)

        return dp[-1]


if __name__ == "__main__":
    prices = [7,1,5,3,6,4]
    sol = Solution()
    result = sol.maxProfit(prices)
    print(result)