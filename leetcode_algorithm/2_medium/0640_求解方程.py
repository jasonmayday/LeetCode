"""
https://leetcode.cn/problems/solve-the-equation/

求解一个给定的方程，将x以字符串 "x=#value" 的形式返回。该方程仅包含 '+' ， '-' 操作，变量 x 和其对应系数。

如果方程没有解，请返回 "No solution" 。如果方程有无限解，则返回 “Infinite solutions” 。

如果方程中只有一个解，题目保证返回值 'x' 是一个整数。

示例 1：
    输入: equation = "x+5-3+x=6+x-2"
    输出: "x=2"

示例 2:
    输入: equation = "x=x"
    输出: "Infinite solutions"

示例 3:
    输入: equation = "2x=x"
    输出: "x=0"
 
提示:
    3 <= equation.length <= 1000
    equation 只有一个 '='.
    equation 方程由整数组成，其绝对值在 [0, 100] 范围内，不含前导零和变量 'x' 。

"""

"""方法一：解析"""
class Solution:
    def solveEquation(self, equation: str) -> str:
        factor = 0  # 表示变量的系数
        val = 0     # 表示常量值
        i = 0
        n = len(equation)
        sign = 1    # 等式左边默认系数为正
        
        while i < n:                # 开始遍历字符串
            if equation[i] == '=':  # 遇到等号时候
                sign = -1           # 等式右边系数为负
                i += 1
                continue

            s = sign
            if equation[i] == '+':  # 去掉前面的符号
                i += 1
            elif equation[i] == '-':
                s = -s
                i += 1

            num  = 0        # 使用 number 记录数字
            valid = False   # valid 表示 number 是否有效
            
            while i < n and equation[i].isdigit():
                valid = True
                num = num * 10 + int(equation[i])
                i += 1

            if i < n and equation[i] == 'x':        # 如果我们解析到的项是变量项
                factor += s * num if valid else s   # 那么相应的更改 factor 变量
                i += 1
            
            else:                                   # 如果我们解析到的项是常数项
                val += s * num                      # 相应的更改 val

        if factor == 0:                     # 如果 factor=0 成立，说明变量 x 对方程无影响
            if val:                         # 如果 val != 0
                return "No solution"        # 无解
            else:                           # 如果 val = 0
                return "Infinite solutions" # 则说明方程有无数解
        
        if val % factor:                # 如果val 不能被factor整除
            return "No solution"        # 说明x没有整数解
        else:
            return f"x={-val // factor}"    # 否则返回对应的整数解

if __name__ == "__main__":
    equation = "x+5-3+x=6+x-2"
    sol = Solution()
    result = sol.solveEquation(equation)
    print(result)