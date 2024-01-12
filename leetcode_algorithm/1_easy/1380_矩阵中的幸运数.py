"""
https://leetcode-cn.com/problems/lucky-numbers-in-a-matrix/

给你一个 m * n 的矩阵，矩阵中的数字 各不相同 。请你按 任意 顺序返回矩阵中的所有幸运数。

幸运数是指矩阵中满足同时下列两个条件的元素：
    在同一行的所有元素中最小
    在同一列的所有元素中最大

示例 1：
    输入：matrix = [[3,7,8],[9,11,13],[15,16,17]]
    输出：[15]
    解释：15 是唯一的幸运数，因为它是其所在行中的最小值，也是所在列中的最大值。

示例 2：
    输入：matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
    输出：[12]
    解释：12 是唯一的幸运数，因为它是其所在行中的最小值，也是所在列中的最大值。

示例 3：
    输入：matrix = [[7,8],[1,2]]
    输出：[7]

提示：
    m == mat.length
    n == mat[i].length
    1 <= n, m <= 50
    1 <= matrix[i][j] <= 10^5
    矩阵中的所有元素都是不同的

"""
from typing import List


""" 解法1：模拟"""
class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        for row in matrix:
            for j, x in enumerate(row):     # 判断 matrix[i][j] 是否是它所在行的最小值和所在列的最大值
                if max(r[j] for r in matrix) <= x <= min(row):
                    ans.append(x)
        return ans


""" 解法2：用zip来获取矩阵的每一列"""
class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        rowmin = [min(i) for i in matrix]           # 返回每一行的最小值
        colmax = [max(i) for i in zip(*matrix)]     # 返回每一列的最大值
        return [i for i in rowmin if i in colmax]
    
""" 解法3 """
class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)         # 行数
        n = len(matrix[0])      # 列数
        min_list = [float('inf')]  * m      # 初始化每一行中的最小值的列表，m 行所以 m 个
        max_list = [float('-inf')] * n      # 初始化每一列中的最大值的列表，n 列所以 n 个
        for i in range(m):              # 遍历每一行
            for j in range(n):          # 遍历每一列
                if matrix[i][j] < min_list[i]:
                    min_list[i] = matrix[i][j]
                if matrix[i][j] > max_list[j]:
                    max_list[j] = matrix[i][j]
        res_set = set(min_list) & set(max_list)
        res = []
        for num in res_set:
            res.append(num)
        return res


if __name__ == "__main__":
    matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
    sol = Solution()
    result = sol.luckyNumbers(matrix)
    print(result)