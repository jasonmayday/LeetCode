"""
https://leetcode-cn.com/problems/maximum-product-subarray/

给你一个整数数组 nums ，请你找出数组中乘积最大的连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。

示例 1:
    输入: [2,3,-2,4]
    输出: 6
    解释: 子数组 [2,3] 有最大乘积 6。

示例 2:
    输入: [-2,0,-1]
    输出: 0
    解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。

"""
from typing import List

""" 滑动窗口 """
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums: return
        cur_pro = 1             # 目前的累乘
        min_pos = 1             # 前面最小的正数
        max_neg = float("-inf") # 前面最大的负数
        res = float("-inf")     # 初始化结果
        
        for num in nums:
            cur_pro *= num  # 遍历数字，不断乘积
            # 考虑三种情况：
            # 累乘的乘积大于0
            if cur_pro > 0:
                res = max(res, cur_pro // min_pos)
                min_pos = min(min_pos, cur_pro)
            # 累乘的乘积小于0
            elif cur_pro < 0:
                if max_neg != float("-inf"):
                    res = max(res, cur_pro // max_neg)
                else:
                    res = max(res, num)
                max_neg = max(max_neg, cur_pro)
            # 累乘的乘积等于 0
            elif cur_pro == 0:
                cur_pro = 1
                min_pos = 1
                max_neg = float("-inf")
                res = max(res, num)
        return res 


""" 动态规划
    根据正负性，同时维护最大值和最小值，因为对于负数来说，前面连续子序列的值越小越好 """
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums: return
        n = len(nums)
        
        dp_max = [0] * n    # [0,0,0,0]
        dp_max[0] = nums[0] # 0

        dp_min = [0] * n
        dp_min[0] = nums[0]
        
        res = nums[0]
        
        for i in range(1, n):
            dp_max[i] = max(nums[i], dp_max[i-1] * nums[i], dp_min[i-1] * nums[i])
            dp_min[i] = min(nums[i], dp_max[i-1] * nums[i], dp_min[i-1] * nums[i])
            res = max(res, dp_max[i])

        return res


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums: return
        res = nums[0]
        pre_max = nums[0]   # 记录前i的最大值
        pre_min = nums[0]   # 记录前i的最小值
        for num in nums[1:]:    # 从第二个数字开始
            cur_max = max(pre_max * num, pre_min * num, num)
            cur_min = min(pre_max * num, pre_min * num, num)
            res = max(res, cur_max)
            pre_max = cur_max
            pre_min = cur_min
        return res

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums: return
        maxi = mini = res = nums[0]
        for num in nums[1:]:
            maxi = max(maxi * num, mini * num, num)
            mini = min(maxi * num, mini * num, num)
            res = max(maxi, res)
        return res

""" 根据符号的个数
    当负数个数为偶数时候，全部相乘一定最大
    当负数个数为奇数时候，它的左右两边的负数个数一定为偶数，只需求两边最大值
    当有 0 情况，重置就可以了"""
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        reverse_nums = nums[::-1]
        for i in range(1, len(nums)):
            nums[i] *= nums[i - 1] or 1
            reverse_nums[i] *= reverse_nums[i - 1] or 1
        return max(nums + reverse_nums)


if __name__ == "__main__":
    nums  = [2,3,-2,4]
    sol = Solution()
    result = sol.maxProduct(nums)
    print(result)