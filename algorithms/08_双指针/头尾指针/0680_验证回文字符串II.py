"""
https://leetcode-cn.com/problems/valid-palindrome-ii

给定一个非空字符串 s，最多删除一个字符。判断是否能成为回文字符串。

示例 1:
    输入: s = "aba"
    输出: true

示例 2:
    输入: s = "abca"
    输出: true
    解释: 你可以删除c字符。

示例 3:
    输入: s = "abc"
    输出: false

提示:
    1 <= s.length <= 10^5
    s 由小写英文字母组成

"""

'''双指针'''
class Solution(object):
    def validPalindrome(self, s):
        # 匿名函数lambda：是指一类无需定义标识符（函数名）的函数或子程序。
        isPalindrome = lambda x : x == x[::-1]  # 判断是否回文使用了 [::-1] 翻转形成了新字符串
        left = 0
        right = len(s) - 1
        while left <= right:
            if s[left] == s[right]:     # 左右指针遇到的元素相等，继续向中间走；
                left += 1
                right -= 1
            else:       # 左右指针遇到的元素不等：[0, left) 和 (right, len(s) - 1] 这两部分已经判断过是回文的，因此不用再次判断。只用判断 [left, right] 区间中的字符串
                return isPalindrome(s[left + 1 : right + 1]) or isPalindrome(s[left: right])
        return True

class Solution:
    def validPalindrome(self, s: str) -> bool:
        def checkPalindrome(left, right):
            i, j = left, right
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        left, right = 0, len(s) - 1
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return checkPalindrome(left + 1, right) or checkPalindrome(left, right - 1)
        return True

if __name__ == "__main__":
    s = "abca"
    sol = Solution()
    result = sol.validPalindrome(s)
    print (result)
