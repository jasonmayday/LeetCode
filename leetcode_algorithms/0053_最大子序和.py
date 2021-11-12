'''
https://leetcode-cn.com/problems/maximum-subarray/

给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

示例 1：
    输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
    输出：6
    解释：连续子数组 [4,-1,2,1] 的和最大，为 6 。

示例 2：
    输入：nums = [1]
    输出：1

示例 3：
    输入：nums = [0]
    输出：0

示例 4：
    输入：nums = [-1]
    输出：-1

示例 5：
    输入：nums = [-100000]
    输出：-100000

提示：
    1 <= nums.length <= 10^5
    -10^4 <= nums[i] <= 10^4

进阶：如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的 分治法 求解。

'''
nums = [-2,1,-3,4,-1,2,1,-5,4]

from typing import List

# 解法1：动态规划 Dynamic Programming
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            nums[i] = nums[i] + max(nums[i-1], 0)   # nums[i-1]是到前一项为止的最大子序和。和0比较是因为只要大于0，就可以相加构造最大子序和。如果小于0则 nums[i] = nums[i]
        return max(nums)                            # 如果 nums[i-1]大于0的话，新的nums[i]就是和前一项的和，否则就是自身。
        
sol = Solution()
result = sol.maxSubArray(nums)
print (result)  
