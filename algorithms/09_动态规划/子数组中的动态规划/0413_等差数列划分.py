"""
https://leetcode-cn.com/problems/arithmetic-slices/

如果一个数列 至少有三个元素 ，并且任意两个相邻元素之差相同，则称该数列为等差数列。

    例如，[1,3,5,7,9]、[7,7,7,7] 和 [3,-1,-5,-9] 都是等差数列。

给你一个整数数组 nums ，返回数组 nums 中所有为等差数组的 子数组 个数。

子数组 是数组中的一个连续序列。

示例 1：
    输入：nums = [1,2,3,4]
    输出：3
    解释：nums 中有三个子等差数组：[1, 2, 3]、[2, 3, 4] 和 [1,2,3,4] 自身。

示例 2：
    输入：nums = [1]
    输出：0

提示：
    1 <= nums.length <= 5000
    -1000 <= nums[i] <= 1000

"""
from typing import List

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        last = None         # 上一个差值
        last_len = ans = 0  # 上一个差值相同的长度
        for i in range(1, n):
            if nums[i] - nums[i-1] == last:     # 相等，差值相同长度加一
                last_len += 1
            else:                               # 否则差值相同长度仅有刚刚这俩的差
                last_len = 0
            ans += last_len     # 从头到尾一共能构成多少种
            last = nums[i] - nums[i-1]
        return ans

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0
        diff = nums[1] - nums[0]    # 差值
        acc_len = 0
        ans = 0
        for i in range(2, len(nums)):       # 长度大于3才开始构成一个子数组，从下标2开始
            if nums[i] - nums[i-1] == diff: # 计算以 nums[i] 为结尾，可以组成几个等差数列
                acc_len += 1
            else:               # 中断了就重新计算
                acc_len = 0
                diff = nums[i] - nums[i-1]
            ans += acc_len      # 求和：计算整个数组可以组成几个等差数列
        return ans  # 1+2=3

""" 动态规划 """
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * (n + 1)  # dp[i] 为以 i 为结尾的话，前 i 个元素可以组成多少个等差数列
        ans = 0
        for i in range(2, n):
            if nums[i] - nums[i-1] == nums[i-1] - nums[i-2]:    # 如果下标各后移一位，数字差值一样
                dp[i] = dp[i-1] + 1 # 多一个为等差数列的子数列
                ans += dp[i]        # 答案加一
        return ans

if __name__ == "__main__":
    nums = [1,2,3,4]
    sol = Solution()
    result = sol.numberOfArithmeticSlices(nums)
    print (result)