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

class Solution:
    def generateMatrix(self, n: int) -> [[int]]:
        l, r, t, b = 0, n - 1, 0, n - 1
        mat = [[0 for _ in range(n)] for _ in range(n)]
        num, tar = 1, n * n
        while num <= tar:
            for i in range(l, r + 1): # left to right
                mat[t][i] = num
                num += 1
            t += 1
            for i in range(t, b + 1): # top to bottom
                mat[i][r] = num
                num += 1
            r -= 1
            for i in range(r, l - 1, -1): # right to left
                mat[b][i] = num
                num += 1
            b -= 1
            for i in range(b, t - 1, -1): # bottom to top
                mat[i][l] = num
                num += 1
            l += 1
        return mat

if __name__ == "__main__":
    candidates = [2,3,6,7]
    target = 7
    sol = Solution()
    result = sol.combinationSum(candidates, target)
    print(result)