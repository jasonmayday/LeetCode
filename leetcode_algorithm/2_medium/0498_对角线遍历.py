"""
https://leetcode.cn/problems/diagonal-traverse/

给你一个大小为 m x n 的矩阵 mat ，请以对角线遍历的顺序，用一个数组返回这个矩阵中的所有元素。

示例 1：
输入：mat = [[1,2,3],[4,5,6],[7,8,9]]
输出：[1,2,4,7,5,3,6,8,9]

示例 2：
输入：mat = [[1,2],[3,4]]
输出：[1,2,3,4]

提示：
m == mat.length
n == mat[i].length
1 <= m, n <= 10^4
1 <= m * n <= 10^4
-10^5 <= mat[i][j] <= 10^5

"""
from typing import List

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        ans = []
        m, n = len(mat), len(mat[0])
        for i in range(m + n - 1):
            if i % 2:
                x = 0 if i < n else i - n + 1
                y = i if i < n else n - 1
                while x < m and y >= 0:
                    ans.append(mat[x][y])
                    x += 1
                    y -= 1
            else:
                x = i if i < m else m - 1
                y = 0 if i < m else i - m + 1
                while x >= 0 and y < n:
                    ans.append(mat[x][y])
                    x -= 1
                    y += 1
        return ans

if __name__ == "__main__":
    mat = [[1,2,3],[4,5,6],[7,8,9]]
    sol = Solution()
    result = sol.findDiagonalOrder(mat)
    print (result)