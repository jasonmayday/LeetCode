"""
https://leetcode-cn.com/problems/number-of-valid-words-in-a-sentence/

句子仅由小写字母（'a' 到 'z'）、数字（'0' 到 '9'）、连字符（'-'）、标点符号（'!'、'.' 和 ','）以及空格（' '）组成。
每个句子可以根据空格分解成 一个或者多个 token ，这些 token 之间由一个或者多个空格 ' ' 分隔。

如果一个 token 同时满足下述条件，则认为这个 token 是一个有效单词：
    仅由小写字母、连字符和/或标点（不含数字）。
    至多一个 连字符 '-' 。如果存在，连字符两侧应当都存在小写字母（"a-b" 是一个有效单词，但 "-ab" 和 "ab-" 不是有效单词）。
    至多一个 标点符号。如果存在，标点符号应当位于 token 的 末尾 。

这里给出几个有效单词的例子："a-b."、"afad"、"ba-c"、"a!" 和 "!" 。

给你一个字符串 sentence ，请你找出并返回 sentence 中 有效单词的数目 。

示例 1：
    输入：sentence = "cat and  dog"
    输出：3
    解释：句子中的有效单词是 "cat"、"and" 和 "dog"

示例 2：
    输入：sentence = "!this  1-s b8d!"
    输出：0
    解释：句子中没有有效单词
    "!this" 不是有效单词，因为它以一个标点开头
    "1-s" 和 "b8d" 也不是有效单词，因为它们都包含数字

示例 3：
    输入：sentence = "alice and  bob are playing stone-game10"
    输出：5
    解释：句子中的有效单词是 "alice"、"and"、"bob"、"are" 和 "playing"
    "stone-game10" 不是有效单词，因为它含有数字

示例 4：
    输入：sentence = "he bought 2 pencils, 3 erasers, and 1  pencil-sharpener."
    输出：6
    解释：句子中的有效单词是 "he"、"bought"、"pencils,"、"erasers,"、"and" 和 "pencil-sharpener."

提示：
    1 <= sentence.length <= 1000
    sentence 由小写英文字母、数字（0-9）、以及字符（' '、'-'、'!'、'.' 和 ','）组成
    句子中至少有 1 个 token

"""

import re

"""解法1：正则表达式"""
class Solution:
    def countValidWords(self, sentence: str) -> int:
        return len(list(filter(lambda x: re.match('^[a-z]*([a-z]-[a-z]+)?[!\.,]?$', x), sentence.split())))

"""解法2：模拟"""
class Solution:
    def countValidWords(self, sentence: str) -> int:
        words = sentence.split()
        res = 0
        signs = ['!', '.', ',']     # 标点符号
        
        for num in words:
            ok = True

            # 不能有数字
            for x in num:
                if x.isdigit():
                    ok = False
                    break

            # 至多一个标点符号
            sign_cnt = 0
            for x in num:
                if x in signs:
                    sign_cnt += 1
                    if sign_cnt > 1:
                        ok = False
                        break
                    
            # 如果存在标点符号，应该在末尾
            if sign_cnt == 1:
                if num[-1] not in signs:
                    ok = False
            
            # 至多一个连字符 '-'
            a = 0
            for x in num:
                if x == '-':
                    a += 1
                    if a > 1:
                        ok = False
                        break
                    
            # 两字符两侧都是小写字母
            if a == 1:
                for i in range(len(num)):
                    if num[i] == '-':
                        if not(0 <= i - 1 and num[i - 1].isalpha() and i + 1 < len(num) and num[i + 1].isalpha()):
                            ok = False
            
            if ok == True:
                res += 1
        return res

if __name__ == "__main__":
    sentence = "alice and  bob are playing stone-game10"
    sol = Solution()
    result = sol.countValidWords(sentence)
    print(result)