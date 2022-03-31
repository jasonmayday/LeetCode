"""
https://leetcode-cn.com/problems/evaluate-reverse-polish-notation/

根据 逆波兰表示法，求表达式的值。

有效的算符包括 +、-、*、/ 。每个运算对象可以是整数，也可以是另一个逆波兰表达式。

注意 两个整数之间的除法只保留整数部分。

可以保证给定的逆波兰表达式总是有效的。换句话说，表达式总会得出有效数值且不存在除数为 0 的情况。

示例 1：
    输入：tokens = ["2","1","+","3","*"]
    输出：9
    解释：该算式转化为常见的中缀算术表达式为：((2 + 1) * 3) = 9

示例 2：
    输入：tokens = ["4","13","5","/","+"]
    输出：6
    解释：该算式转化为常见的中缀算术表达式为：(4 + (13 / 5)) = 6

示例 3：
    输入：tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    输出：22
    解释：该算式转化为常见的中缀算术表达式为：
    ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
    = ((10 * (6 / (12 * -11))) + 17) + 5
    = ((10 * (6 / -132)) + 17) + 5
    = ((10 * 0) + 17) + 5
    = (0 + 17) + 5
    = 17 + 5
    = 22

提示：
    1 <= tokens.length <= 10^4
    tokens[i] 是一个算符（"+"、"-"、"*" 或 "/"），或是在范围 [-200, 200] 内的一个整数

逆波兰表达式：

逆波兰表达式是一种后缀表达式，所谓后缀就是指算符写在后面。
    平常使用的算式则是一种中缀表达式，如 ( 1 + 2 ) * ( 3 + 4 ) 。
    该算式的逆波兰表达式写法为 ( ( 1 2 + ) ( 3 4 + ) * ) 。

逆波兰表达式主要有以下两个优点：
    去掉括号后表达式无歧义，上式即便写成 1 2 + 3 4 + * 也可以依据次序计算出正确结果。
    适合用栈操作运算：遇到数字则入栈；遇到算符则取出栈顶两个数字进行计算，并将结果压入栈中

"""
from typing import List

""" 栈 """
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []  # ["2","1","+","3","*"] ((2 + 1) * 3) = 9
        for t in tokens:    
            if t in {"+", "-", "/", "*"}: # 遇到操作符,弹出栈顶两个元素操作
                num1 = stack.pop()  # 弹出数字 1
                num2 = stack.pop()  # 弹出数字 2
                stack.append(str(int(eval(num2 + t + num1))))   # eval() 函数用来执行一个字符串表达式，并返回表达式的值。
            else:               # 如果遇到数字
                stack.append(t) # 压入栈
        return stack.pop()     

""" 栈 """ 
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []  # ["2","1","+","3","*"] ((2 + 1) * 3) = 9
        operations = {  "+": lambda a, b: b + a,
                        "-": lambda a, b: b - a,
                        "*": lambda a, b: b * a,
                        "/": lambda a, b: int(b / a)}
        for t in tokens:
            if t in operations:
                stack.append(operations[t](stack.pop(), stack.pop()))
            else:
                stack.append(int(t))
        return stack.pop()

""" 栈 """
class Solution:
    def evalRPN(self, tokens):
        stack = []
        for token in tokens:
            if   token == "+": stack[-1] = stack[-2] + stack.pop()
            elif token == "-": stack[-1] = stack[-2] - stack.pop()
            elif token == "*": stack[-1] = stack[-2] * stack.pop()
            elif token == "/": stack[-1] = int(stack[-2] / stack.pop())
            else: stack.append(int(token))
        return stack[0]


if __name__ == "__main__":
    tokens = ["2","1","+","3","*"]  # ((2 + 1) * 3) = 9
    sol = Solution()
    result = sol.evalRPN(tokens)
    print(result)