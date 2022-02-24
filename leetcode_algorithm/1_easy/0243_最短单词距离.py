"""
https://leetcode-cn.com/problems/shortest-word-distance/

给定一个字符串数组 wordDict 和两个已经存在于该数组中的不同的字符串 word1 和 word2 。返回列表中这两个单词之间的最短距离。

示例 1:
    输入: wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "coding", word2 = "practice"
    输出: 3

示例 2:
    输入: wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "makes", word2 = "coding"
    输出: 1

提示:
    1 <= wordsDict.length <= 3 * 10^4
    1 <= wordsDict[i].length <= 10
    wordsDict[i] 由小写英文字母组成
    word1 和 word2 在 wordsDict 中
    word1 != word2

"""

from typing import List

class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        p1 = -1
        p2 = -1
        res = float("inf")
        for idx, word in enumerate(words):
            if word == word1 : p1 = idx
            if word == word2 : p2 = idx
            if (p1 != -1 and p2 != -1):
                res = min(res, abs(p1 - p2))
        return res

if __name__ == "__main__":
    wordsDict = ["practice", "makes", "perfect", "coding", "makes"]
    word1 = "coding"
    word2 = "practice"
    sol = Solution()
    result = sol.shortestDistance(wordsDict, word1, word2)
    print(result)

