'''
https://leetcode-cn.com/problems/valid-parentheses/

给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。

有效字符串需满足：
1. 左括号必须用相同类型的右括号闭合。
2. 左括号必须以正确的顺序闭合。

示例 1：
输入：s = "()"
输出：true

示例 2：
输入：s = "()[]{}"
输出：true

示例 3：
输入：s = "(]"
输出：false

示例 4：
输入：s = "([)]"
输出：false

示例 5：
输入：s = "{[]}"
输出：true

'''
# 使用栈，当遇到匹配的最小括号对时，我们将这对括号从栈中删除（即出栈），如果最后栈为空，那么它是有效的括号，反之不是。

s = "()[]{}"

class Solution:
    def isValid(self, s: str) -> bool:
        dic = {')':'(', ']':'[', '}':'{'}
        stack = []      #  创建一个栈
        for i in s:
            if i in '([{':
                stack.append(i)    # 如果是左括号，直接加入栈中
            elif i in ')]}':       # 如果是右括号：
                if not stack:            # 假如右括号比左括号先出现, 不能闭合
                    return False
                if dic[i] == stack[-1]:  # 假如遇到的右括号和左括号匹配：
                    stack.pop(-1)        # 删除栈中最上面的左括号，出栈
                else:                    # 遇到右括号, 必然要与上一个左括号闭合, 如果不匹配就 False
                    return False       
        if not stack:           # 正常闭合的情况下, 栈里面应该全都弹出去了, 所以应该是空的
            return True
        else:
            return False

sol = Solution()
result = sol.isValid(s)
print (result)