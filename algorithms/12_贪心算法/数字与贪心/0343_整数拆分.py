"""
https://leetcode-cn.com/problems/integer-break/

给定一个正整数 n ，将其拆分为 k 个 正整数 的和（ k >= 2 ），并使这些整数的乘积最大化。

返回 你可以获得的最大乘积 。

示例 1:
    输入: n = 2
    输出: 1
    解释: 2 = 1 + 1, 1 × 1 = 1。

示例 2:
    输入: n = 10
    输出: 36
    解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36。

提示:
    2 <= n <= 58

"""

""" 动态规划 """
class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0] * (n + 1)  # dp[i] 表示将正整数 i 拆分成至少两个正整数的和之后，这些正整数的最大乘积。0 和 1 都不能拆分，因此 dp[0] = dp[1] = 0。
        for i in range(2, n + 1):
            for j in range(i):
                # 假设对正整数 i 拆分出的第一个正整数是 j（1 <= j < i），则有以下两种方案：
                # 1) 将 i 拆分成 j 和 i−j 的和，且 i−j 不再拆分成多个正整数，此时的乘积是 j * (i-j)
                # 2) 将 i 拆分成 j 和 i−j 的和，且 i−j 继续拆分成多个正整数，此时的乘积是 j * dp[i-j]
                dp[i] = max(dp[i], j * (i - j), j * dp[i - j])
        print (dp)  # [0, 0, 1, 2, 4, 6, 9, 12, 18, 27, 36]
        return dp[n]
    
    
""" 贪心算法 """
class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2:
            return 1
        if n == 3:
            return 2
        if n == 4:
            return 4
        
        # 应该尽可能的多拆出 3。这是由于 3x2 > 5（=3+2）, 3x3 > 2x2x2>（6, 7）
        res = 1
        while n >= 5:
            res *= 3
            n -= 3
        res *= n
        return res


if __name__ == "__main__":
    n = 10
    sol = Solution()
    result = sol.integerBreak(n)
    print (result)