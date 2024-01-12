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
        rows = len(matrix)     #  矩阵长度，也就是行数
        cols = len(matrix[0])  #  某一行的数量，也就是列数
        
        #  从右上角开始寻找：
        row = 0                #  第一行
        col = cols - 1         #  最右边一列
        
        while 0 <= row < rows and 0 <= col < cols:  #  在矩阵内寻找
            if matrix[row][col] < target:     #  如果当前值小于目标值:
                row += 1                      #  跳到下一行（向下找）
            elif  matrix[row][col] > target:  #  如果当前值大于目标值：
                col -= 1                      #  跳到上一列（向左找）
            else:
                return True
        return False

if __name__ == "__main__":
    matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
    target = 20
    sol = Solution()
    result = sol.searchMatrix(matrix, target)
    print (result)  
