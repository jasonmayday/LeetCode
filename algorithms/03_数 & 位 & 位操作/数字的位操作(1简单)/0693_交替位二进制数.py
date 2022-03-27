'''
https://leetcode-cn.com/problems/binary-number-with-alternating-bits/

给定一个正整数，检查它的二进制表示是否总是 0、1 交替出现：换句话说，就是二进制表示中相邻两位的数字永不相同。

示例 1：
    输入：n = 5
    输出：true
    解释：5 的二进制表示是：101

示例 2：
    输入：n = 7
    输出：false
    解释：7 的二进制表示是：111.

示例 3：
    输入：n = 11
    输出：false
    解释：11 的二进制表示是：1011.

示例 4：
    输入：n = 10
    输出：true
    解释：10 的二进制表示是：1010.

示例 5：
    输入：n = 3
    输出：false

'''
"""方法一：模拟"""
class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        prev = 2
        while n:            # 用对 2 取模再除以 2 的方法，依次求出输入的二进制表示的每一位
            cur = n % 2     # 并与前一位进行比较
            if cur == prev:     # 如果相同，则不符合条件
                return False
            prev = cur
            n //= 2
        return True

class Solution(object):
    def hasAlternatingBits(self, n: int) -> bool:
        return not ('11' in str(bin(n)) or '00' in str(bin(n)))


"""方法二：位运算"""
class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        a = n ^ (n >> 1)            # 对输入 n 的二进制表示右移一位后，得到的数字再与 n 按位异或得到 a
                                    # 当且仅当输入 n 为交替位二进制数时，a 的二进制表示全为 1（不包括前导 00）
        return a & (a + 1) == 0     # 将 a 与 a+1 按位与，当且仅当 a 的二进制表示全为 1 时，结果为 0


if __name__ == "__main__":
    n = 10
    sol = Solution()
    result = sol.hasAlternatingBits(n)
    print(result)