"""
https://leetcode-cn.com/problems/reverse-words-in-a-string/

给你一个字符串 s ，逐个翻转字符串中的所有 单词 。

单词 是由非空格字符组成的字符串。s 中使用至少一个空格将字符串中的 单词 分隔开。

请你返回一个翻转 s 中单词顺序并用单个空格相连的字符串。

说明：
    输入字符串 s 可以在前面、后面或者单词间包含多余的空格。
    翻转后单词间应当仅用一个空格分隔。
    翻转后的字符串中不应包含额外的空格。

示例 1：
    输入：s = "the sky is blue"
    输出："blue is sky the"

示例 2：
    输入：s = "  hello world  "
    输出："world hello"
    解释：输入字符串可以在前面或者后面包含多余的空格，但是翻转后的字符不能包括。

示例 3：
    输入：s = "a good   example"
    输出："example good a"
    解释：如果两个单词间有多余的空格，将翻转后单词间的空格减少到只含一个。

示例 4：
    输入：s = "  Bob    Loves  Alice   "
    输出："Alice Loves Bob"

示例 5：
    输入：s = "Alice does not even like bob"
    输出："bob like even not does Alice"

提示：
    1 <= s.length <= 104
    s 包含英文大小写字母、数字和空格 ' '
    s 中 至少存在一个 单词

进阶：
    请尝试使用 O(1) 额外空间复杂度的原地解法。

"""
from collections import deque

""" Python内置函数 """
class Solution:
    def reverseWords(self, s: str) -> str:
        # split  将字符串按空格分割成字符串数组；同时去除前后多余空格
        # [::-1] 将字符串数组进行反转；
        # join   将字符串数组拼成一个字符串。
        # return " ".join(reversed(s.split()))
        return " ".join(s.split()[::-1])
        
""" 自行编写对应的函数 """
class Solution:
    
    """ 函数1：去除多余空格 """
    def trim_spaces(self, s: str) -> list:
        left, right = 0, len(s) - 1
        
        while left <= right and s[left] == ' ':     # 去掉字符串开头的空格
            left += 1
        
        while left <= right and s[right] == ' ':    # 去掉字符串末尾的空格
            right -= 1
        
        output = []                     # 将字符串间多余的空白字符去除
        while left <= right:            # 从左到右寻找
            if s[left] != ' ':          # 碰到不是空格的字符
                output.append(s[left])  # 把字符逐个添加到output
            elif output[-1] != ' ':
                output.append(s[left])  # 两个单词间最多一个空格
            left += 1
        return output
    
    """ 函数2：反转整个字符串（双指针） """
    def reverse(self, l: list, left: int, right: int) -> None:
        while left < right:
            l[left], l[right] = l[right], l[left]
            left, right = left + 1, right - 1
    
    """ 函数3：反转每个单词（双指针） """
    def reverse_each_word(self, l: list) -> None:
        n = len(l)
        start = end = 0
        while start < n:
            while end < n and l[end] != ' ':    # 循环至单词的末尾
                end += 1
            self.reverse(l, start, end - 1)     # 翻转单词
            start = end + 1                     # 更新start，去找下一个单词
            end += 1
                
    def reverseWords(self, s: str) -> str:
        l = self.trim_spaces(s)         # 去除多余空格
        self.reverse(l, 0, len(l) - 1)  # 翻转整个字符串
        self.reverse_each_word(l)       # 翻转每个单词
        return ''.join(l)

""" 双端队列 """
class Solution:
    def reverseWords(self, s: str) -> str:
        left, right = 0, len(s) - 1
        # 去掉字符串开头的空白字符
        while left <= right and s[left] == ' ':
            left += 1
        
        # 去掉字符串末尾的空白字符
        while left <= right and s[right] == ' ':
            right -= 1
            
        d = deque() 
        word = []
        # 将单词 push 到队列的头部
        while left <= right:
            if s[left] == ' ' and word:       # 如果字符串最左边为空格，说明到了两个单词之间
                d.appendleft(''.join(word))   # 然后将单词压入队列的头部
                word = []
            elif s[left] != ' ':        # 如果字符串最左边不为空，说明有字母
                word.append(s[left])    # 把字母加入到word中
            left += 1
        d.appendleft(''.join(word))     # 再将队列转成字符串即可。
        return ' '.join(d)


if __name__ == "__main__":
    s = "  hello world  "
    sol = Solution()
    result = sol.reverseWords(s)
    print(result)