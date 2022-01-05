"""
https://leetcode-cn.com/problems/find-first-palindromic-string-in-the-array/

给你一个字符串数组 words ，找出并返回数组中的 第一个回文字符串 。如果不存在满足要求的字符串，返回一个 空字符串 "" 。

回文字符串 的定义为：如果一个字符串正着读和反着读一样，那么该字符串就是一个 回文字符串 。

示例 1：
    输入：words = ["abc","car","ada","racecar","cool"]
    输出："ada"
    解释：第一个回文字符串是 "ada" 。
    注意，"racecar" 也是回文字符串，但它不是第一个。

示例 2：
    输入：words = ["notapalindrome","racecar"]
    输出："racecar"
    解释：第一个也是唯一一个回文字符串是 "racecar" 。

示例 3：
    输入：words = ["def","ghi"]
    输出：""
    解释：不存在回文字符串，所以返回一个空字符串。

提示：
    1 <= words.length <= 100
    1 <= words[i].length <= 100
    words[i] 仅由小写英文字母组成

"""
from typing import List

class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        def isPalindrome(word: str) -> bool:    # 判断字符串是否回文
            n = len(word)
            l = 0
            r = n - 1
            while l < r:
                if word[l] != word[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        for word in words:          # 顺序遍历字符串数组
            if isPalindrome(word):  # 如果遇到回文字符串
                return word         # 则返回字符串
        return ""                   # 未遇到则返回空字符串

if __name__ == "__main__":
    sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
    sol = Solution()
    result = sol.mostWordsFound(sentences)
    print (result)  