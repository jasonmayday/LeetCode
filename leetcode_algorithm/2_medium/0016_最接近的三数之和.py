"""
https://leetcode-cn.com/problems/3sum-closest/

给你一个长度为 n 的整数数组 nums 和 一个目标值 target。请你从 nums 中选出三个整数，使它们的和与 target 最接近。

返回这三个数的和。

假定每组输入只存在恰好一个解。

示例 1：
    输入：nums = [-1,2,1,-4], target = 1
    输出：2
    解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2) 。

示例 2：
    输入：nums = [0,0,0], target = 1
    输出：0

提示：
    3 <= nums.length <= 1000
    -1000 <= nums[i] <= 1000
    -10^4 <= target <= 10^4

"""
from typing import List

""" 方法一：排序 + 双指针
    枚举第一个元素 a，对于剩下的两个元素 b 和 c，我们希望它们的和最接近 target−a """
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        best = 10 ** 7
        
        def update(cur):        # 根据差值的绝对值来更新答案
            nonlocal best
            if abs(cur - target) < abs(best - target):
                best = cur
        
        for i in range(n):      # 枚举第一个元素 a
            if i > 0 and nums[i] == nums[i - 1]:    # 保证和上一次枚举的元素不相等
                continue
            # 为了防止重复枚举，我们在位置 [i+1,n) 的范围内枚举 b 和 c
            j = i + 1   # b 的指针初始位置，即左边界
            k = n - 1   # c 的指针初始位置，即右边界
            while j < k:
                s = nums[i] + nums[j] + nums[k] # 在每一步枚举的过程中，用 a+b+c 来更新答案
                if s == target:     # 如果和为 target 直接返回答案
                    return target
                update(s)           # 使用 update 函数来更新答案
                if s > target:      # 如果和大于 target，
                    k0 = k - 1      # 移动 c 对应的指针
                    while j < k0 and nums[k0] == nums[k]:   # 移动到下一个不相等的元素
                        k0 -= 1     # 将 c 的指针向左移动一个位置
                    k = k0
                else:               # 如果和小于 target，
                    j0 = j + 1      # 移动 b 对应的指针
                    while j0 < k and nums[j0] == nums[j]:   # 移动到下一个不相等的元素
                        j0 += 1     # 将 b 的指针向右移动一个位置
                    j = j0
        return best
    
""" 方法2：排序 + 双指针 （精简版） """
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums = sorted(nums)
        closest = 10 ** 7
        ans = 0

        for i in range(n):
            j = i + 1   # b 的指针初始位置，即左边界
            k = n - 1   # c 的指针初始位置，即右边界
            while j < k:
                sum3 = nums[i] + nums[j] + nums[k]
                if sum3 < target:   # 如果三数和小于 target，
                    j += 1          # 将 b 的指针向右移动一个位置
                elif sum3 > target: # 如果和大于 target
                    k -= 1          # 将 c 的指针向左移动一个位置
                else:               # 如果和为 target 直接返回答案
                    return sum3     # 直接返回答案
                if closest > abs(sum3 - target):
                    closest = abs(sum3 - target)
                    ans = sum3
        return ans

if __name__ == "__main__":
    nums = [-1,2,1,-4]
    target = 1
    sol = Solution()
    result = sol.threeSumClosest(nums, target)
    print (result)