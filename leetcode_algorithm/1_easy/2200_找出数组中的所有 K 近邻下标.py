"""
https://leetcode-cn.com/problems/find-all-k-distant-indices-in-an-array/

给你一个下标从 0 开始的整数数组 nums 和两个整数 key 和 k 。K 近邻下标 是 nums 中的一个下标 i ，并满足至少存在一个下标 j 使得 |i - j| <= k 且 nums[j] == key 。

以列表形式返回按 递增顺序 排序的所有 K 近邻下标。

示例 1：
    输入：nums = [3,4,9,1,3,9,5], key = 9, k = 1
    输出：[1,2,3,4,5,6]
    解释：因此，nums[2] == key 且 nums[5] == key 。
    - 对下标 0 ，|0 - 2| > k 且 |0 - 5| > k ，所以不存在 j 使得 |0 - j| <= k 且 nums[j] == key 。所以 0 不是一个 K 近邻下标。
    - 对下标 1 ，|1 - 2| <= k 且 nums[2] == key ，所以 1 是一个 K 近邻下标。
    - 对下标 2 ，|2 - 2| <= k 且 nums[2] == key ，所以 2 是一个 K 近邻下标。
    - 对下标 3 ，|3 - 2| <= k 且 nums[2] == key ，所以 3 是一个 K 近邻下标。
    - 对下标 4 ，|4 - 5| <= k 且 nums[5] == key ，所以 4 是一个 K 近邻下标。
    - 对下标 5 ，|5 - 5| <= k 且 nums[5] == key ，所以 5 是一个 K 近邻下标。
    - 对下标 6 ，|6 - 5| <= k 且 nums[5] == key ，所以 6 是一个 K 近邻下标。
    因此，按递增顺序返回 [1,2,3,4,5,6] 。

示例 2：
    输入：nums = [2,2,2,2,2], key = 2, k = 2
    输出：[0,1,2,3,4]
    解释：对 nums 的所有下标 i ，总存在某个下标 j 使得 |i - j| <= k 且 nums[j] == key ，所以每个下标都是一个 K 近邻下标。 
    因此，返回 [0,1,2,3,4] 。

提示：
    1 <= nums.length <= 1000
    1 <= nums[i] <= 1000
    key 是数组 nums 中的一个整数
    1 <= k <= nums.length

"""
from typing import List

""" 方法一：暴力"""
class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        n = len(nums)
        ans = []
        for i in range(n):
            flag = False
            for j in range(n):
                if abs(i - j) <= k and nums[j] == key:
                    flag = True
                    break
            if flag:
                ans.append(i)
        return ans

""" 因为要范围update，所以用差分数组 """
class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        n = len(nums)
        diff = [0] * (n + 10)
        
        for i, num in enumerate(nums):
            if num != key:
                continue
            left, right = max(0, i - k), min(n - 1, i + k)
            diff[left] += 1
            diff[right + 1] -= 1
        for i in range(1, len(diff)):
            diff[i] += diff[i - 1]
        return [i for i, num in enumerate(diff) if num]

if __name__ == "__main__":
    nums = [3,4,9,1,3,9,5]
    key = 9
    k = 1
    sol = Solution()
    result = sol.findKDistantIndices(nums, key, k)
    print (result)