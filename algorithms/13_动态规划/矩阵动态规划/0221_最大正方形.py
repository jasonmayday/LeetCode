"""
https://leetcode-cn.com/problems/maximal-square/

在一个由 '0' 和 '1' 组成的二维矩阵内，找到只包含 '1' 的最大正方形，并返回其面积。

示例 1：
    输入：matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
    输出：4

示例 2：
    输入：matrix = [["0","1"],["1","0"]]
    输出：1

示例 3：
    输入：matrix = [["0"]]
    输出：0

提示：
    m == matrix.length
    n == matrix[i].length
    1 <= m, n <= 300
    matrix[i][j] 为 '0' 或 '1'

"""
from typing import List

""" 方法一：暴力法"""

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        
        maxSide = 0
        rows, columns = len(matrix), len(matrix[0])
        for i in range(rows):
            for j in range(columns):            # 遍历矩阵中的每个元素，
                if matrix[i][j] == '1':         # 每次遇到 1，则将该元素作为正方形的左上角；
                    maxSide = max(maxSide, 1)   # 计算可能的最大正方形边长
                    currentMaxSide = min(rows - i, columns - j)     # 以此次遇到的"1"为左上角，最大可能的正方形边长
                    for k in range(1, currentMaxSide):      # 判断新的正方形的一行一列是否均为 1
                        flag = True
                        if matrix[i + k][j + k] == '0':
                            break
                        for m in range(k):
                            if matrix[i + k][j + m] == '0' or matrix[i + m][j + k] == '0':
                                flag = False
                                break
                        if flag:                            # 如果可以组成正方形
                            maxSide = max(maxSide, k + 1)   # 更新当前的最大边长
                        else:
                            break
        
        maxSquare = maxSide * maxSide
        return maxSquare


""" 方法二：动态规划
    用 dp(i,j) 表示以 (i,j) 为右下角，且只包含 1 的正方形的边长最大值。

    原始矩阵如下:
    0 1 1 1 0
    1 1 1 1 0
    0 1 1 1 1
    0 1 1 1 1
    0 0 1 1 1
    
    对应的 dp 值如下:
    0 1 1 1 0
    1 1 2 2 0
    0 1 2 3 1
    0 1 2 3 2
    0 0 1 2 3

"""
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        
        maxSide = 0
        row = len(matrix)
        col = len(matrix[0])
        
        dp = [[0] * col for _ in range(row)]
        
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == '1':     # 如果该位置的值是 1
                    if i == 0 or j == 0:    # 如果位置在第一行或者第一列
                        dp[i][j] = 1        # 说明刚能组成正方形，起始边长为 1
                    else:                   # 如果位置在第一行或者第一列之后
                        dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1    # 则 dp(i,j) 的值由其上方、左方和左上方的三个相邻位置的dp 值决定。
                                                                                            # 具体而言，当前位置的元素值等于三个相邻位置的元素中的最小值加 1
                                            # 如果该位置的值是 0，则 dp(i,j)=0，因为当前位置不可能在由 1 组成的正方形中；所以不做更新
                    maxSide = max(maxSide, dp[i][j])

        maxSquare = maxSide * maxSide
        return maxSquare


if __name__ == "__main__":
    matrix = [["1","0","1","0","0"],
              ["1","0","1","1","1"],
              ["1","1","1","1","1"],
              ["1","0","0","1","0"]]
    sol = Solution()
    result = sol.maximalSquare(matrix)
    print (result)
