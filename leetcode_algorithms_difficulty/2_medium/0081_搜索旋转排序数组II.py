"""
https://leetcode-cn.com/problems/search-in-rotated-sorted-array-ii/

已知存在一个按 非降序 排列的整数数组 nums ，数组中的值不必互不相同。

在传递给函数之前，nums 在预先未知的某个下标 k（0 <= k < nums.length）上进行了 旋转 ，使数组变为 [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]（下标 从 0 开始 计数）。例如， [0,1,2,4,4,4,5,6,6,7] 在下标 5 处经旋转后可能变为 [4,5,6,6,7,0,1,2,4,4] 。

给你 旋转后 的数组 nums 和一个整数 target ，请你编写一个函数来判断给定的目标值是否存在于数组中。如果 nums 中存在这个目标值 target ，则返回 true ，否则返回 false 。

示例 1：
    输入：nums = [2,5,6,0,0,1,2], target = 0
    输出：true

示例 2：
    输入：nums = [2,5,6,0,0,1,2], target = 3
    输出：false

提示：
    1 <= nums.length <= 5000
    -10^4 <= nums[i] <= 10^4
    题目数据保证 nums 在预先未知的某个下标上进行了旋转
    -10^4 <= target <= 10^4

进阶：
    这是 搜索旋转排序数组 的延伸题目，本题中的 nums  可能包含重复元素。
    这会影响到程序的时间复杂度吗？会有怎样的影响，为什么？

"""
from typing import List

""" 二分查找 """
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
                                                        # 参考: 0033_搜索旋转排序树组
        while len(nums) > 1 and nums[0] == nums[-1]:    # 当左端点和右端点相等时，无法判断 mid 在左半边有序数组还是右半边有序数组
            nums.pop()                                  # 只需要一直pop直到左端点和右端点不相等

        l = 0
        r = len(nums)-1
        # 将数组从中间分开成左右两部分的时候，一定有一部分的数组是有序的
        # 二分查找的时候查看当前 mid 为分割位置分割出来的两个部分 [l, mid] 和 [mid + 1, r] 哪个部分是有序的，
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return True
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
        return False

if __name__ == "__main__":
    nums = [8, 9, 10, 11, 1, 2, 3, 4, 5, 6, 7, 8]
    target = 9
    sol = Solution()
    result = sol.search(nums, target)
    print(result)