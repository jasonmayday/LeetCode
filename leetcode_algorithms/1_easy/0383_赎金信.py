"""
https://leetcode-cn.com/problems/ransom-note/

为了不在赎金信中暴露字迹，从杂志上搜索各个需要的字母，组成单词来表达意思。

给你一个赎金信 (ransomNote) 字符串和一个杂志(magazine)字符串，判断 ransomNote 能不能由 magazines 里面的字符构成。

如果可以构成，返回 true ；否则返回 false 。

magazine 中的每个字符只能在 ransomNote 中使用一次。

示例 1：
    输入：ransomNote = "a", magazine = "b"
    输出：false

示例 2：
    输入：ransomNote = "aa", magazine = "ab"
    输出：false

示例 3：
    输入：ransomNote = "aa", magazine = "aab"
    输出：true
 
提示：
    1 <= ransomNote.length, magazine.length <= 10^5
    ransomNote 和 magazine 由小写英文字母组成

"""
from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        a = Counter(ransomNote)     # # 使用Counter类的交集操作，获得交集
        b = Counter(magazine)
        x = a - b
        # x 只保留值大于 0 的符号，当 a 里面的符号个数小于 b 时，不会被保留
        # 所以 x 只保留下了 magazine 不能表达的
        if (len(x) == 0):
            return True
        else:
            return False

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        hashmap = dict()        # use a dict to store the number of letter occurance in ransomNote
        for s in ransomNote:
            if s in hashmap:
                hashmap[s] += 1
            else:
                hashmap[s] = 1
        
        for l in magazine:      # check if the letter we need can be found in magazine
            if l in hashmap:
                hashmap[l] -= 1
        
        for key in hashmap:
            if hashmap[key] > 0:
                return False
        
        return True

if __name__ == "__main__":
    ransomNote = "aa"
    magazine = "aab"
    sol = Solution()
    result = sol.canConstruct(ransomNote, magazine)
    print (result) 