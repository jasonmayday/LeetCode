"""
https://leetcode-cn.com/problems/rotate-image/

给定一个 n × n 的二维矩阵 matrix 表示一个图像。请你将图像顺时针旋转 90 度。

你必须在 原地 旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要 使用另一个矩阵来旋转图像。

示例 1：
    输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
    输出：[[7,4,1],[8,5,2],[9,6,3]]

示例 2：
    输入：matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    输出：[[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

示例 3：
    输入：matrix = [[1]]
    输出：[[1]]

示例 4：
    输入：matrix = [[1,2],[3,4]]
    输出：[[3,1],[4,2]]

提示：
    matrix.length == n
    matrix[i].length == n
    1 <= n <= 20
    -1000 <= matrix[i][j] <= 1000

"""
from typing import List

""" 方法一：使用辅助数组
    对于矩阵中第 i 行的第 j 个元素，在旋转后，它出现在倒数第 i 列的第 j 个位置。"""
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        # Python 这里不能 matrix_new = matrix 或 matrix_new = matrix[:] 因为是引用拷贝
        matrix_new = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                matrix_new[j][n - i - 1] = matrix[i][j] # 对于矩阵中的元素 matrix[row][col]，在旋转后，它的新位置为 matrix_new[col][n−row−1]。
        # 不能写成 matrix = matrix_new
        matrix[:] = matrix_new
        
        
""" 方法二：原地旋转
    如果我们直接将 matrix[row][col] 放到原矩阵中的目标位置 matrix[col][n−row−1]：
    原矩阵中的 matrix[col][n−row−1] 就被覆盖了
    因此我们可以考虑用一个临时变量 temp 暂存 matrix[col][n−row−1] 的值
"""
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for i in range(n // 2):
            for j in range((n + 1) // 2):
                matrix[i][j], matrix[n - j - 1][i], matrix[n - i - 1][n - j - 1], matrix[j][n - i - 1] \
                    = matrix[n - j - 1][i], matrix[n - i - 1][n - j - 1], matrix[j][n - i - 1], matrix[i][j]


"""方法三：用翻转代替旋转"""
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        # 上下翻转
        for i in range(n // 2):
            for j in range(n):
                matrix[i][j], matrix[n - i - 1][j] = matrix[n - i - 1][j], matrix[i][j]
        # 主对角线翻转
        for i in range(n):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

if __name__ == "__main__":
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    sol = Solution()
    result = sol.rotate(matrix)
    print(result)