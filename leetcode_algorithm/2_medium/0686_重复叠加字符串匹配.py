"""
https://leetcode-cn.com/problems/repeated-string-match/

给定两个字符串 a 和 b，寻找重复叠加字符串 a 的最小次数，使得字符串 b 成为叠加后的字符串 a 的子串，如果不存在则返回 -1。

注意：字符串 "abc" 重复叠加 0 次是 ""，重复叠加 1 次是 "abc"，重复叠加 2 次是 "abcabc"。

示例 1：
    输入：a = "abcd", b = "cdabcdab"
    输出：3
    解释：a 重复叠加三遍后为 "abcdabcdabcd", 此时 b 是其子串。

示例 2：
    输入：a = "a", b = "aa"
    输出：2

示例 3：
    输入：a = "a", b = "a"
    输出：1

示例 4：
    输入：a = "abc", b = "wxyz"
    输出：-1

提示：
    1 <= a.length <= 10^4
    1 <= b.length <= 10^4
    a 和 b 由小写英文字母组成

"""

class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        if b in a:
            return 1
        num = 1
        a_sub = a       # 最初的未经重复叠加的字符串 a 定义为 a_sub
        while True:
            num += 1    # 叠加次数
            a += a_sub  # 字符串 a 叠加最初的字符串 a
            if b in a:
                return num
            if len(a) > len(b) + len(a_sub):
                return -1

if __name__ == "__main__":
    a = "abcd"
    b = "cdabcdab"
    sol = Solution()
    result = sol.repeatedStringMatch(a,b)
    print (result) 