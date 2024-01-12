"""
https://leetcode-cn.com/problems/palindrome-permutation-lcci/

给定一个字符串，编写一个函数判定其是否为某个回文串的排列之一。

回文串是指正反两个方向都一样的单词或短语。排列是指字母的重新排列。

回文串不一定是字典当中的单词。

示例1：
    输入："tactcoa"
    输出：true（排列有"tacocat"、"atcocta"，等等）

"""
from collections import defaultdict

""" 根据字符串长度，「回文串」可分为两种情况：
    「回文串」长度为偶数：所有不同字符的出现次数都为「偶数」；
    「回文串」长度为奇数：位于中点的字符出现「奇数」次，其余字符出现「偶数」次；
因此，某字符串是回文串排列之一的「充要条件」为：此字符串中，最多只有一种字符的出现次数为「奇数」，其余所有字符的出现次数都为「偶数」。
"""
class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        dic = defaultdict(int)
        for c in s:
            dic[c] += 1
        odd = 0
        for val in dic.values():
            if val % 2 == 1:
                odd += 1
                if odd > 1:
                    return False
        return True

if __name__ == "__main__":
    s = "tactcoa"
    sol = Solution()
    result = sol.canPermutePalindrome(s)
    print(result)