"""
https://leetcode-cn.com/problems/count-special-quadruplets/

给你一个 下标从 0 开始 的整数数组 nums ，返回满足下述条件的 不同 四元组 (a, b, c, d) 的 数目 ：
    nums[a] + nums[b] + nums[c] == nums[d] ，且
    a < b < c < d

示例 1：
    输入：nums = [1,2,3,6]
    输出：1
    解释：满足要求的唯一一个四元组是 (0, 1, 2, 3) 因为 1 + 2 + 3 == 6 。

示例 2：
    输入：nums = [3,3,6,4,5]
    输出：0
    解释：[3,3,6,4,5] 中不存在满足要求的四元组。

示例 3：
    输入：nums = [1,1,1,3,5]
    输出：4
    解释：满足要求的 4 个四元组如下：
    - (0, 1, 2, 3): 1 + 1 + 1 == 3
    - (0, 1, 3, 4): 1 + 1 + 3 == 5
    - (0, 2, 3, 4): 1 + 1 + 3 == 5
    - (1, 2, 3, 4): 1 + 1 + 3 == 5

提示：
    4 <= nums.length <= 50
    1 <= nums[i] <= 100

"""

from typing import List

"""解法1：暴力"""
class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0
        for a in range(n):
            for b in range(a + 1, n):
                for c in range(b + 1, n):
                    for d in range(c + 1, n):
                        if nums[a] + nums[b] + nums[c] == nums[d]:
                            count += 1
        return count
    
if __name__ == "__main__":
    nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50]
    sol = Solution()
    result = sol.countQuadruplets(nums)
    print (result)