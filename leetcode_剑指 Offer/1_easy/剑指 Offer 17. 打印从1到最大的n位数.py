"""
https://leetcode-cn.com/problems/da-yin-cong-1dao-zui-da-de-nwei-shu-lcof/

输入数字 n，按顺序打印出从 1 到最大的 n 位十进制数。比如输入 3，则打印出 1、2、3 一直到最大的 3 位数 999。

示例 1:
    输入: n = 1
    输出: [1,2,3,4,5,6,7,8,9]

说明：
    用返回一个整数列表来代替打印
    n 为正整数

"""
from typing import List

""" 模拟 """
class Solution:
    def printNumbers(self, n: int) -> List[int]:
        res = []
        for i in range(1, 10 ** n):
            res.append(i)
        return res

""" 大数打印解法 
    基于分治算法的思想，先固定高位，向低位递归，当个位已被固定时，添加数字的字符串。
    例如当 n=2 时（数字范围 1−99 ），固定十位为 0 - 9 ，按顺序依次开启递归，固定个位 0 - 9 ，终止递归并添加数字字符串。
"""
class Solution:
    def printNumbers(self, n: int) -> List[int]:
        def dfs(x):
            if x == n:  # 终止条件：已固定完所有位
                s = ''.join(num[self.start:])
                if s != '0':
                    res.append(int(s)) # 拼接 num 并添加至 res 尾部
                if n - self.start == self.nine: # 当输出数字的所有位都是 9 时
                    self.start -= 1             # 则下个数字需要向更高位进 1 ，此时左边界 start 需要减 1
                return
            for i in range(10): # 遍历 0 - 9
                if i == 9:          # 统计 nine 的方法： 固定第 x 位时，当 i=9 则执行 nine=nine+1
                    self.nine += 1
                num[x] = str(i) # 固定第 x 位为 i
                dfs(x + 1)      # 开启固定第 x + 1 位
            self.nine -= 1  # 在回溯前恢复 nine=nine−1 。
        
        num = ['0'] * n # 起始数字定义为 n 个 0 组成的字符列表
        res = []        # 数字字符串列表
        self.nine = 0
        self.start = n - 1
        dfs(0)          # 开启全排列递归
        return res      # 拼接所有数字字符串，使用逗号隔开，并返回

if __name__ == "__main__":
    n = 9
    sol = Solution()
    result = sol.printNumbers(n)
    print (result)