"""
https://leetcode-cn.com/problems/maximum-erasure-value/

给你一个正整数数组 nums ，请你从中删除一个含有 若干不同元素 的子数组。删除子数组的 得分 就是子数组各元素之 和 。

返回 只删除一个 子数组可获得的 最大得分 。

如果数组 b 是数组 a 的一个连续子序列，即如果它等于 a[l],a[l+1],...,a[r] ，那么它就是 a 的一个子数组。

示例 1：
    输入：nums = [4,2,4,5,6]
    输出：17
    解释：最优子数组是 [2,4,5,6]

示例 2：
    输入：nums = [5,2,1,2,5,2,1,2,5]
    输出：8
    解释：最优子数组是 [5,2,1] 或 [1,2,5]

提示：
    1 <= nums.length <= 10^5
    1 <= nums[i] <= 10^4

给你一个正整数数组 nums ，求累加和最大的无重复元素的连续子数组，返回其累加和的值。

"""
from typing import List

""" 滑动窗口 """
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        max_sum = 0
        win_sum = 0                 # 需要维护的变量: 当前窗口元素和
        window = set()              # 本题涉及去重 (题目规定子数组不能有重复)，因此还需要一个集合
        L = 0                       # 定义窗口的首尾端 (L, R)
        for R in range(n):
            while window and nums[R] in window:     # 最右有重复元素时：右移左指针 L，
                window.remove(nums[L])              # 把最左元素移出集合
                win_sum -= nums[L]                  # 窗口元素和减去最左元素
                L += 1                              # 不断移动窗口左指针直到窗口再次合法（窗口无重复元素）
            window.add(nums[R])         # 最右的数字加入集合
            win_sum += nums[R]          # 最右的数字加入当前窗口元素和
            max_sum = max(max_sum, win_sum)     # 更新
        return max_sum

if __name__ == "__main__":
    nums = [5,2,1,2,5,2,1,2,5]
    sol = Solution()
    result = sol.maximumUniqueSubarray(nums)
    print(result)