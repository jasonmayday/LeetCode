"""
https://leetcode.cn/problems/matchsticks-to-square/

你将得到一个整数数组 matchsticks ，其中 matchsticks[i] 是第 i 个火柴棒的长度。
你要用 所有的火柴棍 拼成一个正方形。你 不能折断 任何一根火柴棒，但你可以把它们连在一起，而且每根火柴棒必须 使用一次 。

如果你能使这个正方形，则返回 true ，否则返回 false 。

示例 1:
    输入: matchsticks = [1,1,2,2,2]
    输出: true
    解释: 能拼成一个边长为2的正方形，每边两根火柴。

示例 2:
    输入: matchsticks = [3,3,3,3,4]
    输出: false
    解释: 不能用所有火柴拼成一个正方形。

提示:
    1 <= matchsticks.length <= 15
    1 <= matchsticks[i] <= 10^8

"""
from re import I
from typing import List

"""方法一：回溯"""
class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        totalLen = sum(matchsticks)     # 火柴总长度
        if totalLen % 4:
            return False                    # 总长度不能被4整除，则一定不能
        matchsticks.sort(reverse = True)

        edges = [0] * 4
        def dfs(idx: int) -> bool:
            if idx == len(matchsticks):
                return True
            for i in range(4):
                edges[i] += matchsticks[idx]
                if edges[i] <= totalLen // 4 and dfs(idx + 1):
                    return True
                edges[i] -= matchsticks[idx]
            return False
        return dfs(0)

"""方法二：状态压缩 + 动态规划"""
class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        totalLen = sum(matchsticks)
        if totalLen % 4:
            return False
        tLen = totalLen // 4

        dp = [-1] * (1 << len(matchsticks))
        dp[0] = 0
        for s in range(1, len(dp)):
            for k, v in enumerate(matchsticks):
                if s & (1 << k) == 0:
                    continue
                s1 = s & ~(1 << k)
                if dp[s1] >= 0 and dp[s1] + v <= tLen:
                    dp[s] = (dp[s1] + v) % tLen
                    break
        return dp[-1] == 0

if __name__ == "__main__":
    matchsticks = [1,1,2,2,2]
    sol = Solution()
    result = sol.makesquare(matchsticks)
    print (result)
    

