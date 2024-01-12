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
        seen = {1}      # 使用哈希集合去重，避免相同元素多次加入堆。
        heap = [1]      # 初始时堆为空。首先将最小的丑数 1 加入堆。
        for _ in range(n - 1):
            curr = heapq.heappop(heap)  # 每次取出堆顶元素 x，则 x 是堆中最小的丑数
            for factor in factors:
                if (nxt := curr * factor) not in seen:
                    seen.add(nxt)
                    heapq.heappush(heap, nxt)

        return heapq.heappop(heap)


""" 思路二：动态规划
        例如 n = 10， primes = [2, 3, 5]。 打印出丑数列表：1, 2, 3, 4, 5, 6, 8, 9, 10, 12
    后面的丑数一定由前面的丑数乘以2，或者乘以3，或者乘以5得来。
    相当于3个数组，分别是能被2、3、5整除的递增数组，且每个数组的第一个数都为1。
        例如，8,9,10,12一定是1, 2, 3, 4, 5, 6乘以2,3,5三个质数中的某一个得到。
    这样的话我们的解题思路就是：从第一个丑数开始，一个个数丑数，并确保数出来的丑数是递增的，直到数到第n个丑数，得到答案。那么问题就是如何递增地数丑数？
    观察上面的例子，假如我们用1, 2, 3, 4, 5, 6去形成后面的丑数，我们可以将1, 2, 3, 4, 5, 6分别乘以2, 3, 5，这样得到一共6*3=18个新丑数。
    也就是说1, 2, 3, 4, 5, 6中的每一个丑数都有一次机会与2相乘，一次机会与3相乘，一次机会与5相乘（一共有18次机会形成18个新丑数），来得到更大的一个丑数。

    这样就可以用三个指针，
        pointer2, 指向1, 2, 3, 4, 5, 6中，还没使用乘2机会的丑数的位置。该指针的前一位已经使用完了乘以2的机会。
        pointer3, 指向1, 2, 3, 4, 5, 6中，还没使用乘3机会的丑数的位置。该指针的前一位已经使用完了乘以3的机会。
        pointer5, 指向1, 2, 3, 4, 5, 6中，还没使用乘5机会的丑数的位置。该指针的前一位已经使用完了乘以5的机会。
    下一次寻找丑数时，则对这三个位置分别尝试使用一次乘2机会，乘3机会，乘5机会，看看哪个最小，最小的那个就是下一个丑数。
    最后，得到下一个丑数的指针位置加一，因为它对应的那次乘法使用完了。
    这里需要注意下去重的问题，如果某次寻找丑数，找到了下一个丑数10，则pointer2和pointer5都需要加一，因为5乘2等于10， 2乘5也等于10，这样可以确保10只被数一次。
"""
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[1] = 1           # dp[i] 表示第 i 个丑数
        p2 = p3 = p5 = 1    # 定义三个指针 p2, p3, p5 ，表示下一个丑数是当前指针指向的丑数乘以对应的质因数。初始时，三个指针的值都是 1。
        for i in range(2, n + 1):
            num2 = dp[p2] * 2   # 下一个丑数是当前指针指向的丑数乘以对应的质因数
            num3 = dp[p3] * 3
            num5 = dp[p5] * 5
            dp[i] = min(num2, num3, num5)   # 三个位置分别尝试使用一次乘2机会，乘3机会，乘5机会，看看哪个最小，最小的那个就是下一个丑数
            if dp[i] == num2:   # 得到下一个丑数的指针位置加一，因为它对应的那次乘法使用完了。
                p2 += 1
            if dp[i] == num3:
                p3 += 1
            if dp[i] == num5:
                p5 += 1
        return dp[n]


if __name__ == "__main__":
    n = 15
    sol = Solution()
    result = sol.nthUglyNumber(n)
    print (result)