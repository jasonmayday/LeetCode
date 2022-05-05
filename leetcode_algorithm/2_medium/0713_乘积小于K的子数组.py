"""
https://leetcode-cn.com/problems/subarray-product-less-than-k/

给你一个整数数组 nums 和一个整数 k ，请你返回子数组内所有元素的乘积严格小于 k 的连续子数组的数目。

示例 1：
    输入：nums = [10,5,2,6], k = 100
    输出：8
    解释：8 个乘积小于 100 的子数组分别为：[10]、[5]、[2],、[6]、[10,5]、[5,2]、[2,6]、[5,2,6]。
    需要注意的是 [10,5,2] 并不是乘积小于 100 的子数组。

示例 2：
    输入：nums = [1,2,3], k = 0
    输出：0

提示: 
    1 <= nums.length <= 3 * 10^4
    1 <= nums[i] <= 1000
    0 <= k <= 10^6

"""
from typing import List
from math import log
import bisect

"""方法一：二分查找"""
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k == 0:
            return 0
        ans = 0
        n = len(nums)
        logPrefix = [0] * (n + 1)
        for i, num in enumerate(nums):
            logPrefix[i + 1] = logPrefix[i] + log(num)
        logK = log(k)
        for j in range(1, n + 1):
            l = bisect.bisect_right(logPrefix, logPrefix[j] - logK + 1e-10, 0, j)
            ans += j - l
        return ans

"""方法二：滑动窗口"""
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        ans = 0     # 子数组的数目
        prod = 1
        i = 0       # 左端点
        for j, num in enumerate(nums):  # 子数组的右端点下标和值
            prod *= num                 # 乘以当前值
            while i <= j and prod >= k: # 当总乘积大于等于k时
                prod //= nums[i]        # 去掉最左边数字
                i += 1                  # 左指针右移一位
            ans += j - i + 1            # 以j为右端点的满足条件的子数组的个数
        return ans

if __name__ == "__main__":
    nums = [10,5,2,6]
    k = 100
    sol = Solution()
    result = sol.numSubarrayProductLessThanK(nums, k)
    print (result)