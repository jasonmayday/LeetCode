"""
https://leetcode-cn.com/problems/longer-contiguous-segments-of-ones-than-zeros/

给你一个二进制字符串 s 。如果字符串中由 1 组成的 最长 连续子字符串 严格长于 由 0 组成的 最长 连续子字符串，返回 true ；否则，返回 false 。

    例如，s = "110100010" 中，由 1 组成的最长连续子字符串的长度是 2 ，由 0 组成的最长连续子字符串的长度是 3 。

注意，如果字符串中不存在 0 ，此时认为由 0 组成的最长连续子字符串的长度是 0 。字符串中不存在 1 的情况也适用此规则。

示例 1：
    输入：s = "1101"
    输出：true
    解释：
    由 1 组成的最长连续子字符串的长度是 2："1101"
    由 0 组成的最长连续子字符串的长度是 1："1101"
    由 1 组成的子字符串更长，故返回 true 。

示例 2：
    输入：s = "111000"
    输出：false
    解释：
    由 1 组成的最长连续子字符串的长度是 3："111000"
    由 0 组成的最长连续子字符串的长度是 3："111000"
    由 1 组成的子字符串不比由 0 组成的子字符串长，故返回 false 。

示例 3：
    输入：s = "110100010"
    输出：false
    解释：
    由 1 组成的最长连续子字符串的长度是 2："110100010"
    由 0 组成的最长连续子字符串的长度是 3："110100010"
    由 1 组成的子字符串不比由 0 组成的子字符串长，故返回 false 。

提示：
    1 <= s.length <= 100
    s[i] 不是 '0' 就是 '1'

"""

"""解法1：遍历字符串"""
class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        max0, max1 = 0, 0
        count = 0
        prev = '#'   # 上个字符
        for ch in s:
            if prev == ch:  # 当前字符与上个字符相等
                count += 1
            else:           # 当前字符与上个字符不相等
                if prev == '0':
                    max0 = max(max0, count)
                elif prev == '1':
                    max1 = max(max1, count)
                count = 1
            prev = ch
            
        # 字符串结尾的连续子串
        if prev == '0':
            max0 = max(max0, count)
        elif prev == '1':
            max1 = max(max1, count)
        return max1 > max0

"""解法2：遍历字符串"""
class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        max0, max1 = 0, 0
        cur0, cur1 = 0, 0
        for ch in s:
            if ch == '0':
                cur0 += 1
                cur1 = 0
            else:
                cur0 = 0
                cur1 += 1
            max0 = max(max0, cur0)
            max1 = max(max1, cur1)
        return max1 > max0

"""解法3："""
class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        if len(max(s.split('0'), key = lambda x: len(x))) >len(max(s.split('1'),key = lambda x: len(x))):
            return True
        else:
            return False

        
if __name__ == "__main__":
    s = "110100010"
    sol = Solution()
    result = sol.checkZeroOnes(s)
    print (result)