"""
https://leetcode-cn.com/problems/split-a-string-in-balanced-strings/

在一个 平衡字符串 中，'L' 和 'R' 字符的数量是相同的。

给你一个平衡字符串 s，请你将它分割成尽可能多的平衡字符串。

注意：分割得到的每个字符串都必须是平衡字符串，且分割得到的平衡字符串是原平衡字符串的连续子串。

返回可以通过分割得到的平衡字符串的 最大数量 。

示例 1：
    输入：s = "RLRRLLRLRL"
    输出：4
    解释：s 可以分割为 "RL"、"RRLL"、"RL"、"RL" ，每个子字符串中都包含相同数量的 'L' 和 'R' 。

示例 2：
    输入：s = "RLLLLRRRLR"
    输出：3
    解释：s 可以分割为 "RL"、"LLLRRR"、"LR" ，每个子字符串中都包含相同数量的 'L' 和 'R' 。

示例 3：
    输入：s = "LLLLRRRR"
    输出：1
    解释：s 只能保持原样 "LLLLRRRR".

示例 4：
    输入：s = "RLRRRLLRLL"
    输出：2
    解释：s 可以分割为 "RL"、"RRRLLRLL" ，每个子字符串中都包含相同数量的 'L' 和 'R' 。

提示：
    1 <= s.length <= 1000
    s[i] = 'L' 或 'R'
    s 是一个 平衡 字符串

"""

''' 因为一开始给出的是平衡字符串，L和R的个数是相等的。
    也就是说当我们分割出去一个平衡子串后，剩下的L和R的个数依然相等。
    每次能分出去都分的话，这样分串是最多的。'''
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        ans = 0
        d = 0   # 变量 d 维护 L 和 R 字符的数量之差
        for ch in s:
            if ch == 'L':
                d += 1
            else:
                d -= 1
            if d == 0:
                ans += 1
        return ans

if __name__ == "__main__":
    s = "RLRRLLRLRL"
    sol = Solution()
    result = sol.balancedStringSplit(s)
    print(result)