"""
https://leetcode-cn.com/problems/reaching-points/

给定四个整数 sx , sy ，tx 和 ty，如果通过一系列的转换可以从起点 (sx, sy) 到达终点 (tx, ty)，则返回 true，否则返回 false。

从点 (x, y) 可以转换到 (x, x+y)  或者 (x+y, y)。

示例 1:
    输入: sx = 1, sy = 1, tx = 3, ty = 5
    输出: true
    解释:
        可以通过以下一系列转换从起点转换到终点：
        (1, 1) -> (1, 2)
        (1, 2) -> (3, 2)
        (3, 2) -> (3, 5)

示例 2:
    输入: sx = 1, sy = 1, tx = 2, ty = 2
    输出: false

示例 3:
    输入: sx = 1, sy = 1, tx = 1, ty = 1
    输出: true

提示:
    1 <= sx, sy, tx, ty <= 10^9

"""

""" 方法一：反向计算
    只有当 tx != ty 时才存在上一个状态，且上一个状态唯一，可能的情况如下：
    如果 tx=ty，不存在上一个状态，状态 (tx,ty) 即为起点状态；
    如果 tx>ty，则上一个状态是 (tx−ty,ty)；
    如果 tx<ty，则上一个状态是 (tx,ty−tx)。
"""
class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        while sx < tx != ty > sy:
            if tx > ty:
                tx %= ty
            else:
                ty %= tx
        if tx == sx and ty == sy:
            return True
        elif tx == sx:
            return ty > sy and (ty - sy) % tx == 0
        elif ty == sy:
            return tx > sx and (tx - sx) % ty == 0
        else:
            return False

if __name__ == "__main__":
    sx = 1,
    sy = 1,
    tx = 3,
    ty = 5
    sol = Solution()
    result = sol.reachingPoints(sx, sy, tx, ty)
    print(result)