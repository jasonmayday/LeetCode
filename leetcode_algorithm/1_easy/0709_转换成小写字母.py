"""
https://leetcode-cn.com/problems/to-lower-case/

给你一个字符串 s ，将该字符串中的大写字母转换成相同的小写字母，返回新的字符串。

示例 1：
    输入：s = "Hello"
    输出："hello"

示例 2：
    输入：s = "here"
    输出："here"

示例 3：
    输入：s = "LOVELY"
    输出："lovely"

提示：
    1 <= s.length <= 100
    s 由 ASCII 字符集中的可打印字符组成

"""
class Solution:
    def toLowerCase(self, s: str) -> str:
        return s.lower()
    
# 'A' - 'Z' 对应的 ascii 是 65 - 90；
# 'a' - 'z' 对应的 ascii 是 97 - 122；
# 大小字母转换相差32，解题只要记住ord(),chr()函数即可
class Solution:
    def toLowerCase(self, str: str) -> str:
        s = []
        for i in str:
            if  65 <= ord(i) <= 90:
                s.append(chr(ord(i) + 32))
            else:
                s.append(i)
        return ''.join(s)

if __name__ == "__main__":
    s = "LOVELY"
    sol = Solution()
    result = sol.toLowerCase(s)
    print(result)
