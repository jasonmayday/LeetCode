"""
https://leetcode-cn.com/problems/largest-palindrome-product/

给定一个整数 n ，返回 可表示为两个 n 位整数乘积的 最大回文整数 。因为答案可能非常大，所以返回它对 1337 取余 。

示例 1:
    输入：n = 2
    输出：987
    解释：99 x 91 = 9009, 9009 % 1337 = 987

示例 2:
    输入： n = 1
    输出： 9

提示:
    1 <= n <= 8

"""

""" 方法一：枚举 """
class Solution:
    def largestPalindrome(self, n: int) -> int:
        if n == 1:
            return 9
        upper = 10 ** n - 1
        for left in range(upper, upper // 10, -1):  # 枚举回文数的左半部分
            p, x = left, left
            while x:
                p = p * 10 + x % 10  # 翻转左半部分到其自身末尾，构造回文数 p
                x //= 10
            x = upper
            while x * x >= p:
                if p % x == 0:  # x 是 p 的因子
                    return p % 1337
                x -= 1

if __name__ == "__main__":
    n = 2
    sol = Solution()
    result = sol.largestPalindrome(n)
    print(result)