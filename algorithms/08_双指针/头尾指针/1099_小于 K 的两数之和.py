"""
https://leetcode-cn.com/problems/two-sum-less-than-k/

给你一个整数数组 nums 和整数 k ，返回最大和 sum ，满足存在 i < j 使得 nums[i] + nums[j] = sum 且 sum < k 。如果没有满足此等式的 i,j 存在，则返回 -1 。

示例 1：
    输入：nums = [34,23,1,24,75,33,54,8], k = 60
    输出：58
    解释：
        34 和 24 相加得到 58，58 小于 60，满足题意。

示例 2：
    输入：nums = [10,20,30], k = 15
    输出：-1
    解释：
        我们无法找到和小于 15 的两个元素。

提示：
    1 <= nums.length <= 100
    1 <= nums[i] <= 1000
    1 <= k <= 2000

"""
from typing import List

""" 双指针 """
class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums.sort()     # [1, 8, 23, 24, 33, 34, 54, 75]
        res = -float('inf')
        left = 0
        right = len(nums) - 1
        while left < right:
            temp = nums[left] + nums[right]
            if temp < k:
                res = max(res, temp)
                left += 1
            else:
                right -= 1

        return res if res != -float('inf') else -1

if __name__ == "__main__":
    nums = [34,23,1,24,75,33,54,8]
    k = 60
    sol = Solution()
    result = sol.twoSumLessThanK(nums, k)
    print(result)