"""
https://leetcode-cn.com/problems/matrix-diagonal-sum/

给你一个正方形矩阵 mat，请你返回矩阵对角线元素的和。

请你返回在矩阵主对角线上的元素和副对角线上且不在主对角线上元素的和。

示例  1：
    输入：mat = [[1,2,3],
                [4,5,6],
                [7,8,9]]
    输出：25
    解释：对角线的和为：1 + 5 + 9 + 3 + 7 = 25
    请注意，元素 mat[1][1] = 5 只会被计算一次。

示例  2：
    输入：mat = [[1,1,1,1],
                [1,1,1,1],
                [1,1,1,1],
                [1,1,1,1]]
    输出：8

示例 3：
    输入：mat = [[5]]
    输出：5

提示：
    n == mat.length == mat[i].length
    1 <= n <= 100
    1 <= mat[i][j] <= 100

"""
from typing import List

"""方法：遍历矩阵"""
class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        return sum(mat[i][j] for i in range(n) for j in range(n) \
                    if i == j or i + j == n - 1)
        
"""方法：加完主对角线后，将其置为零"""
class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        ans = 0
        for i in range(n):
            ans += mat[i][i]        # 加斜对角线（左上到右下）
            mat[i][i] = 0           # 归零
            ans += mat[i][n-i-1]    # 加斜对角线（右上到左下），最中间的已经归零过，所以不会计算两次
        return ans

"""方法：调用numpy"""
class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        import numpy as np
        mat = np.array(mat)
        for i in range(mat.shape[0]):
            for j in range(mat.shape[1]):
                if i != j and i + j + 1 != mat.shape[0]:
                    mat[i, j] = 0
        return int(np.sum(mat))

if __name__ == "__main__":
    mat =  [[1,2,3],
            [4,5,6],
            [7,8,9]]
    sol = Solution()
    result = sol.diagonalSum(mat)
    print (result)