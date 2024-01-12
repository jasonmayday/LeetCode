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

""" 方法 1：模拟 """
class Solution:
    def reverseOnlyLetters(self, s: str) -> str:    # "ab-cd1"
        n = len(s)  
        alpha = []
        
        for i in range(n):
            if s[i].isalpha():
                alpha.append(s[i])  # ['a', 'b', 'c', 'd']
        
        res = []
        i_alpha = len(alpha) - 1    # 字母列表下标的最后一位
        
        for i in range(n):                  # 遍历字符串
            if s[i].isalpha():              # 如果 s 某位是字母
                res.append(alpha[i_alpha])  # 就把字母列表中当前的最后一个加到res中
                i_alpha -= 1                # 字母下标前移一位
            else:                           # 如果 s 某位不是字母
                res.append(s[i])            # 加上 s 原来的该位的字符

        return ''.join(res)


""" 方法 2：字母栈 """
class Solution(object):
    def reverseOnlyLetters(self, s: str) -> str:
        letters = [c for c in s if c.isalpha()] # ['a', 'b', 'c', 'd']        
        ans = []
        for c in s:
            if c.isalpha():
                ans.append(letters.pop())   # 将 s 中的所有字母单独存入栈中，所以出栈等价于对字母反序操作。
            else:
                ans.append(c)
        return "".join(ans)
   
""" 方法 3：双指针 """
class Solution(object):
    def reverseOnlyLetters(self, s: str) -> str:
        res = list(s)
        left = 0
        right = len(res) - 1
        while left < right:
            if not res[left].isalpha():     # 判断左边是否扫描到字母, 如果不是字母：
                left += 1
            elif not res[right].isalpha():  # 判断右边是否扫描到字母, 如果不是字母：
                right -= 1
            else:
                res[left], res[right] = res[right], res[left]
                left += 1
                right -= 1
        return "".join(res)

if __name__ == "__main__":
    S = "ab-cd1"
    sol = Solution()
    result = sol.reverseOnlyLetters(S)
    print (result)