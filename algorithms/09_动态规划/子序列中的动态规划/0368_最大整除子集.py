"""
https://leetcode-cn.com/problems/largest-divisible-subset/

给你一个由 无重复 正整数组成的集合 nums ，请你找出并返回其中最大的整除子集 answer ，子集中每一元素对 (answer[i], answer[j]) 都应当满足：
    answer[i] % answer[j] == 0 ，或
    answer[j] % answer[i] == 0

如果存在多个有效解子集，返回其中任何一个均可。

示例 1：
    输入：nums = [1,2,3]
    输出：[1,2]
    解释：[1,3] 也会被视为正确答案。

示例 2：
    输入：nums = [1,2,4,8]
    输出：[1,2,4,8]

提示：
    1 <= nums.length <= 1000
    1 <= nums[i] <= 2 * 10^9
    nums 中的所有整数 互不相同

"""
from typing import List

""" 子数组, 子序列中的动态规划 """
class Solution(object):
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if not nums: return nums
        if len(nums) == 1: return nums
        
        n = len(nums)
        nums.sort()

        dp = [[i] for i in nums]    # [[1], [2], [3], [4], [5], [6]]
        
        for i in range(1, n):               # i 代表被除数位置
            for j in range(i - 1, -1, -1):  # j 代表除数位置
                if nums[i] % nums[j] == 0:
                    dp[i] = max(dp[j] + [nums[i]], dp[i], key = len)
        # print (dp) [[1], [1, 2], [1, 3], [1, 2, 4], [1, 5], [1, 2, 6]]
        return max(dp, key = len)

""" 子数组, 子序列中的动态规划 """
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums = sorted(nums)
        dp = [[x] for x in nums]
        maxseq = []
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] % nums[j] == 0 and len(dp[j]) + 1 > len(dp[i]):
                    dp[i] = dp[j] + nums[i:i+1]
            if len(dp[i]) > len(maxseq):
                maxseq = dp[i]
        return maxseq

if __name__ == "__main__":
    nums = [1,2,3,4,5,6]
    sol = Solution()
    result = sol.largestDivisibleSubset(nums)
    print (result)
