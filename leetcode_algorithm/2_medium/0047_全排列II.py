"""
https://leetcode-cn.com/problems/permutations-ii/

给定一个可包含重复数字的序列 nums ，按任意顺序 返回所有不重复的全排列。

示例 1：
    输入：nums = [1,1,2]
    输出：
        [[1,1,2],
        [1,2,1],
        [2,1,1]]

示例 2：
    输入：nums = [1,2,3]
    输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

提示：
    1 <= nums.length <= 8
    -10 <= nums[i] <= 10

"""
from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        temp = []
        
        def backtracking(nums, temp):
            if not nums:            # 终止条件
                res.append(temp)
                return
            else:
                for i in range(len(nums)):
                    if i > 0 and nums[i] == nums[i-1]:  # 如果某位数字和前一位相同，就进行去重
                        continue
                    backtracking(nums[:i] + nums[i+1:], temp + [nums[i]])   # 这种拼接方法是天然的标记，判断前一字符是否在循环里。
        backtracking(nums, temp)
        return res

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if not nums: 
            return []
        res = []    # res 用来存放结果
        used = [0] * len(nums)
        def backtracking(nums, used, path):
            if len(path) == len(nums):      # 终止条件
                res.append(path.copy())
                return
            for i in range(len(nums)):
                if not used[i]:
                    if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                        continue
                    used[i] = 1
                    path.append(nums[i])
                    backtracking(nums, used, path)
                    path.pop()
                    used[i] = 0
        # 记得给nums排序
        backtracking(sorted(nums),used,[])
        return res

if __name__ == "__main__":
    nums = [1,1,2]
    sol = Solution()
    result = sol.permuteUnique(nums)
    print(result)