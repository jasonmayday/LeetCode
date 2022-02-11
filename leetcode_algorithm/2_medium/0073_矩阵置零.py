"""
https://leetcode-cn.com/problems/set-matrix-zeroes/

给定一个 m x n 的矩阵，如果一个元素为 0 ，则将其所在行和列的所有元素都设为 0 。请使用 原地 算法。

示例 1：
    输入：matrix = [[1,1,1],[1,0,1],[1,1,1]]
    输出：[[1,0,1],[0,0,0],[1,0,1]]

示例 2：
    输入：matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    输出：[[0,0,0,0],[0,4,5,0],[0,3,1,0]]
 
提示：
    m == matrix.length
    n == matrix[0].length
    1 <= m, n <= 200
    -2^31 <= matrix[i][j] <= 2^31 - 1

进阶：
    一个直观的解决方案是使用  O(mn) 的额外空间，但这并不是一个好的解决方案。
    一个简单的改进方案是使用 O(m + n) 的额外空间，但这仍然不是最好的解决方案。
    你能想出一个仅使用常量空间的解决方案吗？

"""
from typing import List

""" O(m + n) 的额外空间"""
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row = len(matrix)       # 行数
        col = len(matrix[0])    # 列数
        row_zero = set()    # 使用集合存储要变成 0 的行和列，因为原矩阵每行或每列可能有多个0
        col_zero = set()
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:   # 如果出现 0，
                    row_zero.add(i)     # 将此行加入要变成0的行的集合
                    col_zero.add(j)     # 将此列加入要变成0的列的集合
        for i in range(row):
            for j in range(col):
                if i in row_zero or j in col_zero:
                    matrix[i][j] = 0
        return matrix

""" O(1) 的空间"""
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row = len(matrix)
        col = len(matrix[0])
        row0_flag = False
        col0_flag = False
        
        # 找第一行是否有0
        for j in range(col):
            if matrix[0][j] == 0:
                row0_flag = True
                break
            
        # 第一列是否有0
        for i in range(row):
            if matrix[i][0] == 0:
                col0_flag = True
                break

        # 把第一行或者第一列作为 标志位
        for i in range(1, row):
            for j in range(1, col):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0
        # 置0
        for i in range(1, row):
            for j in range(1, col):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if row0_flag:
            for j in range(col):
                matrix[0][j] = 0
        if col0_flag:
            for i in range(row):
                matrix[i][0] = 0
                
        return matrix

if __name__ == "__main__":
    matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    sol = Solution()
    result = sol.setZeroes(matrix)
    print(result)