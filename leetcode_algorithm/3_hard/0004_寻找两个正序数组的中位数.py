"""
https://leetcode-cn.com/problems/median-of-two-sorted-arrays/

给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的 中位数 。

算法的时间复杂度应该为 O(log (m+n)) 。

示例 1：
    输入：nums1 = [1,3], nums2 = [2]
    输出：2.00000
    解释：合并数组 = [1,2,3] ，中位数 2

示例 2：
    输入：nums1 = [1,2], nums2 = [3,4]
    输出：2.50000
    解释：合并数组 = [1,2,3,4] ，中位数 (2 + 3) / 2 = 2.5

提示：
    nums1.length == m
    nums2.length == n
    0 <= m <= 1000
    0 <= n <= 1000
    1 <= m + n <= 2000
    -10^6 <= nums1[i], nums2[i] <= 10^6

"""
from typing import List

""" 二分查找 """
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        len1, len2 = len(nums1), len(nums2)

        left = 0
        right = len1
        half_len = (len1 + len2 + 1) // 2
        mid1 = (left + right) // 2
        mid2 = half_len - mid1

        while left < right:
            if mid1 < len1 and nums2[mid2-1] > nums1[mid1]:
                left = mid1 + 1
            else:
                right = mid1
            mid1 = (left + right) // 2
            mid2 = half_len - mid1

        if mid1 == 0:
            max_of_left = nums2[mid2-1]
        elif mid2 == 0:
            max_of_left = nums1[mid1-1]
        else:
            max_of_left = max(nums1[mid1-1], nums2[mid2-1])

        if (len1 + len2) % 2 == 1:
            return max_of_left

        if mid1 == len1:
            min_of_right = nums2[mid2]
        elif mid2 == len2:
            min_of_right = nums1[mid1]
        else:
            min_of_right = min(nums1[mid1], nums2[mid2])

        return (max_of_left + min_of_right) / 2

if __name__ == "__main__":
    nums1 = [1,2]
    nums2 = [3,4]
    sol = Solution()
    result = sol.findMedianSortedArrays(nums1, nums2)
    print(result)