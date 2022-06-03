"""
https://leetcode.cn/problems/consecutive-numbers-sum/

给定一个正整数 n，返回 连续正整数满足所有数字之和为 n 的组数 。 

示例 1:
    输入: n = 5
    输出: 2
    解释: 5 = 2 + 3，共有两组连续整数([5],[2,3])求和后为 5。

示例 2:
    输入: n = 9
    输出: 3
    解释: 9 = 4 + 5 = 2 + 3 + 4

示例 3:
    输入: n = 15
    输出: 4
    解释: 15 = 8 + 7 = 4 + 5 + 6 = 1 + 2 + 3 + 4 + 5

提示:
    1 <= n <= 10^9​​​​​​​

"""

class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        def isKConsecutive(n: int, k: int) -> bool:
            if k % 2:
                return n % k == 0
            return n % k and 2 * n % k == 0

        ans = 0
        k = 1
        while k * (k + 1) <= n * 2:
            if isKConsecutive(n, k):
                ans += 1
            k += 1
        return ans

if __name__ == "__main__":
    n = 19995
    sol = Solution()
    result = sol.consecutiveNumbersSum(n)
    print(result)