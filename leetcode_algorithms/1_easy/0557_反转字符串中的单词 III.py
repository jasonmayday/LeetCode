"""
https://leetcode-cn.com/problems/reverse-words-in-a-string-iii/

给定一个字符串，你需要反转字符串中每个单词的字符顺序，同时仍保留空格和单词的初始顺序。

示例：
    输入："Let's take LeetCode contest"
    输出："s'teL ekat edoCteeL tsetnoc"

提示：
    在字符串中，每个单词由单个空格分隔，并且字符串中不会有任何额外的空格。

"""

""" 解法1"""
class Solution(object):
    def reverseWords(self, s):
        return " ".join(word[::-1] for word in s.split(" "))    # [::-1] 顺序相反操作

""" 解法2
    先反转单词列表 再反转字符串
    以字符串 “I love drag queen” 为例：

    s.split(" ") 将字符串分割成单词列表:
    ['I', 'love', 'drag', 'queen']

    s.split(" ")[::-1] 将单词列表反转:
    ['queen', 'drag', 'love', 'I']

    " ".join(s.split(" ")[::-1]) 将单词列表转换为字符串，以空格分隔:
    "queen drag love I"

    " ".join(s.split(" ")[::-1])[::-1] 将字符串反转：
    "I evol gard neeuq"

"""
class Solution(object):
    def reverseWords(self, s):
        return " ".join(s.split(" ")[::-1])[::-1]

if __name__ == "__main__":
    s = "Let's take LeetCode contest"
    sol = Solution()
    result = sol.reverseWords(s)
    print(result)