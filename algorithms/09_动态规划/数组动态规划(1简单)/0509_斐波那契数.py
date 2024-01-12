'''
https://leetcode-cn.com/problems/fibonacci-number/

斐波那契数，通常用 F(n) 表示，形成的序列称为 斐波那契数列 。该数列由 0 和 1 开始，后面的每一项数字都是前面两项数字的和。也就是：
    F(0) = 0，F(1) = 1
    F(n) = F(n - 1) + F(n - 2)，其中 n > 1

给你 n ，请计算 F(n) 。

示例 1：
    输入：2
    输出：1
    解释：F(2) = F(1) + F(0) = 1 + 0 = 1

示例 2：
    输入：3
    输出：2
    解释：F(3) = F(2) + F(1) = 1 + 1 = 2

示例 3：
    输入：4
    输出：3
    解释：F(4) = F(3) + F(2) = 2 + 1 = 3

'''

""" 记忆化递归 """
class Solution:
    def fib(self, n: int) -> int:
        F = [0, 1]       # 用数组记录下来所有小于n的fib(n)
        for i in range(2, n+1):
            F.append(F[i-1] + F[i-2])
        return F[n]
    
class Solution:
    def fib(self, n: int) -> int:
        res = [0, 1]
        if n < 2:
            return res[n]
        for i in range(2, n+1):
            res.append(res[i-2]+res[i-1])
        return res[-1]

""" 动态规划 """
class Solution:
    def fib(self, n: int) -> int:
        if n == 0: return 0         # 若求 f(0) 则直接返回 0
        dp = [0] * (n + 1)          # 初始化 dp 列表
        dp[0] = 0
        dp[1] = 1                   # 初始化 f(0), f(1)
        for i in range(2, n + 1):   # 状态转移求取 f(2), f(3), ..., f(n)
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]                # 返回 f(n)

class Solution:
    def fib(self, n: int) -> int:
        if n == 0: return 0       # 若求 f(0) 则直接返回 0
        a, b = 0, 1               # 初始化 f(0), f(1)
        for _ in range(2, n + 1): # 状态转移求取 f(2), f(3), ..., f(n)
            res = a + b
            a = b
            b = res
        return res                # 返回 f(n)

if __name__ == "__main__":
    n = 9
    sol = Solution()
    result = sol.fib(n)
    print(result)