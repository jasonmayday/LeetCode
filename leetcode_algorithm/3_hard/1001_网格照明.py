"""
https://leetcode-cn.com/problems/grid-illumination/

在大小为 n x n 的网格 grid 上，每个单元格都有一盏灯，最初灯都处于 关闭 状态。

给你一个由灯的位置组成的二维数组 lamps ，其中 lamps[i] = [rowi, coli] 表示 打开 位于 grid[rowi][coli] 的灯。即便同一盏灯可能在 lamps 中多次列出，不会影响这盏灯处于 打开 状态。

当一盏灯处于打开状态，它将会照亮 自身所在单元格 以及同一 行 、同一 列 和两条 对角线 上的 所有其他单元格 。

另给你一个二维数组 queries ，其中 queries[j] = [rowj, colj] 。对于第 j 个查询，如果单元格 [rowj, colj] 是被照亮的，则查询结果为 1 ，否则为 0 。在第 j 次查询之后 [按照查询的顺序] ，关闭 位于单元格 grid[rowj][colj] 上及相邻 8 个方向上（与单元格 grid[rowi][coli] 共享角或边）的任何灯。

返回一个整数数组 ans 作为答案， ans[j] 应等于第 j 次查询 queries[j] 的结果，1 表示照亮，0 表示未照亮。

示例 1：
    输入：n = 5, lamps = [[0,0],[4,4]], queries = [[1,1],[1,0]]
    输出：[1,0]
    解释：最初所有灯都是关闭的。在执行查询之前，打开位于 [0, 0] 和 [4, 4] 的灯。
    第 0 次查询检查 grid[1][1] 是否被照亮（蓝色方框）。该单元格被照亮，所以 ans[0] = 1 。然后，关闭红色方框中的所有灯。
    第 1 次查询检查 grid[1][0] 是否被照亮（蓝色方框）。该单元格没有被照亮，所以 ans[1] = 0 。然后，关闭红色矩形中的所有灯。

示例 2：
    输入：n = 5, lamps = [[0,0],[4,4]], queries = [[1,1],[1,1]]
    输出：[1,1]

示例 3：
    输入：n = 5, lamps = [[0,0],[0,4]], queries = [[0,4],[0,1],[1,4]]
    输出：[1,1,0]

提示：
    1 <= n <= 10^9
    0 <= lamps.length <= 20000
    0 <= queries.length <= 20000
    lamps[i].length == 2
    0 <= rowi, coli < n
    queries[j].length == 2
    0 <= rowj, colj < n

"""
from typing import List
from collections import Counter

"""方法一：哈希表"""
class Solution:
    def gridIllumination(self, n: int, lamps: List[List[int]], queries: List[List[int]]) -> List[int]:
        points = set()            # 需要进行去重，因为我们将重复的灯看作同一盏灯。
        row = Counter()           # 行直线
        col = Counter()           # 列直线
        diagonal = Counter()      # 正对角线
        antiDiagonal = Counter()  # 反对角线
        
        for r, c in lamps:  # 将网格转换成一个坐标系，行下标作为 x 坐标，列下标作为 y 坐标
            if (r, c) in points:    # 已经在points中，则继续
                continue
            points.add((r, c))      # 遍历 lamps，将当前遍历到的灯所在的行，列和正/反对角线拥有灯的数目分别加一
            row[r] += 1             # 它所在的行的数值为 xi
            col[c] += 1             # 列的数值为 yi
            diagonal[r-c] += 1      # 正对角线的数值为 xi - yi
            antiDiagonal[r+c] += 1  # 反对角线的数值为 xi + yi

        ans = [0] * len(queries)    # [0,0]
        
        ''' 判断某点在被查询时是否被照亮'''
        for i, (r, c) in enumerate(queries):
            if row[r] or col[c] or diagonal[r-c] or antiDiagonal[r+c]:  # 遍历 queries，判断当前查询点所在的行，列和正/反对角线是否有灯
                ans[i] = 1                                              # 如果有, 则置 1, 即该点在查询时是被照亮的。
            ''' 关闭 位于查询单元格上及相邻 8 个方向上的灯 '''
            for x in range(r - 1, r + 2):
                for y in range(c - 1, c + 2):
                    if x < 0 or y < 0 or x >= n or y >= n or (x, y) not in points:  # 查找查询点所在的八近邻点及它本身是否有灯
                        continue            # 如果无灯，则继续
                    points.remove((x, y))   # 如果有灯，则将灯从网格中去掉。
                    row[x] -= 1             # 并且将该点所在的行，列和正/反对角线的灯数目分别减一
                    col[y] -= 1
                    diagonal[x - y] -= 1
                    antiDiagonal[x + y] -= 1
        return ans

if __name__ == "__main__":
    n = 5
    lamps = [[0,0],[4,4]]
    queries = [[1,1],[1,0]]
    sol = Solution()
    result = sol.gridIllumination(n, lamps, queries)
    print(result)
