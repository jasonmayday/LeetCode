"""
https://leetcode-cn.com/problems/maximum-points-you-can-obtain-from-cards/

几张卡牌 排成一行，每张卡牌都有一个对应的点数。点数由整数数组 cardPoints 给出。

每次行动，你可以从行的开头或者末尾拿一张卡牌，最终你必须正好拿 k 张卡牌。

你的点数就是你拿到手中的所有卡牌的点数之和。

给你一个整数数组 cardPoints 和整数 k，请你返回可以获得的最大点数。

示例 1：
    输入：cardPoints = [1,2,3,4,5,6,1], k = 3
    输出：12
    解释：第一次行动，不管拿哪张牌，你的点数总是 1 。但是，先拿最右边的卡牌将会最大化你的可获得点数。最优策略是拿右边的三张牌，最终点数为 1 + 6 + 5 = 12 。

示例 2：
    输入：cardPoints = [2,2,2], k = 2
    输出：4
    解释：无论你拿起哪两张卡牌，可获得的点数总是 4 。

示例 3：
    输入：cardPoints = [9,7,7,9,7,7,9], k = 7
    输出：55
    解释：你必须拿起所有卡牌，可以获得的点数为所有卡牌的点数之和。

示例 4：
    输入：cardPoints = [1,1000,1], k = 1
    输出：1
    解释：你无法拿到中间那张卡牌，所以可以获得的最大点数为 1 。

示例 5：
    输入：cardPoints = [1,79,80,1,1,1,200,1], k = 3
    输出：202

提示：
    1 <= cardPoints.length <= 10^5
    1 <= cardPoints[i] <= 10^4
    1 <= k <= cardPoints.length

"""
from typing import List

""" preSum """
class Solution(object):
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        N = len(cardPoints)
        preSum = [0] * (N + 1)
        for i in range(N):
            preSum[i + 1] = preSum[i] + cardPoints[i]
        res = float("inf")
        windowSize = N - k
        for i in range(k + 1):
            res = min(res, preSum[windowSize + i] - preSum[i])
        return preSum[N] - res

""" 滑动窗口 """
class Solution(object):
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        N = len(cardPoints)
        windowSize = N - k      # 滑动窗口的大小
        sums = 0
        res = float("inf")
        for i in range(N):      # 右移右边界
            sums += cardPoints[i]
            if i >= windowSize:                     # 当 i >= windowSize 时，
                sums -= cardPoints[i - windowSize]  # 为了固定窗口的元素是 k 个，每次移动时需要将 i - windowSize 位置的元素移除。
            if i >= windowSize - 1:     # 当 i >= windowSize - 1 时，
                res = min(res, sums)    # 滑动窗口内的元素刚好是 k 个，开始计算滑动窗口的最小和。
        return sum(cardPoints) - res

if __name__ == "__main__":
    cardPoints = [1,2,3,4,5,6,1]
    k = 3
    sol = Solution()
    result = sol.maxScore(cardPoints, k)
    print(result)