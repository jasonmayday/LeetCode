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
        smallest = nums[0]   # 创建变量用来临时存放最小值（先假设第一个元素为最小值）
        smallest_index = 0   # 用来存放最小值的索引位置
        for i in range(1, len(nums)):    # 循环遍历数组，找出最小值，并返回最小值索引
            if nums[i] < smallest:
                smallest = nums[i]
                smallest_index = i
        return smallest_index
        
    def sortArray(self, nums: List[int]) -> List[int]:    # 对数组进行排序
        newnums = []   # 创建新数组用来存放每次循环中找出的原数组中的最小值
        for i in range(len(nums)):
            smallest = self.findSmallest(nums)   # 调用上面的函数，找出当前数组的最小值
            newnums.append(nums.pop(smallest))   # .pop（）函数剔除对应位置的元素并返回元素的值  存到新建数组newnums中
        return newnums

sol = Solution()
s = sol.sortArray(nums)
print(s)