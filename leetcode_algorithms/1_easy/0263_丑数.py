"""

给你一个整数 n ，请你判断 n 是否为 丑数 。如果是，返回 true ；否则，返回 false 。

丑数 就是只包含质因数 2、3 和/或 5 的正整数。

示例 1：
    输入：n = 6
    输出：true
    解释：6 = 2 × 3

示例 2：
    输入：n = 8
    输出：true
    解释：8 = 2 × 2 × 2
    
示例 3：
    输入：n = 14
    输出：false
    解释：14 不是丑数，因为它包含了另外一个质因数 7 。

示例 4：
    输入：n = 1
    输出：true
    解释：1 通常被视为丑数。

提示：
    -2^31 <= n <= 2^31 - 1

"""

class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False

        factors = [2, 3, 5]         # 把 n 对 2、3、5 整除，看最后是否仅剩下 1。
        for factor in factors:
            while n % factor == 0:
                n = n // factor     # // 取整除 - 返回商的整数部分
        
        return n == 1

class Solution(object):
    def isUgly(self, n):
        if n <= 0:
            return False
        while n % 2 == 0:
            n //= 2
        while n % 3 == 0:
            n //= 3
        while n % 5 == 0:
            n //= 5
        return n == 1

if __name__ == "__main__":
    n = 8
    sol = Solution()
    result = sol.isUgly(n)
    print(result)