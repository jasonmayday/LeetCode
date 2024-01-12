"""
https://leetcode-cn.com/problems/house-robber/

你是一个专业的小偷，计划偷窃沿街的房屋。
每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。

给定一个代表每个房屋存放金额的非负整数数组，计算你 不触动警报装置的情况下 ，一夜之内能够偷窃到的最高金额。

示例 1：
    输入：[1,2,3,1]
    输出：4
    解释：偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
         偷窃到的最高金额 = 1 + 3 = 4 。

示例 2：
    输入：[2,7,9,3,1]
    输出：12
    解释：偷窃 1 号房屋 (金额 = 2), 偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)。
         偷窃到的最高金额 = 2 + 9 + 1 = 12 。

提示：
    1 <= nums.length <= 100
    0 <= nums[i] <= 400

"""
from typing import List

"""方法一：动态规划"""
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        size = len(nums)
        if size == 1:
            return nums[0]
        
        dp = [0] * size     # [0,0,0,0,0]
        dp[0] = nums[0]     # 用 dp[i] 表示前 i 间房屋能偷窃到的最高总金额
        dp[1] = max(nums[0], nums[1])   # 比较前两个大小
        for i in range(2, size):        # 对于第 k (k>2) 间房屋，有两个选项：
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
        # 1. 偷窃第 k 间房屋，那么就不能偷窃第 k-1 间房屋，偷窃总金额为前 k−2 间房屋的最高总金额与第 k 间房屋的金额之和。
        # 2. 不偷窃第 k 间房屋，偷窃总金额为前 k-1 间房屋的最高总金额。
        return dp[size - 1]

if __name__ == "__main__":
    nums = [2,7,9,3,1]
    sol = Solution()
    result = sol.rob(nums)
    print (result)
