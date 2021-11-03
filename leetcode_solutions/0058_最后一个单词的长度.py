'''
https://leetcode-cn.com/problems/length-of-last-word/

给你一个字符串 s，由若干单词组成，单词前后用一些空格字符隔开。返回字符串中最后一个单词的长度。

单词 是指仅由字母组成、不包含任何空格字符的最大子字符串。

示例 1：
    输入：s = "Hello World"
    输出：5

示例 2：
    输入：s = "   fly me   to   the moon  "
    输出：4

示例 3：
    输入：s = "luffy is still joyboy"
    输出：6

提示：
    1 <= s.length <= 10^4
    s 仅有英文字母和空格 ' ' 组成
    s 中至少存在一个单词

'''
s = "   fly me   to   the moon  "

# 解法1：字符串操作
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1])

# 解法2：指针遍历
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s) - 1                         # i为字符串最后一位的位置，因为计数从0开始所以减一
        while i >= 0 and s[i] == ' ': i -= 1
        j = i 
        while j >= 0 and s[j] != ' ': j -= 1
        return i-j

sol = Solution()
result = sol.lengthOfLastWord(s)
print (result) 