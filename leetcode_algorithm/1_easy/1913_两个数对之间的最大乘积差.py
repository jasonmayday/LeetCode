"""
https://leetcode-cn.com/problems/maximum-product-difference-between-two-pairs/

两个数对 (a, b) 和 (c, d) 之间的 乘积差 定义为 (a * b) - (c * d) 。
    例如，(5, 6) 和 (2, 7) 之间的乘积差是 (5 * 6) - (2 * 7) = 16 。

给你一个整数数组 nums ，选出四个 不同的 下标 w、x、y 和 z ，使数对 (nums[w], nums[x]) 和 (nums[y], nums[z]) 之间的 乘积差 取到 最大值 。

返回以这种方式取得的乘积差中的 最大值 。

示例 1：
    输入：nums = [5,6,2,7,4]
    输出：34
    解释：可以选出下标为 1 和 3 的元素构成第一个数对 (6, 7) 以及下标 2 和 4 构成第二个数对 (2, 4)
    乘积差是 (6 * 7) - (2 * 4) = 34

示例 2：
    输入：nums = [4,2,5,9,7,4,8]
    输出：64
    解释：可以选出下标为 3 和 6 的元素构成第一个数对 (9, 8) 以及下标 1 和 5 构成第二个数对 (2, 4)
    乘积差是 (9 * 8) - (2 * 4) = 64

提示：
    4 <= nums.length <= 10^4
    1 <= nums[i] <= 10^4

"""
from typing import List

class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        n = len(nums)
        max1, max2 = max(nums[0], nums[1]), min(nums[0], nums[1]) # 数组中最大的两个值
        min1, min2 = min(nums[0], nums[1]), max(nums[0], nums[1]) # 数组中最小的两个值
        for i in range(2, n):
            tmp = nums[i]
            if tmp > max1:
                max1, max2 = tmp, max1
            elif tmp > max2:
                max2 = tmp
            if tmp < min1:
                min1, min2 = tmp, min1
            elif tmp < min2:
                min2 = tmp
        return (max1 * max2) - (min1 * min2)

class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort()                 # 2,4,4,5,7,8,9
        a, b = nums[0], nums[1]     # 最小的两个数，(2,4)
        c, d = nums[-2], nums[-1]   # 最大的两个数，(8,9)
        return c * d - a * b        # 最大的两个数的乘积 减去 最小的两个数的乘积

if __name__ == "__main__":
    nums = [4,2,5,9,7,4,8]
    sol = Solution()
    result = sol.maxProductDifference(nums)
    print (result)  