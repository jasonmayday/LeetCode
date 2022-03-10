"""
https://leetcode-cn.com/problems/count-numbers-with-unique-digits/

给定一个非负整数 n，计算各位数字都不同的数字 x 的个数，其中 0 ≤ x < 10^n 。

示例:
    输入: 2
    输出: 91
    解释: 答案应为除去 11,22,33,44,55,66,77,88,99 外，在 [0,100) 区间内的所有数字。

"""

class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        nums = [0 for _ in range(n + 1)]    # [0, 0, 0] 每一位数字的选择数
        nums[0] = 1                         # [1, 0, 0]
        for i in range(1, n + 1):
            new = 9                     # 第 2 位数字，需要去掉第一位选择的，但是多了一个0，所以是9个
            for j in range(i - 1):      # 第 3 位为8个
                new *= (9 - j)          # 第 n 位为(9-n+2)个
            nums[i] = new + nums[i-1]   # 把具有n位数的不同数字的个数计算完后，需要加上n-1位数字的个数，那就是nums[i-1]了
        return nums[n]

class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0: return 1
        res = 10    # 当 n = 1 的时候，也就是只有一位数，自然是有 0 - 9 一共10种选择， return 10
        k = 9
        temp = 9
        for _ in range(2, min(n + 1, 11)):
            temp *= k
            k -= 1
            res += temp
        return res

if __name__ == "__main__":
    n = 2
    sol = Solution()
    result = sol.countNumbersWithUniqueDigits(n)
    print (result)