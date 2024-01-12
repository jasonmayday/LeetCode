"""
https://leetcode-cn.com/problems/combination-sum-ii/

给你一个由候选元素组成的集合 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的每个元素在每个组合中只能使用 一次 。

注意：解集不能包含重复的组合。 

示例 1:
    输入: candidates = [10,1,2,7,6,1,5], target = 8,
    输出:
    [
    [1,1,6],
    [1,2,5],
    [1,7],
    [2,6]
    ]

示例 2:
    输入: candidates = [2,5,2,1,2], target = 5,
    输出:
    [
    [1,2,2],
    [5]
    ]

提示:
    1 <= candidates.length <= 100
    1 <= candidates[i] <= 50
    1 <= target <= 30

"""
from typing import List
from collections import Counter

"""方法一：递归 + 回溯"""
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        path = []
        def backtrack(candidates,target,sum,startIndex):
            if sum == target:       # 和等于target
                res.append(path[:]) # 将组合添加进答案
            for i in range(startIndex,len(candidates)):  # 要对同一树层使用过的元素进行跳过
                if sum + candidates[i] > target:
                    return 
                if i > startIndex and candidates[i] == candidates[i-1]: # 直接用startIndex来去重,要对同一树层使用过的元素进行跳过
                    continue  
                sum += candidates[i]
                path.append(candidates[i])
                backtrack(candidates,target,sum,i+1)  # i+1:每个数字在每个组合中只能使用一次
                sum -= candidates[i]  # 回溯
                path.pop()  # 回溯
        candidates = sorted(candidates)  # 首先把给candidates排序，让其相同的元素都挨在一起。
        backtrack(candidates,target,0,0)
        return res


"""方法2：递归 + 回溯"""
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(tmp, cur, index):
            if cur > target:
                return
            if cur == target:
                res.append(tmp)
                return
            for i in range(index, n):
                if i > index and candidates[i] == candidates[i - 1]:
                    continue
                backtrack(tmp + [candidates[i]], cur + candidates[i], i + 1)
        
        res = []
        n = len(candidates)
        candidates.sort()
        backtrack([], 0, 0)
        return res


if __name__ == "__main__":
    candidates = [1, 1, 2]
    target = 3
    sol = Solution()
    result = sol.combinationSum2(candidates,target)
    print(result)