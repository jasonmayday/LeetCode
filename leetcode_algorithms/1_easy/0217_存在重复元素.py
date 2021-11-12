'''
给定一个整数数组，判断是否存在重复元素。

如果存在一值在数组中出现至少两次，函数返回 true 。如果数组中每个元素都不相同，则返回 false 。

示例 1:
输入: [1,2,3,1]
输出: true

示例 2:
输入: [1,2,3,4]
输出: false

示例 3:
输入: [1,1,1,3,3,4,3,2,4,2]
输出: true

'''
nums = [1,1,1,3,3,4,3,2,4,2]

from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))   # 如果数组的长度不等于元素集，则说明有重复的元素。set() 函数创建一个无序不重复元素集，可进行关系测试

if __name__ == "__main__":
    sol = Solution()
    result = sol.containsDuplicate(nums)
    print (result) 