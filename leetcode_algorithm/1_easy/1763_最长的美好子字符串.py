"""
https://leetcode-cn.com/problems/longest-nice-substring/

当一个字符串 s 包含的每一种字母的大写和小写形式 同时 出现在 s 中，就称这个字符串 s 是 美好 字符串。
比方说，"abABB" 是美好字符串，因为 'A' 和 'a' 同时出现了，且 'B' 和 'b' 也同时出现了。
然而，"abA" 不是美好字符串因为 'b' 出现了，而 'B' 没有出现。

给你一个字符串 s ，请你返回 s 最长的 美好子字符串 。如果有多个答案，请你返回 最早 出现的一个。如果不存在美好子字符串，请你返回一个空字符串。

示例 1：
    输入：s = "YazaAay"
    输出："aAa"
    解释："aAa" 是一个美好字符串，因为这个子串中仅含一种字母，其小写形式 'a' 和大写形式 'A' 也同时出现了。
    "aAa" 是最长的美好子字符串。

示例 2：
    输入：s = "Bb"
    输出："Bb"
    解释："Bb" 是美好字符串，因为 'B' 和 'b' 都出现了。整个字符串也是原字符串的子字符串。

示例 3：
    输入：s = "c"
    输出：""
    解释：没有美好子字符串。

示例 4：
    输入：s = "dDzeE"
    输出："dD"
    解释："dD" 和 "eE" 都是最长美好子字符串。
    由于有多个美好子字符串，返回 "dD" ，因为它出现得最早。

提示：
    1 <= s.length <= 100
    s 只包含大写和小写英文字母。

"""


"""暴力枚举子串 + 检测"""
class Solution(object):
    def longestNiceSubstring(self, s):
        maxsub = ""
        for i in range(len(s)):
            for j in range(i+1, len(s)):
                sub = s[i:j+1]
                if self.isNice(sub):
                    maxsub = max(maxsub, sub, key = len)
        return maxsub

    def isNice(self, s):
        if len(s) < 2:
            return False
        for ch in s:
            if ch.swapcase() not in s:
                return False
        return True


"""暴力枚举子串 + 检测"""
class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        n = len(s)
        maxPos, maxLen = 0, 0
        for i in range(n):
            lower, upper = 0, 0
            for j in range(i, n):
                if s[j].islower():
                    lower |= 1 << (ord(s[j]) - ord('a'))
                else:
                    upper |= 1 << (ord(s[j]) - ord('A'))
                if lower == upper and j - i + 1 > maxLen:
                    maxPos = i
                    maxLen = j - i + 1
        return s[maxPos: maxPos + maxLen]


"""分治"""
class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        d = set(s)
        for ch in s:
            if ch.swapcase() not in d:
                return max((self.longestNiceSubstring(t) for t in s.split(ch)), key=len)
        return s


"""递归"""
class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        if len(s) < 2:
            return '' 
        for i, val in enumerate(s):     # 下标，数字
            if (val.islower() and val.upper() not in s) or (val.isupper() and val.lower() not in s):
                return max((self.longestNiceSubstring(s[:i]),self.longestNiceSubstring(s[i+1:])),key = len)
        return s


"""DFS回溯法"""
class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        def DFS(s): # 递归，不断分割，回溯法
            if len(s)<2:    # 判断长度小于2，则必不可能是美丽字符串
                return ''
            for i, val in enumerate(s): # 对字符串遍历
                if val.islower():               # 如果某字符串是小写
                    if val.upper() not in s:    # 如果对应的大写不在，
                        left_str = DFS(s[:i])   # 则应当在此处对字符串进行分割，即最后的美丽字符串一定不包含当前字符
                        right_str = DFS(s[i+1:])
                        if len(left_str) >= len(right_str): # 对返回的字符串长度判断，长的保留
                            return left_str
                        else:
                            return right_str
                else:                           # 如果某字符串是大写
                    if val.lower() not in s:    #
                        left_str = DFS(s[:i])
                        right_str = DFS(s[i+1:])
                        if len(left_str) >= len(right_str):
                            return left_str
                        else:
                            return right_str
            return s    # 字符串遍历完，所有的字符都有对应的，则表明当前的字符串就是美丽字符串
        return DFS(s)


if __name__ == "__main__":
    s = "YazaAay"
    sol = Solution()
    result = sol.longestNiceSubstring(s)
    print(result)