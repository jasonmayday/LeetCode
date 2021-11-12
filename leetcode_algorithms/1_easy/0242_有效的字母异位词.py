"""
https://leetcode-cn.com/problems/valid-anagram/

给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。

注意：若 s 和 t 中每个字符出现的次数都相同，则称 s 和 t 互为字母异位词。

示例 1:
    输入: s = "anagram", t = "nagaram"
    输出: true

示例 2:
    输入: s = "rat", t = "car"
    输出: false
 
提示:
    1 <= s.length, t.length <= 5 * 10^4
    s 和 t 仅包含小写字母

"""

from collections import Counter

class Solution(object):
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count = {}
        for char in s:
            if char in count:
                count[char] += 1
            else:
                count[char] = 1
        for char in t:
            if char in count:
                count[char] -= 1
            else:
                return False
        for value in count.values():
            if value != 0:
                return False
        return True

    
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s)==Counter(t)


if __name__ == "__main__":
    s = "anagram"
    t = "nagaram"

    sol = Solution()
    result = sol.isAnagram(s, t)
    print(result)