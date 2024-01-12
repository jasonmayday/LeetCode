"""
https://leetcode-cn.com/problems/longest-increasing-path-in-a-matrix/

给定一个 m x n 整数矩阵 matrix ，找出其中 最长递增路径 的长度。

对于每个单元格，你可以往上，下，左，右四个方向移动。 你 不能 在 对角线 方向上移动或移动到 边界外（即不允许环绕）。

示例 1：
    输入：matrix = [[9,9,4],[6,6,8],[2,1,1]]
    输出：4 
    解释：最长递增路径为 [1, 2, 6, 9]。

示例 2：
    输入：matrix = [[3,4,5],[3,2,6],[2,2,1]]
    输出：4 
    解释：最长递增路径是 [3, 4, 5, 6]。注意不允许在对角线方向上移动。

示例 3：
    输入：matrix = [[1]]
    输出：1

提示：
    m == matrix.length
    n == matrix[i].length
    1 <= m, n <= 200
    0 <= matrix[i][j] <= 2^31 - 1

"""

""" 动态规划 """
class Solution(object):
    def longestIncreasingPath(self, matrix):
        if not matrix or not matrix[0]:
            return 0
        m = len(matrix)
        n = len(matrix[0])
        num_index = []
        
        for i in range(m):
            for j in range(n):
                num_index.append((matrix[i][j], i, j))  # 包含数字值和下标的矩阵
        num_index.sort()                                # 对矩阵的值按从小到大排序，按大小顺序才能保证依赖的子问题都求解过了
        dp = [[0 for _ in range(n)] for _ in range(m)]
        for num, i, j in num_index:
            dp[i][j] = 1                                # dp[i][j]表示以matrix[i][j]结尾的最长递增长度，初始dp[i][j]都等于1
            for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:   # 四个方向
                r = i + di
                c = j + dj
                if 0 <= r < m and 0 <= c < n:
                    if matrix[i][j] > matrix[r][c]:             # 若matrix[i][j]四个方向有任意小于它
                        dp[i][j] = max(dp[i][j], 1 + dp[r][c])  # 则可以更新dp[i][j]
        return max([dp[i][j] for i in range(m) for j in range(n)])
    
if __name__ == "__main__":
    matrix = [[9,9,4],
              [6,6,8],
              [2,1,1]]
    sol = Solution()
    result = sol.longestIncreasingPath(matrix)
    print (result) 