"""
https://leetcode-cn.com/problems/dKk3P7/

给定两个字符串 s 和 t ，编写一个函数来判断它们是不是一组变位词（字母异位词）。

注意：若 s 和 t 中每个字符出现的次数都相同且字符顺序不完全相同，则称 s 和 t 互为变位词（字母异位词）。

示例 1:
    输入: s = "anagram", t = "nagaram"
    输出: true

示例 2:
    输入: s = "rat", t = "car"
    输出: false

示例 3:
    输入: s = "a", t = "a"
    输出: false

提示:
    1 <= s.length, t.length <= 5 * 10^4
    s and t 仅包含小写字母

进阶: 如果输入字符串包含 unicode 字符怎么办？你能否调整你的解法来应对这种情况？

注意：本题与主站 242 题相似（字母异位词定义不同）：https://leetcode-cn.com/problems/valid-anagram/

"""
from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return s != t and Counter(s) == Counter(t)
    
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False # 长度不同不可能是
        if s == t:
            return False # 完全相同就不是变位词
        char_map = [0 for _ in range(26)]
        for char in s:
            char_map[ord(char) - ord('a')] += 1     # s字符出现时+1
        for char in t:
            char_map[ord(char) - ord('a')] -= 1     # t字符出现时-1
        for cnt in char_map:
            if cnt:                                 # 最后检查是否全部为0即可。
                return False
        return True

class Solution(object):
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count = {}
        for char in s:              # 用哈希表统计第一个字符串中的字符数量
            if char in count:
                count[char] += 1
            else:
                count[char] = 1
        for char in t:
            if char in count:
                count[char] -= 1    # 再统计第二个字符串时，若字符在哈希表中，计数减一
            else:
                return False
        for value in count.values():
            if value != 0:          # 最后判断哈希表中值是否都为0
                return False
        return True

if __name__ == "__main__":
    s = "anagram"
    t = "nagaram"
    sol = Solution()
    result = sol.isAnagram(s, t)
    print (result)