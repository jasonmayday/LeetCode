"""
https://leetcode-cn.com/problems/min-cost-climbing-stairs/

数组的每个下标作为一个阶梯，第 i 个阶梯对应着一个非负数的体力花费值 cost[i]（下标从 0 开始）。

每当你爬上一个阶梯你都要花费对应的体力值，一旦支付了相应的体力值，你就可以选择向上爬一个阶梯或者爬两个阶梯。

请你找出达到楼层顶部的最低花费。在开始时，你可以选择从下标为 0 或 1 的元素作为初始阶梯。

示例 1：
    输入：cost = [10, 15, 20]
    输出：15
    解释：最低花费是从 cost[1] 开始，然后走两步即可到阶梯顶，一共花费 15 。

示例 2：
    输入：cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    输出：6
    解释：最低花费方式是从 cost[0] 开始，逐个经过那些 1 ，跳过 cost[3] ，一共花费 6 。

提示：
    cost 的长度范围是 [2, 1000]。
    cost[i] 将会是一个整型数据，范围为 [0, 999] 。

"""
from typing import List
# https://leetcode-cn.com/problems/min-cost-climbing-stairs/solution/yi-bu-yi-bu-tui-dao-dong-tai-gui-hua-de-duo-chong-/

"""解法1"""
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        minCost = [0] * n
        minCost[1] = min(cost[0], cost[1])
        for i in range(2, n):
            minCost[i] = min(minCost[i - 1] + cost[i], minCost[i - 2] + cost[i - 1])
            # 第0级台阶： minCost[0] = min(cost[-1], cost[0]) = min(0, cost[0]) = 0
            # 第1级台阶： minCost[1] = min(cost[0], cost[1])
        return minCost[-1]

"""解法2"""
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0] * n
        dp[0], dp[1] = cost[0], cost[1]
        # 踏上第i级台阶有两种方法：
            # 1. 先踏上第i-2级台阶（最小总花费dp[i-2]），再直接迈两步踏上第i级台阶（花费cost[i]），最小总花费dp[i-2] + cost[i]；
            # 2. 先踏上第i-1级台阶（最小总花费dp[i-1]），再迈一步踏上第i级台阶（花费cost[i]），最小总花费dp[i-1] + cost[i]；
        # 则dp[i]是上面这两个最小总花费中的最小值。
        for i in range(2, n):
            dp[i] = min(dp[i - 2], dp[i - 1]) + cost[i]
        return min(dp[-2], dp[-1])


if __name__ == "__main__":
    cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    sol = Solution()
    result = sol.minCostClimbingStairs(cost)
    print(result)