"""
https://leetcode-cn.com/problems/special-positions-in-a-binary-matrix/

给你一个大小为 rows x cols 的矩阵 mat，其中 mat[i][j] 是 0 或 1，请返回 矩阵 mat 中特殊位置的数目 。

特殊位置 定义：如果 mat[i][j] == 1 并且第 i 行和第 j 列中的所有其他元素均为 0（行和列的下标均 从 0 开始 ），则位置 (i, j) 被称为特殊位置。

示例 1：
    输入：mat = [[1,0,0],
                [0,0,1],
                [1,0,0]]
    输出：1
    解释：(1,2) 是一个特殊位置，因为 mat[1][2] == 1 且所处的行和列上所有其他元素都是 0

示例 2：
    输入：mat = [[1,0,0],
                [0,1,0],
                [0,0,1]]
    输出：3
    解释：(0,0), (1,1) 和 (2,2) 都是特殊位置

示例 3：
    输入：mat = [[0,0,0,1],
                [1,0,0,0],
                [0,1,1,0],
                [0,0,0,0]]
    输出：2

示例 4：
    输入：mat = [[0,0,0,0,0],
                [1,0,0,0,0],
                [0,1,0,0,0],
                [0,0,1,0,0],
                [0,0,0,1,1]]
    输出：3

提示：
    rows == mat.length
    cols == mat[i].length
    1 <= rows, cols <= 100
    mat[i][j] 是 0 或 1

"""
from typing import List

class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int: 
       cols = [sum(num) for num in mat]
       rows = [sum(num) for num in zip(*mat)]
       ans = 0
       for i in range(len(cols)):
           if cols[i] == 1:
               ans += (rows[mat[i].index(1)] == 1)  # index() 函数用于从列表中找出某个值第一个匹配项的索引位置。
       return ans

class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        res = 0
        tMat = list(zip(*mat))          # 按照每一列生成矩阵
        for i in range(len(mat)):
            if mat[i].count(1) == 1:    # 统计每一行的1的个数
                if tMat[mat[i].index(1)].count(1) == 1:     # 统计每一列的1的个数
                    res += 1
        return res
    
if __name__ == "__main__":
    mat =  [[1,0,0],
            [0,1,0],
            [0,0,1]]
    sol = Solution()
    result = sol.numSpecial(mat)
    print(result)