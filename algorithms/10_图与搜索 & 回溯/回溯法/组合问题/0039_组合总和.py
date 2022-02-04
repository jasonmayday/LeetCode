"""
https://leetcode-cn.com/problems/combination-sum/

给你一个 无重复元素 的整数数组 candidates 和一个目标整数 target ，找出 candidates 中可以使数字和为目标数 target 的 所有不同组合 ，并以列表形式返回。你可以按 任意顺序 返回这些组合。

candidates 中的 同一个 数字可以 无限制重复被选取 。如果至少一个数字的被选数量不同，则两种组合是不同的。 

对于给定的输入，保证和为 target 的不同组合数少于 150 个。

示例 1：
    输入：candidates = [2,3,6,7], target = 7
    输出：[[2,2,3],[7]]
    解释：
    2 和 3 可以形成一组候选，2 + 2 + 3 = 7 。注意 2 可以使用多次。
    7 也是一个候选， 7 = 7 。
    仅有这两种组合。

示例 2：
    输入: candidates = [2,3,5], target = 8
    输出: [[2,2,2,2],[2,3,3],[3,5]]

示例 3：
    输入: candidates = [2], target = 1
    输出: []

示例 4：
    输入: candidates = [1], target = 1
    输出: [[1]]

示例 5：
    输入: candidates = [1], target = 2
    输出: [[1,1]]

提示：
    1 <= candidates.length <= 30
    1 <= candidates[i] <= 200
    candidate 中的每个元素都 互不相同
    1 <= target <= 500

"""
from typing import List
from collections import defaultdict

""" 回溯算法
    以 target = 7 为 根结点 ，创建一个分支的时 做减法"""
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        def dfs(candidates, begin, size, path, res, target):
            if target < 0:          # 如果剩下的值小于0，也就是说加上某数后总和超过了target
                return              # 返回
            if target == 0:         # 如果剩下的值刚好为0
                res.append(path)    # 意味着找到了一组答案，把path加入到结果
                return

            for i in range(begin, size):    # 从 0 开始遍历
                dfs(candidates, i, size, path + [candidates[i]], res, target - candidates[i])

        size = len(candidates)
        if size == 0:
            return []
        path = []
        res = []
        dfs(candidates, 0, size, path, res, target)
        return res
    
""" 动态规划"""
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        dp = defaultdict(list) # 存储从1到target每个子问题的解集
      
        for i in range(1, target + 1): # 要算target下的结果, 就先算target - 1, target - 2, ..., 1
            # 把 i 当做target
            for j in candidates:
                # 有数直接等于当前target, 直接就是一种答案 (base case)
                if i == j:
                    dp[i].append([i]) 
                # 说明当前数小于当前target, 需要加上i - j才能等于答案
                elif j < i:
                    # dp[i - j]中存储了所有和为i - j的解集, 那么对于每一个解集加上j就变成了和为i的解集，即dp[i]
                    for k in dp[i-j]: 
                        x = k[:]    # 深拷贝, 要不然x在append元素时k也会变，也可以用copy.deepcopy
                        x.append(j) # 每个解集append上j就是dp[i]的解集

                        x.sort() # 升序，便于后续去重
                        if x not in dp[i]: # 可能会慢，可以变成字符串，再维护一个set来去重
                            dp[i].append(x)
        return dp[target]
    
"""回溯算法"""
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates)     # [2,3,6,7]
        ans = []
        def find(start, use, remain):           # use表示已经使用过的数（组成的列表），remain表示距离target还有多大。
            for i in range(start, len(candidates)):
                c = candidates[i]
                if c == remain:                     # 1. 满足条件
                    ans.append(use + [c])           # 则答案加入一条
                if c < remain:                      # 2. 不足
                    find(i, use + [c], remain - c)  # 继续递归
                if c > remain:      # 3. 超出
                    return          # 则直接退出本路线。
        find(0, [], target)

        return ans

if __name__ == "__main__":
    candidates = [2,3,6,7]
    target = 7
    sol = Solution()
    result = sol.combinationSum(candidates, target)
    print(result)