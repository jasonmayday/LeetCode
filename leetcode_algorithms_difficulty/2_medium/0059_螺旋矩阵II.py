"""
https://leetcode-cn.com/problems/spiral-matrix-ii/

给你一个正整数 n ，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的 n x n 正方形矩阵 matrix 。

示例 1：
    输入：n = 3
    输出：[[1,2,3],[8,9,4],[7,6,5]]

示例 2：
    输入：n = 1
    输出：[[1]]

提示：
    1 <= n <= 20

"""
from typing import List

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        l = 0       # 左边界
        r = n - 1   # 右边界
        t = 0       # 上边界
        b = n - 1   # 下边界
        mat = [[0 for _ in range(n)] for _ in range(n)]     # 生成一个 n×n 空矩阵 mat
        num = 1
        while num <= (n * n):
            
            '''从左向右模拟'''
            for i in range(l, r + 1):
                mat[t][i] = num
                num += 1
            t += 1      # 上边界 +1
            
            '''从上向下模拟'''
            for i in range(t, b + 1):
                mat[i][r] = num
                num += 1
            r -= 1      # 右边界 +1
            
            '''从右向左模拟'''
            for i in range(r, l - 1, -1):
                mat[b][i] = num
                num += 1
            b -= 1      # 下边界 +1
            
            '''从下向上模拟'''
            for i in range(b, t - 1, -1):
                mat[i][l] = num
                num += 1
            l += 1      # 左边界 +1
        
        return mat

if __name__ == "__main__":
    n = 4
    sol = Solution()
    result = sol.generateMatrix(n)
    print(result)