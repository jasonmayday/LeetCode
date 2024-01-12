"""
https://leetcode-cn.com/problems/mini-parser/

给定一个字符串 s 表示一个整数嵌套列表，实现一个解析它的语法分析器并返回解析的结果 NestedInteger 。

列表中的每个元素只可能是整数或整数嵌套列表

示例 1：
    输入：s = "324",
    输出：324
    解释：你应该返回一个 NestedInteger 对象，其中只包含整数值 324。

示例 2：
    输入：s = "[123,[456,[789]]]",
    输出：[123,[456,[789]]]
    解释：返回一个 NestedInteger 对象包含一个有两个元素的嵌套列表：
    1. 一个 integer 包含值 123
    2. 一个包含两个元素的嵌套列表：
        i.  一个 integer 包含值 456
        ii. 一个包含一个元素的嵌套列表
            a. 一个 integer 包含值 789

提示：
    1 <= s.length <= 5 * 10^4
    s 由数字、方括号 "[]"、负号 '-' 、逗号 ','组成
    用例保证 s 是可解析的 NestedInteger
    输入中的所有值的范围是 [-10^6, 10^6]

"""

class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        
        if s[0] != '[':
            return NestedInteger(int(s))
        
        stack = []
        # num为数字，sign为符号为，is_num为前一个是否为数字
        num, sign, is_num = 0, 1, False
        
        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
                is_num = True
            elif c == '-':
                sign = -1
            elif c == '[':
                stack.append(NestedInteger())
            elif c == ',' or c == ']':
                # 把刚才遇到的数字append进去
                if is_num:
                    cur_list = stack.pop()
                    cur_list.add(NestedInteger(sign * num))
                    stack.append(cur_list)
                num, sign, is_num = 0, 1, False

                # 此时为嵌套列表
                if c == ']' and len(stack) > 1:
                    cur_list = stack.pop()
                    stack[-1].add(cur_list)

        return stack[0]
