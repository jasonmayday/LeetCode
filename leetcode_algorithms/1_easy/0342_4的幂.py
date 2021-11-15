"""
https://leetcode-cn.com/problems/power-of-four/

给定一个整数，写一个函数来判断它是否是 4 的幂次方。如果是，返回 true ；否则，返回 false 。

整数 n 是 4 的幂次方需满足：存在整数 x 使得 n == 4x

示例 1：
    输入：n = 16
    输出：true

示例 2：
    输入：n = 5
    输出：false

示例 3：
    输入：n = 1
    输出：true

提示：
-2^31 <= n <= 2^31 - 1

进阶：
    你能不使用循环或者递归来完成本题吗？

"""

'''基础循环'''
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n==2 or n==3:
            return False
        while(n>=4):
            if n%4 != 0:
                return False
            else:
                n /= 4
        if n != 1:
            return False
        else:
            return True

'''基础循环'''
class Solution:
    def isPowerOfFour(self, n):
        mi = 0
        while 4 ** mi <= n:
            if n == 4 ** mi:
                return True
            mi += 1
        return False

'''取模性质'''
class Solution:
    def isPowerOfFour(self, n):
        return n > 0 and (n & (n-1)) == 0 and n % 3 == 1

if __name__ == "__main__":
    n = 4294967296
    sol = Solution()
    result = sol.isPowerOfFour(n)
    print (result)