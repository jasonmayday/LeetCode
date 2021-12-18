"""
https://leetcode-cn.com/problems/super-pow/

你的任务是计算 ab 对 1337 取模，a 是一个正整数，b 是一个非常大的正整数且会以数组形式给出。

示例 1：
    输入：a = 2, b = [3]
    输出：8

示例 2：
    输入：a = 2, b = [1,0]
    输出：1024

示例 3：
    输入：a = 1, b = [4,3,3,8,5,2]
    输出：1

示例 4：
    输入：a = 2147483647, b = [2,0,0]
    输出：1198

提示：
    1 <= a <= 231 - 1
    1 <= b.length <= 2000
    0 <= b[i] <= 9
    b 不含前导 0

"""
from typing import List

""" 因为python的int可以无限扩容所以可以认为不会溢出，但是因为指数和底数太大，单纯使用幂运算再取模也会超时。
    可以使用内置的pow函数加上模参数，pow函数会为我们优化运算过程"""
class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        return pow(a,int("".join(map(str,b))),1337)

if __name__ == "__main__":
    a = 2147483647
    b = [2,0,0]
    sol = Solution()
    result = sol.superPow(a,b)
    print (result) 