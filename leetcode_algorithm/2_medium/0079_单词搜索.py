"""
https://leetcode-cn.com/problems/word-search/

给定一个 m x n 二维字符网格 board 和一个字符串单词 word 。如果 word 存在于网格中，返回 true ；否则，返回 false 。

单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。

示例 1：
    输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
    输出：true

示例 2：
    输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
    输出：true

示例 3：
    输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
    输出：false

提示：
    m == board.length
    n = board[i].length
    1 <= m, n <= 6
    1 <= word.length <= 15
    board 和 word 仅由大小写英文字母组成

进阶：你可以使用搜索剪枝的技术来优化解决方案，使其在 board 更大的情况下可以更快解决问题？

"""
from typing import List

""" 回溯 """
class Solution(object):
    directs = [(0, 1), (0, -1), (1, 0), (-1, 0)]    # 定义上下左右四个行走方向
    
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        if m == 0:
            return False
        n = len(board[0])
        mark = [[0 for _ in range(n)] for _ in range(m)]    # 用二维数组 mark 对使用过的元素做标记。初始化为 0
                
        for i in range(len(board)):
            for j in range(len(board[0])):  # 首先遍历 board 的所有元素，
                if board[i][j] == word[0]:  # 先找到和 word 第一个字母相同的元素
                    mark[i][j] = 1          # 将该元素标记为已使用
                    if self.backtrack(i, j, mark, board, word[1:]) == True: # 从 (i, j) 出发，朝它的上下左右试探，看看它周边的这四个元素是否能匹配 word 的下一个字母
                        return True 
                    else:                   # 如果匹配不到
                        mark[i][j] = 0      # 回溯
        return False
        
    def backtrack(self, i, j, mark, board, word):
        if len(word) == 0:
            return True
        
        for direct in self.directs:
            cur_i = i + direct[0]
            cur_j = j + direct[1]
            
            if cur_i >= 0 and cur_i < len(board) and cur_j >= 0 and cur_j < len(board[0]) and board[cur_i][cur_j] == word[0]:
                if mark[cur_i][cur_j] == 1:     # 如果是已经使用过的元素，忽略
                    continue
                mark[cur_i][cur_j] = 1          # 将该元素标记为已使用
                if self.backtrack(cur_i, cur_j, mark, board, word[1:]) == True:
                    return True
                else:
                    mark[cur_i][cur_j] = 0      # 回溯
        return False

if __name__ == "__main__":
    board = [["A","B","C","E"],
             ["S","F","C","S"],
             ["A","D","E","E"]]
    word = "ABCCED"
    sol = Solution()
    result = sol.exist(board, word)
    print(result)