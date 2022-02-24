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
        if not s:
            return 0
        left = 0
        occur = set()   # 哈希集合，记录每个字符是否出现过
        n = len(s)
        max_len = 0     # 最长子串的长度初始化为 0
        cur_len = 0
        for i in range(n):          # 遍历字符串
            cur_len += 1            # 遍历一位，当前子串长度加一
            while s[i] in occur:    # 如果遍历到某字符，但此字符已经出现过，比如 abca，第四位时
                occur.remove(s[left])   # 把队列的左边的元素移出出现过的集合occur，相当于移动队列
                left += 1               # 左指针右移
                cur_len -= 1            # 因为最左边字符被移除，当前的子串长度减一
            if cur_len > max_len:       # 如果当前子串长度大于之前的最大长度
                max_len = cur_len       # 则更新最长子串
            occur.add(s[i])         # 然后刚刚遍历到的字符加入到已出现的字符集合中
        return max_len
    
"""方法一：滑动窗口另一种实现"""  
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        from collections import defaultdict
        lookup = defaultdict(int)
        start = 0
        end = 0
        max_len = 0
        counter = 0
        while end < len(s):
            if lookup[s[end]] > 0:
                counter += 1
            lookup[s[end]] += 1
            end += 1
            while counter > 0:
                if lookup[s[start]] > 1:
                    counter -= 1
                lookup[s[start]] -= 1
                start += 1
            max_len = max(max_len, end - start)
        return max_len

if __name__ == "__main__":
    s = "abcabcbb"
    sol = Solution()
    result = sol.lengthOfLongestSubstring(s)
    print (result)