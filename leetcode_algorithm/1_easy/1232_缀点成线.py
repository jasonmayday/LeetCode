"""
https://leetcode-cn.com/problems/check-if-it-is-a-straight-line/

在一个 XY 坐标系中有一些点，我们用数组 coordinates 来分别记录它们的坐标，其中 coordinates[i] = [x, y] 表示横坐标为 x、纵坐标为 y 的点。

请你来判断，这些点是否在该坐标系中属于同一条直线上，是则返回 true，否则请返回 false。

示例 1：
    输入：coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
    输出：true

示例 2：
    输入：coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
    输出：false

提示：
    2 <= coordinates.length <= 1000
    coordinates[i].length == 2
    -10^4 <= coordinates[i][0], coordinates[i][1] <= 10^4
    coordinates 中不含重复的点

"""
from typing import List

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates) == 2:
            return True
        x1, y1 = coordinates[0][0], coordinates[0][1]
        x2, y2 = coordinates[1][0], coordinates[1][1]
        for i in range(2, len(coordinates)):
            xi, yi = coordinates[i][0], coordinates[i][1]
            if (yi - y2)*(x2 - x1) != (y2 - y1)*(xi - x2):
                return False
        return True

if __name__ == "__main__":
    coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
    sol = Solution()
    result = sol.checkStraightLine(coordinates)
    print(result)