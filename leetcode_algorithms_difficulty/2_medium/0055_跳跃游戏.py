"""
https://leetcode-cn.com/problems/jump-game/

给定一个非负整数数组 nums ，你最初位于数组的 第一个下标 。

数组中的每个元素代表你在该位置可以跳跃的最大长度。

判断你是否能够到达最后一个下标。

示例 1：
    输入：nums = [2,3,1,1,4]
    输出：true
    解释：可以先跳 1 步，从下标 0 到达下标 1, 然后再从下标 1 跳 3 步到达最后一个下标。

示例 2：
    输入：nums = [3,2,1,0,4]
    输出：false
    解释：无论怎样，总会到达下标为 3 的位置。但该下标的最大跳跃长度是 0 ， 所以永远不可能到达最后一个下标。

提示：
    1 <= nums.length <= 3 * 10^4
    0 <= nums[i] <= 10^5

"""
from typing import List

""" 贪心算法 """
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        rightmost = 0
        for i in range(n):      # 依次遍历数组中的每一个位置，并实时维护 最远可以到达的位置
            if i <= rightmost:
                rightmost = max(rightmost, i + nums[i])     # 对于当前遍历到的位置 xx，如果它在 最远可以到达的位置 的范围内，那么我们就可以从起点通过若干次跳跃到达该位置
                if rightmost >= n - 1:  # 如果 最远可以到达的位置 大于等于数组中的最后一个位置，那就说明最后一个位置可达
                    return True
        return False

if __name__ == "__main__":
    nums = [3,2,1,0,4]
    sol = Solution()
    result = sol.canJump(nums)
    print(result)