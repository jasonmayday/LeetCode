'''
https://leetcode-cn.com/problems/trapping-rain-water-ii/

给你一个 m x n 的矩阵，其中的值均为非负整数，代表二维高度图每个单元的高度，请计算图中形状最多能接多少体积的雨水。

示例 1:
    输入: heightMap = [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]
    输出: 4
    解释: 下雨后，雨水将会被上图蓝色的方块中。总的接雨水量为1+2+1=4。

示例 2:
    输入: heightMap = [[3,3,3,3,3],[3,2,2,2,3],[3,2,1,2,3],[3,2,2,2,3],[3,3,3,3,3]]
    输出: 10

提示:
    m == heightMap.length
    n == heightMap[i].length
    1 <= m, n <= 200
    0 <= heightMap[i][j] <= 2 * 10^4

'''

heightMap = [[3,3,3,3,3],[3,2,2,2,3],[3,2,1,2,3],[3,2,2,2,3],[3,3,3,3,3]]

from heapq import *
from typing import List

class Solution: # https://www.youtube.com/watch?v=cJayBq38VYw
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        """
        水从高出往低处流，某个位置储水量取决于四周最低高度，从最外层向里层包抄，用小顶堆动态找到未访问位置最小的高度
        """
        if not heightMap:return 0
        imax = float('-inf')
        ans = 0
        heap = []
        visited = set()
        row = len(heightMap)
        col = len(heightMap[0])
        # 将最外层放入小顶堆
        # 第一行和最后一行
        for j in range(col):
            # 将该位置的高度、横纵坐标插入堆
            heappush(heap, [heightMap[0][j], 0, j])  
            heappush(heap, [heightMap[row - 1][j], row - 1, j])
            visited.add((0, j))
            visited.add((row - 1, j))
        # 第一列和最后一列
        for i in range(row):
            heappush(heap, [heightMap[i][0], i, 0])
            heappush(heap, [heightMap[i][col - 1], i, col - 1])
            visited.add((i, 0))
            visited.add((i, col - 1))
        while heap:
            h, i, j = heappop(heap)
            # 之前最低高度的四周已经探索过了，所以要更新为次低高度开始探索
            imax = max(imax, h)  
            # 从堆顶元素出发，探索四周储水位置
            for x, y in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                tmp_x = x + i 
                tmp_y = y + j
                # 是否到达边界
                if tmp_x < 0 or tmp_y < 0 or tmp_x >= row or tmp_y >= col or (tmp_x, tmp_y) in visited:
                    continue
                visited.add((tmp_x, tmp_y))
                if heightMap[tmp_x][tmp_y] < imax:
                    ans += imax - heightMap[tmp_x][tmp_y]
                heappush(heap, [heightMap[tmp_x][tmp_y], tmp_x, tmp_y])
        return ans

sol = Solution()
result = sol.trapRainWater(heightMap)
print(result)