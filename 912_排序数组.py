'''
https://leetcode-cn.com/problems/sort-an-array/

给你一个整数数组 nums，请你将该数组升序排列。

示例 1：
输入：nums = [5,2,3,1]
输出：[1,2,3,5]

示例 2：
输入：nums = [5,1,1,2,0,0]
输出：[0,0,1,1,2,5]
'''

nums = [5,1,1,2,0,0]
from typing import List

# 选择排序 (Selection sort)
class Solution:
    def findSmallest(self, nums):
        smallest = nums[0]
        smallest_index = 0
        for i in range(1, len(nums)):
            if nums[i] < smallest:
                smallest = nums[i]
                smallest_index = i
        return smallest_index
        
    def sortArray(self, nums: List[int]) -> List[int]:
        newnums = []
        for i in range(len(nums)):
            smallest = self.findSmallest(nums)
            newnums.append(nums.pop(smallest))
        return newnums

sol = Solution()
s = sol.sortArray(nums)
print(s)