"""
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

示例:
    输入: [0,1,0,3,12]
    输出: [1,3,12,0,0]

说明:
    必须在原数组上操作，不能拷贝额外的数组。
    尽量减少操作次数。

"""
from typing import List

"""双指针"""
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        n = len(nums)
        left = 0    # 左指针表示已经处理好的序列
        right = 0   # 右指针表示还没有处理的序列
        while right < n:
            if nums[right] != 0:    # # 左指针应当指向为0的元素，如果右指针不为0就将左右指针指向的元素互换
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            right += 1  # 处理之后左指针以左的序列均是没有0的
        return nums

if __name__ == "__main__":
    nums = [0,1,0,3,12]
    sol = Solution()
    result = sol.moveZeroes(nums)
    print (result)