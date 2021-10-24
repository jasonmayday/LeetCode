'''
https://leetcode-cn.com/problems/search-a-2d-matrix-ii/

编写一个高效的算法来搜索 m x n 矩阵 matrix 中的一个目标值 target 。该矩阵具有以下特性：

每行的元素从左到右升序排列。
每列的元素从上到下升序排列。

+-----------------------------+
|  1  |  4  |  7  | 11  | 15  |
+-----------------------------+
|  2  |  5  |  8  | 12  | 19  |
+-----------------------------+
|  3  |  6  |  9  | 16  | 22  |
+-----------------------------+
| 10  | 13  | 14  | 17  | 24  |
+-----------------------------+
| 18  | 21  | 23  | 26  | 30  |
+-----------------------------+

示例 1：
输入：matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
输出：true

示例 2：
输入：matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20
输出：false

'''
matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target = 20

from typing import List

class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        rows = len(matrix)
        cols = len(matrix[0])

        row = 0
        col = cols - 1 

        while 0 <= row < rows and 0 <= col < cols:
            if matrix[row][col] < target:
                row += 1
            elif  matrix[row][col] > target:
                col -= 1
            else:
                return True
        return False


