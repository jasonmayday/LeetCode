"""
https://leetcode-cn.com/problems/count-square-sum-triples/

一个 平方和三元组 (a,b,c) 指的是满足 a2 + b2 = c2 的 整数 三元组 a，b 和 c 。

给你一个整数 n ，请你返回满足 1 <= a, b, c <= n 的 平方和三元组 的数目。

示例 1：
    输入：n = 5
    输出：2
    解释：平方和三元组为 (3,4,5) 和 (4,3,5) 。

示例 2：
    输入：n = 10
    输出：4
    解释：平方和三元组为 (3,4,5)，(4,3,5)，(6,8,10) 和 (8,6,10) 。

提示：
    1 <= n <= 250

"""

from math import sqrt

class Solution:
    def countTriples(self, n: int) -> int:
        res = 0
        for a in range(1, n + 1):       # 枚举 a 与 b
            for b in range(1, n + 1):   # 判断是否符合要求
                c = int(sqrt(a ** 2 + b ** 2 + 1))
                if c <= n and c ** 2 == a ** 2 + b ** 2:
                    res += 1
        return res
    
class Solution:
    def countTriples(self, n: int) -> int:
        s = set([i*i for i in range(1, n+1)])   # s 是平方数 n = 10: s = {64, 1, 4, 36, 100, 9, 16, 49, 81, 25}
        ans = 0
        for i in range(1, n-1):
            for j in range(i+1, n):
                if i*i + j*j in s:
                    ans += 2
        return ans
    
if __name__ == "__main__":
    n = 10
    sol = Solution()
    result = sol.countTriples(n)
    print (result)  