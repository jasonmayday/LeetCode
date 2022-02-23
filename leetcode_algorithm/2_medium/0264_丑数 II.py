"""
https://leetcode-cn.com/problems/ugly-number-ii/

给你一个整数 n ，请你找出并返回第 n 个 丑数 。

丑数 就是只包含质因数 2、3 和/或 5 的正整数。

示例 1：
    输入：n = 10
    输出：12
    解释：[1, 2, 3, 4, 5, 6, 8, 9, 10, 12] 是由前 10 个丑数组成的序列。

示例 2：
    输入：n = 1
    输出：1
    解释：1 通常被视为丑数。

提示：
    1 <= n <= 1690

"""

import heapq

""" 思路一：最小堆
    因为丑数是2, 3, 5的倍数，我们不断把它们的倍数压入栈中，再按顺序弹出！"""
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        heap = [1]          # 初始时堆为空。首先将最小的丑数 1 加入堆。
        heapq.heapify(heap)
        res = 0
        for _ in range(n):
            res = heapq.heappop(heap)
            while heap and res == heap[0]:
                res = heapq.heappop(heap)
            a, b, c = res * 2, res * 3, res * 5
            for t in [a, b, c]:
                heapq.heappush(heap, t)
        return res

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        factors = [2, 3, 5]
        seen = {1}
        heap = [1]      # 初始时堆为空。首先将最小的丑数 11 加入堆。
        for _ in range(n - 1):
            curr = heapq.heappop(heap)
            for factor in factors:
                if (nxt := curr * factor) not in seen:
                    seen.add(nxt)
                    heapq.heappush(heap, nxt)

        return heapq.heappop(heap)


""" 思路二：动态规划 
dp[i] 表示第i个丑数

那么dp[i] = min(2 * dp[l_2], 3 * dp[l_3], 5 * dp[l_5])

这里 l_2, l_3, l_5是表示，指到的位置。

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp = [0] * n
        dp[0] = 1
        l_2 = 0
        l_3 = 0
        l_5 = 0
        for i in range(1, n):
            dp[i] = min(2 * dp[l_2], 3 * dp[l_3], 5 * dp[l_5])
            if dp[i] == 2 * dp[l_2]:
                l_2 += 1
            if dp[i] == 3 * dp[l_3]:
                l_3 += 1
            if dp[i] == 5 * dp[l_5]:
                l_5 += 1
        return dp[-1]
"""

if __name__ == "__main__":
    n = 15
    sol = Solution()
    result = sol.nthUglyNumber(n)
    print (result) 