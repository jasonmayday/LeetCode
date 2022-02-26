"""
https://leetcode-cn.com/problems/index-pairs-of-a-string/

给出 字符串 text 和 字符串列表 words, 返回所有的索引对 [i, j] 使得在索引对范围内的子字符串 text[i]...text[j]（包括 i 和 j）属于字符串列表 words。

示例 1:
    输入: text = "thestoryofleetcodeandme", words = ["story","fleet","leetcode"]
    输出: [[3,7],[9,13],[10,17]]

示例 2:
    输入: text = "ababa", words = ["aba","ab"]
    输出: [[0,1],[0,2],[2,3],[2,4]]
    解释: 注意，返回的配对可以有交叉，比如，"aba" 既在 [0,2] 中也在 [2,4] 中

提示:
    所有字符串都只包含小写字母。
    保证 words 中的字符串无重复。
    1 <= text.length <= 100
    1 <= words.length <= 20
    1 <= words[i].length <= 50
    按序返回索引对 [i,j]（即，按照索引对的第一个索引进行排序，当第一个索引对相同时按照第二个索引对排序）。

"""
from typing import List

""" 暴力 """
class Solution:
    def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:
        res = []
        for i in range(len(text)):
            for j in range(i, len(text)):
                if text[i:j + 1] in words:
                    res.append([i, j])
        return res

""" 前缀树 / 字典树 / Trie树 """
class Trie:
    def __init__(self):
        self.child = dict()
        self.isWord = False

    def insert(self, word: str):
        root = self
        for c in word:
            if c not in root.child:
                root.child[c] = Trie()
            root = root.child[c]
        root.isWord = True

class Solution:
    def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:
        n = len(text)
        T = Trie()
        for word in words:
            T.insert(word)
        res = []
        for i, c in enumerate(text):
            root = T
            if c not in root.child:
                continue
            j = i
            while j < n and text[j] in root.child:
                root = root.child[text[j]]
                if root.isWord == True:
                    res.append([i, j])
                j += 1
        return res

if __name__ == "__main__":
    text = "thestoryofleetcodeandme"
    words = ["story","fleet","leetcode"]
    sol = Solution()
    result = sol.indexPairs(text, words)
    print(result)