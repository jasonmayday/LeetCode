"""
https://leetcode-cn.com/problems/rotate-function/

给定一个长度为 n 的整数数组 A 。

假设 Bk 是数组 A 顺时针旋转 k 个位置后的数组，我们定义 A 的“旋转函数” F 为：

F(k) = 0 * Bk[0] + 1 * Bk[1] + ... + (n-1) * Bk[n-1]。

计算F(0), F(1), ..., F(n-1)中的最大值。

注意:
    可以认为 n 的值小于 10^5。

示例:
    A = [4, 3, 2, 6]

    F(0) = (0 * 4) + (1 * 3) + (2 * 2) + (3 * 6) = 0 + 3 + 4 + 18 = 25
    F(1) = (0 * 6) + (1 * 4) + (2 * 3) + (3 * 2) = 0 + 4 + 6 + 6 = 16
    F(2) = (0 * 2) + (1 * 6) + (2 * 4) + (3 * 3) = 0 + 6 + 8 + 9 = 23
    F(3) = (0 * 3) + (1 * 2) + (2 * 6) + (3 * 4) = 0 + 2 + 12 + 12 = 26

    所以 F(0), F(1), F(2), F(3) 中的最大值是 F(3) = 26 。

"""
from typing import List

class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        f = 0
        n = len(nums)
        for i in range(n):
            f += i * nums[i]    # 不旋转的 F(0)
        res = f
        numSum = sum(nums)
        for i in range(n - 1, -1, -1):                      # 用前一个F 减去最后一项与权重的积:(n-1) * nums[n-1]
            f = f + numSum - (n - 1) * nums[i] - nums[i]    # 再加上剩下每一项乘1: sum(nums) - num[n-1] 得到新的F
            res = max(f, res)
        return res

if __name__ == "__main__":
    A = [4, 3, 2, 6]
    sol = Solution()
    result = sol.maxRotateFunction(A)
    print (result)