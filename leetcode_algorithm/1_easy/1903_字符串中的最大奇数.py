"""
https://leetcode-cn.com/problems/largest-odd-number-in-string/

给你一个字符串 num ，表示一个大整数。请你在字符串 num 的所有 非空子字符串 中找出 值最大的奇数 ，并以字符串形式返回。如果不存在奇数，则返回一个空字符串 "" 。

子字符串 是字符串中的一个连续的字符序列。

示例 1：
    输入：num = "52"
    输出："5"
    解释：非空子字符串仅有 "5"、"2" 和 "52" 。"5" 是其中唯一的奇数。

示例 2：
    输入：num = "4206"
    输出：""
    解释：在 "4206" 中不存在奇数。

示例 3：
    输入：num = "35427"
    输出："35427"
    解释："35427" 本身就是一个奇数。

提示：
    1 <= num.length <= 10^5
    num 仅由数字组成且不含前导零

"""

"""找最右的奇数，切片"""
class Solution:
    def largestOddNumber(self, num: str) -> str:
        n = len(num)
        for i in range(n - 1, -1, -1):  # 从后开始遍历
            if int(num[i]) % 2 == 1:    # 找到第一个值为奇数的字符
                return num[:i+1]        # 返回 num[:i+1]
        return ""                       # 未找到值为奇数的字符，返回空字符串

"""找最右的奇数，切片"""
class Solution:
    def largestOddNumber(self, num: str) -> str:
        n = len(num)
        i = n - 1                       # 从最后一位开始遍历
        while 0 <= i and int(num[i]) % 2 == 0:  # 偶数位跳过
            i -= 1
        if i == -1:
            return ""
        else:
            return num[:i + 1]

if __name__ == "__main__":
    num = "42016"
    sol = Solution()
    result = sol.largestOddNumber(num)
    print (result)