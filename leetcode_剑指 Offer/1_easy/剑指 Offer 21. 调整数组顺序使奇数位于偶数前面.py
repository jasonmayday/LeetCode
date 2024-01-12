"""
https://leetcode-cn.com/problems/diao-zheng-shu-zu-shun-xu-shi-qi-shu-wei-yu-ou-shu-qian-mian-lcof/

输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有奇数在数组的前半部分，所有偶数在数组的后半部分。

示例：
    输入：nums = [1,2,3,4]
    输出：[1,3,2,4]
    注：[3,1,2,4] 也是正确的答案之一。

提示：
    0 <= nums.length <= 50000
    0 <= nums[i] <= 10000

"""
from typing import List

""" 直接模拟 """
class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        odd, even = [], []
        for i in nums:
            if i % 2 == 1:
                odd.append(i)
            else:
                even.append(i)
        return odd + even

""" 双指针 """
class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        i = 0               # 指针 i 从左向右寻找偶数；
        j = len(nums) - 1   # 指针 j 从右向左寻找奇数；
        while i < j:        # 当 i=j 时跳出循环
            while i < j and nums[i] & 1 == 1:   # 指针 i 遇到奇数
                i += 1                          # 则执行 i=i+1 跳过，直到找到偶数
            while i < j and nums[j] & 1 == 0:   # 指针 j 遇到偶数
                j -= 1                          # 则执行 j=j−1 跳过，直到找到奇数；
            nums[i], nums[j] = nums[j], nums[i] # 交换 nums[i] 和 nums[j] 值；
        return nums

if __name__ == "__main__":
    nums = [1, 2, 3 ,4]
    sol = Solution()
    result = sol.exchange(nums)
    print (result)