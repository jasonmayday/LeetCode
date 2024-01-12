"""
https://leetcode-cn.com/problems/que-shi-de-shu-zi-lcof/

一个长度为n-1的递增排序数组中的所有数字都是唯一的，并且每个数字都在范围0～n-1之内。在范围0～n-1内的n个数字中有且只有一个数字不在该数组中，请找出这个数字。

示例 1:
    输入: [0,1,3]
    输出: 2

示例 2:
    输入: [0,1,2,3,4,5,6,7,9]
    输出: 8

限制：
    1 <= 数组长度 <= 10000

"""
from typing import List

""" 二分查找 """
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        i = 0
        j = len(nums) -1
        while i <= j:
            mid = (i + j) // 2
            if nums[mid] == mid:    # 中点的下标和值相同，说明缺失的数字在中点右边：
                i = mid + 1         # 收缩左边界
            else:                   # 中点的下标和值不同，说明缺失的数字在中点左边：
                j = mid - 1         # 收缩右边界
        return i

if __name__ == "__main__":
    nums = [0,1,2,3,4,5,6,7,9]
    sol = Solution()
    result = sol.missingNumber(nums)
    print (result)