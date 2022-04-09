"""
https://leetcode-cn.com/problems/string-rotation-lcci/

字符串轮转。给定两个字符串s1和s2，请编写代码检查s2是否为s1旋转而成（比如，waterbottle是erbottlewat旋转后的字符串）。

示例1:
    输入：s1 = "waterbottle", s2 = "erbottlewat"
    输出：True

示例2:
    输入：s1 = "aa", s2 = "aba"
    输出：False

提示：
    字符串长度在[0, 100000]范围内。

说明:
    你能只调用一次检查子串的方法吗？

"""

""" 方法一：模拟"""
class Solution:
    def isFlipedString(self, s1: str, s2: str) -> bool:
        m, n = len(s1), len(s2)
        if m != n:
            return False
        if n == 0:
            return True
        for i in range(n):
            for j in range(n):
                if s1[(i + j) % n] != s2[j]:
                    break
            else:
                return True
        return False

""" 方法二：搜索子字符串"""
class Solution:
    def isFlipedString(self, s1: str, s2: str) -> bool:
        return len(s1) == len(s2) and s2 in s1 + s1

if __name__ == "__main__":
    s1 = "waterbottle"
    s2 = "erbottlewat"
    sol = Solution()
    result = sol.isFlipedString(s1, s2)
    print(result)