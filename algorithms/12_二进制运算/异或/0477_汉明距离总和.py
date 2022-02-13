"""
https://leetcode-cn.com/problems/total-hamming-distance/

两个整数的 汉明距离 指的是这两个数字的二进制数对应位不同的数量。

给你一个整数数组 nums，请你计算并返回 nums 中任意两个数之间 汉明距离的总和 。

示例 1：
    输入：nums = [4,14,2]
    输出：6
    解释：在二进制表示中，4 表示为 0100 ，14 表示为 1110 ，2表示为 0010 。（这样表示是为了体现后四位之间关系）
        所以答案为：
        HammingDistance(4, 14) + HammingDistance(4, 2) + HammingDistance(14, 2) = 2 + 2 + 2 = 6

示例 2：
    输入：nums = [4,14,4]
    输出：4

提示：
    1 <= nums.length <= 10^4
    0 <= nums[i] <= 10^9
    给定输入的对应答案符合 32-bit 整数范围

"""
from typing import List
from collections import Counter

"""统计每一位有多少个0，有多少个1"""
class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        trie = Counter()
        max_bit = len(bin(max(nums))) - 2   
        ans = 0
        for i, num in enumerate(nums):
            for j in range(max_bit):
                bit = (num >> j) & 1
                if bit:
                    ans += i - trie[j]
                    trie[j] += 1
                else:
                    ans += trie[j]
        return ans

""" 需要找出单个bit位上，有0和1不同的，才可以算汉明距离；
    假设单个bit位上，1的数量为num1，则0的数量为n - num1，总汉明距离为num1 * (n - num1);
"""
class Solution:
    def totalHammingDistance(self, nums):
        res = 0
        n = len(nums)
        for i in range(30):
            num1 = sum((val >> i) & 1 for val in nums)
            res += num1 * (n - num1)
        return res

    
if __name__ == "__main__":
    nums = [4,14,2]     # 0100, 1110, 0010
    sol = Solution()
    result = sol.totalHammingDistance(nums)
    print (result) 
