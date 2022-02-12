'''
https://leetcode-cn.com/problems/missing-number/

给定一个包含 [0, n] 中 n 个数的数组 nums ，找出 [0, n] 这个范围内没有出现在数组中的那个数。

示例 1：
    输入：nums = [3,0,1]
    输出：2
    解释：n = 3，因为有 3 个数字，所以所有的数字都在范围 [0,3] 内。2 是丢失的数字，因为它没有出现在 nums 中。

示例 2：
    输入：nums = [0,1]
    输出：2
    解释：n = 2，因为有 2 个数字，所以所有的数字都在范围 [0,2] 内。2 是丢失的数字，因为它没有出现在 nums 中。

示例 3：
    输入：nums = [9,6,4,2,3,5,7,0,1]
    输出：8
    解释：n = 9，因为有 9 个数字，所以所有的数字都在范围 [0,9] 内。8 是丢失的数字，因为它没有出现在 nums 中。

示例 4：
    输入：nums = [0]
    输出：1
    解释：n = 1，因为有 1 个数字，所以所有的数字都在范围 [0,1] 内。1 是丢失的数字，因为它没有出现在 nums 中。

提示：
    n == nums.length
    1 <= n <= 10^4
    0 <= nums[i] <= n
    nums 中的所有数字都 独一无二

'''
from typing import List

""" 解法：位运算(异或)
    x ^ x = 0 和 x ^ 0 = x """
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        xor = 0
        print (list(enumerate(nums)))
        for i, num in enumerate(nums):  # (0, 3), (1, 0), (2, 1)
            xor = xor ^ i ^ num         # 利用 a ^ b ^ b = a
        return xor ^ len(nums)


if __name__ == "__main__":
    nums = [3,0,1]
    sol = Solution()
    result = sol.missingNumber(nums)
    print (result) 