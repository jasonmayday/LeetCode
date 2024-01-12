"""
https://leetcode-cn.com/problems/perfect-squares/

给你一个整数 n ，返回 和为 n 的完全平方数的最少数量 。

完全平方数 是一个整数，其值等于另一个整数的平方；换句话说，其值等于一个整数自乘的积。例如，1、4、9 和 16 都是完全平方数，而 3 和 11 不是。

示例 1：
    输入：n = 12
    输出：3
    解释：12 = 4 + 4 + 4

示例 2：
    输入：n = 13
    输出：2
    解释：13 = 4 + 9
 
提示：
    1 <= n <= 10^4

"""

class Solution:
    '''版本一，先遍历背包, 再遍历物品'''
    def numSquares(self, n: int) -> int:
        dp = [n] * (n + 1)
        dp[0] = 0           # dp[i]：和为 i 的完全平方数的最少数量为 dp[i]
        # 遍历背包
        for j in range(1, n+1):
            for i in range(1, n):
                num = i ** 2
                if num > j: break
                # 遍历物品
                if j - num >= 0:
                    dp[j] = min(dp[j], dp[j - num] + 1)
        return dp[n]

class Solution:
    '''版本二， 先遍历物品, 再遍历背包'''
    def numSquares(self, n: int) -> int:
        dp = [i for i in range(n + 1)]  #初始化: 组成和的完全平方数的最多个数，就是只用1构成，因此，dp[i] = i
        # dp[0] = 0 无意义，只是为了方便记录特殊情况:
        # n 本身就是完全平方数，dp[n] = min(dp[n], dp[n - n] + 1) = 1
        for i in range(1, n): # 遍历物品
            if i * i > n:
                break
            num = i * i
            for j in range(num, n + 1): # 遍历背包
                dp[j] = min(dp[j], dp[j - num] + 1)

        return dp[n]

if __name__ == "__main__":
    n = 12
    sol = Solution()
    result = sol.numSquares(n)
    print (result)