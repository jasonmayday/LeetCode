"""
给定一个字符串数组 words，找到 length(word[i]) * length(word[j]) 的最大值，并且这两个单词不含有公共字母。你可以认为每个单词只包含小写字母。如果不存在这样的两个单词，返回 0。

示例 1:
    输入: ["abcw","baz","foo","bar","xtfn","abcdef"]
    输出: 16 
    解释: 这两个单词为 "abcw", "xtfn"。

示例 2:
    输入: ["a","ab","abc","d","cd","bcd","abcd"]
    输出: 4 
    解释: 这两个单词为 "ab", "cd"。

示例 3:
    输入: ["a","aa","aaa","aaaa"]
    输出: 0 
    解释: 不存在这样的两个单词。

提示：
    2 <= words.length <= 1000
    1 <= words[i].length <= 1000
    words[i] 仅包含小写字母

"""
from typing import List
from collections import defaultdict

'''暴力法1'''
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        def pending_str(s1, s2):
            return len([x for x in s1 if x in s2]) == 0     # 判断两个字符串是否有相同字符
        
        max = 0
        for i in range(len(words) - 1):
            for j in range(i + 1, len(words)):
                if pending_str(words[i], words[j]):         # 如果没有相同字符
                    if max < len(words[i]) * len( words[j]):
                        max = len(words[i]) * len( words[j])
        return max

'''暴力法2'''
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        maxPro = 0
        for i in range(len(words) - 1):
            for j in range(i + 1 ,len(words)):
                s = words[i] + words[j]
                if len(set(words[i])) + len(set(words[j])) == len(set(s)):  # 如果集合相加的长度等于集合长度相加，说明没有相同字符
                    maxPro = max(len(words[i]) * len(words[j]), maxPro)
        return maxPro

if __name__ == "__main__":
    words = ["abcw","baz","foo","bar","xtfn","abcdef"]
    sol = Solution()
    result = sol.maxProduct(words)
    print (result)