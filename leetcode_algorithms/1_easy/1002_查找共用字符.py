"""
https://leetcode-cn.com/problems/find-common-characters/

给你一个字符串数组 words ，请你找出所有在 words 的每个字符串中都出现的共用字符（ 包括重复字符），
并以数组形式返回。你可以按 任意顺序 返回答案。

示例 1：
    输入：words = ["bella","label","roller"]
    输出：["e","l","l"]

示例 2：
    输入：words = ["cool","lock","cook"]
    输出：["c","o"]

提示：
    1 <= words.length <= 100
    1 <= words[i].length <= 100
    words[i] 由小写英文字母组成

"""
from typing import List
from collections import Counter

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        if not words: return []
        res = []
        hash = [0] * 26                     # 用来统计所有字符串里字符出现的最小频率
        for i, c in enumerate(words[0]):    # 用第一个字符串给hash初始化
            hash[ord(c) - ord('a')] += 1
            
        for i in range(1, len(words)):      # 统计除第一个字符串外字符的出现频率
            hashOtherStr = [0] * 26
            
            for j in range(len(words[i])):
                hashOtherStr[ord(words[i][j]) - ord('a')] += 1
            
            for k in range(26):
                hash[k] = min(hash[k], hashOtherStr[k])     # 更新hash，保证hash里统计26个字符在所有字符串里出现的最小次数
        
        for i in range(26):                         # 将hash统计的字符次数，转成输出形式
            while hash[i] != 0:                     # 注意这里是while，多个重复的字符
                res.extend(chr(i + ord('a')))
                hash[i] -= 1
        
        return res
    
class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        ans = Counter(A[0])
        for i in A[1:]:
            ans &= Counter(i)
        return list(ans.elements())

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        tmp = Counter(words[0])             # 统计第一个单词中每个字母出现的次数
        res = []
        for i in range(1, len(words)):      # 统计除第一个字符串外字符的出现频率
            tmp = tmp & Counter(words[i])   # 使用 & 取交集
        for j in tmp:           # 剩下的就是每个单词都出现的字符（键），个数（值）
            v = tmp[j]
            while(v):
                res.append(j)
                v -= 1
        return res

if __name__ == "__main__":
    words = ["bella","label","roller"]
    sol = Solution()
    result = sol.commonChars(words)
    print(result)