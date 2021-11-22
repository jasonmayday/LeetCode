"""
https://leetcode-cn.com/problems/backspace-string-compare/

给定 s 和 t 两个字符串，当它们分别被输入到空白的文本编辑器后，请你判断二者是否相等。# 代表退格字符。

如果相等，返回 true ；否则，返回 false 。

注意：如果对空文本输入退格字符，文本继续为空。

示例 1：
    输入：s = "ab#c", t = "ad#c"
    输出：true
    解释：S 和 T 都会变成 “ac”。

示例 2：
    输入：s = "ab##", t = "c#d#"
    输出：true
    解释：s 和 t 都会变成 “”。

示例 3：
    输入：s = "a##c", t = "#a#c"
    输出：true
    解释：s 和 t 都会变成 “c”。

示例 4：
    输入：s = "a#c", t = "b"
    输出：false
    解释：s 会变成 “c”，但 t 仍然是 “b”。

提示：
    1 <= s.length, t.length <= 200
    s 和 t 只含有小写字母以及字符 '#'
 
进阶：
    你可以用 O(N) 的时间复杂度和 O(1) 的空间复杂度解决该问题吗？

"""

class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        def build(s: str) -> str:
            ret = list()
            for ch in s:
                if ch != "#":       # 如果是数字而不是井号，就加到ret里
                    ret.append(ch)
                elif ret:           # 如果是井号，就弹出刚刚加入的
                    ret.pop()
            return "".join(ret)
        
        return build(S) == build(T)

if __name__ == "__main__":
    S = "a##c"
    T = "#a#c"
    sol = Solution()
    result = sol.backspaceCompare(S,T)
    print(result)