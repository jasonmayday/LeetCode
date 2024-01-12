"""
https://leetcode-cn.com/problems/factorial-trailing-zeroes/

给定一个整数 n ，返回 n! 结果中尾随零的数量。

提示 n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1

示例 1：
    输入：n = 3
    输出：0
    解释：3! = 6 ，不含尾随 0

示例 2：
    输入：n = 5
    输出：1
    解释：5! = 120 ，有一个尾随 0

示例 3：
    输入：n = 0
    输出：0

提示：
    0 <= n <= 10^4
 
进阶：
    你可以设计并实现对数时间复杂度的算法来解决此问题吗？

"""

""" 方法一：数学 """
class Solution:
    def trailingZeroes(self, n: int) -> int:
        ans = 0
        for i in range(5, n + 1, 5):
            while i % 5 == 0:
                i //= 5         # 遍历 [1,n] 的所有 55 的倍数求出。
                ans += 1
        return ans

""" 要在末位产生0，则必然是5×2，即使是原数中包含的0也可以分解，因此将题目简化为寻找阶乘中5的个数，即n//5"""
class Solution:
    def trailingZeroes(self, n: int) -> int:
        count = 0
        while n >= 5:
            n = n // 5  # 不断将 n 除以 5，
            count += n  # 并累加每次除后的 n，来得到答案。
        return count

if __name__ == "__main__":
    n = 50
    sol = Solution()
    result = sol.trailingZeroes(n)
    print (result)