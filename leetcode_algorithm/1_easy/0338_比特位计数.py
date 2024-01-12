"""
https://leetcode-cn.com/problems/counting-bits/

给你一个整数 n ，对于 0 <= i <= n 中的每个 i ，计算其二进制表示中 1 的个数 ，返回一个长度为 n + 1 的数组 ans 作为答案。

示例 1：
    输入：n = 2
    输出：[0,1,1]
    解释：
    0 --> 0
    1 --> 1
    2 --> 10

示例 2：
    输入：n = 5
    输出：[0,1,1,2,1,2]
    解释：
    0 --> 0
    1 --> 1
    2 --> 10
    3 --> 11
    4 --> 100
    5 --> 101

提示：
    0 <= n <= 10^5

进阶：
    很容易就能实现时间复杂度为 O(n log n) 的解决方案，你可以在线性时间复杂度 O(n) 内用一趟扫描解决此问题吗？
    你能不使用任何内置函数解决此问题吗？（如，C++ 中的 __builtin_popcount ）

"""
# https://leetcode-cn.com/problems/counting-bits/solution/yi-bu-bu-fen-xi-tui-dao-chu-dong-tai-gui-3yog/

from typing import List

''' 方法1：遍历 与 统计'''
class Solution:
    def countBits(self, num: int) -> List[int]:
        res = []
        for i in range(num + 1):
            res.append(bin(i).count("1"))
        return res

''' 方法2：递归'''
class Solution(object):
    def countBits(self, num):
        res = []
        for i in range(num + 1):
            res.append(self.count(i))
        return res
    
    def count(self, num):
        if num == 0:
            return 0
        if num % 2 == 1:
            return self.count(num - 1) + 1
        return self.count(num // 2)

""" 方法3：动态规划——最低有效位"""
class Solution:
    def countBits(self, n: int) -> List[int]:
        bits = [0]
        for i in range(1, n + 1):
            bits.append(bits[i >> 1] + (i & 1))
        return bits

""" 方法4：动态规划——最低设置位"""
class Solution:
    def countBits(self, n: int) -> List[int]:
        bits = [0]
        for i in range(1, n + 1):
            bits.append(bits[i & (i - 1)] + 1)
        return bits

if __name__ == "__main__":
    n = 10000
    sol = Solution()
    result = sol.countBits(n)
    print (result)