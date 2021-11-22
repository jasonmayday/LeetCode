"""
https://leetcode-cn.com/problems/available-captures-for-rook/

在一个 8 x 8 的棋盘上，有一个白色的车（Rook），用字符 'R' 表示。棋盘上还可能存在空方块，白色的象（Bishop）以及黑色的卒（pawn），分别用字符 '.'，'B' 和 'p' 表示。不难看出，大写字符表示的是白棋，小写字符表示的是黑棋。

车按国际象棋中的规则移动。东，西，南，北四个基本方向任选其一，然后一直向选定的方向移动，直到满足下列四个条件之一：
    棋手选择主动停下来。
    棋子因到达棋盘的边缘而停下。
    棋子移动到某一方格来捕获位于该方格上敌方（黑色）的卒，停在该方格内。
    车不能进入/越过已经放有其他友方棋子（白色的象）的方格，停在友方棋子前。

你现在可以控制车移动一次，请你统计有多少敌方的卒处于你的捕获范围内（即，可以被一步捕获的棋子数）。

示例 1：
    输入：[[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","R",".",".",".","p"],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]
    输出：3
    解释：
    在本例中，车能够捕获所有的卒。
    
示例 2：
    输入：[[".",".",".",".",".",".",".","."],[".","p","p","p","p","p",".","."],[".","p","p","B","p","p",".","."],[".","p","B","R","B","p",".","."],[".","p","p","B","p","p",".","."],[".","p","p","p","p","p",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]
    输出：0
    解释：
    象阻止了车捕获任何卒。

示例 3：
    输入：[[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","p",".",".",".","."],["p","p",".","R",".","p","B","."],[".",".",".",".",".",".",".","."],[".",".",".","B",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."]]
    输出：3
    解释： 
    车可以捕获位置 b5，d6 和 f5 的卒。
 
提示：
    board.length == board[i].length == 8
    board[i][j] 可以是 'R'，'.'，'B' 或 'p'
    只有一个格子上存在 board[i][j] == 'R'

"""
class Solution(object):
    def numRookCaptures(self, board):
        #第一种上下左右匹配，for循环解题
        
        for i in range(len(board)):
            if 'R' in board[i]:
                raw = i
                break
        colum = board[raw].index('R')
        
        result = 0
        #第一种上下左右匹配，for循环解题
        
        #计算上面
        for i in range(raw-1,-1,-1):
            if board[i][colum] !='.' and board[i][colum] == 'p':
                result += 1
                break
            elif board[i][colum] !='.' and board[i][colum] == 'B':
                break
        
        #计算下面
        for i in range(raw+1,8):
            if board[i][colum] !='.' and board[i][colum] == 'p':
                result += 1
                break
            elif board[i][colum] !='.' and board[i][colum] == 'B':
                break
        
        #计算左面
        for i in range(colum-1,-1,-1):
            if board[raw][i] !='.' and board[raw][i] == 'p':
                result += 1
                break
            elif board[raw][i] !='.' and board[raw][i] == 'B':
                break        
                
        #计算右面
        for i in range(colum+1,8):
            if board[raw][i] !='.' and board[raw][i] == 'p':
                result += 1
                break
            elif board[raw][i] !='.' and board[raw][i] == 'B':
                break        
        
        return result

作者：xiao-xue-66
链接：https://leetcode-cn.com/problems/available-captures-for-rook/solution/pythonti-jie-liang-chong-fang-shi-shi-xian-su-du-j/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。