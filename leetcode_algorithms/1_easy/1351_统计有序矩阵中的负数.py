"""
https://leetcode-cn.com/problems/count-negative-numbers-in-a-sorted-matrix/

给你一个 m * n 的矩阵 grid，矩阵中的元素无论是按行还是按列，都以非递增顺序排列。 

请你统计并返回 grid 中 负数 的数目。

示例 1：
    输入：grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
    输出：8
    解释：矩阵中共有 8 个负数。

示例 2：
    输入：grid = [[3,2],[1,0]]
    输出：0

示例 3：
    输入：grid = [[1,-1],[-1,-1]]
    输出：3

示例 4：
    输入：grid = [[-1]]
    输出：1

提示：
    m == grid.length
    n == grid[i].length
    1 <= m, n <= 100
    -100 <= grid[i][j] <= 100

"""
from typing import List
'''
              ←  j=3
i=0 [ 4,  3,  2, -1]
 ↓  [ 3,  2,  1, -1]
    [ 1,  1, -1, -2]
    [-1, -1, -2, -3]
'''
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        total = 0
        i = 0                   # 从上往下的指针，从第一行开始
        j = len(grid[0]) - 1    # 从右往左的指针，从最后一行开始
        while i < len(grid) and j >= 0:
            if grid[i][j] >= 0:
                i += 1
            else:                       # 如果某数为负数，则该数以下所有数都为负，
                total += len(grid) - i  # (总数-i)即为这一列所有负数
                j -= 1                  # 继续下一列
        return total
    
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        n = len(grid)
        ans = 0
        for i in grid:
            left, right = 0, len(i)-1
            while left < right:
                mid = (left + right)//2
                if i[mid] >= 0:
                    left = mid + 1
                else:
                    right = mid
            if i[left] < 0:
                ans += len(i) - left
        return ans

    
if __name__ == "__main__":
    grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
    sol = Solution()
    result = sol.countNegatives(grid)
    print(result)