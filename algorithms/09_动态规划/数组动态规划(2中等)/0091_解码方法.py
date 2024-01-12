"""
https://leetcode-cn.com/problems/decode-ways/

一条包含字母 A-Z 的消息通过以下映射进行了 编码 ：
    'A' -> "1"
    'B' -> "2"
    ...
    'Z' -> "26"

要 解码 已编码的消息，所有数字必须基于上述映射的方法，反向映射回字母（可能有多种方法）。例如，"11106" 可以映射为：
    "AAJF" ，将消息分组为 (1 1 10 6)
    "KJF" ，将消息分组为 (11 10 6)

注意，消息不能分组为  (1 11 06) ，因为 "06" 不能映射为 "F" ，这是由于 "6" 和 "06" 在映射中并不等价。

给你一个只含数字的 非空 字符串 s ，请计算并返回 解码 方法的 总数 。

题目数据保证答案肯定是一个 32 位 的整数。

示例 1：
    输入：s = "12"
    输出：2
    解释：它可以解码为 "AB"（1 2）或者 "L"（12）。

示例 2：
    输入：s = "226"
    输出：3
    解释：它可以解码为 "BZ" (2 26), "VF" (22 6), 或者 "BBF" (2 2 6) 。

示例 3：
    输入：s = "0"
    输出：0
    解释：没有字符映射到以 0 开头的数字。
    含有 0 的有效映射是 'J' -> "10" 和 'T'-> "20" 。
    由于没有字符，因此没有有效的方法对此进行解码，因为所有数字都需要映射。

提示：
    1 <= s.length <= 100
    s 只包含数字，并且可能包含前导零。

"""

""" 动态规划 """
class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)  #  "226"
        f = [1] + [0] * n   # [1, 0, 0, 0]  设 fi 表示字符串 s 的前 i 个字符 s[1..i] 的解码方法数
        for i in range(1, n + 1):
            if s[i - 1] != '0':     # 第一种情况是我们使用了一个字符，即 s[i] 进行解码，那么只要 s[i] != 0，它就可以被解码成 A∼I 中的某个字母。
                f[i] += f[i - 1]
            if i > 1 and s[i - 2] != '0' and int(s[i-2:i]) <= 26:   # 第二种情况是我们使用了两个字符，即 s[i-1] 和 s[i] 进行解码
                                                                    # 并且 s[i−1] 和 s[i] 组成的整数必须小于等于 26，这样它们就可以被解码成 J∼Z 中的某个字母
                f[i] += f[i - 2]                                    # 只有当 i>1 时才能进行转移，否则 s[i−1] 不存在。
        return f[n]
    
""" 动态规划详解 """
class Solution(object):
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0': # 基本情况，直接返回 0
            return 0
        dp = [None] * len(s)     # 构建 dp 数组
        dp[0] = 1                # 只有一个数时肯定为 1
        
        if len(s) > 1:      # 为 dp[1] 填充值
            if s[1] == '0': # s[i] 为 ‘0’ 时
                if int(s[0:2]) <= 26:   # 截取前两数，判断是否小于或等于 26
                    dp[1] = 1           # 因为 s[i] 为 ‘0’ 所以 dp[1] 只有 1 种可能
                else:                   # 前两位数大于 26
                    return 0            # 比如 60 , 此时该序列无法翻译
            else:           # s[i] 不为 ‘0’ 时
                if int(s[0:2]) <= 26:
                    dp[1] = 2           # 比如 16，有两种翻译结果
                else:
                    dp[1] = 1           # 比如 27，只有一种结果
        else: # 只有一个数
            return 1

        for i in range(2, len(s)): # 从 2 开始
            if s[i] == '0': # s[i] 为 ‘0’ 时
                if s[i-1] == '0': # 前一个为 ‘0’
                    return 0 # 无解
                else: # 前一个不为 ‘0’
                    if int(s[i-1:i+1]) <= 26: # s[i-1] 和 s[i] 组成的数 <= 26
                        dp[i] = dp[i-2]
                    else:
                        return 0
            else: # s[i] 不为 ‘0’
                if s[i-1] == '0': # 前一个为 ‘0’
                    dp[i] = dp[i-1]
                else: # 前一个不为 ‘0’
                    if int(s[i-1:i+1]) <= 26: # s[i-1] 和 s[i] 组成的数 <= 26
                        dp[i] = dp[i-1] + dp[i-2]
                    else: # s[i-1] 和 s[i] 组成的数 > 26
                        dp[i] = dp[i-1]

        return dp[len(s) - 1]

""" DFS递归 """

class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        def dfs(i):
            if i == n: return 1
            ans = 0
            if i < n and s[i] != "0":
                ans += dfs(i + 1)
            if i < n - 1 and s[i] != "0" and s[i:i+2] <= "26":
                ans += dfs(i + 2)
            return ans
        
        return dfs(0)
    
if __name__ == "__main__":
    s = "226"   # "BZ" (2 26), "VF" (22 6), 或者 "BBF" (2 2 6) 
    sol = Solution()
    result = sol.numDecodings(s)
    print(result)