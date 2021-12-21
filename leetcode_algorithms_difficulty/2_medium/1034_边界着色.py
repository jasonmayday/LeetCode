"""
https://leetcode-cn.com/problems/coloring-a-border/

给你一个大小为 m x n 的整数矩阵 grid ，表示一个网格。另给你三个整数 row、col 和 color 。网格中的每个值表示该位置处的网格块的颜色。

当两个网格块的颜色相同，而且在四个方向中任意一个方向上相邻时，它们属于同一 连通分量 。

连通分量的边界 是指连通分量中的所有与不在分量中的网格块相邻（四个方向上）的所有网格块，或者在网格的边界上（第一行/列或最后一行/列）的所有网格块。

请你使用指定颜色 color 为所有包含网格块 grid[row][col] 的 连通分量的边界 进行着色，并返回最终的网格 grid 。

示例 1：
    输入：grid = [[1,1],[1,2]], row = 0, col = 0, color = 3
    输出：[[3,3],[3,2]]

示例 2：
    输入：grid = [[1,2,2],[2,3,2]], row = 0, col = 1, color = 3
    输出：[[1,3,3],[2,3,3]]

示例 3：
    输入：grid = [[1,1,1],[1,1,1],[1,1,1]], row = 1, col = 1, color = 2
    输出：[[2,2,2],[2,1,2],[2,2,2]]

提示：
    m == grid.length
    n == grid[i].length
    1 <= m, n <= 50
    1 <= grid[i][j], color <= 1000
    0 <= row < m
    0 <= col < n

"""
from typing import List

class Solution(object):
    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        old_color = grid[row][col]
        new_color = color
        n, m = len(grid), len(grid[0])
        seen = set()
        
        def dfs(i,j):
            if (i,j) in seen: return True
            if not (0 <= i < n and 0 <= j < m and grid[i][j] == old_color):
                return False
            seen.add((i,j))
            if  dfs(i+1, j) + dfs(i-1, j) + dfs(i, j+1) + dfs(i, j-1) < 4:
                grid[i][j] = new_color
            return True
        
        dfs(row, col)
        return grid
    
if __name__ == "__main__":
    grid = [[1,1,1],[1,1,1],[1,1,1]]; row = 1; col = 1; color = 2
    sol = Solution()
    result = sol.colorBorder(grid, row, col, color)
    print(result)