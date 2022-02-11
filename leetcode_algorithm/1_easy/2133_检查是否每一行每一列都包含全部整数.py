"""
https://leetcode-cn.com/problems/check-if-every-row-and-column-contains-all-numbers/

对一个大小为 n x n 的矩阵而言，如果其每一行和每一列都包含从 1 到 n 的 全部 整数（含 1 和 n），则认为该矩阵是一个 有效 矩阵。

给你一个大小为 n x n 的整数矩阵 matrix ，请你判断矩阵是否为一个有效矩阵：如果是，返回 true ；否则，返回 false 。

示例 1：
    输入：matrix = 
    [[1,2,3],
     [3,1,2],
     [2,3,1]]
    输出：true
    解释：在此例中，n = 3 ，每一行和每一列都包含数字 1、2、3 。
    因此，返回 true 。

示例 2：
    输入：matrix = 
    [[1,1,1],
     [1,2,3],
     [1,2,3]]
    输出：false
    解释：在此例中，n = 3 ，但第一行和第一列不包含数字 2 和 3 。
    因此，返回 false 。

提示：
    n == matrix.length == matrix[i].length
    1 <= n <= 100
    1 <= matrix[i][j] <= n

"""
from typing import List

"""解法1"""
class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        occur = set()   # 用哈希集合统计每一行/列出现过的整数
        
        '''判断每一行是否符合要求，如 matrix[1][1], matrix[1][2], matrix[1][3]'''
        for i in range(n):
            occur.clear()   # 确保统计前哈希表为空
            for j in range(n):
                if matrix[i][j] in occur:   # 出现重复整数，该行不符合要求
                    return False
                occur.add(matrix[i][j])
        
        '''判断每一列是否符合要求，如 matrix[1][1], matrix[2][1], matrix[3][1]'''
        for i in range(n):
            occur.clear()   # 确保统计前哈希表为空
            for j in range(n):
                if matrix[j][i] in occur:   # 出现重复整数，该列不符合要求
                    return False
                occur.add(matrix[j][i])
        return True

"""解法2"""
class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        from itertools import chain
        return all(set(list(range(1,len(matrix)+1)))==set(r) for r in chain(matrix,zip(*matrix)))

if __name__ == "__main__":
    matrix = [[1,2,3], [3,1,2], [2,3,1]]
    sol = Solution()
    result = sol.checkValid(matrix)
    print (result)