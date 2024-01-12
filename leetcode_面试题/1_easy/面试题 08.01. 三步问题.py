"""
https://leetcode-cn.com/problems/three-steps-problem-lcci/

三步问题。有个小孩正在上楼梯，楼梯有n阶台阶，小孩一次可以上1阶、2阶或3阶。实现一种方法，计算小孩有多少种上楼梯的方式。结果可能很大，你需要对结果模1000000007。

示例1:
    输入：n = 3
    输出：4
    说明: 有四种走法

示例2:
    输入：n = 5
    输出：13
 
提示:
    n 范围在[1, 1000000]之间

"""
""" 动态规划 """
class Solution:
    def waysToStep(self, n: int) -> int:
        mod = 1000000007
        if n <= 2:
            return n
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n + 1):
            dp[i] = (dp[i - 3] + dp[i - 2] + dp[i - 1]) % mod
        return dp[n]


""" 动态规划: 省空间的做法，只维护数组中的前三个元素，在求出第四个元素后，数组中的第一个元素出队，后三个元素分别前移一个单位"""
class Solution:
    def waysToStep(self, n: int) -> int:
        if n <= 2:
            return n
        elif n == 3:
            return 4
        dp = [1, 2, 4, 0]
        for _ in range(3, n):
            dp[3] = (dp[0] + dp[1]) % 1000000007 + dp[2]
            dp[3] %= 1000000007
            dp[0] = dp[1]
            dp[1] = dp[2]
            dp[2] = dp[3]
        return dp[3]

if __name__ == "__main__":
    n = 3
    sol = Solution()
    result = sol.waysToStep(n)
    print(result)