"""
https://leetcode-cn.com/problems/longest-word-in-dictionary/

给出一个字符串数组words组成的一本英语词典。从中找出最长的一个单词，该单词是由words词典中其他单词逐步添加一个字母组成。若其中有多个可行的答案，则返回答案中字典序最小的单词。

若无答案，则返回空字符串。

示例 1：
    输入：
    words = ["w","wo","wor","worl", "world"]
    输出："world"
    解释： 单词"world"可由"w", "wo", "wor", 和 "worl"添加一个字母组成。

示例 2：
    输入：
    words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
    输出："apple"
    解释："apply"和"apple"都能由词典中的单词组成。但是"apple"的字典序小于"apply"。

提示：
    所有输入的字符串都只包含小写字母。
    words数组长度范围为[1,1000]。
    words[i]的长度范围为[1,30]。

"""
from typing import List

class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort()    # ['a', 'ap', 'app', 'appl', 'apple', 'apply', 'banana']
        maxword = ""
        wordset = set()
        for word in words:
            if len(word) == 1 or word[:-1] in wordset:
                wordset.add(word)
                if len(word) > len(maxword):    # 大于maxword才更新，保证若有多个长度相同的答案，返回答案中字典序最小的单词
                    maxword = word
        return maxword

class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort(key=lambda x: (-len(x), x), reverse=True)    # 首先按照单词的长度升序排序，如果单词的长度相同则按照字典序降序排序
        print('words: ', words)                                 # ['a', 'ap', 'app', 'appl', 'apply', 'apple', 'banana']
        maxword = ""
        wordset = {""}
        for word in words:
            if word[:-1] in wordset:    # 不断加入集合
                maxword = word          # 因为长度相同则按照字典序降序排序，所以最后出现的就是答案
                wordset.add(word)
        return maxword

if __name__ == "__main__":
    words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
    sol = Solution()
    result = sol.longestWord(words)
    print(result)