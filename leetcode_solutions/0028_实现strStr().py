'''
https://leetcode-cn.com/problems/implement-strstr/

实现 strStr() 函数。

给你两个字符串 haystack 和 needle ，请你在 haystack 字符串中找出 needle 字符串出现的第一个位置（下标从 0 开始）。如果不存在，则返回  -1 。

说明：

当 needle 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。

对于本题而言，当 needle 是空字符串时我们应当返回 0 。这与 C 语言的 strstr() 以及 Java 的 indexOf() 定义相符。

示例 1：
    输入：haystack = "hello", needle = "ll"
    输出：2

示例 2：
    输入：haystack = "aaaaa", needle = "bba"
    输出：-1

示例 3：
    输入：haystack = "", needle = ""
    输出：0

提示：
    0 <= haystack.length, needle.length <= 5 * 104
    haystack 和 needle 仅由小写英文字符组成

'''
haystack = "hello"
needle = "ll"

# 解法1：遍历法
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == '':
            return 0
        for i in range(0, len(haystack) - len(needle) + 1):  # 0-4范围内
            if haystack[i:i+len(needle)] == needle:
                return i
            return -1

# 解法2：调用find函数，str1.find(str2) 函数检测字符串str1中是否包含子字符串str2，如果包含子字符串返回开始的索引值，否则返回-1。
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)

# 解法3：KMP算法
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        a=len(needle)
        b=len(haystack)
        if a==0:
            return 0
        next=self.getnext(a,needle)
        p=-1
        for j in range(b):
            while p>=0 and needle[p+1]!=haystack[j]:
                p=next[p]
            if needle[p+1]==haystack[j]:
                p+=1
            if p==a-1:
                return j-a+1
        return -1

    def getnext(self,a,needle):
        next=['' for i in range(a)]
        k=-1
        next[0]=k
        for i in range(1,len(needle)):
            while (k>-1 and needle[k+1]!=needle[i]):
                k=next[k]
            if needle[k+1]==needle[i]:
                k+=1
            next[i]=k
        return next

sol = Solution()
result = sol.strStr(haystack, needle)
print(result)