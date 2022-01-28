"""
https://leetcode-cn.com/problems/combinations/

给定两个整数 n 和 k，返回范围 [1, n] 中所有可能的 k 个数的组合。

你可以按 任何顺序 返回答案。

示例 1：
    输入：n = 4, k = 2
    输出：
        [
        [2,4],
        [3,4],
        [2,3],
        [1,2],
        [1,3],
        [1,4],
        ]

示例 2：
    输入：n = 1, k = 1
    输出：[[1]]

提示：
    1 <= n <= 20
    1 <= k <= n

"""
from typing import List

""" 回溯+剪枝 """
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []    # 存放符合条件结果的集合
        path = []   # 用来存放符合条件结果
        
        def backtrack(n, k, StartIndex):
            if len(path) == k:      # 一旦找到了某个 k 个数的组合
                res.append(path[:]) # 添加进结果的集合
                return
            for i in range(StartIndex, n-(k-len(path)) + 2):
                path.append(i)          # 处理节点 
                backtrack(n, k, i+1)    # 递归
                path.pop()              # 回溯，撤销处理的节点
        
        backtrack(n, k, 1)
        return res

if __name__ == "__main__":
    n = 8
    k = 4
    sol = Solution()
    result = sol.combine(n, k)
    print(result)