"""
https://leetcode-cn.com/problems/longest-valid-parentheses/

给你一个只包含 '(' 和 ')' 的字符串，找出最长有效（格式正确且连续）括号子串的长度。

示例 1：
    输入：s = "(()"
    输出：2
    解释：最长有效括号子串是 "()"

示例 2：
    输入：s = ")()())"
    输出：4
    解释：最长有效括号子串是 "()()"

示例 3：
    输入：s = ""
    输出：0

提示：
    0 <= s.length <= 3 * 104
    s[i] 为 '(' 或 ')'

"""

""" 栈 """
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s:
            return 0
        res = 0
        stack = [-1]
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    res = max(res,i - stack[-1])
        return res

""" 动态规划 """
class Solution(object):
    def longestValidParentheses(self, s: str) -> int:
        length = len(s)
        if length == 0:
            return 0
        dp = [0] * length       # dp[i] 表示以 i 结尾的最长有效括号长度
        for i in range(1,length):
            if s[i] == ')':     # 当遇到右括号时，尝试向前匹配左括号
                pre = i - dp[i-1] -1
                if pre >= 0 and s[pre] == '(':  # 如果是左括号，则更新匹配长度
                    dp[i] = dp[i-1] + 2
                    # 处理独立的括号对的情形 类似()()、()(())
                    if pre > 0:
                        dp[i] += dp[pre-1]
        return max(dp)

""" 贪心 """
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        def comp(strings, order=True):
            ret = 0
            left = right = 0
            for i in strings:
                if i == '(':
                    left += 1
                else:
                    right += 1
                if left == right:
                    ret = max(ret, left * 2)
                elif order ^ (left > right):
                    left = right = 0
            return ret
        return max(comp(s), comp(s[::-1], False))


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        if n == 0: return 0
        dp = [0] * n
        res = 0
        for i in range(n):
            if i>0 and s[i] == ")":
                if  s[i - 1] == "(":
                    dp[i] = dp[i - 2] + 2
                elif s[i - 1] == ")" and i - dp[i - 1] - 1 >= 0 and s[i - dp[i - 1] - 1] == "(":
                    dp[i] = dp[i - 1] + 2 + dp[i - dp[i - 1] - 2]
                if dp[i] > res:
                    res = dp[i]
        return res

if __name__ == "__main__":
    s = ")()())"
    sol = Solution()
    result = sol.longestValidParentheses(s)
    print(result)