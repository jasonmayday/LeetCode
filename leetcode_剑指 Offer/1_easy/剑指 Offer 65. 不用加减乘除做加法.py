"""
https://leetcode-cn.com/problems/bu-yong-jia-jian-cheng-chu-zuo-jia-fa-lcof/

写一个函数，求两个整数之和，要求在函数体内不得使用 “+”、“-”、“*”、“/” 四则运算符号。

示例:
    输入: a = 1, b = 1
    输出: 2

提示：
    a, b 均可能是负数或 0
    结果不会溢出 32 位整数

"""

""" 位运算"""
class Solution:
    def add(self, a: int, b: int) -> int:
        x = 0xffffffff
        a = a & x   # 获取负数的补码： 需要将数字与十六进制数 0xffffffff 相与
        b = b & x   # 可理解为舍去此数字 32 位以上的数字（将 32 位以上都变为 0 ），从无限长度变为一个 32 位整数。
        while b != 0:
            a, b = (a ^ b), (a & b) << 1 & x
        if a <= 0x7fffffff:
            return a
        else:
            return ~(a ^ x)

if __name__ == "__main__":
    a = -1
    b = 1
    sol = Solution()
    result = sol.add(a, b)
    print (result)