"""
https://leetcode-cn.com/problems/combination-sum-iv/

给你一个由 不同 整数组成的数组 nums ，和一个目标整数 target 。请你从 nums 中找出并返回总和为 target 的元素组合的个数。

题目数据保证答案符合 32 位整数范围。

示例 1：
    输入：nums = [1,2,3], target = 4
    输出：7
    解释：
    所有可能的组合为：
    (1, 1, 1, 1)
    (1, 1, 2)
    (1, 2, 1)
    (1, 3)
    (2, 1, 1)
    (2, 2)
    (3, 1)
    请注意，顺序不同的序列被视作不同的组合。

示例 2：
    输入：nums = [9], target = 3
    输出：0

提示：
    1 <= nums.length <= 200
    1 <= nums[i] <= 1000
    nums 中的所有元素 互不相同
    1 <= target <= 1000
 
进阶：如果给定的数组中含有负数会发生什么？问题会产生何种变化？如果允许负数出现，需要向题目中添加哪些限制条件？

"""
from typing import List

""" 动态规划 背包问题"""
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [1] + [0] * target         # dp[x] 表示选取的元素之和等于 x 的方案数
        # dp = [1, 0, 0, 0, 0]  动态规划的边界是 dp[0]=1。只有当不选取任何元素时，元素之和才为 0，因此只有 1 种方案
        for i in range(1, target + 1):  # 当 1 ≤ i ≤ target 时，如果存在一种排列，其中的元素之和等于 i
            for num in nums:            # 则该排列的最后一个元素一定是数组 nums 中的一个元素。
                if num <= i:            # 假设该排列的最后一个元素是 num，则一定有 num≤i，对于元素之和等于 i−num 的每一种排列，在最后添加 num 之后即可得到一个元素之和等于 i 的排列，
                    dp[i] += dp[i - num]# 因此在计算 dp[i] 时，应该计算所有的 dp[i−num] 之和。
        return dp[target]

if __name__ == "__main__":
    nums = [1,2,3]
    target = 4
    sol = Solution()
    result = sol.combinationSum4(nums, target)
    print(result)