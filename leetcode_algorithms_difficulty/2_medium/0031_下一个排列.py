"""
https://leetcode-cn.com/problems/next-permutation/

实现获取 下一个排列 的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列（即，组合出下一个更大的整数）。

如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。

必须 原地 修改，只允许使用额外常数空间。

示例 1：
    输入：nums = [1,2,3]
    输出：[1,3,2]

示例 2：
    输入：nums = [3,2,1]
    输出：[1,2,3]

示例 3：
    输入：nums = [1,1,5]
    输出：[1,5,1]

示例 4：
    输入：nums = [1]
    输出：[1]

提示：
    1 <= nums.length <= 100
    0 <= nums[i] <= 100

"""
from typing import List

""" 方法一：两遍扫描
    1. 我们需要将一个左边的「较小数」与一个右边的「较大数」交换，以能够让当前排列变大，从而得到下一个排列。
    2. 同时我们要让这个「较小数」尽量靠右，而「较大数」尽可能小。
    3. 当交换完成后，「较大数」右边的数需要按照升序重新排列。这样可以在保证新排列大于原来排列的情况下，使变大的幅度尽可能小。"""
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        i = len(nums) - 2                           # i 初始为倒数第 2 位
        while i >= 0 and nums[i] >= nums[i + 1]:    # 【先满足条件1】：首先从后向前查找第一个顺序对 (i,i+1)，满足 a[i] < a[i+1]
            i -= 1                                  # 如果左边比右边大，i 向左移动一位，直到找到 nums[i] < nums[i+1]
        if i >= 0:                  # 如果找到了顺序对，【下一步要满足条件2】：
            j = len(nums) - 1       # 那么在区间 [i+1,n) 中从后向前查找第一个元素 j 满足 a[i] < a[j]
            while j >= 0 and nums[i] >= nums[j]:    # 如果 i 比 j 大，
                j -= 1                              # j 向左移动一位，直到找到 nums[i] < nums[j]。这样「较大数」即为 a[j]
            nums[i], nums[j] = nums[j], nums[i]     # 交换 a[i] 与 a[j]
        # 此时可以证明区间 [i+1,n) 必为降序。
        left = i + 1
        right = len(nums) - 1
        while left < right:                                     # 【为了满足条件3】：
            nums[left], nums[right] = nums[right], nums[left]   # 我们可以直接使用双指针反转区间 [i+1,n) 使其变为升序
            left += 1
            right -= 1
        return nums

if __name__ == "__main__":
    nums = [4,5,2,6,3,1]
    sol = Solution()
    result = sol.nextPermutation(nums)
    print (result)