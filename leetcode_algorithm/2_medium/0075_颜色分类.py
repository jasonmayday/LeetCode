"""
https://leetcode-cn.com/problems/sort-colors/

给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。

此题中，我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。

示例 1：
    输入：nums = [2,0,2,1,1,0]
    输出：[0,0,1,1,2,2]

示例 2：
    输入：nums = [2,0,1]
    输出：[0,1,2]

示例 3：
    输入：nums = [0]
    输出：[0]

示例 4：
    输入：nums = [1]
    输出：[1]

提示：
    n == nums.length
    1 <= n <= 300
    nums[i] 为 0、1 或 2

进阶：
    你可以不使用代码库中的排序函数来解决这道题吗？
    你能想出一个仅使用常数空间的一趟扫描算法吗？

"""

from typing import List

""" 1. 排序"""
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        return sorted(nums)

""" 2. 单指针
    对数组进行两次遍历。
    在第一次遍历中，我们将数组中所有的 0 交换到数组的头部。
    在第二次遍历中，我们将数组中所有的 1 交换到头部的 0 之后。
    此时，所有的 2 都出现在数组的尾部"""
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        n = len(nums)   # 我们使用一个指针 cur 表示「头部」的范围，cur 中存储了一个整数，表示数组 nums 从位置 0 到位置 cur−1 都属于「头部」。
        cur = 0         # cur 的初始值为 0，表示还没有数处于「头部」。
        for i in range(n):
            if nums[i] == 0:                            # 如果找到了 0
                nums[i], nums[cur] = nums[cur], nums[i] # 就需要将 0 与「头部」位置的元素进行交换，
                cur += 1                                # 并将「头部」向后扩充一个位置。
        for i in range(cur, n):
            if nums[i] == 1:
                nums[i], nums[cur] = nums[cur], nums[i]
                cur += 1

""" 3. 双指针"""
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        n = len(nums)
        p0 = 0  # 指针 p0 来交换 0
        p1 = 0  # 指针 p1 来交换 1
        for i in range(n):
            if nums[i] == 1:                            # 如果找到了 1，
                nums[i], nums[p1] = nums[p1], nums[i]   # 那么将其与 nums[p1] 进行交换
                p1 += 1                                 # 并将 p1 向后移动一个位置
            elif nums[i] == 0:
                nums[i], nums[p0] = nums[p0], nums[i]
                if p0 < p1:
                    nums[i], nums[p1] = nums[p1], nums[i]
                p0 += 1
                p1 += 1

""" 4. 双指针(前后)"""
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        n = len(nums)
        p0 = 0      # 指针 p0 来交换 0
        p2 = n - 1  # 指针 p2 来交换 2
        i = 0
        while i <= p2:
            while i <= p2 and nums[i] == 2:
                nums[i], nums[p2] = nums[p2], nums[i]
                p2 -= 1
            if nums[i] == 0:
                nums[i], nums[p0] = nums[p0], nums[i]
                p0 += 1
            i += 1

if __name__ == "__main__":
    nums = [2,0,2,1,1,0]
    sol = Solution()
    result = sol.sortColors(nums)
    print(result)