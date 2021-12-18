"""
https://leetcode-cn.com/problems/find-the-difference/

给定两个字符串 s 和 t，它们只包含小写字母。

字符串 t 由字符串 s 随机重排，然后在随机位置添加一个字母。

请找出在 t 中被添加的字母。

示例 1：
    输入：s = "abcd", t = "abcde"
    输出："e"
    解释：'e' 是那个被添加的字母。

示例 2：
    输入：s = "", t = "y"
    输出："y"

示例 3：
    输入：s = "a", t = "aa"
    输出："a"

示例 4：
    输入：s = "ae", t = "aea"
    输出："a"
 
提示：
    0 <= s.length <= 1000
    t.length == s.length + 1
    s 和 t 只包含小写字母

"""
from collections import Counter
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        return list(Counter(t) - Counter(s))[0]

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s = list(s)
        t = list(t)
        s.sort()
        t.sort()
        for i in range(len(s)):
            if s[i] != t[i]:
                return t[i]
        return t[-1]

'''出现奇数次的字母即为不同的数字'''
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        a = "".join([s,t])              # 首先将两个字符串合并为a
        for ch in a:
            if a.count(ch) % 2 == 1:    # 在a中遍历，如果出现奇数次的字符即为不同的字符
                return ch

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        for i in t:
            if t.count(i) - s.count(i)==1:
                return i

if __name__ == "__main__":
    s = "abcd"
    t = "abcde"
    sol = Solution()
    result = sol.findTheDifference(s,t)
    print (result) 