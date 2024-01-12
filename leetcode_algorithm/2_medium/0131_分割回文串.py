"""
https://leetcode-cn.com/problems/palindrome-partitioning/

给你一个字符串 s，请你将 s 分割成一些子串，使每个子串都是 回文串 。返回 s 所有可能的分割方案。

回文串 是正着读和反着读都一样的字符串。

示例 1：
    输入：s = "aab"
    输出：[["a","a","b"],["aa","b"]]

示例 2：
    输入：s = "a"
    输出：[["a"]]

提示：
    1 <= s.length <= 16
    s 仅由小写英文字母组成

"""
from typing import List

""" 回溯
    递归用来纵向遍历，for循环用来横向遍历"""
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []  
        path = []  # 放已经回文的子串
        
        def backtrack(s,startIndex):
            if startIndex >= len(s):    # 如果起始位置已经大于s的大小，说明已经找到了一组分割方案了
                return res.append(path[:])
            for i in range(startIndex,len(s)):
                p = s[startIndex: i+1]   # 获取[startIndex,i+1]在s中的子串
                if p == p[::-1]:    # 是回文子串
                    path.append(p)  
                else: continue      # 不是回文，跳过
                backtrack(s,i+1)    # 寻找i+1为起始位置的子串
                path.pop()          # 回溯过程，弹出本次已经填在path的子串
        
        backtrack(s,0)
        return res
                

""" 回溯 + 双指针 """
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []    # 存放答案的集合
        path = []   # 放已经回文的子串
        
        def isPalindrome(s):    # 双指针法判断是否是回文串
            n = len(s)          # 一个指针从前向后，一个指针从后先前，如果前后指针所指向的元素是相等的，就是回文字符串了。
            i, j = 0, n - 1
            while i < j: 
                if s[i] != s[j]: return False
                i += 1
                j -= 1
            return True
            
        def backtrack(s, startIndex):
            if startIndex >= len(s): # 如果起始位置已经大于s的大小，说明已经找到了一组分割方案了
                res.append(path[:])
                return  
            for i in range(startIndex, len(s)):
                p = s[startIndex: i+1]  # 获取[startIndex, i+1]在s中的子串
                if isPalindrome(p):     # 是回文子串，则记录
                    path.append(p)
                else:           # 不是回文，跳过
                    continue
                backtrack(s, i + 1)     # 起始位置后移，保证不重复
                path.pop() # 回溯过程，弹出本次已经填在path的子串
                
        backtrack(s, 0)
        return res
    

if __name__ == "__main__":
    s = "aab"
    sol = Solution()
    result = sol.partition(s)
    print(result)