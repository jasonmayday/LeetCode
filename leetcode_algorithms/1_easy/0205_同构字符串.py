"""
https://leetcode-cn.com/problems/isomorphic-strings/

给定两个字符串 s 和 t，判断它们是否是同构的。

如果 s 中的字符可以按某种映射关系替换得到 t ，那么这两个字符串是同构的。

每个出现的字符都应当映射到另一个字符，同时不改变字符的顺序。不同字符不能映射到同一个字符上，相同字符只能映射到同一个字符上，字符可以映射到自己本身。

示例 1:
    输入：s = "egg", t = "add"
    输出：true

示例 2：
    输入：s = "foo", t = "bar"
    输出：false

示例 3：
    输入：s = "paper", t = "title"
    输出：true
 
提示：
    可以假设 s 和 t 长度相同。

"""

class Solution(object):
    def isIsomorphic(self, s, t):
        if not s:
            return True     # 当s是空字符串时（此时t也是空字符串），返回True。
        dic = {}
        for i in range(len(s)):
            if s[i] not in dic:
                if t[i] in dic.values():
                    return False
                else:
                    dic[s[i]]=t[i]
            else:
                if dic[s[i]]!=t[i]:
                    return False
        return True

if __name__ == "__main__":
    s = "paper"
    t = "title"
    sol = Solution()
    result = sol.isIsomorphic(s, t)
    print (result)
