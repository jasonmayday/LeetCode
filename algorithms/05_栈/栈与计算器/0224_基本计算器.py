"""
https://leetcode-cn.com/problems/basic-calculator/

给你一个字符串表达式 s ，请你实现一个基本计算器来计算并返回它的值。

注意:不允许使用任何将字符串作为数学表达式计算的内置函数，比如 eval() 。

示例 1：
    输入：s = "1 + 1"
    输出：2

示例 2：
    输入：s = " 2-1 + 2 "
    输出：3

示例 3：
    输入：s = "(1+(4+5+2)-3)+(6+8)"
    输出：23

提示：
    1 <= s.length <= 3 * 10^5
    s 由数字、'+'、'-'、'('、')'、和 ' ' 组成
    s 表示一个有效的表达式
    '+' 不能用作一元运算(例如， "+1" 和 "+(2 + 3)" 无效)
    '-' 可以用作一元运算(即 "-1" 和 "-(2 + 3)" 是有效的)
    输入中不存在两个连续的操作符
    每个数字和运行的计算将适合于一个有符号的 32位 整数

"""

""" 栈
    重点：先算括号里面的表达式 """
class Solution(object):
    def calculate(self, s):
        # 数字(1)，运算符(2)，数字(3)
        res = 0     # res 表示左边表达式除去栈内保存元素的计算结果；
        num = 0     # 表示当前遇到的数字，会更新到 res 中
        sign = 1    # 表示运算符(第一位为正，所以默认为 1)
        stack = []  # 栈保存遇到左括号时前面计算好了的结果和运算符。
        
        for c in s:
            if c.isdigit():                 # 如果当前是数字，那么更新计算当前数字；
                num = 10 * num + int(c)
            
            elif c == "+" or c == "-":          # 如果当前是操作符 + 或者 -
                res += sign * num               # 那么需要更新计算当前计算的结果 res
                num = 0                         # 并把当前数字 num 设为 0
                sign = 1 if c == "+" else -1    # sign 设为正负，重新开始；
            
            elif c == "(":              # 如果当前是 ( ，那么说明遇到了右边的表达式，而后面的小括号里的内容需要优先计算，
                stack.append(res)       # 所以要把 res，sign 进栈
                stack.append(sign)
                res = 0                 # 更新 res 和 sign 为新的开始
                sign = 1
            
            elif c == ")":              # 如果当前是 )，那么说明右边的表达式结束，即当前括号里的内容已经计算完毕
                res += sign * num       
                num = 0
                res *= stack.pop()      # 所以要把之前的结果出栈，然后计算整个式子的结果；
                res += stack.pop()
        
        res += sign * num               # 最后，当所有数字结束的时候，需要把最后的一个 num 也更新到 res 中。
        return res
    
""" 栈 """
class Solution:
    def calculate(self, s: str) -> int:
        ops = [1]
        sign = 1

        ret = 0
        n = len(s)
        i = 0
        while i < n:
            if s[i] == ' ':
                i += 1
            elif s[i] == '+':
                sign = ops[-1]
                i += 1
            elif s[i] == '-':
                sign = -ops[-1]
                i += 1
            elif s[i] == '(':
                ops.append(sign)
                i += 1
            elif s[i] == ')':
                ops.pop()
                i += 1
            else:
                num = 0
                while i < n and s[i].isdigit():
                    num = num * 10 + ord(s[i]) - ord('0')
                    i += 1
                ret += num * sign
        return ret


if __name__ == "__main__":
    s = "(1+(4+5+2)-3)+(6+8)"
    sol = Solution()
    result = sol.calculate(s)
    print(result)