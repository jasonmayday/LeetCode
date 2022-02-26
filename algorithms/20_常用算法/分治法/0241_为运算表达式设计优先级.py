"""
https://leetcode-cn.com/problems/different-ways-to-add-parentheses/

给你一个由数字和运算符组成的字符串 expression ，按不同优先级组合数字和运算符，计算并返回所有可能组合的结果。你可以 按任意顺序 返回答案。

示例 1：
    输入：expression = "2-1-1"
    输出：[0,2]
    解释：
        ((2-1)-1) = 0 
        (2-(1-1)) = 2

示例 2：
    输入：expression = "2*3-4*5"
    输出：[-34,-14,-10,-10,10]
    解释：
        (2*(3-(4*5))) = -34 
        ((2*3)-(4*5)) = -14 
        ((2*(3-4))*5) = -10 
        (2*((3-4)*5)) = -10 
        (((2*3)-4)*5) = 10

提示：
    1 <= expression.length <= 20
    expression 由数字和算符 '+'、'-' 和 '*' 组成。
    输入表达式中的所有整数值在范围 [0, 99] 

"""
from typing import List


""" 分治算法 """
class Solution:
    def diffWaysToCompute(self, s: str) -> List[int]:
        if s.isdigit():     # 如果只有数字，直接返回
            return [int(s)]
        res = []
        for i, char in enumerate(s):
            if char in '+-*':                           # 1.拆分：遇到运算符，计算左右两侧的结果集
                left = self.diffWaysToCompute(s[:i])    # 2.治理：递归函数求出子问题的解
                right = self.diffWaysToCompute(s[i+1:])
                for l in left:                          # 3.合并：根据运算符合并子问题的解
                    for r in right:
                        if char == '+':
                            res.append(l + r)
                        elif char == '-':
                            res.append(l - r)
                        else:
                            res.append(l * r)
        return res


""" 分治精简版 """
class Solution:
    def diffWaysToCompute(self, s: str) -> List[int]:
        if s.isdigit():     # 如果只有数字，直接返回
            return [int(s)]
        res = []
        for i, ch in enumerate(s):
            if ch in '+-*':
                for left in self.diffWaysToCompute(s[:i]):
                    for right in self.diffWaysToCompute(s[i+1:]):
                        res.append(eval(f'{left}{ch}{right}'))
        return res


if __name__ == "__main__":
    expression = "2*3-4*5"
    sol = Solution()
    result = sol.diffWaysToCompute(expression)
    print (result)  