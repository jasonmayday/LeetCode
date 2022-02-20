"""
https://leetcode-cn.com/problems/basic-calculator-ii/

给你一个字符串表达式 s ，请你实现一个基本计算器来计算并返回它的值。

整数除法仅保留整数部分。

示例 1：
    输入：s = "3+2*2"
    输出：7

示例 2：
    输入：s = " 3/2 "
    输出：1

示例 3：
    输入：s = " 3+5 / 2 "
    输出：5

提示：
    1 <= s.length <= 3 * 10^5
    s 由整数和算符 ('+', '-', '*', '/') 组成，中间由一些空格隔开
    s 表示一个 有效表达式
    表达式中的所有整数都是非负整数，且在范围 [0, 2^31 - 1] 内
    题目数据保证答案是一个 32-bit 整数

"""

""" 栈 
    思路就是把所有的 *，/ 先计算出来，最后计算只有 +， - 运算符的表达式"""
class Solution:
    def calculate(self, s):
        # 数字(1)，运算符(2)，数字(3)
        stack = []      # 用栈保存运算符前的数字 (1)
        pre_op = '+'    # 用变量 pre_op 保存运算符 (2)  (对于第一个数字，其之前的运算符视为加号)
        num = 0         # 一个变量 num 保存运算符后的数字 (3)
        for i, ch in enumerate(s):
            if ch.isdigit():
                num = 10 * num + int(ch)
            if i == (len(s)-1) or ch in '+-*/':     # 运算符决定了现在的操作
                if pre_op == '+':       # 如果运算符为 +
                    stack.append(num)   # 把数字入栈
                
                elif pre_op == '-':     # 如果运算符为 -
                    stack.append(-num)  # 把数字取反入栈
                
                elif pre_op == '*':     # 如果运算符为 *
                    stack.append(stack.pop() * num) # 则需要计算 数字(1) 运算符(2) 数字(3)，然后把结果 入栈。
                
                elif pre_op == '/':     # 如果运算符为 /
                    top = stack.pop()   # 则需要计算 数字(1) 运算符(2) 数字(3)，然后把结果 入栈。
                    if top < 0:         # (如果遇到负数的除法，先使用的用「浮点除 / 」再取整的方式)
                        stack.append(int(top / num))
                    else:
                        stack.append(top // num)
                pre_op = ch     # 更新完栈后要记得更新数字和符号
                num = 0
        return sum(stack)       # 最后将栈里面所有元素相加

if __name__ == "__main__":
    s = "3+2*2"
    sol = Solution()
    result = sol.calculate(s)
    print (result)