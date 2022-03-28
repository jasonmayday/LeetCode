"""
https://leetcode-cn.com/problems/spiral-matrix/

给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。

示例 1：
    输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
    输出：[1,2,3,6,9,8,7,4,5]

示例 2：
    输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    输出：[1,2,3,4,8,12,11,10,9,5,6,7]

提示：
    m == matrix.length
    n == matrix[i].length
    1 <= m, n <= 10
    -100 <= matrix[i][j] <= 100

"""
from typing import List

""" 模拟 """
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return list()
        
        rows, columns = len(matrix), len(matrix[0])         # 行、列
        visited = [[False] * columns for _ in range(rows)]  # 与输入矩阵大小相同的辅助矩阵, 其中的每个元素表示该位置是否被访问过
        total = rows * columns  # 总元素数
        res = [0] * total

        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]] # 四个方向：右，下，左，上
        row, column = 0, 0  # 初始位置是矩阵的左上角
        directionIndex = 0
        for i in range(total):  # 总步数为总元素数
            res[i] = matrix[row][column]    # 访问某个元素，加入答案
            visited[row][column] = True     # 标记该元素为已访问
            nextRow = row + directions[directionIndex][0]       # 行数的改变与方向向量的下标0有关
            nextColumn = column + directions[directionIndex][1] # 行数的改变与方向向量的下标1有关
            if not (0 <= nextRow < rows and 0 <= nextColumn < columns and not visited[nextRow][nextColumn]):
                directionIndex = (directionIndex + 1) % 4    # 初始方向是向右，然后向下，（右，下，左，上 轮换）
            row += directions[directionIndex][0]
            column += directions[directionIndex][1]
        return res

""" 按层模拟
    定义矩阵的第 k 层是到最近边界距离为 k 的所有顶点"""
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return list()
        
        rows, columns = len(matrix), len(matrix[0])
        order = list()
        left, right = 0, columns - 1
        top, bottom = 0, rows - 1
        while left <= right and top <= bottom:
            for column in range(left, right + 1):   # 从左到右遍历上侧元素
                order.append(matrix[top][column])
            for row in range(top + 1, bottom + 1):  # 从上到下遍历右侧元素
                order.append(matrix[row][right])
            if left < right and top < bottom:
                for column in range(right - 1, left, -1):   # 则从右到左遍历下侧元素
                    order.append(matrix[bottom][column])
                for row in range(bottom, top, -1):          # 从下到上遍历左侧元素
                    order.append(matrix[row][left])
            left, right, top, bottom = left + 1, right - 1, top + 1, bottom - 1     # 进入下一层继续遍历
        return order

""" 动态边界法 """
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        if matrix is None:
            return res
        top = 0
        bottom = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1      # 初始化上下左右四个边界
        
        while True:
            
            for i in range(left, right+1):      # ➡️
                res.append(matrix[top][i])
            top += 1            # 遍历后修改边界：到最右边后，换到下一行
            if top > bottom:    # 边界中没有元素时退出
                break
            
            for i in range(top, bottom+1):      # ⬇️
                res.append(matrix[i][right])
            right -= 1          # 遍历后修改边界：到最右边后，最右边下标-1
            if right < left:
                break
            
            for i in range(right, left-1, -1):  # ⬅️
                res.append(matrix[bottom][i])
            bottom -= 1         # 遍历后修改边界：到最右边后，最下面下标-1
            if bottom < top:
                break
            
            for i in range(bottom, top-1, -1):  # ⬆️
                res.append(matrix[i][left])
            left += 1           # 遍历后修改边界：到最右边后，最左边下标+1
            if left > right:
                break
            
        return res
    
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        while matrix:
            res += matrix.pop(0)                # 每次提取第一排元素
            matrix = list(zip(*matrix))[::-1]   # 将剩下的逆时针转九十度，等待下次被削
        return res
    
if __name__ == "__main__":
    matrix = [[1,2,3],
              [4,5,6],
              [7,8,9]]
    sol = Solution()
    result = sol.spiralOrder(matrix)
    print(result)