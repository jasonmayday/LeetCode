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

class Solution(object):
    def rob(self, nums: List[int]) -> int:
        #   那么，很明显可以分为三种情况：
        #   1. 首位都不偷
        #   2. 偷首不偷尾
        #   3. 不偷首偷尾
        # 显然，第1种方式损失太大，选取2、3。
        # 那么，分为两种情况，分别计算不包含首和不包含尾这两种情况来判断哪个大哪个小

        # 1.dp[i] 代表当前最大子序和
        # 2.动态方程: dp[i] = max(dp[i-1] and , nums[i-1]+dp[i-2])
        # 3.初始化: 给没有房子时，dp一个位置，即：dp[0]
        #   3.1 当size=0时，没有房子，dp[0]=0；
        #   3.2 当size=1时，有一间房子，偷即可：dp[1]=nums[0]

        # 依照《打家劫舍I》的优化方案进行计算

        # nums处理，分别切割出去首和去尾的子串
        nums1 = nums[1:]
        nums2 = nums[:-1]

        size = len(nums)
        if size == 0:
            return 0
        if size == 1:
            return nums[0]

        def handle(size, nums):
            dp1 = 0
            dp2 = nums[0]
            for i in range(2, size+1):
                dp1 = max(dp2, nums[i-1]+dp1)
                dp1, dp2 = dp2, dp1
            return dp2

        res1 = handle(size-1, nums1)
        res2 = handle(size-1, nums2)

        return max(res1, res2)

if __name__ == "__main__":
    nums = [1,2,3,1]
    sol = Solution()
    result = sol.rob(nums)
    print (result)