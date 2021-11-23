"""
https://leetcode-cn.com/problems/valid-boomerang

回旋镖定义为一组三个点，这些点各不相同且不在一条直线上。

给出平面上三个点组成的列表，判断这些点是否可以构成回旋镖。

示例 1：
    输入：[[1,1],[2,3],[3,2]]
    输出：true

示例 2：
    输入：[[1,1],[2,2],[3,3]]
    输出：false
 
提示：
    points.length == 3
    points[i].length == 2
    0 <= points[i][j] <= 100

"""
from typing import List

"""斜率"""
class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        if points[0][0] == points[1][0] and points[1][0] == points[2][0]:
                return False

        # print(k1,k2)
        return (points[0][1]-points[1][1]) * (points[0][0]-points[2][0]) != \
               (points[0][1]-points[2][1]) * (points[0][0]-points[1][0])

"""是否能组成三角形"""
class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        (x1,y1),(x2,y2),(x3,y3) = points
        return (x1*y2 + x2*y3 + x3*y1 - y1*x2 - y2*x3 - y3*x1) != 0

if __name__ == "__main__":
    points = [[1,1],[2,3],[3,2]]
    sol = Solution()
    result = sol.isBoomerang(points)
    print(result)