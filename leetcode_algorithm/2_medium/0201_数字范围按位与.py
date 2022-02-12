"""
https://leetcode-cn.com/problems/bitwise-and-of-numbers-range/

给你两个整数 left 和 right ，表示区间 [left, right] ，返回此区间内所有数字 按位与 的结果（包含 left 、right 端点）。

示例 1：
    输入：left = 5, right = 7
    输出：4

示例 2：
    输入：left = 0, right = 0
    输出：0

示例 3：
    输入：left = 1, right = 2147483647
    输出：0

提示：
    0 <= left <= right <= 2^31 - 1

"""

""" 位移 + 公共前缀
    规律：对所有数字执行按位与运算的结果是所有对应二进制字符串的公共前缀再用零补上后面的剩余位。 """
class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        shift = 0
        while left < right:
            left = left >> 1    # 将二进制不断做右移，
            right = right >> 1  # 当 left 和 right 相同时停止，这样可以找到二进制的公共前缀
            shift += 1          # 每右移一位，位移次数计数 +1
        return right << shift   # 再把变化后的 left 或者 right 左移 之前 右移过的步数
"""
9   0000 1001
10  0000 1010
11  0000 1011
12  0000 1100
"""
if __name__ == "__main__":
    left = 9
    right = 12
    sol = Solution()
    result = sol.rangeBitwiseAnd(left, right)
    print (result)