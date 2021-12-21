"""
https://leetcode-cn.com/problems/find-greatest-common-divisor-of-array/

给你一个整数数组 nums ，返回数组中最大数和最小数的 最大公约数 。

两个数的 最大公约数 是能够被两个数整除的最大正整数。

示例 1：
    输入：nums = [2,5,6,9,10]
    输出：2
    解释：
    nums 中最小的数是 2
    nums 中最大的数是 10
    2 和 10 的最大公约数是 2

示例 2：
    输入：nums = [7,5,6,8,3]
    输出：1
    解释：
    nums 中最小的数是 3
    nums 中最大的数是 8
    3 和 8 的最大公约数是 1

示例 3：
    输入：nums = [3,3]
    输出：3
    解释：
    nums 中最小的数是 3
    nums 中最大的数是 3
    3 和 3 的最大公约数是 3

提示：
    2 <= nums.length <= 1000
    1 <= nums[i] <= 1000

"""
from typing import List
import math

"""方法1：调库"""
class Solution:
    def findGCD(self, nums: List[int]) -> int:
        mx = max(nums)
        mn = min(nums)
        return math.gcd(mx, mn)
    
"""方法2：手写gcd"""
class Solution:
    def findGCD(self, nums: List[int]) -> int:
        mx = max(nums)
        mn = min(nums)
        if mx % mn == 0: return mn
        for i in range(mn - 1, 0, -1):
            if mx % i == 0 and mn % i == 0:
                return i
        return 1

if __name__ == "__main__":
    nums = [2,5,6,9,10]
    sol = Solution()
    result = sol.findGCD(nums)
    print (result)