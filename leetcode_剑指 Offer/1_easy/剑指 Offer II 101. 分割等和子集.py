"""
https://leetcode-cn.com/problems/NUPfPr/

给定一个非空的正整数数组 nums ，请判断能否将这些数字分成元素和相等的两部分。

示例 1：
    输入：nums = [1,5,11,5]
    输出：true
    解释：nums 可以分割成 [1, 5, 5] 和 [11] 。

示例 2：
    输入：nums = [1,2,3,5]
    输出：false
    解释：nums 不可以分为和相等的两部分

提示：
    1 <= nums.length <= 200
    1 <= nums[i] <= 100

"""
from typing import List

""" 这个问题可以转换成「0−1 背包问题」。
    这道题与传统的「0−1 背包问题」的区别在于，传统的「0−1 背包问题」要求选取的物品的重量之和不能超过背包的总容量，
    这道题则要求选取的数字的和恰好等于整个数组的元素和的一半。
"""

""" 方法一：动态规划优化 """
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        target = total // 2
        
        dp = [True] + [False] * target
        
        for i, num in enumerate(nums):
            for j in range(target, num - 1, -1):
                dp[j] |= dp[j - num]
        return dp[target]
    
""" 动态规划 """
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        taraget = sum(nums)
        if taraget % 2 == 1:
            return False
        taraget //= 2
        
        dp = [0] * 10001    # dp[j] 有没有和为j的子集，有为True，没有为False。
        for i in range(len(nums)):
            for j in range(taraget, nums[i] - 1, -1):
                dp[j] = max(dp[j], dp[j - nums[i]] + nums[i])
        return taraget == dp[taraget]

""" 动态规划 """
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False        # 计算sum，如果是奇数则可以直接排除
        target = sum(nums) // 2
        
        dp = [False] * (target + 1) # dp[j] 有没有和为j的子集，有为True，没有为False。
        dp[0] = True                # 长度为 target + 1，用于存储子集的和从0到target是否可能取到的情况。
        
        for i in range(len(nums)):                      # 典型的01背包方法: 外层遍历背包, 对遍历到的数nums[i]有两种操作，一个是选择这个数，一个是不选择这个数。
            for j in range(target, nums[i] - 1, -1):    # 内层逆序遍历子集的和从nums[i]到target的所有情况, 判断当前数加入后，dp数组中哪些和的情况可以从False变成True。
                dp[j] = dp[j] or dp[j - nums[i]]        # 如果不选择当前数，那么和为j的情况保持不变，dp[j]仍然是dp[j]，原来是True就还是True，原来是False也还是False；
                                                        # 如果选择当前数，那么如果j - nums[i]这种情况是True的话和为j的情况也会是True。比如和为0一定为True，只要 j - nums[i] == 0，那么dp[j]就变成了True。
                                                        # dp[j] 和 dp[j-nums[i]] 只要有一个为 True，dp[j] 就变成True，因此用or连接两者。
        return dp[-1]   # 看dp[-1]是不是True，也就是dp[target]是不是True

if __name__ == "__main__":
    nums = [1,5,11,5]
    sol = Solution()
    result = sol.canPartition(nums)
    print (result)