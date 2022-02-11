'''
https://leetcode-cn.com/problems/power-of-two/

给你一个整数 n，请你判断该整数是否是 2 的幂次方。如果是，返回 true ；否则，返回 false 。

如果存在一个整数 x 使得 n == 2^x ，则认为 n 是 2 的幂次方。

示例 1：
输入：n = 1
输出：true
解释：2^0 = 1

示例 2：
输入：n = 16
输出：true
解释：2^4 = 16

示例 3：
输入：n = 3
输出：false

示例 4：
输入：n = 4
输出：true

示例 5：
输入：n = 5
输出：false

提示：
-2 ^ 31 <= n <= 2 ^ 31 - 1

'''
# 在题目给定的 32 位有符号整数的范围内，最大的 2 的幂为 2 ^ 30 = 10737418242。
# 我们只需要判断 n 是否是 2^30 的约数即可。


class Solution:
    BIG = 2 ** 30
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and Solution.BIG % n == 0

if __name__ == "__main__":
    n = 512
    sol = Solution()
    result = sol.isPowerOfTwo(n)
    print(result)