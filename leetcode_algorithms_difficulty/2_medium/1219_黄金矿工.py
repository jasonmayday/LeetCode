"""
https://leetcode-cn.com/problems/path-with-maximum-gold/

你要开发一座金矿，地质勘测学家已经探明了这座金矿中的资源分布，并用大小为 m * n 的网格 grid 进行了标注。每个单元格中的整数就表示这一单元格中的黄金数量；如果该单元格是空的，那么就是 0。

为了使收益最大化，矿工需要按以下规则来开采黄金：
    每当矿工进入一个单元，就会收集该单元格中的所有黄金。
    矿工每次可以从当前位置向上下左右四个方向走。
    每个单元格只能被开采（进入）一次。
    不得开采（进入）黄金数目为 0 的单元格。
    矿工可以从网格中 任意一个 有黄金的单元格出发或者是停止。

示例 1：
    输入：grid = [[0,6,0],[5,8,7],[0,9,0]]
    输出：24
    解释：
       [[0,6,0],
        [5,8,7],
        [0,9,0]]
    一种收集最多黄金的路线是：9 -> 8 -> 7。

示例 2：
    输入：grid = [[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]
    输出：28
    解释：
       [[1,0,7],
        [2,0,6],
        [3,4,5],
        [0,3,0],
        [9,0,20]]
    一种收集最多黄金的路线是：1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7。

提示：
    1 <= grid.length, grid[i].length <= 15
    0 <= grid[i][j] <= 100
    最多 25 个单元格中有黄金。

"""
from typing import List

""" 回溯算法 """
class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m = len(grid)       # 行数
        n = len(grid[0])    # 列数
        res = 0
        
        def dfs(x, y, gold):
            record = grid[x][y]
            grid[x][y] = 0
            maxGold = gold + record
            for nx, ny in [[x, y-1], [x-1, y], [x, y+1], [x+1, y]]:     # 上下左右四个方向
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] != 0:   # 如果往某一个方向不会走出网格，并且走到的位置的值不为 0
                    maxGold = max(maxGold, dfs(nx, ny, gold + record))  # 就可以进行递归搜索
            grid[x][y] = record
            return maxGold
        
        def isCorner(x, y): # 只有角落的矿值得作为起点尝试，寻找角落的矿
            cnt = 0
            for nx, ny in [[x, y-1], [x-1, y], [x, y+1], [x+1, y]]:
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] != 0:
                    cnt += 1
            return cnt <= 2
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] and isCorner(i, j):
                    res = max(res, dfs(i, j, 0))
        return res

if __name__ == "__main__":
    grid = [[0,6,0],[5,8,7],[0,9,0]]
    difference = 2
    sol = Solution()
    result = sol.getMaximumGold(grid)
    print(result)  