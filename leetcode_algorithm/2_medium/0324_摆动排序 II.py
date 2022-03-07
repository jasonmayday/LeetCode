"""
https://leetcode-cn.com/problems/wiggle-sort-ii/

给你一个整数数组 nums，将它重新排列成 nums[0] < nums[1] > nums[2] < nums[3]... 的顺序。

你可以假设所有输入数组都可以得到满足题目要求的结果。

示例 1：
    输入：nums = [1,5,1,1,6,4]
    输出：[1,6,1,5,1,4]
    解释：[1,4,1,5,1,6] 同样是符合题目要求的结果，可以被判题程序接受。

示例 2：
    输入：nums = [1,3,2,2,3,1]
    输出：[2,3,1,3,1,2]

提示：
    1 <= nums.length <= 5 * 10^4
    0 <= nums[i] <= 5000
    题目数据保证，对于给定的输入 nums ，总能产生满足题目要求的结果

进阶：你能用 O(n) 时间复杂度和 / 或原地 O(1) 额外空间来实现吗？

"""
class Solution:
    def wiggleSort(self, nums):
        nums.sort()                 # nums:  [1, 2, 3, 4, 5, 6]
        s = len(nums)-len(nums)//2  # s = 3
        a = nums[:s][::-1]  # a:  [3, 2, 1]
        b = nums[s:][::-1]  # b:  [6, 5, 4]
        nums.clear()
        for i in range(s):      # 前半部分
            nums.append(a[i])
            if i < len(b):      # 后半部分
                nums.append(b[i])
        return nums # [3, 6, 2, 5, 1, 4]

class Solution:
    def wiggleSort(self, nums):
        nums.sort()             # nums:  [1, 1, 1, 4, 5, 6]
        half = len(nums[::2])   # half:  3
        nums[::2], nums[1::2] = nums[:half][::-1], nums[half:][::-1]
        return nums

if __name__ == "__main__":
    nums = [1,5,3,2,6,4]
    sol = Solution()
    result = sol.wiggleSort(nums)
    print (result)
