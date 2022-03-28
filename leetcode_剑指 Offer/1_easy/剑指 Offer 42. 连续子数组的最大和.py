"""
https://leetcode-cn.com/problems/lian-xu-zi-shu-zu-de-zui-da-he-lcof/

输入一个整型数组，数组中的一个或连续多个整数组成一个子数组。求所有子数组的和的最大值。

要求时间复杂度为O(n)。

示例1:
    输入: nums = [-2,1,-3,4,-1,2,1,-5,4]
    输出: 6
    解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。

提示：
    1 <= arr.length <= 10^5
    -100 <= arr[i] <= 100
    注意：本题与主站 53 题相同：https://leetcode-cn.com/problems/maximum-subarray/

"""

from typing import List

""" 解法1：动态规划（模板） """
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        dp = [0] * len(nums)    # 初始化 dp 数组 [0,0,0,0,0,0,0,0,0]
        dp[0] = nums[0]
        result = dp[0]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i-1] + nums[i], nums[i]) # 状态转移公式
            result = max(result, dp[i])             # result 保存dp[i]的最大值
        return result


""" 解法1：动态规划（简化版） """
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            nums[i] = nums[i] + max(nums[i-1], 0)   # nums[i-1]是到前一项为止的最大子序和。和0比较是因为只要大于0，就可以相加构造最大子序和。如果小于0则 nums[i] = nums[i]
        return max(nums)
    # 如果 nums[i-1]大于0的话，新的nums[i]就是和前一项的和，否则就是自身。


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