"""
https://leetcode-cn.com/problems/search-in-rotated-sorted-array/

整数数组 nums 按升序排列，数组中的值 互不相同 。

在传递给函数之前，nums 在预先未知的某个下标 k（0 <= k < nums.length）上进行了 旋转，使数组变为 [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]（下标 从 0 开始 计数）。例如， [0,1,2,4,5,6,7] 在下标 3 处经旋转后可能变为 [4,5,6,7,0,1,2] 。

给你 旋转后 的数组 nums 和一个整数 target ，如果 nums 中存在这个目标值 target ，则返回它的下标，否则返回 -1 。

示例 1：
    输入：nums = [4,5,6,7,0,1,2], target = 0
    输出：4

示例 2：
    输入：nums = [4,5,6,7,0,1,2], target = 3
    输出：-1

示例 3：
    输入：nums = [1], target = 0
    输出：-1

提示：
    1 <= nums.length <= 5000
    -10^4 <= nums[i] <= 10^4
    nums 中的每个值都 独一无二
    题目数据保证 nums 在预先未知的某个下标上进行了旋转
    -10^4 <= target <= 10^4

"""
from typing import List

"""方法一：二分查找"""
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        l, r = 0, len(nums)-1
        # 将数组从中间分开成左右两部分的时候，一定有一部分的数组是有序的
        # 二分查找的时候查看当前 mid 为分割位置分割出来的两个部分 [l, mid] 和 [mid + 1, r] 哪个部分是有序的，
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if nums[0] <= nums[mid]:                # 如果第一个数字小于中间数，说明左半边[l,mid]是有序数组
                if nums[0] <= target < nums[mid]:   # 如果目标在左半边
                    r = mid - 1                     # 在 [l, mid-1] 中寻找
                else:                               # 如果目标在右半边
                    l = mid + 1                     # 在 [mid+1，r] 中寻找
            else:                                               # 如果第一个数字小于中间数，说明右半边[mid+1,r]是有序数组
                if nums[mid] < target <= nums[len(nums) - 1]:   # 如果目标在右半边
                    l = mid + 1                                 # 在 [mid+1，r] 中寻找
                else:                                           # 如果目标在左半边
                    r = mid - 1                                 # 在 [l, mid-1] 中寻找
        return -1

if __name__ == "__main__":
    nums = [4,5,6,7,0,1,2]
    target = 0
    sol = Solution()
    result = sol.search(nums, target)
    print (result)