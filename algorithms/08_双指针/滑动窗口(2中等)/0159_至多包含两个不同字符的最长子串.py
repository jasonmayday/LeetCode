"""
https://leetcode-cn.com/problems/longest-substring-with-at-most-two-distinct-characters/

给定一个字符串 s ，找出 至多 包含两个不同字符的最长子串 t ，并返回该子串的长度。

示例 1:
    输入: "eceba"
    输出: 3
    解释: t 是 "ece"，长度为3。

示例 2:
    输入: "ccaabbb"
    输出: 5
    解释: t 是 "aabbb"，长度为5。

"""

from collections import defaultdict

""" 滑动窗口 + 哈希表 """
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: 'str') -> 'int':
        n = len(s)
        if n < 3:
            return n
        left = 0    # 使用一个左指针和一个右指针表示滑动窗口的边界。
        right = 0   # 一开始，让两个指针都指向 0

        hashmap = defaultdict()     # 字符串里的字符都当做键，在窗口中的最右边的字符位置作为值。
        max_len = 2

        while right < n:
            if len(hashmap) < 3:            # 当窗口包含的字符不超过 2 个不同的字符时
                hashmap[s[right]] = right   # 将当前字符 s[right] 放到 hashmap 中
                right += 1                  # 将右指针往右移动一次。

            if len(hashmap) == 3:               # 如果在某一个位置有 3 个不同的字符，
                del_idx = min(hashmap.values())
                del hashmap[s[del_idx]]         # 将最左边的字符从 哈希表中删去
                left = del_idx + 1              # 移动左指针，直到窗口内包含不超过 2 个不同字符。

            max_len = max(max_len, right - left)

        return max_len


if __name__ == "__main__":
    s = "ccaabbb"
    sol = Solution()
    result = sol.lengthOfLongestSubstringTwoDistinct(s)
    print(result)