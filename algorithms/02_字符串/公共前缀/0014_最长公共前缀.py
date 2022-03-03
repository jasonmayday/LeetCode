'''
https://leetcode-cn.com/problems/longest-common-prefix/

编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

示例 1：
    输入：strs = ["flower","flow","flight"]
    输出："fl"

示例 2：
    输入：strs = ["dog","racecar","car"]
    输出：""
    解释：输入不存在公共前缀。

提示：
    1 <= strs.length <= 200
    0 <= strs[i].length <= 200
    strs[i] 仅由小写英文字母组成

'''


from typing import List

'''解法1：先找出数组中字典序最小和最大的字符串(两者的差别是最大的), 最长公共前缀即为这两个字符串的公共前缀'''
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''
        str0 = min(strs)
        str1 = max(strs)
        for i in range(len(str0)):
            if str0[i] != str1[i]:
                return str0[:i]
        return str0

'''解法2：find()函数，取一个单词s, 和后面单词比较, 看s与每个单词相同的最长前缀是多少！遍历所有单词。'''
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        res = strs[0]                       # 将第一个字符串作为前缀， res = "flower"
        i = 1
        for i in range(1, len(strs)):       # 遍历从第二个字符串开始的所有字符串
                                            # find() 方法检测字符串 str 中是否包含子字符串 s, 如果包含子字符串返回开始的索引值, 否则返回-1
            while strs[i].find(res) != 0:   # 如果包含子字符串返回开始的索引值，!= 0说明有公共前缀
                res = res[0: len(res) - 1]
        return res

if __name__ == "__main__":
    strs = ["flower","flow","flight"]
    sol = Solution()
    result = sol.longestCommonPrefix(strs)
    print(result)