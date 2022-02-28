"""
https://leetcode-cn.com/problems/beautiful-arrangement/

假设有从 1 到 n 的 n 个整数。用这些整数构造一个数组 perm（下标从 1 开始），只要满足下述条件 之一 ，该数组就是一个 优美的排列 ：
    perm[i] 能够被 i 整除
    i 能够被 perm[i] 整除

给你一个整数 n ，返回可以构造的 优美排列 的 数量 。

示例 1：
    输入：n = 2
    输出：2
    解释：
    第 1 个优美的排列是 [1,2]：
        - perm[1] = 1 能被 i = 1 整除
        - perm[2] = 2 能被 i = 2 整除
    第 2 个优美的排列是 [2,1]:
        - perm[1] = 2 能被 i = 1 整除
        - i = 2 能被 perm[2] = 1 整除

示例 2：
    输入：n = 1
    输出：1

提示：
    1 <= n <= 15

"""
from collections import defaultdict
from functools import lru_cache

""" 方法一：回溯 """
class Solution:
    def countArrangement(self, n: int) -> int:
        match = defaultdict(list)
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if i % j == 0 or j % i == 0:
                    match[i].append(j)      # 1: [1, 2, 3], 2: [1, 2], 3: [1, 3]}
        num = 0
        vis = set() # 用 vis 数组标记哪些数被使用过

        def backtrack(index: int) -> None:
            if index == n + 1:
                nonlocal num
                num += 1
                return
            
            for x in match[index]:
                if x not in vis:            # 回溯过程中，每次我们选中一个数 x
                    vis.add(x)              # 我们就将 vis[x] 标记为 true
                    backtrack(index + 1)    # 回溯完成后，
                    vis.discard(x)          # 我们再将其置为 false。
                   
        backtrack(1)
        return num


""" 状态压缩 + 动态规划 (记忆化递归)"""
class Solution:
    def countArrangement(self, n: int) -> int:
        canFill = defaultdict(list)
        for i in range(1,n+1):
            for j in range(1, n+1):
                # 每个位置可以填入哪些数
                if j % i == 0 or i % j == 0:
                    canFill[i].append(j-1)
        # 根据可填入数字的个数排序，优先填入个数少的
        order = sorted(canFill.keys(), key=lambda x:len(canFill[x]))
        end = (1 << n) - 1

        @lru_cache(None)
        def dfs(state):
            # 全部填入
            if state == end:
                return 1
            cnts = ans = 0
            # 当前该填第几个位置
            for i in range(n):
                if (1 << i) & state:
                    cnts += 1
            # 当前位置可以填哪些数
            for i in canFill[order[cnts]]:
                # 哪些数还没被填
                if not ((1 << i) & state):
                    ans += dfs(state ^ (1 << i))
            return ans
        
        return dfs(0)

if __name__ == "__main__":
    n = 3
    sol = Solution()
    result = sol.countArrangement(n)
    print (result) 
