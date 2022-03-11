"""
https://leetcode-cn.com/problems/kth-smallest-element-in-a-sorted-matrix/

给你一个 n x n 矩阵 matrix ，其中每行和每列元素均按升序排序，找到矩阵中第 k 小的元素。
请注意，它是 排序后 的第 k 小元素，而不是第 k 个 不同 的元素。

你必须找到一个内存复杂度优于 O(n2) 的解决方案。

示例 1：
    输入：matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
    输出：13
    解释：矩阵中的元素为 [1,5,9,10,11,12,13,13,15]，第 8 小元素是 13

示例 2：
    输入：matrix = [[-5]], k = 1
    输出：-5

提示：
    n == matrix.length
    n == matrix[i].length
    1 <= n <= 300
    -10^9 <= matrix[i][j] <= 10^9
    题目数据 保证 matrix 中的所有行和列都按 非递减顺序 排列
    1 <= k <= n^2

进阶：
    你能否用一个恒定的内存(即 O(1) 内存复杂度)来解决这个问题?
    你能在 O(n) 的时间复杂度下解决这个问题吗?这个方法对于面试来说可能太超前了，但是你会发现阅读这篇文章（ this paper ）很有趣。

"""
from typing import List
import heapq

""" 将这个二维数组转成一维数组，并对该一维数组进行排序"""
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        rec = sorted(sum(matrix, []))
        return rec[k - 1]

""" 小根堆
    由题目给出的性质可知，这个矩阵的每一行均为一个有序数组。问题即转化为从这 n 个有序数组中找第 k 大的数，可以想到利用归并排序的做法，归并到第 k 个数即可停止。
"""
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)                                 # 题目中这个矩阵是n*n的，所以长宽都是n
        heap = [(matrix[i][0], i, 0) for i in range(n)] # 取出第一列候选人
        # heap [(1, 0, 0), (10, 1, 0), (12, 2, 0)]
        # matrix[i][0]是具体的值，后面的(i,0)是在记录候选人在矩阵中的位置，方便每次右移添加下一个候选人
        heapq.heapify(heap)
        for i in range(k - 1):              # 一共弹k次：这里k-1次，return的时候1次
            num, x, y = heapq.heappop(heap) # 弹出候选人里最小一个
            if y != n - 1:                  # 如果这一行还没被弹完
                heapq.heappush(heap, (matrix[x][y + 1], x, y + 1))  # 加入这一行的下一个候选人
        return heapq.heappop(heap)[0]

""" 二分查找 """
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)

        def check(mid):
            i, j = n - 1, 0
            num = 0
            while i >= 0 and j < n:
                if matrix[i][j] <= mid:
                    num += i + 1
                    j += 1
                else:
                    i -= 1
            return num >= k

        left, right = matrix[0][0], matrix[-1][-1]
        # 整个二维数组中 matrix[0][0] 为最小值，matrix[n−1][n−1] 为最大值，现在我们将其分别记作 left 和 right

        while left < right:
            mid = (left + right) // 2
            if check(mid):
                right = mid
            else:
                left = mid + 1
        
        return left


if __name__ == "__main__":
    matrix = [[ 1, 5, 9],
              [10,11,13],
              [12,13,15]]
    k = 8
    sol = Solution()
    result = sol.kthSmallest(matrix, k)
    print (result)