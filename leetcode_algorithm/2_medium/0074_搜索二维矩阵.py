"""
https://leetcode-cn.com/problems/search-a-2d-matrix/

编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性：
    每行中的整数从左到右按升序排列。
    每行的第一个整数大于前一行的最后一个整数。

示例 1：
    输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
    输出：true

示例 2：
    输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
    输出：false

提示：
    m == matrix.length
    n == matrix[i].length
    1 <= m, n <= 100
    -10^4 <= matrix[i][j], target <= 10^4

"""

from typing import List
import bisect
    
""" 1. 暴力遍历 """
class Solution(object):
    def searchMatrix(self, matrix, target):
        M, N = len(matrix), len(matrix[0])
        for i in range(M):
            for j in range(N):
                if matrix[i][j] == target:
                    return True
        return False

""" 2. 从左下角或者右上角开始查找 """
class Solution(object):
    def searchMatrix(self, matrix, target):
        if not matrix or not matrix[0]:
            return False
        rows = len(matrix)
        cols = len(matrix[0])
        row, col = 0, cols - 1
        while True:
            if row < rows and col >= 0:
                if matrix[row][col] == target:
                    return True
                elif matrix[row][col] < target: # 如果要搜索的 target 比当前元素大
                    row += 1                    # 那么让行增加
                else:                           # 如果要搜索的 target 比当前元素小
                    col -= 1                    # 那么让列减小
            else:
                return False

""" 3. 先寻找到所在行 """
class Solution(object):
    def searchMatrix(self, matrix, target):
        M, N = len(matrix), len(matrix[0])
        for i in range(M):
            if target > matrix[i][N - 1]:   # target 大于这一行的末尾元素
                continue                    # 那么target 一定不在这一行中，只能出现在矩阵的下面的行中。
            if target in matrix[i]:
                return True
        return False

""" 4. 两次二分查找"""
class Solution(object):
    def searchMatrix(self, matrix, target):
        M, N = len(matrix), len(matrix[0])
        col0 = [row[0] for row in matrix]
        target_row = bisect.bisect_right(col0, target) - 1
        if target_row < 0:
            return False
        target_col = bisect.bisect_left(matrix[target_row], target)
        if target_col >= N:
            return False
        if matrix[target_row][target_col] == target:
            return True
        return False

""" 5. 将「二维矩阵」当做「一维矩阵」 """
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)     # 行数
        n = len(matrix[0])  # 列数
        l = 0           # 左指针
        r = m * n - 1   # 右指针
        while l <= r:
            mid = (l + r) >> 1
            x = mid // n    # 返回商的整数部分
            y = mid % n     # 返回除法的余数
            if matrix[x][y] > target:
                r = mid - 1
            elif matrix[x][y] < target:
                l = mid + 1
            else:
                return True
        return False

""" 使用 numpy reshape成一维数组"""
import numpy as np
class Solution(object):
    def searchMatrix(self, matrix, target):
        matrix = np.reshape(matrix, [1, -1])
        return target in matrix

if __name__ == "__main__":
    matrix = [[ 1, 3, 5, 7],
              [10,11,16,20],
              [23,30,34,60]]
    target = 3
    sol = Solution()
    result = sol.searchMatrix(matrix, target)
    print(result)