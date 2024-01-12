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
        one_word = len(words[0])    # 每个单词的长度
        word_num = len(words)       # 单词数量
        n = len(s)
        
        if not s or not words:  # 字符串 s 或者 单词 为空
            return []           # 返回空数组
        
        if n < one_word:        # 单个单词长度 大于 字符串长度
            return []           # 返回空数组
        
        words = Counter(words)  # {'bar': 1, 'foo': 1, 'the': 1}
        res = []
        
        for i in range(0, one_word):    # 只讨论从0，1，...， one_word-1 开始的子串情况，
            cur_cnt = 0                 # 每次进行匹配的窗口大小为 one_word，每次后移一个单词长度，由左右窗口维持当前窗口位置
            left = i
            right = i                   # 左右窗口
            cur_Counter = Counter()     # 统计每个符合要求的 word
            while right + one_word <= n:        # 右窗口不能超出主串长度
                w = s[right: right + one_word]  # 得到一个单词
                right += one_word               # 右窗口右移
                if w not in words:      # words[] 中没有这个单词，
                    left = right        # 那么当前窗口肯定匹配失败，直接右移到这个单词后面
                    cur_Counter.clear() # 窗口内单词统计map清空，重新统计
                    cur_cnt = 0         # 符合要求的单词数清 0
                else:
                    cur_Counter[w] += 1 # 统计当前子串中这个单词出现的次数
                    cur_cnt += 1        # 如果这个单词出现的次数大于words[]中它对应的次数，又由于每次匹配和words长度相等的子串
                                        # 如 ["foo","bar","foo","the"]  "| foobarfoobar| foothe"
                                        # 第二个 bar 虽然是 words[] 中的单词，但是次数抄了，那么右移一个单词长度后 "|barfoobarfoo|the"
                                        # bar 还是不符合，所以直接从这个不符合的bar之后开始匹配，也就是将这个不符合的bar和它之前的单词(串)全移出去
                    while cur_Counter[w] > words[w]:
                        left_w = s[left:left + one_word]    # 从当前窗口字符统计map中删除从左窗口开始到数量超限的所有单词(次数减一)
                        left += one_word                    # 左窗口位置右移
                        cur_Counter[left_w] -= 1            # 符合的单词数减一
                        cur_cnt -= 1
                    if cur_cnt == word_num :    # 当前窗口字符串满足要求
                        res.append(left)
        return res

if __name__ == "__main__":
    s = "barfoofoobarthefoobarman"
    words = ["bar","foo","the"]
    sol = Solution()
    result = sol.findSubstring(s, words)
    print(result)