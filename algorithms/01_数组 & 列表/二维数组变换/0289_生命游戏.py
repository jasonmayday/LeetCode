"""
https://leetcode-cn.com/problems/game-of-life/

根据 百度百科 ， 生命游戏 ，简称为 生命 ，是英国数学家约翰·何顿·康威在 1970 年发明的细胞自动机。

给定一个包含 m × n 个格子的面板，每一个格子都可以看成是一个细胞。每个细胞都具有一个初始状态： 1 即为 活细胞 （live），或 0 即为 死细胞 （dead）。每个细胞与其八个相邻位置（水平，垂直，对角线）的细胞都遵循以下四条生存定律：
    1. 如果活细胞周围八个位置的活细胞数少于两个，则该位置活细胞死亡；
    2. 如果活细胞周围八个位置有两个或三个活细胞，则该位置活细胞仍然存活；
    3. 如果活细胞周围八个位置有超过三个活细胞，则该位置活细胞死亡；
    4. 如果死细胞周围正好有三个活细胞，则该位置死细胞复活；

下一个状态是通过将上述规则同时应用于当前状态下的每个细胞所形成的，其中细胞的出生和死亡是同时发生的。给你 m x n 网格面板 board 的当前状态，返回下一个状态。

示例 1：
    输入：board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
    输出：[[0,0,0],[1,0,1],[0,1,1],[0,1,0]]

示例 2：
    输入：board = [[1,1],[1,0]]
    输出：[[1,1],[1,1]]

提示：
    m == board.length
    n == board[i].length
    1 <= m, n <= 25
    board[i][j] 为 0 或 1

进阶：
    你可以使用原地算法解决本题吗？请注意，面板上所有格子需要同时被更新：你不能先更新某些格子，然后使用它们的更新后的值再更新其他格子。
    本题中，我们使用二维数组来表示面板。原则上，面板是无限的，但当活细胞侵占了面板边界时会造成问题。你将如何解决这些问题？

"""
from typing import List
import numpy as np

""" 卷积 """
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        r = len(board)      # 行数
        c = len(board[0])   # 列数
        # 初始化 zero padding，如果不在原始的 board 的周围补零，对于 board 最外围的一圈值处理起来比较麻烦，而通过补零我们可以统一进行处理
        board_exp = np.array([[0 for _ in range(c + 2)] for _ in range(r + 2)])
        print('board_exp: ', board_exp)
        # 把 board 的数值加进 board_exp
        board_exp[1:1 + r, 1:1 + c] = np.array(board)
        print('board_exp: ', board_exp)

        # 设置卷积核
        kernel = np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]])

        # 开始卷积
        for i in range(1, r + 1):
            for j in range(1, c + 1):
                # 统计细胞周围 8 个位置的状态
                temp_sum = np.sum(kernel * board_exp[i - 1:i + 2, j - 1:j + 2])
                # 按照题目规则进行判断
                if board_exp[i, j] == 1:
                    if temp_sum < 2 or temp_sum > 3:
                        board[i - 1][j - 1] = 0
                else:
                    if temp_sum == 3:
                        board[i - 1][j - 1] = 1
        return board

if __name__ == "__main__":
    board = [[0,1,0],
             [0,0,1],
             [1,1,1],
             [0,0,0]]
    sol = Solution()
    result = sol.gameOfLife(board)
    print (result)