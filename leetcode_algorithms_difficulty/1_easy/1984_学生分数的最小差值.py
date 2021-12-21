"""
https://leetcode-cn.com/problems/minimum-difference-between-highest-and-lowest-of-k-scores/

给你一个 下标从 0 开始 的整数数组 nums ，其中 nums[i] 表示第 i 名学生的分数。另给你一个整数 k 。

从数组中选出任意 k 名学生的分数，使这 k 个分数间 最高分 和 最低分 的 差值 达到 最小化 。

返回可能的 最小差值 。

示例 1：
    输入：nums = [90], k = 1
    输出：0
    解释：选出 1 名学生的分数，仅有 1 种方法：
    - [90] 最高分和最低分之间的差值是 90 - 90 = 0
    可能的最小差值是 0

示例 2：
    输入：nums = [9,4,1,7], k = 2
    输出：2
    解释：选出 2 名学生的分数，有 6 种方法：
    - [9,4,1,7] 最高分和最低分之间的差值是 9 - 4 = 5
    - [9,4,1,7] 最高分和最低分之间的差值是 9 - 1 = 8
    - [9,4,1,7] 最高分和最低分之间的差值是 9 - 7 = 2
    - [9,4,1,7] 最高分和最低分之间的差值是 4 - 1 = 3
    - [9,4,1,7] 最高分和最低分之间的差值是 7 - 4 = 3
    - [9,4,1,7] 最高分和最低分之间的差值是 7 - 1 = 6
    可能的最小差值是 2

提示：
    1 <= k <= nums.length <= 1000
    0 <= nums[i] <= 10^5
    
"""
from typing import List

""" 先将nums排好序，然后把所有长度为k的连续子序列取出，找开头元素和结尾元素的差。简单一点，找到所有的前端和后端求差即可。
    zip的特点：返回结果个数与最短的列表一致。这样就不用分片前端了。
"""
class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        return min(j - i for i, j in zip(nums, nums[k-1:]))

""" 排序 + 滑动窗口 """
class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()                 # [9,4,1,7] → [1,4,7,9]
        res = float('inf')
        for right in range(k - 1, n):   # 1 - 4
            left = right - k + 1        # 0
            cur = nums[right] - nums[left]
            res = min(res, cur)
        return res
    
class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans = nums[-1]
        for i in range(0, len(nums)-k+1):
            ans = min(ans, nums[i + k-1] - nums[i])
        return 0 if len(nums)==1 and k==1 else ans

if __name__ == "__main__":
    nums = [9,4,1,7]
    k = 2
    sol = Solution()
    result = sol.minimumDifference(nums, k)
    print (result)