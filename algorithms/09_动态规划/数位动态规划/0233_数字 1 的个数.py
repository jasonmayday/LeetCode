"""
https://leetcode-cn.com/problems/number-of-digit-one/

给定一个整数 n，计算所有小于等于 n 的非负整数中数字 1 出现的个数。

示例 1：
    输入：n = 13
    输出：6

示例 2：
    输入：n = 0
    输出：0

提示：
    0 <= n <= 10^9

"""

class Solution:
    def countDigitOne(self, n: int) -> int:
        digit = 1
        res = 0
        
        high = n // 10  # 高位
        cur = n % 10    # 当前位
        low = 0         # 低位
        
        while high != 0 or cur != 0:
            if cur == 0:
                res += high * digit
            elif cur == 1:
                res += high * digit + low + 1
            else:
                res += (high + 1) * digit
            low += cur * digit
            cur = high % 10
            high //= 10
            digit *= 10
        return res

if __name__ == "__main__":
    n = 123456789
    sol = Solution()
    result = sol.countDigitOne(n)
    print(result)