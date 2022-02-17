"""
你是一个专业的小偷，计划偷窃沿街的房屋，每间房内都藏有一定的现金。这个地方所有的房屋都 围成一圈 ，这意味着第一个房屋和最后一个房屋是紧挨着的。同时，相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警 。

给定一个代表每个房屋存放金额的非负整数数组，计算你 在不触动警报装置的情况下 ，今晚能够偷窃到的最高金额。

示例 1：
    输入：nums = [2,3,2]
    输出：3
    解释：你不能先偷窃 1 号房屋（金额 = 2），然后偷窃 3 号房屋（金额 = 2）, 因为他们是相邻的。

示例 2：
    输入：nums = [1,2,3,1]
    输出：4
    解释：你可以先偷窃 1 号房屋（金额 = 1），然后偷窃 3 号房屋（金额 = 3）。
         偷窃到的最高金额 = 1 + 3 = 4 。

示例 3：
    输入：nums = [1,2,3]
    输出：3

提示：
    1 <= nums.length <= 100
    0 <= nums[i] <= 1000

"""

from typing import List

""" 动态规划 (使用辅助函数)"""
class Solution(object):
    def rob(self, nums: List[int]) -> int:
        nums1 = nums[1:]    # 不偷第一个房子
        nums2 = nums[:-1]   # 不偷最后一个房子

        def helper(nums):
            if not nums:
                return 0
            if len(nums) == 1:
                return nums[0]
            dp = [0] * len(nums)
            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])
            for i in range(2, len(nums)):
                dp[i] = max(dp[i-2]+nums[i], dp[i-1])
            return dp[-1] 
        
        res1 = helper(nums1)
        res2 = helper(nums2)
        
        if len(nums) == 1:
            return nums[0]
        
        return max(res1, res2)
    

""" 动态规划 (不使用辅助函数)"""
class Solution(object):
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        # 第一间「必然不选」的情况
        f = [[0] * 2 for _ in range(n)]
        for i in range(1, n-1):
            f[i][0] = max(f[i - 1][0], f[i - 1][1])
            f[i][1] = f[i - 1][0] + nums[i]
        a = max(f[n - 2][1], f[n - 2][0] + nums[n - 1])
        
        # 第一间「允许选」的情况
        f[0][0], f[0][1] = 0, nums[0]
        for i in range(1,n-1):
            f[i][0] = max(f[i - 1][0], f[i - 1][1])
            f[i][1] = f[i - 1][0] + nums[i]
        b = max(f[n - 2][0], f[n - 2][1])
        
        return max(a, b)


""" 动态规划 """
class Solution:
    def rob(self, nums: List[int]) -> int:
        def my_rob(nums):
            cur, pre = 0, 0
            for num in nums:
                cur, pre = max(pre + num, cur), cur
            return cur
        return max(my_rob(nums[:-1]),my_rob(nums[1:])) if len(nums) != 1 else nums[0]


if __name__ == "__main__":
    nums = [1,2,3,1]
    sol = Solution()
    result = sol.rob(nums)
    print (result)