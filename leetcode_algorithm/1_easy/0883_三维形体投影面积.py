"""
https://leetcode-cn.com/problems/projection-area-of-3d-shapes/

在 N * N 的网格中，我们放置了一些与 x，y，z 三轴对齐的 1 * 1 * 1 立方体。

每个值 v = grid[i][j] 表示 v 个正方体叠放在单元格 (i, j) 上。

现在，我们查看这些立方体在 xy、yz 和 zx 平面上的投影。

投影就像影子，将三维形体映射到一个二维平面上。

在这里，从顶部、前面和侧面看立方体时，我们会看到“影子”。

返回所有三个投影的总面积。

示例 1：
    输入：[[2]]
    输出：5

示例 2：
    输入：[[1,2],[3,4]]
    输出：17
    解释：
    这里有该形体在三个轴对齐平面上的三个投影(“阴影部分”)。

示例 3：
    输入：[[1,0],[0,2]]
    输出：8

示例 4：
    输入：[[1,1,1],[1,0,1],[1,1,1]]
    输出：14

示例 5：
    输入：[[2,2,2],[2,1,2],[2,2,2]]
    输出：21

提示：
    1 <= grid.length = grid[0].length <= 50
    0 <= grid[i][j] <= 50

"""
from typing import List

"""解法1"""
class Solution:
    def projectionArea(self, grid):
        N = len(grid)
        ans = 0
        for i in range(N):
            best_row = 0  # max of grid[i][j]
            best_col = 0  # max of grid[j][i]
            for j in range(N):
                if grid[i][j]: ans += 1  # top shadow
                best_row = max(best_row, grid[i][j])
                best_col = max(best_col, grid[j][i])
            ans += best_row + best_col
        return ans

"""解法2"""
class Solution:
    def projectionArea(self, grid):
        ans =  sum(map(max, zip(*grid)))                # 从前面看，由该形状生成的阴影将是网格中每一列的最大值。
        ans += sum(map(max, grid))                      # 从侧面看，由该形状生成的阴影将是网格中每一行的最大值。
        ans += sum(v > 0 for row in grid for v in row)  # 从顶部看，由该形状生成的阴影将是网格中非零值的数目。
        return ans

"""解法3"""
class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        ans =  sum([max(a) for a in zip(*grid)])    # x 的投影：从前面看，由该形状生成的阴影将是网格中每一列的最大值。
        ans += sum([max(b) for b in grid])          # y 的投影：从侧面看，由该形状生成的阴影将是网格中每一行的最大值。
        ans += sum(k > 0 for k in sum(grid, []))    # z 的投影：从顶部看，由该形状生成的阴影将是网格中非零值的数目。
        return ans

if __name__ == "__main__":
    grid = [[2,2,2],[2,1,2],[2,2,2]]
    sol = Solution()
    result = sol.projectionArea(grid)
    print(result)