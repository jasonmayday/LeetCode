"""
给定字符串 s 和 t ，判断 s 是否为 t 的子序列。

字符串的一个子序列是原始字符串删除一些（也可以不删除）字符而不改变剩余字符相对位置形成的新字符串。（例如，"ace"是"abcde"的一个子序列，而"aec"不是）。

进阶：
    如果有大量输入的 S，称作 S1, S2, ... , Sk 其中 k >= 10亿，你需要依次检查它们是否为 T 的子序列。在这种情况下，你会怎样改变代码？

示例 1：
    输入：s = "abc", t = "ahbgdc"
    输出：true

示例 2：
    输入：s = "axc", t = "ahbgdc"
    输出：false

提示：
    0 <= s.length <= 100
    0 <= t.length <= 10^4
    两个字符串都只由小写字符组成。

"""

'''双指针'''
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = j = 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == len(s)

'''递归'''
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:       # 递归停止条件。如果s是空：
            return True # 返回True。
        if s[0] in t:
            inx = t.index(s[0])
            return self.isSubsequence(s[1:], t[inx+1:]) # 将后面的字符串当参数传递给isSubsequence并返回。
        return False

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        for i in t:
            if s[0] == i:
                s = s[1:]
            if not s:
                return True
        return False

if __name__ == "__main__":
    s = "abc"
    t = "ahbgdc"
    sol = Solution()
    result = sol.isSubsequence(s,t)
    print (result) 