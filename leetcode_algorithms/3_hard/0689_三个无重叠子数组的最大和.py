"""
https://leetcode-cn.com/problems/maximum-sum-of-3-non-overlapping-subarrays/

给你一个整数数组 nums 和一个整数 k ，找出三个长度为 k 、互不重叠、且 3 * k 项的和最大的子数组，并返回这三个子数组。

以下标的数组形式返回结果，数组中的每一项分别指示每个子数组的起始位置（下标从 0 开始）。如果有多个结果，返回字典序最小的一个。

示例 1：
    输入：nums = [1,2,1,2,6,7,5,1], k = 2
    输出：[0,3,5]
    解释：子数组 [1, 2], [2, 6], [7, 5] 对应的起始下标为 [0, 3, 5]。
    也可以取 [2, 1], 但是结果 [1, 3, 5] 在字典序上更大。

示例 2：
    输入：nums = [1,2,1,2,1,2,1,2,1], k = 2
    输出：[0,2,4]

提示：
    1 <= nums.length <= 2 * 104
    1 <= nums[i] < 216
    1 <= k <= floor(nums.length / 3)

"""
from typing import List

class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        best1Seq = [0]
        best2Seq = [0, k]
        best3Seq = [0, k, k*2]      # 当前最佳的一个，两个，三个子数组的索引列表
        
        s1 = sum(nums[0: k])
        s2 = sum(nums[k: 2*k])
        s3 = sum(nums[2*k: 3*k])     # 每个子数组的区间和
        
        max1Sum = s1
        max2Sum = s1 + s2
        max3Sum = s1 + s2 + s3      # 一个，两个，三个子数组的最大区间和
        
        for i in range(1, len(nums)-3*k+1):
            # 更新第一、第二、第三个子数组的区间和
            s1 += nums[i + k - 1] - nums[i - 1]
            s2 += nums[i + k * 2 - 1] - nums[i + k - 1]
            s3 += nums[i + k * 3 - 1] - nums[i + k* 2 - 1]
            
            # 更新一个子数组的最大区间和以及对应的索引列表
            if s1 > max1Sum:
                best1Seq, max1Sum = [i], s1
            
            # 更新两个子数组的最大区间和以及对应的索引列表
            if s2 + max1Sum > max2Sum:
                best2Seq, max2Sum = best1Seq + [i+k], s2 + max1Sum
            
            # 更新三个字数组的最大区间和以及对应的索引列表
            if s3 + max2Sum > max3Sum:
                best3Seq, max3Sum = best2Seq + [i+k*2], s3 + max2Sum
                
        return best3Seq

if __name__ == "__main__":
    nums = [1,2,1,2,6,7,5,1]
    k = 2
    sol = Solution()
    result = sol.maxSumOfThreeSubarrays(nums, k)
    print(result)