"""
https://leetcode-cn.com/problems/make-the-string-great/

给你一个由大小写英文字母组成的字符串 s 。

一个整理好的字符串中，两个相邻字符 s[i] 和 s[i+1]，其中 0<= i <= s.length-2 ，要满足如下条件:
    若 s[i] 是小写字符，则 s[i+1] 不可以是相同的大写字符。
    若 s[i] 是大写字符，则 s[i+1] 不可以是相同的小写字符。

请你将字符串整理好，每次你都可以从字符串中选出满足上述条件的 两个相邻 字符并删除，直到字符串整理好为止。

请返回整理好的 字符串 。题目保证在给出的约束条件下，测试样例对应的答案是唯一的。

注意：空字符串也属于整理好的字符串，尽管其中没有任何字符。

示例 1：
    输入：s = "leEeetcode"
    输出："leetcode"
    解释：无论你第一次选的是 i = 1 还是 i = 2，都会使 "leEeetcode" 缩减为 "leetcode" 。

示例 2：
    输入：s = "abBAcC"
    输出：""
    解释：存在多种不同情况，但所有的情况都会导致相同的结果。例如：
    "abBAcC" --> "aAcC" --> "cC" --> ""
    "abBAcC" --> "abBA" --> "aA" --> ""

示例 3：
    输入：s = "s"
    输出："s"

"""

"""解法1"""
class Solution:
    def makeGood(self, s: str) -> str:
        ret = list()
        for ch in s:    # 从左到右扫描字符串 s 的每个字符
            if ret and ret[-1].lower() == ch.lower() and ret[-1] != ch: 
                                # 字符 ch 与字符串 ret 的最后一个字符互为同一个字母的大小写：
                ret.pop()       # 根据题意，两个字符都要在整理过程中被删除，因此要弹出 ret 的最后一个字符；
            else:               # 否则：两个字符都需要被保留，
                ret.append(ch)  # 因此要将字符 ch 附加在字符串 ret 的后面。
        return "".join(ret)

"""解法2：栈"""
class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for ele in s:
            if stack:
                if abs(ord(ele)-ord(stack[-1])) != 32:
                    stack.append(ele)
                else:
                    stack.pop()
            else:
                stack.append(ele)
        res = ''
        for ele in stack:
            res += ele
        return res
        
if __name__ == "__main__":
    s = "leEeetcode"
    sol = Solution()
    result = sol.makeGood(s)
    print(result)