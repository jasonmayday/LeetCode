"""
https://leetcode-cn.com/problems/remove-outermost-parentheses

有效括号字符串为空 ""、"(" + A + ")" 或 A + B ，其中 A 和 B 都是有效的括号字符串，+ 代表字符串的连接。

例如，""，"()"，"(())()" 和 "(()(()))" 都是有效的括号字符串。
如果有效字符串 s 非空，且不存在将其拆分为 s = A + B 的方法，我们称其为原语（primitive），其中 A 和 B 都是非空有效括号字符串。

给出一个非空有效字符串 s，考虑将其进行原语化分解，使得：s = P_1 + P_2 + ... + P_k，其中 P_i 是有效括号字符串原语。

对 s 进行原语化分解，删除分解中每个原语字符串的最外层括号，返回 s 。

示例 1：
    输入：s = "(()())(())"
    输出："()()()"
    解释：
    输入字符串为 "(()())(())"，原语化分解得到 "(()())" + "(())"，
    删除每个部分中的最外层括号后得到 "()()" + "()" = "()()()"。

示例 2：
    输入：s = "(()())(())(()(()))"
    输出："()()()()(())"
    解释：
    输入字符串为 "(()())(())(()(()))"，原语化分解得到 "(()())" + "(())" + "(()(()))"，
    删除每个部分中的最外层括号后得到 "()()" + "()" + "()(())" = "()()()()(())"。

示例 3：
    输入：s = "()()"
    输出：""
    解释：
    输入字符串为 "()()"，原语化分解得到 "()" + "()"，
    删除每个部分中的最外层括号后得到 "" + "" = ""。

提示：
    1 <= s.length <= 10^5
    s[i] 为 '(' 或 ')'
    s 是一个有效括号字符串

"""

''' 方法1：双指针
    1. 原语化
    2. 拆除各原语最外层括号。
    双指针查找各原语下标
    ( ( ) ( ) ) ( )
    1 2 1 2 1 0 1 0     '''
class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        # 双指针 寻找原语化的最外层括号下标
        primitive_indices = []
        left, count = 0, 0
        for i in range(len(S)):
            if S[i] == "(": count += 1
            elif S[i] == ")": count -= 1
            if count == 0:                          # 找到最外层右括号
                primitive_indices.append((left, i)) # 添加答案
                left = i + 1                        # 更新最外层左括号指针
        # 根据下标，提取原语，切片拆除括号
        return "".join( S[m+1:n] for m, n in primitive_indices )


''' 方法2：单指针计数
    不保存下标。
    一次遍历过程中，直接把非最外层的括号放进答案里'''
class Solution:
    def removeOuterParentheses(self, S):
        res, count = [], 0
        for c in S:
            if c == '(' and count > 0: res.append(c)    # 非最外层的左括号
            if c == ')' and count > 1: res.append(c)    # 非最外层的右括号
            count += 1 if c == '(' else -1
        return "".join(res)


''' 方法3：辅助栈
    碰到 "(" 就入栈，碰到 ")" 就把栈顶的一个 "(" 消掉。就像消消乐一样。
    如果栈为空，那么刚刚碰到的 “)” 就是最外层右括号；如果入栈前栈为空，则即将入栈的 “(” 就是最外层左括号。'''
class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        res = ""
        stack = []
        for c in S:     # 非外层括号加入结果中
            if c == "(":            # 怎么判断是非外层括号？
                if stack: res += c  # 1. 左括号加入前，栈不为空。
                stack.append("(")
            if c == ")":
                stack.pop()
                if stack: res += c  # 2. 右括号加入并消括号后，栈不为空
        return res

    
if __name__ == "__main__":
    s = "(()())(())"
    sol = Solution()
    result = sol.removeOuterParentheses(s)
    print(result)