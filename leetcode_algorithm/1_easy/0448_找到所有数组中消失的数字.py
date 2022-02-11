"""
https://leetcode-cn.com/problems/find-all-numbers-disappeared-in-an-array/

给你一个含 n 个整数的数组 nums ，其中 nums[i] 在区间 [1, n] 内。请你找出所有在 [1, n] 范围内但没有出现在 nums 中的数字，并以数组的形式返回结果。

示例 1：
    输入：nums = [4,3,2,7,8,2,3,1]
    输出：[5,6]

示例 2：
    输入：nums = [1,1]
    输出：[2]

提示：
    n == nums.length
    1 <= n <= 10^5
    1 <= nums[i] <= n
    进阶：你能在不使用额外空间且时间复杂度为 O(n) 的情况下解决这个问题吗? 你可以假定返回的数组不算在额外空间内。

"""
from typing import List

'''遍历寻找'''
class Solution(object):
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        counter = set(nums)
        n = len(nums)
        res = []
        for i in range(1, n + 1):   # 对 1 到 n 的所有数字进行遍历，判断每个数字是否在数组中存在。
            if i not in counter:
                res.append(i)
        return res

'''数组的原地操作'''
class Solution(object):
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i, num in enumerate(nums):
            if nums[abs(num) - 1] > 0:
                nums[abs(num) - 1] *= -1
        res = []
        for i in range(len(nums)):
            if nums[i] > 0:
                res.append(i + 1)
        return res

if __name__ == "__main__":
    nums = [4,3,2,7,8,2,3,1]
    sol = Solution()
    result = sol.findDisappearedNumbers(nums)
    print(result)