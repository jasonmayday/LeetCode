'''
https://leetcode-cn.com/problems/single-number/

给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

说明：

你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？

示例 1:
输入: [2,2,1]
输出: 1

示例 2:
输入: [4,1,2,1,2]
输出: 4

'''
from typing import List
from functools import reduce

""" 异或运算
    异或交换律：a ^ b ^ c <=> a ^ c ^ b
    任何数于0异或为任何数 0 ^ n => n
    相同的数异或为0: n ^ n => 0
    a = [2,3,2,4,4]
    2 ^ 3 ^ 2 ^ 4 ^ 4 = 2 ^ 2 ^ 4 ^ 4 ^ 3 => 0 ^ 0 ^ 3 => 3
"""
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return reduce(lambda x, y: x ^ y, nums)

if __name__ == "__main__":
    nums = [2,2,1]
    sol = Solution()
    result = sol.singleNumber(nums)
    print(result)