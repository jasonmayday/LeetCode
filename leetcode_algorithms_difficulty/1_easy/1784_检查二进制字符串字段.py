"""
https://leetcode-cn.com/problems/check-if-binary-string-has-at-most-one-segment-of-ones/

给你一个二进制字符串 s ，该字符串 不含前导零 。

如果 s 包含 零个或一个由连续的 '1' 组成的字段 ，返回 true​​​ 。否则，返回 false 。

示例 1：
    输入：s = "1001"
    输出：false
    解释：字符串中的 1 没有形成一个连续字段。

示例 2：
    输入：s = "110"
    输出：true

提示：
    1 <= s.length <= 100
    s[i]​​​​ 为 '0' 或 '1'
    s[0] 为 '1'

"""

class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        return '01' not in s

if __name__ == "__main__":
    s = "1001"
    sol = Solution()
    result = sol.checkOnesSegment(s)
    print(result)