"""
https://leetcode-cn.com/problems/minimum-value-to-get-positive-step-by-step-sum/

给你一个整数数组 nums 。你可以选定任意的 正数 startValue 作为初始值。

你需要从左到右遍历 nums 数组，并将 startValue 依次累加上 nums 数组中的值。

请你在确保累加和始终大于等于 1 的前提下，选出一个最小的 正数 作为 startValue 。

示例 1：
    输入：nums = [-3,2,-3,4,2]
    输出：5
    解释：如果你选择 startValue = 4，在第三次累加时，和小于 1 。
                    累加求和
                    startValue = 4 | startValue = 5 | nums
                      (4 -3 ) = 1  | (5 -3 ) = 2    |  -3
                      (1 +2 ) = 3  | (2 +2 ) = 4    |   2
                      (3 -3 ) = 0  | (4 -3 ) = 1    |  -3
                      (0 +4 ) = 4  | (1 +4 ) = 5    |   4
                      (4 +2 ) = 6  | (5 +2 ) = 7    |   2

示例 2：
    输入：nums = [1,2]
    输出：1
    解释：最小的 startValue 需要是正数。

示例 3：
    输入：nums = [1,-2,-3]
    输出：5

提示：
    1 <= nums.length <= 100
    -100 <= nums[i] <= 100

"""
from typing import List
from itertools import accumulate

class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        return max(-min(accumulate(nums)), 0) + 1

"""动态规划"""
class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        for i in range(len(nums)):  # 逐步求和的过程中一定存在一个最小值，利用DP求出最小值；
            if i:
                nums[i] += nums[i-1]
        if min(nums) >= 0:          # 若最小值大于等于0，则返回 1
            return 1
        else:
            return abs(min(nums)) + 1   # 否则返回（相反数+1）

"""一次遍历"""
class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        startvalue = 1          # 设初始值为startvalue = 1
        sum_nums = startvalue   # 当前的累加和即为sum_nums = startvalue；
        for num in nums:        # 从第一个值开始遍历
            sum_nums += num     # 如果当前累加和 >= 1， 继续遍历
            if sum_nums < 1:    # 如果累加和 < 1
                startvalue += (1 - sum_nums)  # 则将初始值startvalue提高 1-sum_nums
                sum_nums = 1
        return startvalue       # 此时的累加和便为1

if __name__ == "__main__":
    nums = [-3,2,-3,4,2]
    sol = Solution()
    result = sol.minStartValue(nums)
    print(result)