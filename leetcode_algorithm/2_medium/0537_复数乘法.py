"""
https://leetcode-cn.com/problems/complex-number-multiplication/

复数 可以用字符串表示，遵循 "实部+虚部i" 的形式，并满足下述条件：
    实部 是一个整数，取值范围是 [-100, 100]
    虚部 也是一个整数，取值范围是 [-100, 100]
    i^2 == -1

给你两个字符串表示的复数 num1 和 num2 ，请你遵循复数表示形式，返回表示它们乘积的字符串。

示例 1：
    输入：num1 = "1+1i", num2 = "1+1i"
    输出："0+2i"
    解释：(1 + i) * (1 + i) = 1 + i2 + 2 * i = 2i ，你需要将它转换为 0+2i 的形式。

示例 2：
    输入：num1 = "1+-1i", num2 = "1+-1i"
    输出："0+-2i"
    解释：(1 - i) * (1 - i) = 1 + i2 - 2 * i = -2i ，你需要将它转换为 0+-2i 的形式。

提示：
    num1 和 num2 都是有效的复数表示。

"""

""" 方法一：模拟 """
class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        real1, imag1 = map(int, num1[:-1].split('+'))
        real2, imag2 = map(int, num2[:-1].split('+'))
        return f'{real1 * real2 - imag1 * imag2}+{real1 * imag2 + imag1 * real2}i'


class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        # (a0 + b0*i) * (a1 + b1*i) = (a0 * a1 - b0 * b1) + (a0 * b1 + a1 * b0) * i
        a0, b0 = map(int, num1[:-1].split("+"))
        a1, b1 = map(int, num2[:-1].split("+"))
        return "{}+{}i".format(a0 * a1 - b0 * b1, a0 * b1 + a1 * b0)


if __name__ == "__main__":
    num1 = "1+1i"
    num2 = "1+1i"
    sol = Solution()
    result = sol.complexNumberMultiply(num1, num2)
    print (result)
