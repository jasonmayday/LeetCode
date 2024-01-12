"""
https://leetcode-cn.com/problems/occurrences-after-bigram/

给出第一个词 first 和第二个词 second，考虑在某些文本 text 中可能以 "first second third" 形式出现的情况，其中 second 紧随 first 出现，third 紧随 second 出现。

对于每种这样的情况，将第三个词 "third" 添加到答案中，并返回答案。

示例 1：
    输入：text = "alice is a good girl she is a good student", first = "a", second = "good"
    输出：["girl","student"]

示例 2：
    输入：text = "we will we will rock you", first = "we", second = "will"
    输出：["we","rock"]

提示：
    1 <= text.length <= 1000
    text 由一些用空格分隔的单词组成，每个单词都由小写英文字母组成
    1 <= first.length, second.length <= 10
    first 和 second 由小写英文字母组成

"""
from typing import List

class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        word_list = text.split()
        res = []
        for i in range(1, len(word_list)):
            if word_list[i-1] == first and word_list[i] == second and i+1 < len(word_list):
                res.append(word_list[i+1])
        return res

if __name__ == "__main__":
    text = "alice is a good girl she is a good student"
    first = "a"
    second = "good"
    sol = Solution()
    result = sol.findOcurrences(text,first,second)
    print(result)