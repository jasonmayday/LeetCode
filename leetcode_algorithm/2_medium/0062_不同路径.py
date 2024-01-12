"""
https://leetcode-cn.com/problems/unique-paths/

一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为 “Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish” ）。

问总共有多少条不同的路径？

示例 1：
    输入：m = 3, n = 7
    输出：28

示例 2：
    输入：m = 3, n = 2
    输出：3
    解释：
    从左上角开始，总共有 3 条路径可以到达右下角。
    1. 向右 -> 向下 -> 向下
    2. 向下 -> 向下 -> 向右
    3. 向下 -> 向右 -> 向下

示例 3：
    输入：m = 7, n = 3
    输出：28

示例 4：
    输入：m = 3, n = 3
    输出：6

提示：
    1 <= m, n <= 100
    题目数据保证答案小于等于 2 * 10^9

"""

from typing import List

"""动态规划"""
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1]*n] + [[1]+[0] * (n-1) for _ in range(m-1)]
        # print(dp)                     # dp(i,j) 表示从左上角走到 (i,j) 的路径数量，
        # [[1, 1, 1, 1, 1, 1, 1],       # 其中 i 和 j 的范围分别是 [0,m) 和 [0,n)。
        #  [1, 0, 0, 0, 0, 0, 0],
        #  [1, 0, 0, 0, 0, 0, 0]]
        # 最终：
        # [[1, 1, 1, 1,  1,  1,  1], 
        #  [1, 2, 3, 4,  5,  6,  7],
        #  [1, 3, 6, 10, 15, 21, 28]]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]  # 每个位置的路径 = 该位置左边的路径 + 该位置上边的路径
        return dp[m-1][n-1]
    
""" 动态规划：优化1：空间复杂度 O(2n)O(2n)
    由于dp[i][j] = dp[i-1][j] + dp[i][j-1]，因此只需要保留当前行与上一行的数据 (在动态方程中，即pre[j] = dp[i-1][j])，两行，空间复杂度O(2n)；"""
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        pre = [1] * n
        cur = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                cur[j] = pre[j] + cur[j-1]
            pre = cur[:]
        return pre[-1]

""" 动态规划：优化2：空间复杂度 O(n)O(n)
    cur[j] += cur[j-1], 即cur[j] = cur[j] + cur[j-1] 等价于思路二-->> cur[j] = pre[j] + cur[j-1]，因此空间复杂度为O(n)."""
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cur = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                cur[j] += cur[j-1]
        return cur[-1]

if __name__ == "__main__":
    m = 3
    n = 7
    sol = Solution()
    result = sol.uniquePaths(m,n)
    print(result)