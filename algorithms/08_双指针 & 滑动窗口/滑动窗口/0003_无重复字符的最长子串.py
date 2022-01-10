"""
https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/

给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。

示例 1:
    输入: s = "abcabcbb"
    输出: 3 
    解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

示例 2:
    输入: s = "bbbbb"
    输出: 1
    解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。

示例 3:
    输入: s = "pwwkew"
    输出: 3
    解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
         请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。

示例 4:
    输入: s = ""
    输出: 0

提示：
    0 <= s.length <= 5 * 104
    s 由英文字母、数字、符号和空格组成

"""

"""方法一：滑动窗口"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        occur = set()   # 哈希集合，记录每个字符是否出现过
        n = len(s)
        rk = -1         # 右指针，初始值为 -1，相当于我们在字符串的左边界的左侧，还没有开始移动
        ans = 0
        for i in range(n):
            if i != 0:
                # 左指针向右移动一格，移除一个字符
                occur.remove(s[i - 1])
            while rk + 1 < n and s[rk + 1] not in occur:
                # 不断地移动右指针
                occur.add(s[rk + 1])
                rk += 1
            # 第 i 到 rk 个字符是一个极长的无重复字符子串
            ans = max(ans, rk - i + 1)
        return ans

if __name__ == "__main__":
    s = "abcabcbb"
    sol = Solution()
    result = sol.lengthOfLongestSubstring(s)
    print (result)