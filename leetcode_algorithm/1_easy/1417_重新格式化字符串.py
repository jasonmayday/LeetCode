"""
https://leetcode-cn.com/problems/reformat-the-string/

给你一个混合了数字和字母的字符串 s，其中的字母均为小写英文字母。

请你将该字符串重新格式化，使得任意两个相邻字符的类型都不同。也就是说，字母后面应该跟着数字，而数字后面应该跟着字母。

请你返回 重新格式化后 的字符串；如果无法按要求重新格式化，则返回一个 空字符串 。

示例 1：
    输入：s = "a0b1c2"
    输出："0a1b2c"
    解释："0a1b2c" 中任意两个相邻字符的类型都不同。 "a0b1c2", "0a1b2c", "0c2a1b" 也是满足题目要求的答案。

示例 2：
    输入：s = "leetcode"
    输出：""
    解释："leetcode" 中只有字母，所以无法满足重新格式化的条件。

示例 3：
    输入：s = "1229857369"
    输出：""
    解释："1229857369" 中只有数字，所以无法满足重新格式化的条件。

示例 4：
    输入：s = "covid2019"
    输出："c2o0v1i9d"

示例 5：
    输入：s = "ab123"
    输出："1a2b3"

提示：
    1 <= s.length <= 500
    s 仅由小写英文字母和/或数字组成。

"""

""" 方法一：双指针 """
class Solution:
    def reformat(self, s: str) -> str:
        digit = [c for c in s if c.isdigit()]   # 分别找到数字和字母    ['2', '0', '1', '9']
        alpha = [c for c in s if c.isalpha()]   # ['c', 'o', 'v', 'i', 'd']
        if abs(len(digit) - len(alpha)) > 1:    # 如果字母和数字数量差大于1，无法满足重新格式化的条件。
            return ''
        ans = ['' for _ in range(len(digit) + len(alpha))]  # 初始化答案ans:  ['', '', '', '', '', '', '', '', '']
        if len(digit) > len(alpha):         # 因为后面想构建的字母第一个字符为字母，所以假如数字更多，交换
            digit, alpha = alpha, digit     # 所以保持digit的长度不大于alpha，以便在总长度为奇数时能够间隔插入
        # 分别在奇数位和偶数位, 插入不同类型的字符
        ans[::2], ans[1::2] = alpha, digit  # 第一个字符为字母，隔一个字符插入不同性质的。
        return ''.join(ans)

class Solution:
    def reformat(self, s: str) -> str:
        sumDigit = sum(c.isdigit() for c in s)
        sumAlpha = len(s) - sumDigit
        if abs(sumDigit - sumAlpha) > 1:        # 如果字母和数字数量差大于1，无法满足重新格式化的条件。
            return ""
        moreDigit = sumDigit > sumAlpha  # 数字更多，moreDigit 为True
        ans = list(s)         # ['c', 'o', 'v', 'i', 'd', '2', '0', '1', '9']
        j = 1
        for i in range(0, len(ans), 2):
            if ans[i].isdigit() != moreDigit:
                while ans[j].isdigit() != moreDigit:
                    j += 2
                ans[i], ans[j] = ans[j], ans[i]
        return ''.join(ans)


if __name__ == "__main__":
    s = "covid2019"
    sol = Solution()
    result = sol.reformat(s)
    print(result)