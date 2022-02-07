"""
https://leetcode-cn.com/problems/rotate-array/

给你一个数组，将数组中的元素向右轮转 k 个位置，其中 k 是非负数。

示例 1:
    输入: nums = [1,2,3,4,5,6,7], k = 3
    输出: [5,6,7,1,2,3,4]
    解释:
    向右轮转 1 步: [7,1,2,3,4,5,6]
    向右轮转 2 步: [6,7,1,2,3,4,5]
    向右轮转 3 步: [5,6,7,1,2,3,4]

示例 2:
    输入：nums = [-1,-100,3,99], k = 2
    输出：[3,99,-1,-100]
    解释: 
    向右轮转 1 步: [99,-1,-100,3]
    向右轮转 2 步: [3,99,-1,-100]

提示：
    1 <= nums.length <= 10^5
    -2^31 <= nums[i] <= 2^31 - 1
    0 <= k <= 10^5

进阶：
    尽可能想出更多的解决方案，至少有 三种 不同的方法可以解决这个问题。
    你可以使用空间复杂度为 O(1) 的 原地 算法解决这个问题吗？

"""

from typing import List


""" 思路一：插入"""
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n              # k 取除以数组长度的余数
        for _ in range(k): 
            nums.insert(0, nums.pop())  # 把数组最后一位的数字弹出，然后插入到最前端，执行k次
        return nums


""" 思路二：拼接"""
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n              # k 取除以数组长度的余数
        nums[:] = nums[-k:] + nums[:-k]
        return nums


""" 思路三：三个翻转，整体翻转，前k翻转，后k翻转 """
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n                      # [1, 2, 3, 4, 5, 6, 7] 
        nums[:] = nums[::-1]        # [7, 6, 5, 4, 3, 2, 1]  整体翻转
        nums[:k] = nums[:k][::-1]   # [5, 6, 7, 4, 3, 2, 1]  前 k 次翻转
        nums[k:] = nums[k:][::-1]   # [5, 6, 7, 1, 2, 3, 4]  后 k 次反转
        return nums


""" 思路三：三个翻转（手写版本） """
class Solution:
    def rotate(self, A: List[int], k: int) -> None:
        def reverse(i, j):
            while i < j:
                A[i], A[j] = A[j], A[i]
                i += 1
                j -= 1
        n = len(A)
        k %= n
        reverse(0, n - 1)
        reverse(0, k - 1)
        reverse(k, n - 1)
        return nums

        
""" 思路四：模拟过程"""
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n              # k 取除以数组长度的余数
        if k == 0:
            return 
        start = 0
        tmp = nums[start]
        cnt = 0
        while cnt < n:
            nxt = (start + k) % n
            while nxt != start:
                nums[nxt], tmp = tmp, nums[nxt]
                nxt = (nxt+k) % n
                cnt += 1
            nums[nxt] = tmp
            start += 1
            tmp = nums[start]
            cnt += 1
        return nums


if __name__ == "__main__":
    nums = [1,2,3,4,5,6,7]
    k = 3
    sol = Solution()
    result = sol.rotate(nums, k)
    print (result)

