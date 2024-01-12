"""
https://leetcode-cn.com/problems/largest-subarray-length-k/

在数组 A 和数组 B 中，对于第一个满足 A[i] != B[i] 的索引 i ，当 A[i] > B[i] 时，数组 A 大于数组 B。

例如，对于索引从 0 开始的数组：

    [1,3,2,4] > [1,2,2,4] ，因为在索引 1 上， 3 > 2。
    [1,4,4,4] < [2,1,1,1] ，因为在索引 0 上， 1 < 2。

一个数组的子数组是原数组上的一个连续子序列。

给定一个包含不同整数的整数类型数组 nums ，返回 nums 中长度为 k 的最大子数组。

示例 1:
    输入: nums = [1,4,5,2,3], k = 3
    输出: [5,2,3]
    解释: 长度为 3 的子数组有： [1,4,5]、 [4,5,2] 和 [5,2,3]。
    在这些数组中， [5,2,3] 是最大的。

示例 2:
    输入: nums = [1,4,5,2,3], k = 4
    输出: [4,5,2,3]
    解释: 长度为 4 的子数组有： [1,4,5,2] 和 [4,5,2,3]。
    在这些数组中， [4,5,2,3] 是最大的。

示例 3:
    输入: nums = [1,4,5,2,3], k = 1
    输出: [5]

提示：
    1 <= k <= nums.length <= 10^5
    1 <= nums[i] <= 10^9
    nums 中的所有整数都是不同的。

"""
from typing import List

class Solution:
    def largestSubarray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        max_num = nums[n-k]
        max_idx = n - k
        for i in range(n-k-1, -1, -1):
            if nums[i] > max_num:
                max_num = nums[i]
                max_idx = i
        return nums[max_idx : max_idx + k]

class Solution:
    def largestSubarray(self, nums: List[int], k: int) -> List[int]:
        if k > 1:
            start = max(nums[:(-k+1)])  # 在倒数第 k 个数字前寻找最大值
        else:
            start = max(nums)       # 如果只需要长度为 1 的子数组，直接取最大值
        return nums[nums.index(start):nums.index(start) + k]    # 从 start 数字开始长度为k的数组

if __name__ == "__main__":
    nums = [1,4,2,5,3]
    k = 3
    sol = Solution()
    result = sol.largestSubarray(nums, k)
    print(result)