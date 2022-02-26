"""
https://leetcode-cn.com/problems/minimum-size-subarray-sum/

给定一个含有 n 个正整数的数组和一个正整数 target 。

找出该数组中满足其和 ≥ target 的长度最小的 连续子数组 [numsl, numsl+1, ..., numsr-1, numsr] ，并返回其长度。如果不存在符合条件的子数组，返回 0 。

示例 1：
    输入：target = 7, nums = [2,3,1,2,4,3]
    输出：2
    解释：子数组 [4,3] 是该条件下的长度最小的子数组。

示例 2：
    输入：target = 4, nums = [1,4,4]
    输出：1

示例 3：
    输入：target = 11, nums = [1,1,1,1,1,1,1,1]
    输出：0

提示：
    1 <= target <= 10^9
    1 <= nums.length <= 10^5
    1 <= nums[i] <= 10^5

"""
from typing import List

""" 滑动窗口 """
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if not nums:
            return 0
        length = len(nums)
        ans = length + 1
        start, end = 0, 0   # 定义两个指针 start 和 end 分别表示子数组（滑动窗口窗口）的开始位置和结束位置
        total = 0
        while end < length:         # end 不断右移遍历
            total += nums[end]      # 加上 end 指针的数字
            while total >= target:  # 直到总和 大于等于 目标值
                ans = min(ans, end - start + 1) # 计算数组长度，更新答案
                total -= nums[start]            # 总和减去最左边的数字
                start += 1                      # start 指针右移
            end += 1                # 直到总和小于 tartget，然后右指针再右移
        
        return 0 if ans == length + 1 else ans


""" 滑动窗口 """
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if not nums:
            return 0
        left = 0
        cur = 0
        res = float("inf")
        for right in range(len(nums)):
            cur += nums[right]
            while cur >= s:
                res = min(res, right - left + 1)
                cur -= nums[left]
                left += 1
        return res if res != float("inf") else 0
    
    
if __name__ == "__main__":
    target = 7
    nums = [2,3,1,2,4,3]
    sol = Solution()
    result = sol.minSubArrayLen(target, nums)
    print (result)