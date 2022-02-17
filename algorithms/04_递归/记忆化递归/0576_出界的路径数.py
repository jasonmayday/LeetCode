"""
https://leetcode-cn.com/problems/out-of-boundary-paths/

给你一个大小为 m x n 的网格和一个球。球的起始坐标为 [startRow, startColumn] 。你可以将球移到在四个方向上相邻的单元格内（可以穿过网格边界到达网格之外）。你 最多 可以移动 maxMove 次球。

给你五个整数 m、n、maxMove、startRow 以及 startColumn ，找出并返回可以将球移出边界的路径数量。因为答案可能非常大，返回对 109 + 7 取余 后的结果。

示例 1：
    输入：m = 2, n = 2, maxMove = 2, startRow = 0, startColumn = 0
    输出：6

示例 2：
    输入：m = 1, n = 3, maxMove = 3, startRow = 0, startColumn = 1
    输出：12

提示：
    1 <= m, n <= 50
    0 <= maxMove <= 50
    0 <= startRow < m
    0 <= startColumn < n

"""
from functools import lru_cache

"""记忆化递归"""
class Solution:
    def findPaths(self, m: int, n: int, N: int, i: int, j: int) -> int:
        @lru_cache(None)
        def dfs(i, j, N):
            if i < 0 or i >= m or j < 0 or j >= n:
                return 1
            if N == 0:
                return 0
            
            return dfs(i + 1, j, N - 1) + dfs(i - 1, j, N - 1) + dfs(i, j + 1, N - 1) + dfs(i, j - 1, N - 1)
        
        return dfs(i, j, N) % (10 ** 9 + 7)

""" 动态规划 """
class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        res = 0
        dp = [[[0] * (n + 2) for _ in range(m + 2)] for _ in range(maxMove + 1)]
        # dp[k][r][c] 表示球移动 k 次之后位于坐标 (r, c) 的路径数量。
        for r in range(m + 2):
            dp[0][r][0] = 1
            dp[0][r][n + 1] = 1

        for c in range(n + 2):
            dp[0][0][c] = 1
            dp[0][m + 1][c] = 1

        for k in range(1, maxMove + 1):
            for r in range(1, m + 1):
                for c in range(1, n + 1):
                    dp[k][r][c] = dp[k - 1][r - 1][c] + dp[k - 1][r + 1][c] + dp[k - 1][r][c - 1] + dp[k - 1][r][c + 1]
        
        for k in range(1, maxMove + 1):
            res += dp[k][startRow + 1][startColumn + 1]
            
        return res % (10 ** 9 + 7)
    
""" 动态规划 """
class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        MOD = 10**9 + 7

        res = 0
        dp = [[[0] * n for _ in range(m)] for _ in range(maxMove + 1)]
        dp[0][startRow][startColumn] = 1    # dp[k][r][c] 表示球移动 k 次之后位于坐标 (r, c) 的路径数量。
        for k in range(maxMove):    # 步数
            for r in range(m):      # 行数
                for c in range(n):  # 列数
                    if dp[k][r][c] > 0:
                        for r_move, c_move in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:     # 四个方向搜索
                            if 0 <= r_move < m and 0 <= c_move < n:     # 不出界，在网格之内移动
                                dp[k + 1][r_move][c_move] = (dp[k + 1][r_move][c_move] + dp[k][r][c]) % MOD
                            else:
                                res = (res + dp[k][r][c]) % MOD
        return res


if __name__ == "__main__":
    m = 1
    n = 3
    maxMove = 3
    startRow = 0
    startColumn = 1
    sol = Solution()
    result = sol.findPaths(m, n, maxMove, startRow, startColumn)
    print(result)