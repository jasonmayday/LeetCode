"""
https://leetcode-cn.com/problems/jump-game-ii/

给你一个非负整数数组 nums ，你最初位于数组的第一个位置。

数组中的每个元素代表你在该位置可以跳跃的最大长度。

你的目标是使用最少的跳跃次数到达数组的最后一个位置。

假设你总是可以到达数组的最后一个位置。

示例 1:
    输入: nums = [2,3,1,1,4]
    输出: 2
    解释: 跳到最后一个位置的最小跳跃数是 2。
         从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。

示例 2:
    输入: nums = [2,3,0,1,4]
    输出: 2

提示:
    1 <= nums.length <= 10^4
    0 <= nums[i] <= 1000

"""
from typing import List

"""正向查找: 贪心"""
class Solution:
    def jump(self, nums: List[int]) -> int:
        ans = 0
        maxPos = 0  # 实时更新每步所能到达的最远位置maxPos
        end = 0
        for i in range(len(nums) - 1):
            maxPos = max(maxPos, i + nums[i])   # 更新当前最右可以跳到哪里
            if end == i:
                end = maxPos                    # 到达上次跳的最远的距离后更新end值
                ans += 1
        return ans
    
if __name__ == "__main__":
    n = 8
    sol = Solution()
    result = sol.jump(n)
    print(result)