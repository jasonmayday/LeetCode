"""
https://leetcode-cn.com/problems/shun-shi-zhen-da-yin-ju-zhen-lcof/

输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字。

示例 1：
    输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
    输出：[1,2,3,6,9,8,7,4,5]

示例 2：
    输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    输出：[1,2,3,4,8,12,11,10,9,5,6,7]

限制：
    0 <= matrix.length <= 100
    0 <= matrix[i].length <= 100

注意：本题与主站 54 题相同：https://leetcode-cn.com/problems/spiral-matrix/

"""

from typing import List

"""解法1：动态边界法"""
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