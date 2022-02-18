"""
https://leetcode-cn.com/problems/shortest-unsorted-continuous-subarray/

给你一个整数数组 nums ，你需要找出一个 连续子数组 ，如果对这个子数组进行升序排序，那么整个数组都会变为升序排序。

请你找出符合题意的 最短 子数组，并输出它的长度。

示例 1：
    输入：nums = [2,6,4,8,10,9,15]
    输出：5
    解释：你只需要对 [6, 4, 8, 10, 9] 进行升序排序，那么整个表都会变为升序排序。

示例 2：
    输入：nums = [1,2,3,4]
    输出：0

示例 3：
    输入：nums = [1]
    输出：0

提示：
    1 <= nums.length <= 10^4
    -10^5 <= nums[i] <= 10^5

进阶：你可以设计一个时间复杂度为 O(n) 的解决方案吗？

"""
from typing import List

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        p1 = 0
        p2 = len(nums) - 1
        while p1 <= p2 and sorted_nums[p1] == nums[p1]:
            p1 += 1
        while p1 <= p2 and sorted_nums[p2] == nums[p2]:
            p2 -= 1
        return p2 - p1 + 1

""" 贪心算法 """
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        # 寻找连续子数组的终点
        m = -float('inf')
        end = -1            # 需要进行排序的 子数组的 终点下标
        print (list(enumerate(nums)))
        for i, num in enumerate(nums):  # 获取下标和数字
            if num > m:     # 如果遍历的数字大于 m
                m = num     # 说明 升序，不用排序，更新 m
            elif num < m:   # 遍历到的数字小于 m
                end = i     # 更新 end 下标，在遍历的过程中，end下标会不断更新和右移，直到最后一个不是升序的位置
        if end == -1:
            return 0
        print ("end index:", end)
        
        # 寻找连续子数组的起点
        m = float('inf')
        start = len(nums)   # 需要进行排序的 子数组的 起始下标
        for i in range(len(nums)-1,-1,-1):  # 从最后一位，倒序遍历  range(start, stop, step)
            if nums[i] < m:     # 如果遍历的数字小于 m
                m = nums[i]     # 说明 升序，不用排序，更新 m
            elif nums[i] > m:   # 遍历到的数字大于 m
                start = i       # 更新 start 下标
        print ("start index:", start)
        return (end - start + 1)


if __name__ == "__main__":
    nums = [2,6,4,8,10,9,15]
    sol = Solution()
    result = sol.findUnsortedSubarray(nums)
    print(result)