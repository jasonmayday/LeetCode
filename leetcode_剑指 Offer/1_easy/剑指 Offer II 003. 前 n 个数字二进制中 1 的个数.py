"""
https://leetcode-cn.com/problems/w3tCBm/

给定一个非负整数 n ，请计算 0 到 n 之间的每个数字的二进制表示中 1 的个数，并输出一个数组。

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

进阶:
    给出时间复杂度为 O(n*sizeof(integer)) 的解答非常容易。但你可以在线性时间 O(n) 内用一趟扫描做到吗？
    要求算法的空间复杂度为 O(n) 。
    你能进一步完善解法吗？要求在C++或任何其他语言中不使用任何内置函数（如 C++ 中的 __builtin_popcount ）来执行此操作。

注意：本题与主站 338 题相同：https://leetcode-cn.com/problems/counting-bits/

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