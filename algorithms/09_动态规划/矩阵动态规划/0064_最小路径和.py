"""
https://leetcode-cn.com/problems/minimum-path-sum/

给定一个包含非负整数的 m x n 网格 grid ，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

说明：每次只能向下或者向右移动一步。

示例 1：
    输入：grid = [[1,3,1],[1,5,1],[4,2,1]]
    输出：7
    解释：因为路径 1→3→1→1→1 的总和最小。

示例 2：
    输入：grid = [[1,2,3],[4,5,6]]
    输出：12

提示：
    m == grid.length
    n == grid[i].length
    1 <= m, n <= 200
    0 <= grid[i][j] <= 100

"""
from typing import List

""" 动态规划（原地修改）
    设 dp 为大小 m×n 矩阵，其中 dp[i][j] 的值代表直到走到 (i,j) 的最小路径和。
    不需要建立 dp 矩阵浪费额外空间，直接遍历 grid[i][j] 修改即可。"""
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int: 
        for i in range(len(grid)):          # i 为行数，j 为列数
            for j in range(len(grid[0])):   # 一行一行地遍历矩阵
                if i == j == 0:     # 当左边和上边都是矩阵边界时
                    continue        # 其实就是起点， dp[i][j] = grid[i][j]，不做加法
                elif i == 0:                                    # 当只有左边是矩阵边界时
                    grid[i][j] = grid[i][j-1] + grid[i][j]      # 只能从上面向下来：原地修改grid[i][j]，为上边数字和当前数字相加
                elif j == 0:                                    # 当只有上边是矩阵边界时
                    grid[i][j] = grid[i-1][j] + grid[i][j]      # 只能从左面向右来：原地修改grid[i][j]，为左边数字和当前数字相加
                else:                                                           # 当左边和上边都不是矩阵边界时
                    grid[i][j] = min(grid[i-1][j], grid[i][j-1]) + grid[i][j]   # 选取（）（）最小值
        return grid[-1][-1]

""" 动态规划（创建dp矩阵修改）"""
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        row = len(grid)
        col = len(grid[0])
        dp = [[0] * col for _ in range(row)]    # 创建 dp 矩阵，数值都初始为0
        dp[0][0] = grid[0][0]                   # 最左上角数字与原矩阵相同
        for i in range(1, row):                     # 第一列
            dp[i][0] = dp[i - 1][0] + grid[i][0]    # 为上边数字与当前数字相加
        for j in range(1, col):                     # 第一行
            dp[0][j] = dp[0][j - 1] + grid[0][j]    # 为左边数字与当前数字相加
        for i in range(1, row):
            for j in range(1, col):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        return dp[row - 1][col - 1]

if __name__ == "__main__":
    grid = [[1,3,1],
            [1,5,1],
            [4,2,1]]
    sol = Solution()
    result = sol.minPathSum(grid)
    print(result)