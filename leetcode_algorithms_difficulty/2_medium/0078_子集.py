"""
https://leetcode-cn.com/problems/subsets/

给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。

解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。

示例 1：
    输入：nums = [1,2,3]
    输出：[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

示例 2：
    输入：nums = [0]
    输出：[[],[0]]

提示：
    1 <= nums.length <= 10
    -10 <= nums[i] <= 10
    nums 中的所有元素 互不相同

"""

from typing import List
from  itertools import combinations

""" 1. 使用combinations实现排列组合 """
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        for i in range(len(nums) + 1):
            for combo in combinations(nums, i):   # combinations(nums, i) 返回 nums 中所有长度为 i 的子序列
                res.append(combo)
        return res
    
""" 2. 迭代"""
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for i in nums:
            res = res + [[i] + num for num in res]
        return res

""" 3. 递归(回溯算法)"""
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        
        def helper(i, combo):
            res.append(combo)
            for j in range(i, n):
                helper(j + 1, combo + [nums[j]] )
                
        helper(0, [])
        return res  

if __name__ == "__main__":
    nums = [1,2,3]
    sol = Solution()
    result = sol.subsets(nums)
    print(result)