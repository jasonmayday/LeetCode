"""
https://leetcode-cn.com/problems/detect-capital/

我们定义，在以下情况时，单词的大写用法是正确的：
    全部字母都是大写，比如 "USA" 。
    单词中所有字母都不是大写，比如 "leetcode" 。
    如果单词不只含有一个字母，只有首字母大写， 比如 "Google" 。

给你一个字符串 word 。如果大写用法正确，返回 true ；否则，返回 false 。

示例 1：
    输入：word = "USA"
    输出：true

示例 2：
    输入：word = "FlaG"
    输出：false
 
提示：
    1 <= word.length <= 100
    word 由小写和大写英文字母组成

"""
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if str.islower(word[0]):
            return str.islower(word)        # 若首字母小写，整个单词字母必须也小写
        if len(word) <= 2:
            return True                     # 若只有一个字母，直接返回True
        if str.islower(word[1]):
            return str.islower(word[2:])    # 若第二个字母小写，剩下字母也必须小写
        return str.isupper(word)

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return word.islower() or word.isupper() or (word[0].isupper() and word[1:].islower())

if __name__ == "__main__":
    word = "FlaG"
    sol = Solution()
    result = sol.detectCapitalUse(word)
    print(result)