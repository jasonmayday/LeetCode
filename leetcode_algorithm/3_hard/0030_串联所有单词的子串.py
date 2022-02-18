"""
https://leetcode-cn.com/problems/substring-with-concatenation-of-all-words/

给定一个字符串 s 和一些 长度相同 的单词 words 。找出 s 中恰好可以由 words 中所有单词串联形成的子串的起始位置。

注意子串要与 words 中的单词完全匹配，中间不能有其他字符 ，但不需要考虑 words 中单词串联的顺序。

示例 1：
    输入：s = "barfoothefoobarman", words = ["foo","bar"]
    输出：[0,9]
    解释：
        从索引 0 和 9 开始的子串分别是 "barfoo" 和 "foobar" 。
        输出的顺序不重要, [9,0] 也是有效答案。

示例 2：
    输入：s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]
    输出：[]

示例 3：
    输入：s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]
    输出：[6,9,12]

提示：
    1 <= s.length <= 10^4
    s 由小写英文字母组成
    1 <= words.length <= 5000
    1 <= words[i].length <= 30
    words[i] 由小写英文字母组成

"""
from typing import List
from collections import Counter

""" 滑动窗口 """
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:return []
        one_word = len(words[0])
        word_num = len(words)
        n = len(s)
        if n < one_word:return []
        words = Counter(words)
        res = []
        for i in range(0, one_word):
            cur_cnt = 0
            left = i
            right = i
            cur_Counter = Counter()
            while right + one_word <= n:
                w = s[right:right + one_word]
                right += one_word
                if w not in words:
                    left = right
                    cur_Counter.clear()
                    cur_cnt = 0
                else:
                    cur_Counter[w] += 1
                    cur_cnt += 1
                    while cur_Counter[w] > words[w]:
                        left_w = s[left:left+one_word]
                        left += one_word
                        cur_Counter[left_w] -= 1
                        cur_cnt -= 1
                    if cur_cnt == word_num :
                        res.append(left)
        return res

if __name__ == "__main__":
    s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]
    sol = Solution()
    result = sol.findSubstring(nums1, nums2)
    print(result)