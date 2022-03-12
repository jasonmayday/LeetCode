"""
https://leetcode-cn.com/problems/decode-string/

给定一个经过编码的字符串，返回它解码后的字符串。

编码规则为: k[encoded_string]，表示其中方括号内部的 encoded_string 正好重复 k 次。注意 k 保证为正整数。

你可以认为输入字符串总是有效的；输入字符串中没有额外的空格，且输入的方括号总是符合格式要求的。

此外，你可以认为原始数据不包含数字，所有的数字只表示重复的次数 k ，例如不会出现像 3a 或 2[4] 的输入。

示例 1：
    输入：s = "3[a]2[bc]"
    输出："aaabcbc"

示例 2：
    输入：s = "3[a2[c]]"
    输出："accaccacc"

示例 3：
    输入：s = "2[abc]3[cd]ef"
    输出："abcabccdcdcdef"

示例 4：
    输入：s = "abc3[cd]xyz"
    输出："abccdcdcdxyz"

提示：
    1 <= s.length <= 30
    s 由小写英文字母、数字和方括号 '[]' 组成
    s 保证是一个 有效 的输入。
    s 中所有整数的取值范围为 [1, 300] 

"""

""" 解法一：辅助栈法 """
class Solution:
    def decodeString(self, s: str) -> str:
        stack, res, multi = [], "", 0
        for c in s:
            if c == '[':                    # 当 c 为 '[' 时
                stack.append([multi, res])  # 将当前 multi 和 res 入栈
                res, multi = "", 0          # 并分别置空置 0
            elif c == ']':
                cur_multi, last_res = stack.pop()
                res = last_res + cur_multi * res
            elif '0' <= c <= '9':                   # 当 c 为数字时
                multi = multi * 10 + int(c)         # 考虑数字是2位以上的情况，将数字字符转化为数字 multi，用于后续倍数计算
            else:               # 当 c 为字母时，直接在 res 尾部添加 c
                res += c
        return res

""" 解法二：递归法 """
class Solution:
    def decodeString(self, s: str) -> str:
        def dfs(s, i):
            res, multi = "", 0
            while i < len(s):   # 这里不能用for i in range(len(s)),因为递归调用时，新的循环不从0开始从i开始
                if '0' <= s[i] <= '9':              # 当 c 为数字时
                    multi = multi * 10 + int(s[i])  # 考虑数字是2位以上的情况，将数字字符转化为数字 multi，用于后续倍数计算
                elif s[i] == '[':           # 当 s[i] == '[' 时，开启新一层递归，
                    i, tmp = dfs(s, i + 1)  # 记录此 [...] 内字符串 tmp 和递归后的最新索引 i，
                    res += multi * tmp      # 并执行 res + multi * tmp 拼接字符串。
                    multi = 0               # 重置 multi
                elif s[i] == ']':   # 当 s[i] == ']' 时，递归终止
                    return i, res   # 返回当前括号内记录的 res 字符串与 ] 的索引 i （更新上层递归指针位置）；
                else:           # 当 c 为字母时，直接在 res 尾部添加 c
                    res += s[i]
                i += 1
            return res
        return dfs(s,0)

if __name__ == "__main__":
    s = "2[abc]3[cd]ef"
    sol = Solution()
    result = sol.decodeString(s)
    print (result)