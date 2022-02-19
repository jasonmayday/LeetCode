"""
https://leetcode-cn.com/problems/1-bit-and-2-bit-characters/

有两种特殊字符。第一种字符可以用一比特0来表示。第二种字符可以用两比特(10 或 11)来表示。

现给一个由若干比特组成的字符串。问最后一个字符是否必定为一个一比特字符。给定的字符串总是由0结束。

示例 1:
    输入: 
    bits = [1, 0, 0]
    输出: True
    解释: 
    唯一的编码方式是一个两比特字符和一个一比特字符。所以最后一个字符是一比特字符。

示例 2:
    输入: 
    bits = [1, 1, 1, 0]
    输出: False
    解释: 
    唯一的编码方式是两比特字符和两比特字符。所以最后一个字符不是一比特字符。

注意:
    1 <= len(bits) <= 1000.
    bits[i] 总是0 或 1.

"""
from typing import List


""" 方法一：正序遍历
    第一种字符一定以 0 开头，第二种字符一定以 1 开头"""
class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        i, n = 0, len(bits)
        while i < n - 1:
            i += bits[i] + 1
        return i == n - 1


""" 方法二：倒序遍历 """
class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        n = len(bits)
        i = n - 2
        while i >= 0 and bits[i]:
            i -= 1
        return (n - i) % 2 == 0


'''只与最后一个元素0的前面的连续1的个数有关系。'''
class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        n = len(bits)-1         # 最后一个下标
        i = 0
        while i < n:            # 遍历数组，
            if bits[i] == 0:    # 遇 0 索引 +1
                i += 1          # 因为第一种字符为0开头，只有1位
            else:               # 遇 1 索引 +2
                i += 2          # 因为第二种字符为1开头，10 或 11 都有2位
        if i > n:               # 下标超出范围
            return False
        else:                   # 刚好遍历到最后一个元素
            if bits[i] == 0:
                return True
            else:
                return False

        
if __name__ == "__main__":
    bits = [1, 1, 1, 0]
    sol = Solution()
    result = sol.isOneBitCharacter(bits)
    print(result)