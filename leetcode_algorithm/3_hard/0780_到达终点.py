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
    如果 tx = ty，不存在上一个状态，状态 (tx, ty) 即为起点状态；
    如果 tx > ty，则上一个状态是 (tx−ty, ty)；
    如果 tx < ty，则上一个状态是 (tx, ty−tx)。
"""
class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        while sx < tx != ty > sy:
            if tx > ty:
                tx %= ty
            else:
                ty %= tx
        if tx == sx and ty == sy:   # 如果 tx = sx 且 ty = sy
            return True             # 则已经到达起点状态，因此可以从起点转换到终点
        elif tx == sx:                              # 如果 tx = sx 且 ty != sy，则 tx 不能继续减小，只能减小 ty，
            return ty > sy and (ty - sy) % tx == 0  # 因此只有当 ty > sy 且 (ty−sy) mod tx = 0 时可以从起点转换到终点。
        elif ty == sy:                              # 如果 ty = sy 且 tx != sx，则 ty 不能继续减小，只能减小 tx，
            return tx > sx and (tx - sx) % ty == 0  # 因此只有当 tx  >sx 且 (tx−sx) mod ty = 0 时可以从起点转换到终点。
        else:               # 如果 tx != sx 且 ty != sy
            return False    # 则不可以从起点转换到终点
    
class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        # 思路：反推，每轮一定是大的去减小的得到上一轮，重复若干次直到目标某分量小于起点
        # 但直接一直减会超时，所以考虑用除法计算出要减几次，然后用一次减法代替多次减法
        while tx >= sx and ty >= sy:
            if tx == sx and ty == sy:
                return True
            # 注意如果tx == ty且不是起点，那么一定False，因为减完某分量是0，题面规定只有正数
            if tx == ty:
                return False
            # max的含义：每次至少要减一次，否则tx,ty均无变化，会死循环
            # min的含义：
            #   假设现在有tx >= ty，那么可以一直做tx -= ty
            #   重复了n次直到以下两种情况之一发生为止：
            #       1.tx - n*ty 恰大于 sx，即  tx - n*ty > sx > tx - (n+1)*ty
            #       2.tx - n*ty 恰大于0，即    tx - n*ty > 0  > tx - (n+1)*ty
            #         min中if-else从句的意思就是保证减完仍是正的
            #   min的意思就是谁先发生就到此为止
            if tx >= ty:
                tx -= max(1, min(tx // ty * ty if tx % ty else (tx // ty - 1), (tx - sx) // ty)) * ty
            else:
                ty -= max(1, min(ty // tx * tx if ty % tx else (ty // tx - 1), (ty - sy) // tx)) * tx
            print(tx, ty)
        return False

if __name__ == "__main__":
    sx = 1,
    sy = 1,
    tx = 3,
    ty = 5
    sol = Solution()
    result = sol.reachingPoints(sx, sy, tx, ty)
    print(result)