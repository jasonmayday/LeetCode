"""
https://leetcode-cn.com/problems/sum-of-all-odd-length-subarrays/

给你一个正整数数组 arr ，请你计算所有可能的奇数长度子数组的和。

子数组 定义为原数组中的一个连续子序列。

请你返回 arr 中 所有奇数长度子数组的和 。

示例 1：
    输入：arr = [1,4,2,5,3]
    输出：58
    解释：所有奇数长度子数组和它们的和为：
    [1] = 1
    [4] = 4
    [2] = 2
    [5] = 5
    [3] = 3
    [1,4,2] = 7
    [4,2,5] = 11
    [2,5,3] = 10
    [1,4,2,5,3] = 15
    我们将所有值求和得到 1 + 4 + 2 + 5 + 3 + 7 + 11 + 10 + 15 = 58

示例 2：
    输入：arr = [1,2]
    输出：3
    解释：总共只有 2 个长度为奇数的子数组，[1] 和 [2]。它们的和为 3 。

示例 3：
    输入：arr = [10,11,12]
    输出：66

提示：
    1 <= arr.length <= 100
    1 <= arr[i] <= 1000

"""
from typing import List

class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        sum = 0
        for start in range(len(arr)):   # 起始元素从 0 位开始
            length = 1                  # 先统计 1 个元素的数组
            while start + length <= len(arr):
                for val in arr[start:start + length]:   # 从 arr[0:1]开始
                    sum += val                          # 把 统计到的奇数个数字的总和加到结果中
                length += 2                             # 统计下一个奇数长度的数组
        return sum

class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        ans = 0    
        for n in range(1, len(arr) + 1, 2):
            for i in range(len(arr) - n + 1):   # 要保证 i+n 的值不能大于数组长度
                ans += sum(arr[i : i + n])     
        return ans

if __name__ == "__main__":
    arr = [1,4,2,5,3]
    sol = Solution()
    result = sol.sumOddLengthSubarrays(arr)
    print(result)