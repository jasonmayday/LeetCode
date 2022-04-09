"""
https://leetcode-cn.com/problems/convert-integer-lcci/

整数转换。编写一个函数，确定需要改变几个位才能将整数A转成整数B。

示例1:
    输入：A = 29 （或者0b11101）, B = 15（或者0b01111）
    输出：2

示例2:
    输入：A = 1，B = 2
    输出：2

提示:
    A，B范围在[-2147483648, 2147483647]之间

本题与主站 461 题相同：https://leetcode-cn.com/problems/hamming-distance/

"""

class Solution:
    def convertInteger(self, A: int, B: int) -> int:
        res = 0
        c = A ^ B
        for i in range(32):
            res += c >> i & 1
        return res

class Solution:
    def convertInteger(self, A: int, B: int) -> int:
        return bin((A & 0xffffffff) ^ (B & 0xffffffff)).count('1') # 异或运算：0^0=0; 0^1=1; 1^0=1; 1^1=0

if __name__ == "__main__":
    A = 29
    B = 15
    sol = Solution()
    result = sol.convertInteger(A, B)
    print(result)