"""
https://leetcode-cn.com/problems/reshape-the-matrix

在 MATLAB 中，有一个非常有用的函数 reshape ，它可以将一个 m x n 矩阵重塑为另一个大小不同（r x c）的新矩阵，但保留其原始数据。

给你一个由二维数组 mat 表示的 m x n 矩阵，以及两个正整数 r 和 c ，分别表示想要的重构的矩阵的行数和列数。

重构后的矩阵需要将原始矩阵的所有元素以相同的 行遍历顺序 填充。

如果具有给定参数的 reshape 操作是可行且合理的，则输出新的重塑矩阵；否则，输出原始矩阵。

示例 1：
    输入：mat = [[1,2],[3,4]], r = 1, c = 4
    输出：[[1,2,3,4]]

示例 2：
    输入：mat = [[1,2],[3,4]], r = 2, c = 4
    输出：[[1,2],[3,4]]
 
提示：
    m == mat.length
    n == mat[i].length
    1 <= m, n <= 100
    -1000 <= mat[i][j] <= 1000
    1 <= r, c <= 300

"""
from typing import List
import numpy as np

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        if m*n != r*c:      # 先判断reshape操作是否可行
            return mat      # 不相等则直接返回原数组
        unfold = []
        for row in mat:
            unfold.extend(row)  # 将数组展开成一行，extend() 函数用于在列表末尾一次性追加另一个序列中的多个值
        reshape_mat = []
        for i in range(0, len(unfold), c):  # 每隔 c 个位置放入新的一行
            row = []
            for j in range(i, i+c):
                row.append(unfold[j])
            reshape_mat.append(row)
        return reshape_mat
    
"""解法2：numpy"""
class Solution(object):
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        M, N = len(mat), len(mat[0])
        if M * N != r * c:
            return mat
        return np.asarray(mat).reshape((r, c))

if __name__ == "__main__":
    mat = [[1,2],[3,4]]
    r = 1   # 行数 row
    c = 4   # 列数 column
    sol = Solution()
    result = sol.matrixReshape(mat,r,c)
    print(result)
