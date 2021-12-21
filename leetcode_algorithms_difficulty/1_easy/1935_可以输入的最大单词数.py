"""
https://leetcode-cn.com/problems/maximum-number-of-words-you-can-type/

键盘出现了一些故障，有些字母键无法正常工作。而键盘上所有其他键都能够正常工作。

给你一个由若干单词组成的字符串 text ，单词间由单个空格组成（不含前导和尾随空格）；另有一个字符串 brokenLetters ，由所有已损坏的不同字母键组成，返回你可以使用此键盘完全输入的 text 中单词的数目。

示例 1：
    输入：text = "hello world", brokenLetters = "ad"
    输出：1
    解释：无法输入 "world" ，因为字母键 'd' 已损坏。

示例 2：
    输入：text = "leet code", brokenLetters = "lt"
    输出：1
    解释：无法输入 "leet" ，因为字母键 'l' 和 't' 已损坏。

示例 3：
    输入：text = "leet code", brokenLetters = "e"
    输出：0
    解释：无法输入任何单词，因为字母键 'e' 已损坏。

提示：
    1 <= text.length <= 10^4
    0 <= brokenLetters.length <= 26
    text 由若干用单个空格分隔的单词组成，且不含任何前导和尾随空格
    每个单词仅由小写英文字母组成
    brokenLetters 由 互不相同 的小写英文字母组成

"""

class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        broken = set(brokenLetters)     # 无法输入的字符集合
        res = 0                         # 初始化 可以完全输入的单词数目
        canType = True              # 当前字符所在单词是否可被完全输入
        for ch in text:
            if ch == ' ':           # 若当前字符为空格：
                if canType:         # 检查上一个单词状态，更新 canType 数目
                    res += 1        # 每次遇到空格才检查 canType 状态
                canType = True      # 初始化 canType
            elif ch in broken:      # 当前字符不可被输入，所在单词无法被输入
                canType = False     # canType 为 False
        if canType:                 # 判断最后一个单词状态并更新数目
            res += 1
        return res

class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        broken = set(brokenLetters)
        return sum(all(ch not in broken for ch in s) for s in text.split(' '))


if __name__ == "__main__":
    text = "hello world"
    brokenLetters = "ad"
    sol = Solution()
    result = sol.canBeTypedWords(s)
    print(result)