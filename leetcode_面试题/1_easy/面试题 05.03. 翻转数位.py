"""
https://leetcode-cn.com/problems/reverse-bits-lcci/

给定一个32位整数 num，你可以将一个数位从0变为1。请编写一个程序，找出你能够获得的最长的一串1的长度。

示例 1：
    输入: num = 1775(110111011112)
    输出: 8

示例 2：
    输入: num = 7(01112)
    输出: 4

"""

""" 动态规划 + 位运算 """
class Solution(object):
    def reverseBits(self, num):
        cur = 0     # cur：当前位置为止连续1的个数，遇到0归零，遇到1加1
        insert = 0  # insert：在当前位置变成1，往前数连续1的最大个数，遇到0变为cur+1，遇到1加1
        res = 1     # res:保存insert的最大值即可
        for i in range(32):
            if num & (1 << i):
                cur += 1
                insert +=1
            else:
                insert = cur + 1
                cur = 0
            res = max(res, insert)
        return res

""" 双指针 + 位运算 """
class Solution:
    def reverseBits(self, num: int) -> int:
        pre = 0     # pre表示上一个连续1的长度+1
        cur = 0     # cur表示当前连续1的长度
        res = 1     # 结果即为最大的pre+cur
        for i in range(32):
            if num & (1 << i):
                cur += 1
            else:
                res = max(res, pre + cur)
                pre = cur + 1
                cur = 0
        res = max(res, pre + cur)
        return res

if __name__ == "__main__":
    num = 1775
    sol = Solution()
    result = sol.reverseBits(num)
    print(result)