"""
https://leetcode-cn.com/problems/counting-words-with-a-given-prefix/

给你一个字符串数组 words 和一个字符串 pref 。

返回 words 中以 pref 作为 前缀 的字符串的数目。

字符串 s 的 前缀 就是  s 的任一前导连续字符串。

示例 1：
    输入：words = ["pay","attention","practice","attend"], pref = "at"
    输出：2
    解释：以 "at" 作为前缀的字符串有两个，分别是："attention" 和 "attend" 。

示例 2：
    输入：words = ["leetcode","win","loops","success"], pref = "code"
    输出：0
    解释：不存在以 "code" 作为前缀的字符串。

提示：
    1 <= words.length <= 100
    1 <= words[i].length, pref.length <= 100
    words[i] 和 pref 由小写英文字母组成

"""
from typing import List

""" startswith 函数 """
class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        cnt = 0
        for i in range(len(words)):
            if (words[i].startswith(pref)) == True:
                cnt += 1
        return cnt

""" startswith 函数 """
class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        return len([word for word in words if word.startswith(pref)])

""" 遍历前缀 """
class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        cnt = 0
        for word in words:                  # 遍历words中每个单词
            for i in range(0, len(word)+1): # 每个单词中下标0到i
                # print(word[0:i])
                if word[0:i] == pref:       # 只要搜索到前缀与pref相同，就可以加一，并返回搜索下个单词。
                    cnt += 1
        return cnt

if __name__ == "__main__":
    words = ["pay","attention","practice","attend"]
    pref = "at"
    sol = Solution()
    result = sol.prefixCount(words, pref)
    print (result)
