"""
https://leetcode-cn.com/problems/map-of-highest-peak/

给你一个大小为 m x n 的整数矩阵 isWater ，它代表了一个由 陆地 和 水域 单元格组成的地图。
    如果 isWater[i][j] == 0 ，格子 (i, j) 是一个 陆地 格子。
    如果 isWater[i][j] == 1 ，格子 (i, j) 是一个 水域 格子。

你需要按照如下规则给每个单元格安排高度：
    每个格子的高度都必须是非负的。
    如果一个格子是是 水域 ，那么它的高度必须为 0 。
    任意相邻的格子高度差 至多 为 1 。当两个格子在正东、南、西、北方向上相互紧挨着，就称它们为相邻的格子。（也就是说它们有一条公共边）

找到一种安排高度的方案，使得矩阵中的最高高度值 最大 。

请你返回一个大小为 m x n 的整数矩阵 height ，其中 height[i][j] 是格子 (i, j) 的高度。如果有多种解法，请返回 任意一个 。

示例 1：
    输入：isWater = [[0,1],[0,0]]
    输出：[[1,0],[2,1]]
    解释：上图展示了给各个格子安排的高度。
    蓝色格子是水域格，绿色格子是陆地格。

示例 2：
    输入：isWater = [[0,0,1],[1,0,0],[0,0,0]]
    输出：[[1,1,0],[0,1,1],[1,2,2]]
    解释：所有安排方案中，最高可行高度为 2 。
    任意安排方案中，只要最高高度为 2 且符合上述规则的，都为可行方案。

提示：
    m == isWater.length
    n == isWater[i].length
    1 <= m, n <= 1000
    isWater[i][j] 要么是 0 ，要么是 1 。
    至少有 1 个水域格子。

"""
from typing import List
from collections import deque

""" 多源广度优先搜索(BFS) """
class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        m = len(isWater)      # 行数
        n = len(isWater[0])   # 列数
        ans = [[0] * n for _ in range(m)]
        d = deque()
        for i in range(m):
            for j in range(n):
                if isWater[i][j]:   # 水域作为起点入队
                    d.append((i, j))
                ans[i][j] = 0 if isWater[i][j] else -1  #  没被访问过的陆地起始为-1，水域在答案里要求为0

        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        h = 1   #  初始高度（和水域相邻的点最高只能为1）
        while d:
            size = len(d)   # 当前队列的大小，因为遍历中要往队列里添加元素（下一层），这样写是必要的（避免当前层和下一层的遍历混淆）
            for _ in range(size):
                x, y = d.popleft()
                for di in dirs:
                    nx, ny = x + di[0], y + di[1]
                    if 0 <= nx < m and 0 <= ny < n and ans[nx][ny] == -1:
                        ans[nx][ny] = h # 目前是bfs到nx，ny这个点最近的方式了，也就是该点最高的高度
                        d.append((nx, ny))  # 作为下一层遍历的元素入队
            h += 1  # 陆地高度逐级累加
        return ans
    
""" 广度优先搜索(BFS) """
class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        m, n = len(isWater), len(isWater[0])
        
        # 初始化答案高度矩阵, 水域为 0，陆地为 -1 
        ans = [[isWater[i][j] - 1 for j in range(n)] for i in range(m)]

        # 记录下所有水域的位置
        water = deque((i, j) for i in range(m) for j in range(n) if isWater[i][j] == 1)
        # water = ([(0, 2), (1, 0)])
        
        # 从水域坐标开始，执行广度优先搜索，计算出所有陆地格子的高度，即为答案
        while water:
            i, j = water.popleft()    # 双端队列，队首元素（坐标）出队
            
            # 遍历坐标 (i, j) 的相邻坐标 (i, j + 1) - 上, (i, j - 1) - 下, (i - 1, j) - 左, (i + 1, j) - 右
            for x, y in ((i, j + 1), (i, j - 1), (i - 1, j), (i + 1, j)):

                # 确保坐标的合法性，且该坐标格子为未被安排高度的陆地（即未被访问的 -1）
                # 这里用高度为-1标记有没有遍历过即可，因为高度更新后必不为-1了，不用再专门用标记集合了
                if 0 <= x < m and 0 <= y < n and ans[x][y] == -1:
                    ans[x][y] = ans[i][j] + 1  # 由水域坐标开始广度优先遍历，格子的高度逐层递增
                    
                    # 将当前陆地格子坐标入队
                    water.append((x, y))

        return ans

if __name__ == "__main__":
    isWater = [[0,0,1],  #    [1, 1, 0]
               [1,0,0],  #  → [0, 1, 1]
               [0,0,0]]  #    [1, 2, 2]
    sol = Solution()
    result = sol.highestPeak(isWater)
    print(result)  