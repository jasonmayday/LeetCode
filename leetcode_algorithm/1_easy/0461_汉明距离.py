"""
https://leetcode-cn.com/problems/hamming-distance/

两个整数之间的 汉明距离 指的是这两个数字对应二进制位不同的位置的数目。

给你两个整数 x 和 y，计算并返回它们之间的汉明距离。

示例 1：
    输入：x = 1, y = 4
    输出：2
    解释：
    1    (0 0 0 1)
    4    (0 1 0 0)
            ↑   ↑
    上面的箭头指出了对应二进制位不同的位置。

示例 2：
    输入：x = 3, y = 1
    输出：1
 
提示：
    0 <= x, y <= 2^31 - 1

"""

'''解法1：异或运算'''
class Solution:
    def convertInteger(self, A: int, B: int) -> int:
        x = A ^ B
        count = 0
        while x != 0:
            x &= x - 1
            count += 1
        return count

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x ^ y).count('1') # 异或运算：0^0=0; 0^1=1; 1^0=1; 1^1=0

if __name__ == "__main__":
    x = 1
    y = 4
    sol = Solution()
    result = sol.hammingDistance(x, y)
    print(result)
