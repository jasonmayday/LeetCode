"""
https://leetcode-cn.com/problems/is-unique-lcci/comments/

实现一个算法，确定一个字符串 s 的所有字符是否全都不同。

示例 1：
    输入: s = "leetcode"
    输出: false

示例 2：
    输入: s = "abc"
    输出: true

限制：
    0 <= len(s) <= 100
    如果你不使用额外的数据结构，会很加分。

"""

import collections

""" 哈希集合"""
class Solution:
    def isUnique(self, s: str) -> bool:
        dic = collections.defaultdict(int)
        for i in s:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        for j in dic.values():
            if j != 1:
                return False
        return True

""" 使用内置函数，Counter()"""
class Solution:
    def isUnique(self, s: str) -> bool:
        dic = collections.Counter(s)
        for i in dic.values():
            if i != 1:
                return False
        return True

""" 排序后，进行比较"""
class Solution:
    def isUnique(self, s: str) -> bool:
        n = len(s)
        if n < 2:
            return True
        s = sorted(s)
        for i in range(1, n):
            if s[i] == s[i - 1]:
                return False
        return True

""" 集合去重，比较长度"""
class Solution:
    def isUnique(self, s: str) -> bool:
        return len(set(s)) == len(s)

""" 位运算 """
class Solution:
    def isUnique(self, s: str) -> bool:
        mark = 0
        for char in s:
            move_bit = ord(char) - ord('a')
            if (mark & (1 << move_bit)) != 0:
                return False
            else:
                mark |= (1 << move_bit)
        return True

class Solution:
    def isUnique(self, s: str) -> bool:
        mask = 0
        for ch in s:
            move = ord(ch) - ord('a')
            #   判断是否出现过多次
            #   得到当前 move 位是否为 1
            if mask & (1 << move) != 0:
                return False
            else:
                #   将 mask 第 move 位改为 1
                mask |= (1 << move)
        return True

if __name__ == "__main__":
    s = "leetcode"
    sol = Solution()
    result = sol.isUnique(s)
    print(result)