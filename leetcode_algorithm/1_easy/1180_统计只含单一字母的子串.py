"""
https://leetcode-cn.com/problems/count-substrings-with-only-one-distinct-letter/

给你一个字符串 s，返回 只含 单一字母 的子串个数 。

示例 1：
    输入： s = "aaaba"
    输出： 8
    解释： 只含单一字母的子串分别是 "aaa"， "aa"， "a"， "b"。
        "aaa" 出现 1 次。
        "aa" 出现 2 次。
        "a" 出现 4 次。
        "b" 出现 1 次。
        所以答案是 1 + 2 + 4 + 1 = 8。

示例 2:
    输入： s = "aaaaaaaaaa"
    输出： 55

提示：
    1 <= s.length <= 1000
    s[i] 仅由小写英文字母组成

"""

class Solution:
    def countLetters(self, S: str) -> int:
        n = len(S)
        res = 0
        cnt = 1
        for i in range(1, n):
            if S[i-1] == S[i]:
                cnt += 1
            else:               # 当出现下一个不同的字符时：
                res += (cnt + 1) * cnt // 2 # 开始统计该字符之前的连续字符的子字符个数
                cnt = 1
        res += (cnt + 1) * cnt // 2
        return res


if __name__ == "__main__":
    s = "aaaba"
    sol = Solution()
    result = sol.countLetters(s)
    print(result)