"""
https://leetcode-cn.com/problems/number-of-enclaves/https://leetcode-cn.com/problems/number-of-enclaves/

给你一个大小为 m x n 的二进制矩阵 grid ，其中 0 表示一个海洋单元格、1 表示一个陆地单元格。

一次 移动 是指从一个陆地单元格走到另一个相邻（上、下、左、右）的陆地单元格或跨过 grid 的边界。

返回网格中 无法 在任意次数的移动中离开网格边界的陆地单元格的数量。

示例 1：
    输入：grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
    输出：3
    解释：有三个 1 被 0 包围。一个 1 没有被包围，因为它在边界上。

示例 2：
    输入：grid = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
    输出：0
    解释：所有 1 都在边界上或可以到达边界。

提示：
    m == grid.length
    n == grid[i].length
    1 <= m, n <= 500
    grid[i][j] 的值为 0 或 1

"""
from typing import List
from collections import deque


""" 方法一：深度优先搜索
    0从四周临边的1开始把所有相连的1都变为，最后统计grid中1的数量"""
class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:

        def dfs(i, j):  # 从某点开始搜索
            grid[i][j] = 0
            for x, y in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:      # 向四个方向搜索
                if 0 <= x < m and 0 <= y < n and grid[x][y]:    # 定义边界：不越界且有数值
                    dfs(x, y)

        m, n = len(grid), len(grid[0])

        for i in range(m):                      # 从四周临边的1开始把所有相连的 1 都变为 0
            if grid[i][0] == 1:    dfs(i, 0)    # 第一列
            if grid[i][n-1] == 1:  dfs(i, n-1)  # 最后一列

        for j in range(n):
            if grid[0][j] == 1:    dfs(0, j)    # 第一行
            if grid[m-1][j] == 1:  dfs(m-1, j)  # 最后一行

        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]: ans += 1     # 统计grid中1的数量
        return ans



""" 方法二：广度优先搜索
    通过广度优先搜索判断每个陆地单元格是否和网格边界相连。"""
class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        def bfs(i, j):
            grid[i][j] = 0
            Q = deque([[i, j]])
            while Q:
                i, j = Q.popleft()
                for x, y in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
                    if 0 <= x < m and 0 <= y < n and grid[x][y]:
                        grid[x][y] = 0
                        Q.append([x, y])

        m, n = len(grid), len(grid[0])
        for i in range(m):
            if grid[i][0] == 1:    bfs(i, 0)
            if grid[i][n-1] == 1:  bfs(i, n-1)   
        for j in range(n):
            if grid[0][j] == 1:    bfs(0, j)
            if grid[m-1][j] == 1:  bfs(m-1, j)
                
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]: ans += 1
        return ans



if __name__ == "__main__":
    grid = [[0,0,0,0],
            [1,0,1,0],
            [0,1,1,0],
            [0,0,0,0]]
    sol = Solution()
    result = sol.numEnclaves(grid)
    print(result)