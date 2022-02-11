"""
https://leetcode-cn.com/problems/largest-triangle-area/

给定包含多个点的集合，从其中取三个点组成三角形，返回能组成的最大三角形的面积。

示例:
    输入: points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
    输出: 2
    解释: 
    这五个点如下图所示。组成的橙色三角形是最大的，面积为2。

注意:
    3 <= points.length <= 50.
    不存在重复的点。
     -50 <= points[i][j] <= 50.
    结果误差值在 10^-6 以内都认为是正确答案。

"""
from typing import List
# 求简单多边形面积时非常有用的“鞋带公式”
# 三角形面积=|(x1 * y2 + x2 * y3 + x3 * y1 - y1 * x2 - y2 * x3 - y3 * x1)|/2

class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        res=0
        for i in points:
            for j in points:
                for k in points:
                    res = max(res,abs(i[0]*j[1] + j[0]*k[1] + k[0]*i[1] - i[1]*j[0] - j[1]*k[0] - k[1]*i[0]))
        return res/2

if __name__ == "__main__":
    points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
    sol = Solution()
    result = sol.largestTriangleArea(points)
    print(result)