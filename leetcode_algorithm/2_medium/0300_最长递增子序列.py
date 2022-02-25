"""
https://leetcode-cn.com/problems/longest-increasing-subsequence/

给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。

子序列 是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7] 的子序列。

示例 1：
    输入：nums = [10,9,2,5,3,7,101,18]
    输出：4
    解释：最长递增子序列是 [2,3,7,101]，因此长度为 4 。

示例 2：
    输入：nums = [0,1,0,3,2,3]
    输出：4

示例 3：
    输入：nums = [7,7,7,7,7,7,7]
    输出：1

提示：
    1 <= nums.length <= 2500
    -10^4 <= nums[i] <= 10^4

进阶：
    你能将算法的时间复杂度降低到 O(n log(n)) 吗?

"""
from typing import List

""" 动态规划 """
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        dp = []             # dp[i] 为考虑前 i 个元素，以第 i 个数字结尾的最长上升子序列的长度
        for right in range(len(nums)):
            dp.append(1)    # dp[0] = 1
            for left in range(right):
                if nums[right] > nums[left]:   # 如果右边大于左边
                    dp[right] = max(dp[right], dp[left] + 1)   # 其中 0 ≤ j < i 且 num[j] < num[i]
        return max(dp)

""" 动态规划 + 二分查找
    重新设计状态定义，使整个 dp 为一个排序列表"""
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tails = [0] * len(nums)     # 每个元素 tails[k] 的值代表 长度为 k+1 的子序列尾部元素的值
        res = 0
        for num in nums:
            i, j = 0, res
            while i < j:
                m = (i + j) // 2
                if tails[m] < num: i = m + 1 # 如果要求非严格递增，将此行 '<' 改为 '<=' 即可。
                else: j = m
            tails[i] = num
            if j == res: res += 1
        return res

if __name__ == "__main__":
    nums = [10,9,2,5,3,7,101,18]    # [2,3,7,101]
    sol = Solution()
    result = sol.lengthOfLIS(nums)
    print (result)