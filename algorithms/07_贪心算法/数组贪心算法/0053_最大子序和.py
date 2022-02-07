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

from typing import List

""" 解法2：贪心
    局部最优：当前“连续和”为负数的时候立刻放弃，从下一个元素重新计算“连续和”，因为负数加上下一个元素 “连续和”只会越来越小。
    全局最优：选取最大“连续和” """
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = -float('inf')
        count = 0   # 计算起点的时候，一定是从大于 0 的数字开始计算，因为负数只会拉低总和
        for i in range(len(nums)):
            count += nums[i]
            if count > result:  # 区间的终止位置，
                result = count  # 其实就是如果count取到最大值了
            if count <= 0:  # 如果count一旦加上nums[i]变为负数，那么就应该从nums[i+1]开始从0累积count了
                count = 0   # 因为已经变为负数的count，只会拖累总和。
        return result

if __name__ == "__main__":
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    sol = Solution()
    result = sol.maxSubArray(nums)
    print (result)  
