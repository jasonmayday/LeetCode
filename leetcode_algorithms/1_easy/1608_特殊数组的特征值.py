"""
https://leetcode-cn.com/problems/special-array-with-x-elements-greater-than-or-equal-x/

给你一个非负整数数组 nums 。如果存在一个数 x ，使得 nums 中恰好有 x 个元素 大于或者等于 x ，那么就称 nums 是一个 特殊数组 ，而 x 是该数组的 特征值 。

注意： x 不必 是 nums 的中的元素。

如果数组 nums 是一个 特殊数组 ，请返回它的特征值 x 。否则，返回 -1 。可以证明的是，如果 nums 是特殊数组，那么其特征值 x 是 唯一的 。

示例 1：
    输入：nums = [3,5]
    输出：2
    解释：有 2 个元素（3 和 5）大于或等于 2 。

示例 2：
    输入：nums = [0,0]
    输出：-1
    解释：没有满足题目要求的特殊数组，故而也不存在特征值 x 。
    如果 x = 0，应该有 0 个元素 >= x，但实际有 2 个。
    如果 x = 1，应该有 1 个元素 >= x，但实际有 0 个。
    如果 x = 2，应该有 2 个元素 >= x，但实际有 0 个。
    x 不能取更大的值，因为 nums 中只有两个元素。

示例 3：
    输入：nums = [0,4,3,0,4]
    输出：3
    解释：有 3 个元素大于或等于 3 。

示例 4：
    输入：nums = [3,6,7,7,0]
    输出：-1

提示：
    1 <= nums.length <= 100
    0 <= nums[i] <= 1000

"""
from typing import List

class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()     # [0,0,3,4,4]
        for i in range(1, len(nums) + 1):
            if (nums[-i] < i):      # 倒数第一位开始排查，直到排查到倒数第 n 位数字小于 n
                if nums[-i] < i-1:  # 然后验算一下这个数字是不是也小于n-1 。
                    return (i-1)    # 如果是，n-1就是我们要的特征值了。
                else:
                    return -1
        return len(nums)
    
""" 排序 + 左右夹逼 """
class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort(reverse = True)       # 将数组由大到小排列  [4,4,3,0,0]
        res = -1
        for i, num in enumerate(nums):  # 如果索引为i的元素大于等于 i+1
            if num >= i + 1:
                res = i + 1
            else:
                break
        if sum(num >= res for num in nums) == res:
            return res 
        else: return -1

if __name__ == "__main__":
    nums = [0,4,3,0,4]
    sol = Solution()
    result = sol.specialArray(nums)
    print(result)