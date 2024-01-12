"""
https://leetcode-cn.com/problems/max-consecutive-ones-iii/

给定一个二进制数组 nums 和一个整数 k ，如果可以翻转最多k 个 0 ，则返回 数组中连续 1 的最大个数 。

示例 1：
    输入：nums = [1,1,1,0,0,0,1,1,1,1,0], K = 2
    输出：6
    解释：[1,1,1,0,0,1,1,1,1,1,1]
    粗体数字从 0 翻转到 1，最长的子数组长度为 6。

示例 2：
    输入：nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], K = 3
    输出：10
    解释：[0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
    粗体数字从 0 翻转到 1，最长的子数组长度为 10。

提示：
    1 <= nums.length <= 10^5
    nums[i] 不是 0 就是 1
    0 <= k <= nums.length

"""
from typing import List

""" 滑动窗口 """
class Solution(object):
    def longestOnes(self, nums, K):
        n = len(nums)
        res = 0
        left, right = 0, 0
        zeros = 0
        while right < n:
            if nums[right] == 0:
                zeros += 1
            while zeros > K:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            res = max(res, right - left + 1)
            right += 1
        return res

if __name__ == "__main__":
    nums = [1,1,1,0,0,0,1,1,1,1,0]
    k = 2
    sol = Solution()
    result = sol.longestOnes(nums, k)
    print(result)