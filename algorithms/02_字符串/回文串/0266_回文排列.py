"""
https://leetcode-cn.com/problems/palindrome-permutation/

给定一个字符串，判断该字符串中是否可以通过重新排列组合，形成一个回文字符串。

示例 1：
    输入: "code"
    输出: false

示例 2：
    输入: "aab"
    输出: true

示例 3：
    输入: "carerac"
    输出: true

"""
from collections import Counter

class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        return sum(x % 2 for x in Counter(s).values()) <= 1

class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        seen = set()
        for char in s:
            if char in seen:
                seen.remove(char)
            else:
                seen.add(char)
        return len(seen) <= 1

if __name__ == "__main__":
    s = "carerac"
    sol = Solution()
    result = sol.canPermutePalindrome(s)
    print (result)