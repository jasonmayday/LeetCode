"""
https://leetcode-cn.com/problems/dungeon-game/

一些恶魔抓住了公主（P）并将她关在了地下城的右下角。地下城是由 M x N 个房间组成的二维网格。我们英勇的骑士（K）最初被安置在左上角的房间里，他必须穿过地下城并通过对抗恶魔来拯救公主。

骑士的初始健康点数为一个正整数。如果他的健康点数在某一时刻降至 0 或以下，他会立即死亡。

有些房间由恶魔守卫，因此骑士在进入这些房间时会失去健康点数（若房间里的值为负整数，则表示骑士将损失健康点数）；其他房间要么是空的（房间里的值为 0），要么包含增加骑士健康点数的魔法球（若房间里的值为正整数，则表示骑士将增加健康点数）。

为了尽快到达公主，骑士决定每次只向右或向下移动一步。

编写一个函数来计算确保骑士能够拯救到公主所需的最低初始健康点数。

例如，考虑到如下布局的地下城，如果骑士遵循最佳路径 右 -> 右 -> 下 -> 下，则骑士的初始健康点数至少为 7。

-2 (K)	 -3	     3
-5	    -10	     1
10	     30	    -5 (P)

说明:
    骑士的健康点数没有上限。

    任何房间都可能对骑士的健康点数造成威胁，也可能增加骑士的健康点数，包括骑士进入的左上角房间以及公主被监禁的右下角房间。

"""
from typing import List

""" 动态规划 (从右下往左上进行动态规划) """
class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        r = len(dungeon)    # 行数
        c = len(dungeon[0]) # 列数
        BIG = 10 ** 9
        dp = [[BIG] * (c + 1) for _ in range(r + 1)]
        # 从右下往左上进行动态规划，令 dp[i][j] 表示从坐标 (i,j) 到终点所需的最小初始值
        dp[r][c - 1] = dp[r - 1][c] = 1 # 边界条件
        for i in range(r - 1, -1, -1):
            for j in range(c - 1, -1, -1):
                minn = min(dp[i + 1][j], dp[i][j + 1])
                dp[i][j] = max(minn - dungeon[i][j], 1)

        return dp[0][0]


""" 动态规划 (从右下往左上进行动态规划) """
class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        x = len(dungeon)
        y = len(dungeon[0])
        dp = [[None for __ in range(y)] for __ in range(x)]
        
        # 先填充最后一格
        dp[-1][-1] = 1 if dungeon[-1][-1] >= 0 else -dungeon[-1][-1]+1
        
        # 填充最后一列
        for i in range(x-2, -1, -1):
            tmp = dp[i+1][-1]-dungeon[i][-1]
            dp[i][-1] = 1 if tmp <= 0 else tmp
        
        # 填充最后一行
        for i in range(y-2, -1, -1):
            tmp = dp[-1][i+1]-dungeon[-1][i]
            dp[-1][i] = 1 if tmp <= 0 else tmp
        
        # 填充其他
        for i in range(x-2, -1, -1):
            for j in range(y-2, -1, -1):
                tmp = min(dp[i][j+1], dp[i+1][j])-dungeon[i][j]
                dp[i][j] = 1 if tmp <= 0 else tmp

        return dp[0][0]


if __name__ == "__main__":
    dungeon =  [[-2,  -3,  3],
                [-5, -10,  1],
                [10,  30, -5]]
    sol = Solution()
    result = sol.calculateMinimumHP(dungeon)
    print(result)