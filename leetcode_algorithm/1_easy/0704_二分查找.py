'''
https://leetcode-cn.com/problems/binary-search/

给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target  ，
写一个函数搜索 nums 中的 target，如果目标值存在返回下标，否则返回 -1。

示例 1:
    输入: nums = [-1,0,3,5,9,12], target = 9
    输出: 4
    解释: 9 出现在 nums 中并且下标为 4

示例 2:
    输入: nums = [-1,0,3,5,9,12], target = 2
    输出: -1
    解释: 2 不存在 nums 中因此返回 -1

'''

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0                 # 最小数下标
        high = len(nums) - 1    # 最大数下标
        while low <= high:      # 要使用 <= ，因为left == right是有意义的
            mid = (high - low) // 2 + low    # 中间数下标
            # use mid = (high - low) // 2 + low instead of (low + high) // 2 because it avoid overflow
            mid_num = nums[mid]
            if mid_num == target:   # 如果中间数下标等于target, 返回
                return mid
            elif mid_num > target:  # 如果target在中间数左边, 移动high下标
                high = mid - 1
            else:                   # 如果target在中间数右边, 移动low下标
                low = mid + 1
        return -1

if __name__ == "__main__":
    nums = [-1,0,3,5,9,12]
    target = 9
    sol = Solution()
    result = sol.search(nums,target)
    print(result)