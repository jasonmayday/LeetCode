"""
https://leetcode-cn.com/problems/find-closest-lcci/

有个内含单词的超大文本文件，给定任意两个不同的单词，找出在这个文件中这两个单词的最短距离(相隔单词数)。如果寻找过程在这个文件中会重复多次，而每次寻找的单词不同，你能对此优化吗?

示例：
    输入：words = ["I","am","a","student","from","a","university","in","a","city"], word1 = "a", word2 = "student"
    输出：1

提示：
    words.length <= 100000

"""
from typing import List

"""方法一：一次遍历"""
class Solution:
    def findClosest(self, words: List[str], word1: str, word2: str) -> int:
        ans = len(words)
        index1, index2 = -1, -1
        for i, word in enumerate(words):
            if word == word1:
                index1 = i
            elif word == word2:
                index2 = i
            if index1 >= 0 and index2 >= 0:
                ans = min(ans, abs(index1 - index2))
        return ans

if __name__ == "__main__":
    words = ["I","am","a","student","from","a","university","in","a","city"]
    word1 = "a"
    word2 = "student"
    sol = Solution()
    result = sol.findClosest(words, word1, word2)
    print(result)