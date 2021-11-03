'''
https://leetcode-cn.com/problems/add-binary/

给你两个二进制字符串，返回它们的和（用二进制表示）。

输入为 非空 字符串且只包含数字 1 和 0。

示例 1:
    输入: a = "11", b = "1"
    输出: "100"

示例 2:
    输入: a = "1010", b = "1011"
    输出: "10101"

提示：
    每个字符串仅由字符 '0' 或 '1' 组成。
    1 <= a.length, b.length <= 10^4
    字符串如果不是 "0" ，就都不含前导零。

'''
a = "1010"
b = "1011"

class Solution:
    def addBinary(self, a, b) -> str:
        return '{0:b}'.format(int(a, 2) + int(b, 2))
        # {0:b}.format 将整型转换为二进制。b、d、o、x分别是二进制、十进制、八进制、十六进制
        # int(x, base) 函数用于将一个字符串或数字转换为整型。

sol = Solution()
result = sol.addBinary(a, b)
print (result)