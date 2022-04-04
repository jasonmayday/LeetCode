'''
https://leetcode-cn.com/problems/prime-number-of-set-bits-in-binary-representation/

给定两个整数 L 和 R ，找到闭区间 [L, R] 范围内，计算置位位数为质数的整数个数。

（注意，计算置位代表二进制表示中1的个数。例如 21 的二进制表示 10101 有 3 个计算置位。还有，1 不是质数。）

示例 1:
    输入: L = 6, R = 10
    输出: 4
    解释:
        6 -> 110 (2 个计算置位，2 是质数)
        7 -> 111 (3 个计算置位，3 是质数)
        9 -> 1001 (2 个计算置位，2 是质数)
        10-> 1010 (2 个计算置位，2 是质数)

示例 2:
    输入: L = 10, R = 15
    输出: 5
    解释:
        10 -> 1010 (2 个计算置位, 2 是质数)
        11 -> 1011 (3 个计算置位, 3 是质数)
        12 -> 1100 (2 个计算置位, 2 是质数)
        13 -> 1101 (3 个计算置位, 3 是质数)
        14 -> 1110 (3 个计算置位, 3 是质数)
        15 -> 1111 (4 个计算置位, 4 不是质数)

注意:
    L, R 是 L <= R 且在 [1, 10^6] 中的整数。
    R - L 的最大值为 10000。

'''

""" 方法一：数学 + 位运算"""
class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        prime = [2,3,5,7,11,13,17,19]  # 大概找到2^20以内的 即20以内的素数即可，要求1 <= left <= right <= 10^6
        def count(num): # 位运算计算二进制表示中 1 的个数
            cnt = 0
            while num > 0:
                if num & 1:
                    cnt += 1
                num >>= 1
            return cnt
        # 遍历求结果
        res = 0
        for i in range(left, right + 1):
            if count(i) in prime:
                res += 1
        return res

""" 方法二 """
class Solution:
    def isPrime(self, x: int) -> bool:
        if x < 2:
            return False
        i = 2
        while i * i <= x:
            if x % i == 0:
                return False
            i += 1
        return True

    def countPrimeSetBits(self, left: int, right: int) -> int:
        return sum(self.isPrime(bin(x).count("1")) for x in range(left, right + 1))

class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        ans = 0
        for i in range(left, right + 1):
            if bin(i).count('1') in [2, 3, 5, 7, 11, 13, 17, 19]:   # 计算该数字转换为二进制有多少个 1。如果数量是 2, 3, 5, 7, 11, 13, 17, 19，则我们增加质数的计数
                ans += 1                                            # 10^6 的二进制数字最多20个位，所以考虑20以内的质数即可。
        return ans

if __name__ == "__main__":
    left = 1
    right = 9999
    sol = Solution()
    result = sol.countPrimeSetBits(left, right)
    print(result)