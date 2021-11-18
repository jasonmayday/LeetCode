"""
https://leetcode-cn.com/problems/integer-replacement/

给定一个正整数 n ，你可以做如下操作：
    1. 如果 n 是偶数，则用 n / 2替换 n 。
    2. 如果 n 是奇数，则可以用 n + 1或n - 1替换 n 。
n 变为 1 所需的最小替换次数是多少？

示例 1：
    输入：n = 8
    输出：3
    解释：8 -> 4 -> 2 -> 1

示例 2：
    输入：n = 7
    输出：4
    解释：7 -> 8 -> 4 -> 2 -> 1
    或 7 -> 6 -> 3 -> 2 -> 1

示例 3：
    输入：n = 4
    输出：2

提示：
    1 <= n <= 2^31 - 1
"""

class Solution:
    def integerReplacement(self, n: int) -> int:
        if n == 1:
            return 0
        if n % 2 == 0:
            return 1 + self.integerReplacement(n // 2)  # 当 n 为偶数时，我们只有唯一的方法将 n 替换为 n/2，递归时次数加 1
        return 2 + min(self.integerReplacement(n // 2), self.integerReplacement(n // 2 + 1))  
        # 如果 n 是奇数，n+1 或者 n-1 一定是偶数，接着计算 n/2 即可，所以，再递归计算 n/2 和 n/2 + 1 的值

if __name__ == "__main__":
    n = 100
    sol = Solution()
    result = sol.integerReplacement(n)
    print (result) 