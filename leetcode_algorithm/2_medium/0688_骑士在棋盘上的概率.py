"""
https://leetcode-cn.com/problems/knight-probability-in-chessboard/

在一个 n x n 的国际象棋棋盘上，一个骑士从单元格 (row, column) 开始，并尝试进行 k 次移动。行和列是 从 0 开始 的，所以左上单元格是 (0,0) ，右下单元格是 (n - 1, n - 1) 。

象棋骑士有8种可能的走法，如下图所示。每次移动在基本方向上是两个单元格，然后在正交方向上是一个单元格。

每次骑士要移动时，它都会随机从8种可能的移动中选择一种(即使棋子会离开棋盘)，然后移动到那里。

骑士继续移动，直到它走了 k 步或离开了棋盘。

返回 骑士在棋盘停止移动后仍留在棋盘上的概率 。

示例 1：
    输入: n = 3, k = 2, row = 0, column = 0
    输出: 0.0625
    解释: 有两步(到(1,2)，(2,1))可以让骑士留在棋盘上。
        在每一个位置上，也有两种移动可以让骑士留在棋盘上。
        骑士留在棋盘上的总概率是0.0625。

示例 2：
    输入: n = 1, k = 0, row = 0, column = 0
    输出: 1.00000

提示:
    1 <= n <= 25
    0 <= k <= 100
    0 <= row, column <= n

"""

""" 动态规划 """
class Solution:
    def knightProbability(self, n: int, k: int, r: int, c: int) -> float:
        dp = [[0] * n for _ in range(n)]    # dp[i][j]： 位置(i, j)有马的概率
        dp[r][c] = 1                        # 初始化状态：dp[r][c] = 1
        for _ in range(k):
            nxt = [[0] * n for _ in range(n)]   # 用两个dp数组，dp 记录当前概率，nxt 记录移动一次以后的概率
            for i in range(n):                  # (x, y) 是移动后位置，(i, j) 是移动前位置
                for j in range(n):
                    for x, y in ((i+2, j+1), (i+2, j-1), (i-2, j+1), (i-2, j-1), 
                                 (i+1, j+2), (i-1, j+2), (i+1, j-2), (i-1, j-2)):
                        if 0 <= x < n and 0 <= y < n:
                            nxt[x][y] += dp[i][j] / 8   #  (i, j) 有 1/8 的概率移动到 (x, y)
            dp = nxt
        return sum(map(sum, dp))    # 返回 dp 所有位置的概率和


""" 动态规划 """
class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        # dp[step][i][j] 表示骑士从棋盘上的点 (i, j)(i,j) 出发，走了 step 步时仍然留在棋盘上的概率。
        # 当点 (i,j) 不在棋盘上时，dp[step][i][j] = 0；当点 (i,j) 在棋盘上且 step=0 时，[step][i][j] = 1。
        dp = [[[0] * n for _ in range(n)] for _ in range(k + 1)]
        for step in range(k + 1):
            for i in range(n):
                for j in range(n):
                    if step == 0:
                        dp[step][i][j] = 1
                    else:
                        for di, dj in ((-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2)):
                            ni = i + di # (di,dj) 表示走法对坐标的偏移量
                            nj = j + dj
                            if 0 <= ni < n and 0 <= nj < n:
                                dp[step][i][j] += dp[step - 1][ni][nj] / 8
        return dp[k][row][column]


if __name__ == "__main__":
    n = 3
    k = 2
    row = 0
    column = 0
    sol = Solution()
    result = sol.knightProbability(n, k, row, column)
    print (result)