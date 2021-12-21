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

"""解法1：哈希表"""
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

"""解法2：使用集合"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        result = True
        set_tmp = set(s)    # 利用 Python 数据结构 set 去重去序
    # 先判断组成字符串的各个字符元素是否一致
        if set_tmp == set(t):
            for i in set_tmp:
            # 利用逻辑运算符判断各个字符元素的数量一致，均为 True 才输出 True
                result = result and (s.count(i) == t.count(i))
        else:
            result = False
        return (result)

"""解法3：使用Counter功能"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s)==Counter(t)


if __name__ == "__main__":
    s = "anagram"
    t = "nagaram"

    sol = Solution()
    result = sol.isAnagram(s, t)
    print(result)