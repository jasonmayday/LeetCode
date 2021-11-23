"""
https://leetcode-cn.com/problems/reverse-only-letters/

给定一个字符串 S，返回 “反转后的” 字符串，其中不是字母的字符都保留在原地，而所有字母的位置发生反转。

示例 1：
    输入："ab-cd"
    输出："dc-ba"

示例 2：
    输入："a-bC-dEf-ghIj"
    输出："j-Ih-gfE-dCba"

示例 3：
    输入："Test1ng-Leet=code-Q!"
    输出："Qedo1ct-eeLg=ntse-T!"

提示：
    S.length <= 100
    33 <= S[i].ASCIIcode <= 122 
    S 中不包含 \ or "

"""

"""方法 1：字母栈"""
class Solution(object):
    def reverseOnlyLetters(self, S):
        letters = [c for c in S if c.isalpha()]
        ans = []
        for c in S:
            if c.isalpha():
                ans.append(letters.pop())   # 将 s 中的所有字母单独存入栈中，所以出栈等价于对字母反序操作。
            else:
                ans.append(c)
        return "".join(ans)
    
"""方法 2：双指针"""
class Solution(object):
    def reverseOnlyLetters(self, S):
        S = list(S)
        left, right = 0, len(S) - 1
        while left < right:
            if not S[left].isalpha():   # 如果不是字母：
                left += 1
            elif not S[right].isalpha():
                right -= 1
            else:
                S[left], S[right] = S[right], S[left]
                left += 1
                right -= 1
        return "".join(S)

if __name__ == "__main__":
    S = "Test1ng-Leet=code-Q!"
    sol = Solution()
    result = sol.reverseOnlyLetters(S)
    print (result)