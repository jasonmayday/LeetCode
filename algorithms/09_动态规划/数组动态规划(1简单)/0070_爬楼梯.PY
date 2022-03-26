'''
https://leetcode-cn.com/problems/climbing-stairs/

假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

注意：给定 n 是一个正整数。

示例 1：
    输入： 2
    输出： 2
    解释： 有两种方法可以爬到楼顶。
        1.  1 阶 + 1 阶
        2.  2 阶

示例 2：
    输入： 3
    输出： 3
    解释： 有三种方法可以爬到楼顶。
        1.  1 阶 + 1 阶 + 1 阶
        2.  1 阶 + 2 阶
        3.  2 阶 + 1 阶

'''

""" 动态规划
    比如：现在我们的小青蛙就站在第五个台阶上，它一次跳两个台阶就上去了，或者现在就站在第六个台阶上，一次跳一个上去了。
    那么我们只要知道小青蛙跳五层台阶和跳六层台阶的方案数目即可。
"""
class Solution(object):
    def climbStairs(self, n):
        if n == 1: return 1
        if n == 2: return 2
        dp = [0] * n
        dp[0] = 1
        dp[1] = 2
        for i in range(2, n):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[-1]

class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [1, 1]
        for i in range(2, n + 1):
            dp.append(dp[i - 1] + dp[i - 2])
        return dp[n]

class Solution:
    def climbStairs(self, n: int) -> int:
        cur, nxt = 1, 1
        for _ in range(n):
            cur, nxt = nxt, cur + nxt
        return cur

if __name__ == "__main__":
    n = 20
    sol = Solution()
    result = sol.climbStairs(n)
    print(result)
