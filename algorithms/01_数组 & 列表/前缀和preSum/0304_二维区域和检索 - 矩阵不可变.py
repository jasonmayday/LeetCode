"""
https://leetcode-cn.com/problems/range-sum-query-2d-immutable/

给定一个二维矩阵 matrix，以下类型的多个请求：
    计算其子矩形范围内元素的总和，该子矩阵的 左上角 为 (row1, col1) ，右下角 为 (row2, col2) 。

实现 NumMatrix 类：
    NumMatrix(int[][] matrix) 给定整数矩阵 matrix 进行初始化
    int sumRegion(int row1, int col1, int row2, int col2) 返回 左上角 (row1, col1) 、右下角 (row2, col2) 所描述的子矩阵的元素 总和 。

示例 1：
    输入:
        ["NumMatrix","sumRegion","sumRegion","sumRegion"]
        [[[[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]]],[2,1,4,3],[1,1,2,2],[1,2,2,4]]
    输出:
        [null, 8, 11, 12]

    解释:
        NumMatrix numMatrix = new NumMatrix([[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]]);
        numMatrix.sumRegion(2, 1, 4, 3); // return 8 (红色矩形框的元素总和)
        numMatrix.sumRegion(1, 1, 2, 2); // return 11 (绿色矩形框的元素总和)
        numMatrix.sumRegion(1, 2, 2, 4); // return 12 (蓝色矩形框的元素总和)
 
提示：
    m == matrix.length
    n == matrix[i].length
    1 <= m, n <= 200
    -10^5 <= matrix[i][j] <= 10^5
    0 <= row1 <= row2 < m
    0 <= col1 <= col2 < n
    最多调用 10^4 次 sumRegion 方法

"""
from typing import List

""" 方法一：一维前缀和"""
class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        m = len(matrix)
        n = len(matrix[0]) if matrix else 0
        self.sums = [[0] * (n + 1) for _ in range(m)]   # 创建 m 行 n+1 列的二维数组 sums
        preSum = self.sums                               # sums[i] 为 matrix[i] 的前缀和数组。将 sums 的列数设为 n+1 的目的是为了方便计算每一行的子数组和
        for i in range(m):
            for j in range(n):
                preSum[i][j + 1] = preSum[i][j] + matrix[i][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        preSum = self.sums
        total = sum(preSum[i][col2 + 1] - preSum[i][col1] for i in range(row1, row2 + 1))
        return total

""" 方法二：二维前缀和"""
class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        m, n = len(matrix), (len(matrix[0]) if matrix else 0)
        self.sums = [[0] * (n + 1) for _ in range(m + 1)]
        preSum = self.sums
        for i in range(m):
            for j in range(n):
                preSum[i + 1][j + 1] = preSum[i][j + 1] + preSum[i + 1][j] - preSum[i][j] + matrix[i][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        preSum = self.sums
        return preSum[row2 + 1][col2 + 1] - preSum[row1][col2 + 1] - preSum[row2 + 1][col1] + preSum[row1][col1]

if __name__ == "__main__":
    numMatrix = NumMatrix([[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]])
    print(numMatrix.sumRegion(2, 1, 4, 3)) # return 8 (红色矩形框的元素总和)
    print(numMatrix.sumRegion(1, 1, 2, 2)) # return 11 (绿色矩形框的元素总和)
    print(numMatrix.sumRegion(1, 2, 2, 4)) # return 12 (蓝色矩形框的元素总和)