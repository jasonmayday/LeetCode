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

""" 要在末位产生0，则必然是5×2，即使是原数中包含的0也可以分解，因此将题目简化为寻找阶乘中5的个数，即n//5"""
class Solution:
    def trailingZeroes(self, n: int) -> int:
        count = 0
        while n >= 5:
            n = n // 5
            count += n
        return count

if __name__ == "__main__":
    n = 5
    sol = Solution()
    result = sol.trailingZeroes(n)
    print (result) 