"""
https://leetcode-cn.com/problems/greatest-common-divisor-of-strings

对于字符串 S 和 T，只有在 S = T + ... + T（T 自身连接 1 次或多次）时，我们才认定 “T 能除尽 S”。

返回最长字符串 X，要求满足 X 能除尽 str1 且 X 能除尽 str2。

示例 1：
    输入：str1 = "ABCABC", str2 = "ABC"
    输出："ABC"

示例 2：
    输入：str1 = "ABABAB", str2 = "ABAB"
    输出："AB"

示例 3：
    输入：str1 = "LEET", str2 = "CODE"
    输出：""

提示：
    1 <= str1.length <= 1000
    1 <= str2.length <= 1000
    str1[i] 和 str2[i] 为大写英文字母

"""
import math

'''递归'''
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ''
        difference = len(str1) - len(str2)
        if difference == 0:
            return str1
        elif difference > 0:
            str1 = str1[len(str2): len(str1)]
        else:
            str2 = str2[len(str1): len(str2)]
        
        return self.gcdOfStrings(str1, str2)

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1: 
            return ''
        if str1 + str2 == str2 + str1:  
            return str1[:math.gcd(len(str1), len(str2))]


if __name__ == "__main__":
    str1 = "ABABAB"
    str2 = "ABAB"
    sol = Solution()
    result = sol.gcdOfStrings(str1,str2)
    print(result)