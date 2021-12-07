'''
https://leetcode-cn.com/problems/expression-add-operators/

给定一个仅包含数字 0-9 的字符串 num 和一个目标值整数 target ，在 num 的数字之间添加 二元 运算符（不是一元）+、- 或 * ，返回所有能够得到目标值的表达式。

示例 1:
输入: num = "123", target = 6
输出: ["1+2+3", "1*2*3"] 

示例 2:
输入: num = "232", target = 8
输出: ["2*3+2", "2+3*2"]

示例 3:
输入: num = "105", target = 5
输出: ["1*0+5","10-5"]

示例 4:
输入: num = "00", target = 0
输出: ["0+0", "0-0", "0*0"]

示例 5:
输入: num = "3456237490", target = 9191
输出: []

'''


from typing import List

class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:

        def dfs(rest, expression, prev, val):
            """
            :param rest: 剩余的待拆分的字符串
            :param expression: 当前已经组成的表达式
            :param prev: expression中最后一个单项式的值，用于乘法的情况处理
            :param val: expression的值，相当于eval(expression)，设置该变量可重复计算
            :return:
            """
            if not rest and val == target:                      # 如果没有剩余字符，并且expression的值恰好等于目标值target
                ans.append(expression)                          # 则当当前表达式expression加入到结果列表ans中
            for i in range(1, len(rest)+1):                     # 尝试所有切分方式
                select, rest_next = rest[:i], rest[i:]          # 将剩余字符rest切分成select和rest_next两部分
                if len(select) > 1 and select[0] == "0":        # 一个二位及以上位数字的开头不能是零，比如0+01是不合法的
                    break                                       # 继续遍历，select肯定更长，没必要研究了
                n = int(select)                                 # 整数化当前选择的数字
                if len(expression) == 0:                        # 这一段话本来应该在函数外面的，用来给一个初始prev
                    dfs(rest_next, select, n, n)                # 整个表达式的第一个数字，并不涉及操作符
                    continue                                    # 不应继续后续代码，因为后续代码执行的前提是表达式不为空，即最终表达式的开头必须是数字而非操作符“+-*
                dfs(rest_next, expression + '+' + select, n, val + n)   # 尝试把当前数字n用加号接到expression后面
                dfs(rest_next, expression + '-' + select, -n, val - n)  # 尝试把当前数字n用减号接到expression后面
                dfs(rest_next, expression + '*' + select, prev * n, val - prev + prev * n) # 这里注意因为乘法优先级高于加减，所以遇到乘法时，应该减去expression中最后一个单项式的值

        ans = []                                                # 全局变量，用来保存最终结果所有可能
        dfs(num, "", 0, 0)                                      # 调用回溯函数
        return ans                                              # 返回结果列表，结果列表在调用时已被更新

if __name__ == "__main__":
    num = "105"
    target = 5
    sol = Solution()
    result = sol.addOperators(num, target)
    print(result)
