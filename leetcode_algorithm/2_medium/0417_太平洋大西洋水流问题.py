"""
https://leetcode-cn.com/problems/pacific-atlantic-water-flow/

有一个 m × n 的矩形岛屿，与 太平洋 和 大西洋 相邻。 “太平洋” 处于大陆的左边界和上边界，而 “大西洋” 处于大陆的右边界和下边界。

这个岛被分割成一个由若干方形单元格组成的网格。给定一个 m x n 的整数矩阵 heights ， heights[r][c] 表示坐标 (r, c) 上单元格 高于海平面的高度 。

岛上雨水较多，如果相邻单元格的高度 小于或等于 当前单元格的高度，雨水可以直接向北、南、东、西流向相邻单元格。水可以从海洋附近的任何单元格流入海洋。

返回 网格坐标 result 的 2D列表 ，其中 result[i] = [ri, ci] 表示雨水可以从单元格 (ri, ci) 流向 太平洋和大西洋 。

示例 1：
    输入: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
    输出: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]

示例 2：
    输入: heights = [[2,1],[1,2]]
    输出: [[0,0],[0,1],[1,0],[1,1]]

提示：
    m == heights.length
    n == heights[r].length
    1 <= m, n <= 200
    0 <= heights[r][c] <= 10^5

"""
from typing import List

""" 一次BFS遍历所有坐标 """
class Solution(object):
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        def bfs(r, c, visited):
            queue = [(r, c)]
            visited.add((r, c))
            while queue:
                r, c = queue.pop(0)
                for x, y in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                    br, bc = r + x, c + y
                    if 0 <= br < row and 0 <= bc < col and heights[br][bc] >= heights[r][c] and (br, bc) not in visited:
                        queue.append((br, bc))
                        visited.add((br, bc))
        
        res = []
        row = len(heights)
        if not row: return res
        col = len(heights[0])
        visited_pacific = set()     # 存放能流入太平洋的坐标
        visited_atlantic = set()        # 存放能流入大西洋的坐标
        for r in range(row):
            bfs(r, 0, visited_pacific)
            bfs(r, col - 1, visited_atlantic)
        for c in range(col):
            bfs(0, c, visited_pacific)
            bfs(row - 1, c, visited_atlantic)
        res = list(visited_pacific & visited_atlantic)
        return res

""" 两次BFS分别遍历大西洋和太平洋的入海处 """
import collections
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        def pacific_BFS(start):     # 从太平洋出发反向流动，能到达的坐标存入集合 visited_pacific 中。
            queue = collections.deque()
            if start not in visited_pacific:
                queue.append(start)
                visited_pacific.add(start)
            while queue:
                nx, ny = queue.popleft()
                for x, y in [(nx+1, ny), (nx, ny+1), (nx-1, ny), (nx, ny-1)]:
                    if 0 <= x < len(heights) and 0 <= y < len(heights[0]) \
                        and heights[x][y] >= heights[nx][ny] \
                            and (x, y) not in visited_pacific:
                        queue.append((x, y))
                        visited_pacific.add((x, y))
        
        def atlantic_BFS(start):    # 从大西洋出发反向流动，能到达的坐标存入集合 visited_atlantic 中
            queue = collections.deque()
            if start not in visited_atlantic:
                queue.append(start)
                visited_atlantic.add(start)
            while queue:
                nx, ny = queue.popleft()
                for x, y in [(nx+1, ny), (nx, ny+1), (nx-1, ny), (nx, ny-1)]:
                    if 0 <= x < len(heights) and 0 <= y < len(heights[0]) \
                        and heights[x][y] >= heights[nx][ny] \
                            and (x, y) not in visited_atlantic:
                        queue.append((x, y))
                        visited_atlantic.add((x, y))
        
        visited_pacific = set()  # 存放能流向太平洋的坐标
        visited_atlantic = set() # 存放能流向大西洋的坐标
        for x in range(len(heights)):   # 只需要遍历海洋和陆地交界处（也就是矩阵外围一圈即可）。
            pacific_BFS((x, 0))
            atlantic_BFS((x, len(heights[0])-1))
        for y in range(len(heights[0])):
            pacific_BFS((0, y))
            atlantic_BFS((len(heights)-1, y))
        return list(visited_pacific & visited_atlantic) # 两个集合的交集就是答案。

""" DFS """
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        visited_pacific = set()
        visited_atlantic = set()
        if not heights or not heights[0]:
            return []
        row = len(heights)
        col = len(heights[0])
        def dfs(i, j, visited):
            visited.add((i, j))
            for x, y in [[+1, 0], [-1, 0], [0, +1], [0, -1]]:
                tmp_i = i + x
                tmp_j = j + y
                if 0 <= tmp_i < row and 0 <= tmp_j < col and (tmp_i,tmp_j) not in visited and heights[tmp_i][tmp_j] >= heights[i][j]:
                    dfs(tmp_i, tmp_j, visited)
            
        for i in range(row):
            dfs(i, 0, visited_pacific)
        for i in range(col):
            dfs(0, i, visited_pacific)
        for i in range(row):
            dfs(i, col-1, visited_atlantic)
        for i in range(col):
            dfs(row-1, i, visited_atlantic)
        return list(visited_pacific & visited_atlantic)
    
if __name__ == "__main__":
    heights = [[1,2,2,3,5],
               [3,2,3,4,4],
               [2,4,5,3,1],
               [6,7,1,4,5],
               [5,1,1,2,4]]
    sol = Solution()
    result = sol.pacificAtlantic(heights)
    print (result)