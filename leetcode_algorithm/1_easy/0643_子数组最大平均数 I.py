"""
https://leetcode-cn.com/problems/maximum-average-subarray-i/

给你一个由 n 个元素组成的整数数组 nums 和一个整数 k 。

请你找出平均数最大且 长度为 k 的连续子数组，并输出该最大平均数。

任何误差小于 10-5 的答案都将被视为正确答案。

示例 1：
    输入：nums = [1,12,-5,-6,50,3], k = 4
    输出：12.75
    解释：最大平均数 (12-5-6+50)/4 = 51/4 = 12.75

示例 2：
    输入：nums = [5], k = 1
    输出：5.00000

提示：
    n == nums.length
    1 <= k <= n <= 10^5
    -10^4 <= nums[i] <= 10^4

"""
from typing import List

""" 方法1：滑动窗口 """
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxTotal = total = sum(nums[:k])            # 初始化，取前 k 个数字之和
        n = len(nums)
        for i in range(k, n):                       # 从 k 位置开始遍历
            total = total - nums[i - k] + nums[i]   # 新的总和为之前的总和减去滑动窗口最左边的，然后加上新的
            maxTotal = max(maxTotal, total)
        return maxTotal / k

''' 方法2：preSum '''
class Solution(object):
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        preSum = range(n + 1)   # 定义一个长度为 n+1 的 preSum 数组
        for i in range(n):      # 从左向右遍历数组
            preSum[i + 1] = preSum[i] + nums[i]     # 当遍历到数组的 i 位置时，preSum 表示 i 位置左边的元素之和（不包含当前元素）。
        largest = float("-inf")
        for i in range(k - 1, n):                   # 再遍历一次
            largest = max(preSum[i + 1] - preSum[i + 1 - k], largest)   # 求长度为 k 的每个区间的最大和
        return largest / float(k)

if __name__ == "__main__":
    nums = [1,12,-5,-6,50,3]
    k = 4
    sol = Solution()
    result = sol.findMaxAverage(nums, k)
    print (result)