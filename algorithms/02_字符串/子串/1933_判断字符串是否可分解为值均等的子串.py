"""
https://leetcode-cn.com/problems/check-if-string-is-decomposable-into-value-equal-substrings/

一个字符串的所有字符都是一样的，被称作等值字符串。
    举例，"1111" 和 "33" 就是等值字符串。
    相比之下，"123"就不是等值字符串。

规则：给出一个数字字符串s，将字符串分解成一些等值字符串，如果有且仅有一个等值子字符串长度为2，其他的等值子字符串的长度都是3.

如果能够按照上面的规则分解字符串s，就返回真，否则返回假。

子串就是原字符串中连续的字符序列。

示例 1：
    输入: s = "000111000"
    输出: false
    解释: s只能被分解长度为3的等值子字符串。

示例 2：
    输入: s = "00011111222"
    输出: true
    解释: s 能被分解为 ["000","111","11","222"].

示例 3：
    输入: s = "01110002223300"
    输出: false
    解释: 一个不能被分解的原因是在开头有一个0.

提示:
    1 <= s.length <= 1000
    s 仅包含数字。

"""

class Solution:
    def isDecomposable(self, s: str) -> bool:
        have_len2 = False   # 初始化：字符串中是否有长度为2的等值子字符串
        n = len(s)
        i = 0
        while i < n:
            cur_len = 1
            while i + 1 < n and s[i] == s[i+1]:
                i += 1
                cur_len += 1
            if cur_len % 3 == 2:        # 某段连续相同的字符串长度模3为2。比如2，5，8...
                if have_len2 == True:   # 如果 之前已经有长度为2的等值子字符串
                    return False        # 返回False，因为长度为2的只能有一个
                have_len2 = True    # 如果还没有，标记 have_len2 为 True
            else:
                if cur_len % 3 != 0:    # 某段连续相同的字符串长度模3为0。比如3，6，9...
                    return False        # 如果不是三的倍数，返回 False
            i += 1      # 指向下一段的第一个位置
        return have_len2

if __name__ == "__main__":
    s = "00011111222"
    sol = Solution()
    result = sol.isDecomposable(s)
    print(result)