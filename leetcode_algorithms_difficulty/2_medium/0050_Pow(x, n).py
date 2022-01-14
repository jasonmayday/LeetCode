"""
https://leetcode-cn.com/problems/powx-n/

实现 pow(x, n) ，即计算 x 的 n 次幂函数（即，xn ）。

示例 1：
    输入：x = 2.00000, n = 10
    输出：1024.00000

示例 2：
    输入：x = 2.10000, n = 3
    输出：9.26100

示例 3：
    输入：x = 2.00000, n = -2
    输出：0.25000
    解释：2-2 = 1/22 = 1/4 = 0.25

提示：
    -100.0 < x < 100.0
    -2^31 <= n <= 2^31-1
    -10^4 <= x^n <= 10^4

"""

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0.0:
            return 0.0
        res = 1
        if n < 0:
            x, n = 1 / x, -n
        while n:
            if n & 1:
                res *= x
            x *= x
            n >>= 1
        return res
    
if __name__ == "__main__":
    x = 2.10000
    n = 3
    sol = Solution()
    result = sol.myPow(x, n)
    print(result)