"""
https://leetcode-cn.com/problems/path-crossing/

给你一个字符串 path，其中 path[i] 的值可以是 'N'、'S'、'E' 或者 'W'，分别表示向北、向南、向东、向西移动一个单位。

你从二维平面上的原点 (0, 0) 处开始出发，按 path 所指示的路径行走。

如果路径在任何位置上与自身相交，也就是走到之前已经走过的位置，请返回 true ；否则，返回 false 。

示例 1：
    输入：path = "NES"
    输出：false 
    解释：该路径没有在任何位置相交。

示例 2：
    输入：path = "NESWW"
    输出：true
    解释：该路径经过原点两次。
 
提示：
    1 <= path.length <= 104
    path[i] 为 'N'、'S'、'E' 或 'W'

"""

"""模拟二维坐标系操作，遍历字符串，看是否坐标有重复"""
class Solution:
    def isPathCrossing(self, path: str) -> bool:
        s = set()
        coor = (0, 0)       # 初始坐标
        s.add(coor)         # 加入集合
        for p in path:      # 遍历path，读取前进方向
            if p == 'N':
                x, y = 0, 1
            elif p == 'S':
                x, y = 0, -1
            elif p == 'E':
                x, y = 1, 0
            else:
                x, y = -1, 0
            coor = (coor[0] + x, coor[1] + y)   # 新的坐标
            if coor in s:       # 判断坐标是否在集合中
                return True     # 遍历过程中，如果碰到 coor 存在于集合中，说明有重复的坐标，返回True
            s.add(coor)         # 不断把coor加入集合中
        return False            # 遍历完path，如果还没有重复的坐标，返回False

if __name__ == "__main__":
    path = "NESWW"
    sol = Solution()
    result = sol.isPathCrossing(path)
    print(result)