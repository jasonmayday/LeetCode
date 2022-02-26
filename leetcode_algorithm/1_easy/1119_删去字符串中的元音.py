"""
https://leetcode-cn.com/problems/remove-vowels-from-a-string/

给你一个字符串 s ，请你删去其中的所有元音字母 'a'，'e'，'i'，'o'，'u'，并返回这个新字符串。

示例 1：
    输入：s = "leetcodeisacommunityforcoders"
    输出："ltcdscmmntyfrcdrs"

示例 2：
    输入：s = "aeiou"
    输出：""

提示：
    1 <= S.length <= 1000
    s 仅由小写英文字母组成

"""
class Solution:
    def removeVowels(self, s: str) -> str:
        return ''.join([i for i in s if i not in ['a', 'e', 'i', 'o', 'u']])

if __name__ == "__main__":
    s = "leetcodeisacommunityforcoders"
    sol = Solution()
    result = sol.removeVowels(s)
    print(result)