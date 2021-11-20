"""
https://leetcode-cn.com/problems/maximum-product-of-three-numbers/

给你一个整型数组 nums ，在数组中找出由三个数组成的最大乘积，并输出这个乘积。

示例 1：
    输入：nums = [1,2,3]
    输出：6

示例 2：
    输入：nums = [1,2,3,4]
    输出：24

示例 3：
    输入：nums = [-1,-2,-3]
    输出：-6

提示：
3 <= nums.length <= 10^4
-1000 <= nums[i] <= 1000

"""
from typing import List

class Solution:
    def maximumProduct1(self, nums: List[int]) -> int:
        nums.sort()
        a = nums[-1] * nums[-2] * nums[-3]  #  4, 1, 0  # 如果全为正数或全为负数，最大三个数的乘积为a
        b = nums[0] * nums[1] * nums[-1]    # -4,-3, 4  # 如果存在两个以上负数，两个最小负数与最大正数的乘积 b
        return max(a, b)

if __name__ == "__main__":
    nums = [-4,-3,-2,-1,0,1,4]
    sol = Solution()
    result = sol.maximumProduct1(nums)
    print(result)