"""
https://leetcode-cn.com/problems/find-the-duplicate-number/

给定一个包含 n + 1 个整数的数组 nums ，其数字都在 [1, n] 范围内（包括 1 和 n），可知至少存在一个重复的整数。

假设 nums 只有 一个重复的整数 ，返回 这个重复的数 。

你设计的解决方案必须 不修改 数组 nums 且只用常量级 O(1) 的额外空间。

示例 1：
    输入：nums = [1,3,4,2,2]
    输出：2

示例 2：
    输入：nums = [3,1,3,4,2]
    输出：3

提示：
    1 <= n <= 10^5
    nums.length == n + 1
    1 <= nums[i] <= n
    nums 中 只有一个整数 出现 两次或多次 ，其余整数均只出现 一次

进阶：
    如何证明 nums 中至少存在一个重复的数字?
    你可以设计一个线性级时间复杂度 O(n) 的解决方案吗？

"""
from typing import List

""" 二分法 """
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        left = 1
        right = len(nums) - 1
        while(left < right):
            mid = (left + right) // 2
            count = 0
            for num in nums:
                if (num <= mid):
                    count += 1  # 统计数组中小于等于 mid 的数字的个数 count
            if (count <= mid):  # 若 count <= mid，说明重复数字一定在 (mid, right] 的范围内。
                left = mid + 1
            else:               # 若  left > mid， 说明重复数字一定在 [0, mid] 的范围内。
                right = mid
        return left


""" 快慢指针 (求环的第一个节点)
    数组有重复元素时候， 通过索引号移动会有环出现"""
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[nums[0]]
        while slow != fast:
            print(slow, fast)
            slow = nums[slow]
            fast = nums[nums[fast]]
        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow

if __name__ == "__main__":
    nums = [6,2,3,4,2,5,1]
    sol = Solution()
    result = sol.findDuplicate(nums)
    print (result)