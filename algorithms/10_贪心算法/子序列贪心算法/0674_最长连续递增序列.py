"""
https://leetcode-cn.com/problems/longest-continuous-increasing-subsequence/

给定一个未经排序的整数数组，找到最长且 连续递增的子序列，并返回该序列的长度。

连续递增的子序列 可以由两个下标 l 和 r（l < r）确定，如果对于每个 l <= i < r，都有 nums[i] < nums[i + 1] ，那么子序列 [nums[l], nums[l + 1], ..., nums[r - 1], nums[r]] 就是连续递增子序列。

示例 1：
    输入：nums = [1,3,5,4,7]
    输出：3
    解释：最长连续递增序列是 [1,3,5], 长度为3。
    尽管 [1,3,5,7] 也是升序的子序列, 但它不是连续的，因为 5 和 7 在原数组里被 4 隔开。 

示例 2：
    输入：nums = [2,2,2,2,2]
    输出：1
    解释：最长连续递增序列是 [2], 长度为1。

提示：
    1 <= nums.length <= 10^4
    -10^9 <= nums[i] <= 10^9

"""
from typing import List

""" 贪心 """
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        start = 0       # 令 start 表示连续递增序列的开始下标，初始时 start = 0
        for i in range(n):      # 遍历数组
            if i > 0 and nums[i] <= nums[i - 1]:    # 如果下标 i>0 且 nums[i] ≤ nums[i−1]：说明当前元素小于或等于上一个元素
                start = i   # 因此nums[i−1] 和 nums[i] 不可能属于同一个连续递增序列，必须从下标 i 处开始一个新的连续递增序列
            ans = max(ans, i - start + 1)   # 下标范围 [start,i] 的连续子序列是递增序列，其长度为 i−start+1
        return ans

""" 滑动窗口 """
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        l = r = 0
        max_len = 0
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                r = i
            else:
                if r - l + 1 > max_len:
                    max_len = r - l + 1
                l = r = i
        return max(max_len, r - l + 1)

""" 动态规划 """
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        result = 1
        dp = [1] * len(nums)
        for i in range(len(nums)-1):
            if nums[i+1] > nums[i]: #连续记录
                dp[i+1] = dp[i] + 1
            result = max(result, dp[i+1])
        return result

if __name__ == "__main__":
    nums = [1,3,5,4,7]
    sol = Solution()
    result = sol.findLengthOfLCIS(nums)
    print (result)