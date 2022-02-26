"""
https://leetcode-cn.com/problems/number-of-islands/

给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。

岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。

此外，你可以假设该网格的四条边均被水包围。

示例 1：
    输入：grid = [
    ["1","1","1","1","0"],
    ["1","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
    ]
    输出：1

示例 2：
    输入：grid = [
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
    ]
    输出：3

提示：
    m == grid.length
    n == grid[i].length
    1 <= m, n <= 300
    grid[i][j] 的值为 '0' 或 '1'

"""
from typing import List

"""思路一：深度优先遍历DFS"""
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(grid, i, j):    # dfs方法： 设目前指针指向一个岛屿中的某一点 (i, j)，寻找包括此点的岛屿边界。
            if not 0 <= i < len(grid) or not 0 <= j < len(grid[0]) or grid[i][j] == '0':    # dfs 终止条件
                return          # 终止条件：(i, j) 越过矩阵边界; grid[i][j] == 0，代表此分支已越过岛屿边界。
            grid[i][j] = '0'    # 将岛屿所有节点删除，以免之后重复搜索相同岛屿。
            dfs(grid, i + 1, j)     # 下
            dfs(grid, i, j + 1)     # 右
            dfs(grid, i - 1, j)     # 上
            dfs(grid, i, j - 1)     # 左
        
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):   # 遍历整个矩阵
                if grid[i][j] == '1':   # 遇到陆地：
                    dfs(grid, i, j)     # 开始做深度优先搜索 dfs
                    count += 1          # 岛屿数 +1
        return count


"""思路二：广度优先遍历 BFS"""
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def bfs(grid, i, j):
            queue = [[i, j]]    # 借用一个队列 queue，判断队列首部节点 (i, j) 是否未越界且为 1
            while queue:
                [i, j] = queue.pop(0)   # 循环 pop 队列首节点，直到整个队列为空，此时已经遍历完此岛屿。
                if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == '1':  # 若是岛屿
                    grid[i][j] = '0'        # 则置零（删除岛屿节点）
                    queue += [[i+1, j], [i-1, j], [i, j-1], [i, j + 1]]   # 并将此节点上下左右节点加入队列；
        
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '0': continue
                bfs(grid, i, j)
                count += 1
        return count


if __name__ == "__main__":
    grid = [["1","1","0","0","0"],
            ["1","1","0","0","0"],
            ["0","0","1","0","0"],
            ["0","0","0","1","1"]]
    sol = Solution()
    result = sol.rob(grid)
    print (result)

