"""
https://leetcode-cn.com/problems/surrounded-regions/

给你一个 m x n 的矩阵 board ，由若干字符 'X' 和 'O' ，找到所有被 'X' 围绕的区域，并将这些区域里所有的 'O' 用 'X' 填充。

示例 1：
    输入：board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
    输出：[["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
    解释：被围绕的区间不会存在于边界上，换句话说，任何边界上的 'O' 都不会被填充为 'X'。 任何不在边界上，或不与边界上的 'O' 相连的 'O' 最终都会被填充为 'X'。如果两个元素在水平或垂直方向相邻，则称它们是“相连”的。

示例 2：
    输入：board = [["X"]]
    输出：[["X"]]

提示：
    m == board.length
    n == board[i].length
    1 <= m, n <= 200
    board[i][j] 为 'X' 或 'O'

"""
from typing import List

"""思路一: DFS"""
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board or not board[0]:
            return
        row = len(board)    # 行数
        col = len(board[0]) # 列数
        
        """ dfs函数1 """
        def dfs(i, j):  # 
            board[i][j] = "B"
            for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]: # 上下左右四个方向
                tmp_i = i + x
                tmp_j = j + y
                # 需要被填充的，不越界条件：第二 (行/列) 到 倒数第二 (行/列)，并且为 "O"
                if 1 <= tmp_i < row and 1 <= tmp_j < col and board[tmp_i][tmp_j] == "O":
                    dfs(tmp_i, tmp_j)
        
        """ dfs函数2 """
        def dfs(i, j):
            # 如果i，j中有一个越界或者遇到了X则不继续扫描
            if i < 0 or j < 0 or i >= row or j >= col or board[i][j] != 'O':
                return
            board[i][j] = 'B'   # 否则把数组中的 "O" 变成 "B" ，意思是这个 "O" 和边缘是连通的
            dfs(i-1, j)         # 之后从当前坐标开始上下左右进行递归搜索
            dfs(i+1, j)
            dfs(i, j-1)
            dfs(i, j+1)

        for j in range(col):            # 把第一行和最后一行的 "O" 变为 临时的 "B"
            if board[0][j] == "O":      # 第一行
                dfs(0, j)
            if board[row-1][j] == "O":  # 最后一行
                dfs(row-1, j)

        for i in range(row):            # 把第一列和最后一列的 "O" 变为 临时的 "B"
            if board[i][0] == "O":      # 第一列
                dfs(i, 0)
            if board[i][col-1] == "O":  # 最后一列
                dfs(i, col-1)

        for i in range(row):        # 因为边界的 "O" 已经变为临时的 "B"，所以不用担心越界
            for j in range(col):
                if board[i][j] == "O":  # 填充被围绕的 "O"
                    board[i][j] = "X"
                if board[i][j] == "B":  # 回复临时编成 "B" 的 "O"
                    board[i][j] = "O"


"""思路二: BFS"""
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board or not board[0]:
            return
        row = len(board)
        col = len(board[0])

        def bfs(i, j):
            from collections import deque
            queue = deque()
            queue.appendleft((i, j))
            while queue:
                i, j = queue.pop()
                if 0 <= i < row and 0 <= j < col and board[i][j] == "O":
                    board[i][j] = "B"
                    for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        queue.appendleft((i + x, j + y))

        for j in range(col):
            # 第一行
            if board[0][j] == "O":
                bfs(0, j)
            # 最后一行
            if board[row - 1][j] == "O":
                bfs(row - 1, j)

        for i in range(row):

            if board[i][0] == "O":
                bfs(i, 0)
            if board[i][col - 1] == "O":
                bfs(i, col - 1)

        for i in range(row):
            for j in range(col):
                if board[i][j] == "O":
                    board[i][j] = "X"
                if board[i][j] == "B":
                    board[i][j] = "O"


"""思路三 : 并查集"""
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        f = {}
        def find(x):
            f.setdefault(x, x)
            if f[x] != x:
                f[x] = find(f[x])
            return f[x]
        def union(x, y):
            f[find(y)] = find(x)

            
        if not board or not board[0]:
            return
        row = len(board)
        col = len(board[0])
        dummy = row * col
        for i in range(row):
            for j in range(col):
                if board[i][j] == "O":
                    if i == 0 or i == row - 1 or j == 0 or j == col - 1:
                        union(i * col + j, dummy)
                    else:
                        for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                            if board[i + x][j + y] == "O":
                                union(i * col + j, (i + x) * col + (j + y))
        for i in range(row):
            for j in range(col):
                if find(dummy) == find(i * col + j):
                    board[i][j] = "O"
                else:
                    board[i][j] = "X"
        return board


if __name__ == "__main__":
    board = [["X","X","X","X"],     # ['X', 'X', 'X', 'X']
             ["X","O","O","X"],     # ['X', 'X', 'X', 'X']
             ["X","X","O","X"],     # ['X', 'X', 'X', 'X']
             ["X","O","X","X"]]     # ['X', 'O', 'X', 'X']
    sol = Solution()
    result = sol.solve(board)
    print(result)