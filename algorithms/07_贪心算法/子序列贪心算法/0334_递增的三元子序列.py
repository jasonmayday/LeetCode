"""
https://leetcode-cn.com/problems/increasing-triplet-subsequence/

给你一个整数数组 nums ，判断这个数组中是否存在长度为 3 的递增子序列。

如果存在这样的三元组下标 (i, j, k) 且满足 i < j < k ，使得 nums[i] < nums[j] < nums[k] ，返回 true ；否则，返回 false 。

示例 1：
    输入：nums = [1,2,3,4,5]
    输出：true
    解释：任何 i < j < k 的三元组都满足题意

示例 2：
    输入：nums = [5,4,3,2,1]
    输出：false
    解释：不存在满足题意的三元组

示例 3：
    输入：nums = [2,1,5,0,4,6]
    输出：true
    解释：三元组 (3, 4, 5) 满足题意，因为 nums[3] == 0 < nums[4] == 4 < nums[5] == 6

提示：
    1 <= nums.length <= 5 * 10^5
    -2^31 <= nums[i] <= 2^31 - 1

进阶：你能实现时间复杂度为 O(n) ，空间复杂度为 O(1) 的解决方案吗？

"""
from typing import List

""" 贪心算法 """
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 3:
            return False
        first = nums[0]         # first  表示递增的三元子序列中的第 1 个数
        second = float('inf')   # second 表示递增的三元子序列中的第 2 个数，任何时候都有 first < second
        for i in range(1, n):
            num = nums[i]       # 当遍历到下标 i 时，令 num = nums[i]
            if num > second:    # 如果 num > second，则找到了一个递增的三元子序列，返回 true
                return True
            if num > first:     # 如果 num 比 second 小，但是比 first 大，则将 second 的值更新为 num
                second = num
            else:               # 如果 num 比 first 还小
                first = num     # 将first 的值更新为 num。
        return False    # 如果遍历结束时没有找到递增的三元子序列，返回 False

if __name__ == '__main__':
    nums = [2,1,5,0,4,6]
    sol = Solution()
    result = sol.increasingTriplet(nums)
    print (result)