"""
https://leetcode-cn.com/problems/max-consecutive-ones-ii/

给定一个二进制数组 nums ，如果最多可以翻转一个 0 ，则返回数组中连续 1 的最大个数。

示例 1：
    输入：nums = [1,0,1,1,0]
    输出：4
    解释：翻转第一个 0 可以得到最长的连续 1。
         当翻转以后，最大连续 1 的个数为 4。

示例 2:
    输入：nums = [1,0,1,1,0,1]
    输出：4

提示:
    1 <= nums.length <= 10^5
    nums[i] 不是 0 就是 1.
     
进阶：
    如果输入的数字是作为 无限流 逐个输入如何处理？换句话说，内存不能存储下所有从流中输入的数字。您可以有效地解决吗？

"""
from typing import List
from collections import deque

""" 记录第一个0前面的连续1的个数 """
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        prev = 0
        cnt = 0
        for num in nums:
            cnt += 1        # 如果不是 0 ，计数 +1，统计连续1 的个数
            if num == 0:    # 遇到 0
                prev = cnt  # prev 为 0前面的连续1的个数
                cnt = 0
            res = max(res, prev + cnt)
        return res

""" 滑动窗口 """
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        left = 0
        res = 0
        cur_zero_num = 0
        for right in range(len(nums)):  # 进 R
            if nums[right] == 0:        # 遇到 0
                cur_zero_num += 1       # 0 的计数加一
            while cur_zero_num > 1:     # 遇到第二个0：弹 L
                if nums[left] == 0:
                    cur_zero_num -= 1
                left += 1
            res = max(res, right - left + 1)    # 更新res
        return res

""" 动态规划 """
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # dp[i][0] 不使用翻转操作的最长1序列长度
        # dp[i][1] 使用过翻转操作的最长1序列长度
        n = len(nums)
        dp = [[0,0] for _ in range(n+1)]
        res = 0
        for i in range(1, n+1):
            if nums[i-1] == 1:
                dp[i][0] = dp[i-1][0]+1
                dp[i][1] = dp[i-1][1]+1
            else:
                dp[i][0] = 0
                dp[i][1] = dp[i-1][0]+1
            res = max(res,dp[i][0],dp[i][1])
        return res

""" [状态压缩]动态规划"""
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res,dp1,dp0 = 0,0,0
        for i in range(len(nums)):
            if nums[i] == 1:
                dp0+=1
                dp1+=1
            else:
                dp1 = dp0+1
                dp0 = 0
            res = max(res,dp0,dp1)
        return res

""" 对于 无限流 数据，只需记录前面0的位置即可 """
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        left = 0
        res = 0
        cur_zero_num = 0
        queue = deque()
        for right in range(len(nums)):
            if nums[right] == 0:
                cur_zero_num += 1
                queue.appendleft(right)
            while cur_zero_num > 1:
                left = queue.pop() + 1
                cur_zero_num -= 1
            res = max(res, right - left + 1)
        return res

if __name__ == "__main__":
    nums = [1,0,1,1,0]
    sol = Solution()
    result = sol.findMaxConsecutiveOnes(nums)
    print (result)
