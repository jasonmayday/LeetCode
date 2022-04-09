"""
https://leetcode-cn.com/problems/check-permutation-lcci/

给定两个字符串 s1 和 s2，请编写一个程序，确定其中一个字符串的字符重新排列后，能否变成另一个字符串。

示例 1：
    输入: s1 = "abc", s2 = "bca"
    输出: true

示例 2：
    输入: s1 = "abc", s2 = "bad"
    输出: false

说明：
    0 <= len(s1) <= 100
    0 <= len(s2) <= 100

"""
from collections import defaultdict

""" 哈希表"""
class Solution:
    def CheckPermutation(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False
        dic = defaultdict(int)
        for c in s1:
            dic[c] += 1
        for c in s2:
            dic[c] -= 1
        for val in dic.values():
            if val != 0:
                return False
        return True
    
""" 位运算 """
class Solution:
    def CheckPermutation(self, s1: str, s2: str) -> bool:
        length_1= len(s1)
        if length_1 != len(s2):
            return False

        result = 0
        for i in range(length_1):
            result += 1<< ord(s1[i])
            result -= 1<< ord(s2[i])

        return result == 0


if __name__ == "__main__":
    s1 = "abc"
    s2 = "bca"
    sol = Solution()
    result = sol.CheckPermutation(s1, s2)
    print(result)