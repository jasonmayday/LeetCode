"""
https://leetcode-cn.com/problems/triangle/

给定一个三角形 triangle ，找出自顶向下的最小路径和。

每一步只能移动到下一行中相邻的结点上。相邻的结点 在这里指的是 下标 与 上一层结点下标 相同或者等于 上一层结点下标 + 1 的两个结点。也就是说，如果正位于当前行的下标 i ，那么下一步可以移动到下一行的下标 i 或 i + 1 。

示例 1：
    输入：triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
    输出：11
    解释：如下面简图所示：
       2
      3 4
     6 5 7
    4 1 8 3
    自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。

示例 2：
    输入：triangle = [[-10]]
    输出：-10

提示：
    1 <= triangle.length <= 200
    triangle[0].length == 1
    triangle[i].length == triangle[i - 1].length + 1
    -10^4 <= triangle[i][j] <= 10^4

进阶：
    你可以只使用 O(n) 的额外空间（n 为三角形的总行数）来解决这个问题吗？

"""
from typing import List

''' 方法1：动态规划，从上往下
       2        2
      3 4   →   3 4
     6 5 7  →   6 5 7
    4 1 8 3     4 1 8 3
'''
class Solution(object):
    def minimumTotal(self, tri):
        if not tri:
            return 0
        n = len(tri)       # 行数
        m = len(tri[-1])   # 最下一面一行的数量
        dp = [[0 for _ in range(m)] for _ in range(n)]  # 创建 n*m 的二维数组
        dp[0][0] = tri[0][0]   # 初始化dp[0][0]
        
        '''状态转移条件1：第一列需要单独计算，只有 1 条转移路径'''
        for i in range(1,n):
            dp[i][0] = dp[i-1][0] + tri[i][0]  # 第一列的数字等于 (上面的dp数组) + (同位置三角形数组)
        
        # 第一列之外的
        for i in range(1,n):    # 每行的遍历
            j = 1               # 列数
            
            '''状态转移条件2：三角形里面的（除去左边和斜边），有 2 条转移路径'''
            while j < len(tri[i])-1:                                    # 注意计算的是三角形每一行的长度都不同。 最后一列需要单独计算(斜边)，所以是从遍历的个数是size()-1
                dp[i][j] = min(dp[i-1][j-1], dp[i-1][j]) + tri[i][j]    # 状态转移公式（dp数组中左上方和上方较小的值 + 同位置的三角形数组的值）
                j += 1          # 进入下一列
            
            '''状态转移条件3：三角形斜边需要单独计算，只有 1 条转移路径'''
            dp[i][j] = dp[i-1][j-1] + tri[i][j]                         # 状态转移公式（dp数组左上方的值 + 同位置的三角形数组的值
        return min(dp[-1])      # 最后一行保存了每条路径的计算结果，对最后一行数组求min即为最终结果


''' 方法2：动态规划，自下而上
       2        2
      3 4   →   3 4
     6 5 7  →   6 5 7
    4 1 8 3     4 1 8 3
'''
class Solution(object):
    def minimumTotal(self, triangle):
        if not triangle:
            return 0
        n = len(triangle)
        m = len(triangle[-1])
        dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
        # 自下而上推到
        for i in range(n-1,-1,-1):
            # 对于三角形的每一行，从右向左计算
            for j in range(len(triangle[i])-1,-1,-1):
                dp[i][j] = min(dp[i+1][j+1],dp[i+1][j]) + triangle[i][j]
        # 最终结果就保存在第一行第一列中
        return dp[0][0]
    
    
'''空间优化'''
class Solution(object):
    def minimumTotal(self, triangle):
        if not triangle:
            return 0
        n = len(triangle)
        m = len(triangle[-1])
        # 申请的dp数组为最长列+1
        dp = [0 for _ in range(m+1)]
        for i in range(n-1,-1,-1):
            # 从左到右的方式计算
            for j in range(len(triangle[i])):
                dp[j] = min(dp[j],dp[j+1]) + triangle[i][j]
        # dp数组的第一个元素即为最终结果
        return dp[0]


if __name__ == "__main__":
    triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
    sol = Solution()
    result = sol.minimumTotal(triangle)
    print (result)
    
    