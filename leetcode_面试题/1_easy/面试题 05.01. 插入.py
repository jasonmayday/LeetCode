"""
https://leetcode-cn.com/problems/insert-into-bits-lcci/

给定两个整型数字 N 与 M，以及表示比特位置的 i 与 j（i <= j，且从 0 位开始计算）。

编写一种方法，使 M 对应的二进制数字插入 N 对应的二进制数字的第 i ~ j 位区域，不足之处用 0 补齐。具体插入过程如图所示。

题目保证从 i 位到 j 位足以容纳 M， 例如： M = 10011，则 i～j 区域至少可容纳 5 位。

示例1:
    输入：N = 1024(10000000000), M = 19(10011), i = 2, j = 6
    输出：N = 1100(10001001100)

示例2:
    输入： N = 0, M = 31(11111), i = 0, j = 4
    输出：N = 31(11111)

"""

class Solution:
    def insertBits(self, N: int, M: int, i: int, j: int) -> int:
        # 将 n 的 i - j 位变为 0
        for k in range(i, j + 1):
            N &= ~(1 << k)
        # 将 m 左移 i 位 ,与 n 做或运算,等价于将 m 插入 i - j 位
        return N | (M << i)

if __name__ == "__main__":
    N = 1024
    M = 19
    i = 2
    j = 6
    sol = Solution()
    result = sol.insertBits(N, M, i, j)
    print(result)