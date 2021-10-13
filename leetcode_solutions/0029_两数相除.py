'''

给定两个整数，被除数 dividend 和除数 divisor。将两数相除，要求不使用乘法、除法和 mod 运算符。

返回被除数 dividend 除以除数 divisor 得到的商。

整数除法的结果应当截去（truncate）其小数部分，例如：truncate(8.345) = 8 以及 truncate(-2.7335) = -2

示例 1:
输入: dividend = 10, divisor = 3
输出: 3
解释: 10/3 = truncate(3.33333..) = truncate(3) = 3

示例 2:
输入: dividend = 7, divisor = -3
输出: -2
解释: 7/-3 = truncate(-2.33333..) = -2

'''
# 方法1：递归
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        MIN_INT, MAX_INT = -2147483648, 2147483647  # [−2**31, 2**31−1]
        flag = 1                                    # 存储正负号，并将分子分母转化为正数
        if dividend < 0: flag, dividend = -flag, -dividend
        if divisor < 0: flag, divisor  = -flag, -divisor 
        
        def div(dividend, divisor):                 # 例：1023 / 1 = 512 + 256 + 128 + 64 + 32 + 16 + 8 + 4 + 1
            if dividend < divisor:
                return 0
            cur = divisor
            multiple = 1
            while cur + cur < dividend:             # 用加法求出保证divisor * multiple <= dividend的最大multiple
                cur += cur                          # 即cur分别乘以1, 2, 4, 8, 16...2^n，即二进制搜索
                multiple += multiple
            return multiple + div(dividend - cur, divisor)
        res = div(dividend, divisor)

        res = res if flag > 0 else -res             # 恢复正负号
        
        if res < MIN_INT:                           # 根据是否溢出返回结果
            return MIN_INT
        elif MIN_INT <= res <= MAX_INT:
            return res
        else:
            return MAX_INT
