"""
https://leetcode-cn.com/problems/n-th-tribonacci-number/

泰波那契序列 Tn 定义如下： 

T0 = 0, T1 = 1, T2 = 1, 且在 n >= 0 的条件下 Tn+3 = Tn + Tn+1 + Tn+2

给你整数 n，请返回第 n 个泰波那契数 Tn 的值。

示例 1：
    输入：n = 4
    输出：4
    解释：
    T_3 = 0 + 1 + 1 = 2
    T_4 = 1 + 1 + 2 = 4

示例 2：
    输入：n = 25
    输出：1389537

提示：
    0 <= n <= 37
    答案保证是一个 32 位整数，即 answer <= 2^31 - 1。
    
"""
import functools

'''递归 + 记忆化搜索'''
class Solution:
    @functools.lru_cache()
    def tribonacci(self, n: int) -> int:
        if n == 0: return 0
        if n == 1: return 1
        if n == 2: return 1
        return self.tribonacci(n - 1) + self.tribonacci(n - 2) + self.tribonacci(n - 3)

'''动态规划'''
class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n <= 2:
            return 1
        
        a, b, c = 0, 1, 1
        for i in range(3, n + 1):
            d = a + b + c
            a, b, c = b, c, d
        return d

if __name__ == "__main__":
    n = 37
    sol = Solution()
    result = sol.tribonacci(n)
    print(result)