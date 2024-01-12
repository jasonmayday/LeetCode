"""
https://leetcode-cn.com/problems/largest-substring-between-two-equal-characters/

给你一个字符串 s，请你返回 两个相同字符之间的最长子字符串的长度 ，计算长度时不含这两个字符。如果不存在这样的子字符串，返回 -1 。

子字符串 是字符串中的一个连续字符序列。

示例 1：
    输入：s = "aa"
    输出：0
    解释：最优的子字符串是两个 'a' 之间的空子字符串。

示例 2：
    输入：s = "abca"
    输出：2
    解释：最优的子字符串是 "bc" 。

示例 3：
    输入：s = "cbzxy"
    输出：-1
    解释：s 中不存在出现出现两次的字符，所以返回 -1 。

示例 4：
    输入：s = "cabbac"
    输出：4
    解释：最优的子字符串是 "abba" ，其他的非最优解包括 "bb" 和 "" 。

提示：
    1 <= s.length <= 300
    s 只含小写英文字母

"""

"""解法：双指针遍历"""
class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        res = -1
        for i in range(len(s) - 1):
            j = len(s) - 1                  # j 从最后一位开始
            while j > i:
                if s[i] == s[j]:            # 如果碰到相同的字符
                    res = max(res, j-i-1)   # 计算他们之间的字符数
                    break                   # 然后终止遍历
                j -= 1                      # j 向左移动一位
        return res

"""解法：字典查询"""
class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        seen = dict()
        res = -1
        for index,ch in enumerate(s):
            if ch in seen:
                res = max(res, index - seen[ch]-1)
            else:
                seen[ch] = index
        return res


if __name__ == "__main__":
    s = "cabbac"
    sol = Solution()
    result = sol.maxLengthBetweenEqualCharacters(s)
    print(result)