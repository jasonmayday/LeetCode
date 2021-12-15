"""
https://leetcode-cn.com/problems/check-if-the-sentence-is-pangram/

全字母句 指包含英语字母表中每个字母至少一次的句子。

给你一个仅由小写英文字母组成的字符串 sentence ，请你判断 sentence 是否为 全字母句 。

如果是，返回 true ；否则，返回 false 。

示例 1：
    输入：sentence = "thequickbrownfoxjumpsoverthelazydog"
    输出：true
    解释：sentence 包含英语字母表中每个字母至少一次。

示例 2：
    输入：sentence = "leetcode"
    输出：false

提示：
    1 <= sentence.length <= 1000
    sentence 由小写英语字母组成

"""

"""解法1：创建HASH表遍历数组"""
class Solution:
    def checkIfPangram(self, sentence):
        dict = set()
        for i in sentence:
            dict.add(i)
        return len(dict) == 26

"""解法2：使用内置函数"""
class Solution:
    def checkIfPangram(self, sentence):
        from collections import Counter
        return len(Counter(sentence)) == 26
    
"""解法3：set集合快速解题"""
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        return len(list(set(sentence))) == 26

if __name__ == "__main__":
    sentence = "thequickbrownfoxjumpsoverthelazydog"
    sol = Solution()
    result = sol.checkIfPangram(sentence)
    print(result)