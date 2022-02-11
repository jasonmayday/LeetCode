"""
给你一个字符串 s，找到 s 中最长的回文子串。

示例 1：
    输入：s = "babad"
    输出："bab"
    解释："aba" 同样是符合题意的答案。

示例 2：
    输入：s = "cbbd"
    输出："bb"

示例 3：
    输入：s = "a"
    输出："a"

示例 4：
    输入：s = "ac"
    输出："a"

提示：
    1 <= s.length <= 1000
    s 仅由数字和英文字母（大写和/或小写）组成

"""

"""方法一：动态规划"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s
        
        max_len = 1
        begin = 0
        dp = [[False] * n for _ in range(n)]    # dp[i][j] 表示 s[i..j] 是否是回文串
        for i in range(n):
            dp[i][i] = True
        
        # 递推开始
        # 先枚举子串长度
        for L in range(2, n + 1):
            for i in range(n):  # 枚举左边界，左边界的上限设置可以宽松一些
                j = L + i - 1   # 由 L 和 i 可以确定右边界，即 j - i + 1 = L 得
                if j >= n:      # 如果右边界越界
                    break       # 就可以退出当前循环
                    
                if s[i] != s[j]:
                    dp[i][j] = False 
                else:
                    if j - i < 3:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]
                
                # 只要 dp[i][L] == true 成立，就表示子串 s[i..L] 是回文，此时记录回文长度和起始位置
                if dp[i][j] and j - i + 1 > max_len:
                    max_len = j - i + 1
                    begin = i
        return s[begin:begin + max_len]

"""方法二：中心扩展算法"""
class Solution:
    def expandAroundCenter(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return left + 1, right - 1

    def longestPalindrome(self, s: str) -> str:
        start, end = 0, 0
        for i in range(len(s)):
            left1, right1 = self.expandAroundCenter(s, i, i)
            left2, right2 = self.expandAroundCenter(s, i, i + 1)
            if right1 - left1 > end - start:
                start, end = left1, right1
            if right2 - left2 > end - start:
                start, end = left2, right2
        return s[start: end + 1]

"""方法三：Manacher 算法"""
class Solution:
    def expand(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return (right - left - 2) // 2

    def longestPalindrome(self, s: str) -> str:
        end, start = -1, 0
        s = '#' + '#'.join(list(s)) + '#'
        arm_len = []
        right = -1
        j = -1
        for i in range(len(s)):
            if right >= i:
                i_sym = 2 * j - i
                min_arm_len = min(arm_len[i_sym], right - i)
                cur_arm_len = self.expand(s, i - min_arm_len, i + min_arm_len)
            else:
                cur_arm_len = self.expand(s, i, i)
            arm_len.append(cur_arm_len)
            if i + cur_arm_len > right:
                j = i
                right = i + cur_arm_len
            if 2 * cur_arm_len + 1 > end - start:
                start = i - cur_arm_len
                end = i + cur_arm_len
        return s[start+1:end+1:2]

if __name__ == "__main__":
    s = "babad"
    sol = Solution()
    result = sol.longestPalindrome(s)
    print (result)