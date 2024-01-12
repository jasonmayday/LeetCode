"""
https://leetcode-cn.com/problems/single-element-in-a-sorted-array/

给你一个仅由整数组成的有序数组，其中每个元素都会出现两次，唯有一个数只会出现一次。

请你找出并返回只出现一次的那个数。

你设计的解决方案必须满足 O(log n) 时间复杂度和 O(1) 空间复杂度。

示例 1:
    输入: nums = [1,1,2,3,3,4,4,8,8]
    输出: 2

示例 2:
    输入: nums =  [3,3,7,7,10,11,11]
    输出: 10

提示:
    1 <= nums.length <= 10^5
    0 <= nums[i] <= 10^5

"""
from typing import List


""" 方法一：全数组的二分查找
    假设只出现一次的元素位于下标 x，由于其余每个元素都出现两次，因此下标 x 的左边和右边都有偶数个元素，数组的长度是奇数。
    由于数组是有序的，因此数组中相同的元素一定相邻。
    对于下标 x 左边的下标 y，如果 nums[y] = nums[y+1]，则 y 一定是偶数；
    对于下标 x 右边的下标 z，如果 nums[z] = nums[z+1]，则 z 一定是奇数。
    由于下标 x 是相同元素的开始下标的奇偶性的分界，因此可以使用二分查找的方法寻找下标 x。

"""
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1
        while low < high:
            mid = (low + high) // 2         # 每次取左右边界的平均值 mid 作为待判断的下标

            if (mid % 2) == 0:              # 如果 mid 是偶数
                if nums[mid] == nums[mid + 1]:  # 则比较 nums[mid] 和 nums[mid+1] 是否相等
                    low = mid + 1               # 如果相等，则 mid < x，调整左边界
                else:
                    high = mid                  # 否则 mid ≥ x，调整右边界

            if (mid % 2) != 0:              # 如果 mid 是奇数
                if nums[mid - 1] == nums[mid]:  # 则比较 nums[mid-1] 和 nums[mid] 是否相等
                    low = mid + 1               # 如果相等，则 mid < x，调整左边界
                else:
                    high = mid                  # 否则 mid ≥ x，调整右边界

        return nums[low]


""" 方法二：偶数下标的二分查找
    由于只出现一次的元素所在下标 xx 的左边有偶数个元素，因此下标 x 一定是偶数，可以在偶数下标范围内二分查找 
    二分查找的目标是找到满足 nums[x] = nums[x+1] 的最小的偶数下标 x，则下标 x 处的元素是只出现一次的元素。

"""
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1 # 右边界是数组的最大偶数下标（由于数组的长度是奇数，因此数组的最大偶数下标等于数组的长度减 1）
        while low < high:
            mid = (low + high) // 2
            if (mid % 2) == 0:                  # 如果 mid 是偶数，不用执行额外操作
                if nums[mid] == nums[mid + 1]:  # 比较 nums[mid] 和 nums[mid+1] 是否相等
                    low = mid + 2               # 如果相等，调整左边界，查找下一个偶数下标
                else:                           # 如果不相等
                    high = mid                  # 调整右边界

            if (mid % 2) != 0:                  # 如果 mid 是奇数
                mid -= 1                        # 则将 mid 减 1，确保 mid 是偶数
                if nums[mid] == nums[mid + 1]:  # 然后执行相同操作
                    low = mid + 2
                else:
                    high = mid

        return nums[low]

if __name__ == "__main__":
    nums = [1,1,2,3,3,4,4,8,8]
    sol = Solution()
    result = sol.singleNonDuplicate(nums)
    print (result)