"""
https://leetcode.cn/problems/find-closest-number-to-zero/

给你一个长度为 n 的整数数组 nums ，请你返回 nums 中最 接近 0 的数字。如果有多个答案，请你返回它们中的 最大值 。

示例 1：
    输入：nums = [-4,-2,1,4,8]
    输出：1
    解释：
        -4 到 0 的距离为 |-4| = 4 。
        -2 到 0 的距离为 |-2| = 2 。
        1 到 0 的距离为 |1| = 1 。
        4 到 0 的距离为 |4| = 4 。
        8 到 0 的距离为 |8| = 8 。
        所以，数组中距离 0 最近的数字为 1 。

示例 2：
    输入：nums = [2,-1,1]
    输出：1
    解释：1 和 -1 都是距离 0 最近的数字，所以返回较大值 1 。

提示：
    1 <= n <= 1000
    -10^5 <= nums[i] <= 10^5

"""

from typing import List

"""方法1：遍历"""
class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        res = nums[0]   # 已遍历元素中绝对值最小且数值最大的元素
        dis = abs(nums[0])   # 已遍历元素的最小绝对值
        for num in nums:
            if abs(num) < dis:  # 第一种情况
                dis = abs(num)  # 此时我们需要将 res 更新为 num，
                res = num       # 并将 dis 更新为 ∣num∣
            elif abs(num) == dis:
                res = max(res, num)
        return res
    
"""方法2：排序"""
class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        nums.sort(key=lambda x: [abs(x), -x])   # 按照“绝对值升序，值本身降序”进行二次排序，第一个元素就是答案
        return nums[0]

if __name__ == "__main__":
    nums = [-4,-2,1,4,8]
    sol = Solution()
    result = sol.findClosestNumber(nums)
    print (result)