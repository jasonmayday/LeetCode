"""
https://leetcode-cn.com/problems/remove-duplicate-letters/

给你一个字符串 s ，请你去除字符串中重复的字母，使得每个字母只出现一次。需保证 返回结果的字典序最小（要求不能打乱其他字符的相对位置）。

示例 1：
    输入：s = "bcabc"
    输出："abc"

示例 2：
    输入：s = "cbacdcbc"
    输出："acdb"

提示：
    1 <= s.length <= 10^4
    s 由小写英文字母组成

注意：
    该题与 1081 https://leetcode-cn.com/problems/smallest-subsequence-of-distinct-characters 相同

"""
from collections import Counter

""" 方法一：贪心 + 单调栈 """
class Solution:
    def removeDuplicateLetters(self, s) -> int:
        stack = []
        remain_counter = Counter(s)
        for c in s:
            if c not in stack:
                while stack and c < stack[-1] and remain_counter[stack[-1]] > 0:
                    stack.pop()
                stack.append(c)
            remain_counter[c] -= 1
        return ''.join(stack)

if __name__ == "__main__":
    s = "bcabc"
    sol = Solution()
    result = sol.removeDuplicateLetters(s)
    print (result)