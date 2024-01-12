"""
https://leetcode-cn.com/problems/permutations/

给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。

示例 1：
    输入：nums = [1,2,3]
    输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

示例 2：
    输入：nums = [0,1]
    输出：[[0,1],[1,0]]

示例 3：
    输入：nums = [1]
    输出：[[1]]

提示：
    1 <= nums.length <= 6
    -10 <= nums[i] <= 10
    nums 中的所有整数 互不相同

"""
from typing import List
import itertools

"""解法1：itertools.permutations"""
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return list(itertools.permutations(nums))

"""解法2：回溯算法"""
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(nums, tmp):   # 递归函数，表示从左往右填到第 first 个位置，当前排列为 output
            if not nums:
                res.append(tmp)
                return 
            for i in range(len(nums)):
                backtrack(nums[:i] + nums[i+1:], tmp + [nums[i]])
        backtrack(nums, [])
        return res

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(first = 0):
            if first == n:              # 所有数都填完了
                res.append(nums[:])
            for i in range(first, n):
                nums[first], nums[i] = nums[i], nums[first] # 动态维护数组
                backtrack(first + 1)                        # 继续递归填下一个数
                nums[first], nums[i] = nums[i], nums[first] # 撤销操作
        n = len(nums)
        res = []
        backtrack()
        return res

if __name__ == "__main__":
    nums = [1,2,3]
    sol = Solution()
    result = sol.permute(nums)
    print(result)