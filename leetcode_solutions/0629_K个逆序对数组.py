'''

给出两个整数 n 和 k，找出所有包含从 1 到 n 的数字，且恰好拥有 k 个逆序对的不同的数组的个数。

逆序对的定义如下：对于数组的第i个和第j个元素，如果满 i < j 且 a[i] > a[j]，则其为一个逆序对；否则不是。

例如，数组（3，1，4，5，2）的逆序对有 (3,1) (3,2) (4,2) (5,2)，共4个。

由于答案可能很大，只需要返回 答案 mod 10^9 + 7 的值。

示例 1:
    输入: n = 3, k = 0
    输出: 1
    解释: 
    只有数组 [1,2,3] 包含了从1到3的整数并且正好拥有 0 个逆序对。

示例 2:
    输入: n = 3, k = 1
    输出: 2
    解释: 
    数组 [1,3,2] 和 [2,1,3] 都有 1 个逆序对。

说明:
    n 的范围是 [1, 1000] 并且 k 的范围是 [0, 1000]。

'''

class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        mod = 10**9 + 7

        dp = [[0] * (k+1) for _ in range(n+1)]

        for i in range(1, n+1): dp[i][0] = 1            # 所有无逆序对的数组个数皆为1，即升序排列
        for j in range(1, k+1): dp[1][j] += dp[1][j-1]  # 前缀和优化，先对`n==1`的情况进行前缀和

        for i in range(2, n+1):                         # 从2开始遍历
            for j in range(1, k+1):                     # 逆序对的个数从1开始遍历

                dp[i][j] = dp[i-1][j] + dp[i][j-1]      # 一部分是加上左侧的，构成前缀和；另外一部分是求得当前的结果
                if j-i+1 > 0:
                    dp[i][j] -= dp[i-1][j-i]
                dp[i][j] %= mod
        
        if k > 0:
            return (dp[n][k] - dp[n][k-1]) % mod
        else:
            return dp[n][k] % mod


if __name__ == "__main__":
    n = 10000
    k = 5

    sol = Solution()
    result = sol.kInversePairs(n, k)
    print(result)