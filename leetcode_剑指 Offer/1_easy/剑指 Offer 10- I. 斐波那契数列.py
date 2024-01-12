"""
https://leetcode-cn.com/problems/fei-bo-na-qi-shu-lie-lcof/

写一个函数，输入 n ，求斐波那契（Fibonacci）数列的第 n 项（即 F(N)）。斐波那契数列的定义如下：

    F(0) = 0,   F(1) = 1
    F(N) = F(N - 1) + F(N - 2), 其中 N > 1.

斐波那契数列由 0 和 1 开始，之后的斐波那契数就是由之前的两数相加而得出。

答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。

示例 1：
    输入：n = 2
    输出：1

示例 2：
    输入：n = 5
    输出：5

提示：
    0 <= n <= 100

"""

""" 记忆化递归 """
class Solution:
    def fib(self, n: int) -> int:
        F = [0, 1]       # 用数组记录下来所有小于n的fib(n)
        for i in range(2, n+1):
            F.append(F[i-1] + F[i-2])
        return F[n]

""" 动态规划 """
class Solution:
    def fib(self, n: int) -> int:
        if n == 0: return 0         # 若求 f(0) 则直接返回 0
        dp = [0] * (n + 1)          # 初始化 dp 列表, dp[n]是数列的第n项
        dp[0] = 0
        dp[1] = 1                   # 初始化 f(0), f(1)
        for i in range(2, n + 1):   # 状态转移求取 f(2), f(3), ..., f(n)
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n] % 1000000007   # 返回 f(n)

class Solution:
    def fib(self, n: int) -> int:
        if n == 0: return 0       # 若求 f(0) 则直接返回 0
        a, b = 0, 1               # 初始化 f(0), f(1)
        for _ in range(2, n + 1): # 状态转移求取 f(2), f(3), ..., f(n)
            a = b
            b = a + b
        return b                  # 返回 f(n)

if __name__ == "__main__":
    n = 100
    sol = Solution()
    result = sol.fib(n)
    print(result)
