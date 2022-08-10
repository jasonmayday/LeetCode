"""
https://leetcode.cn/problems/number-of-arithmetic-triplets/

给你一个下标从 0 开始、严格递增 的整数数组 nums 和一个正整数 diff 。如果满足下述全部条件，则三元组 (i, j, k) 就是一个 算术三元组 ：
    i < j < k ，
    nums[j] - nums[i] == diff 且
    nums[k] - nums[j] == diff

返回不同 算术三元组 的数目。

示例 1：
    输入：nums = [0,1,4,6,7,10], diff = 3
    输出：2
    解释：
        (1, 2, 4) 是算术三元组：7 - 4 == 3 且 4 - 1 == 3 。
        (2, 4, 5) 是算术三元组：10 - 7 == 3 且 7 - 4 == 3 。

示例 2：
    输入：nums = [4,5,6,7,8,9], diff = 2
    输出：2
    解释：
        (0, 2, 4) 是算术三元组：8 - 6 == 2 且 6 - 4 == 2 。
        (1, 3, 5) 是算术三元组：9 - 7 == 2 且 7 - 5 == 2 。

提示：
    3 <= nums.length <= 200
    0 <= nums[i] <= 200
    1 <= diff <= 50
    nums 严格 递增

"""
from typing import List

"""方法一：哈希表"""
class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        s = set(nums)   # 用哈希表记录每个元素
        return sum(x - diff in s and x + diff in s for x in nums)
    
class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        ans = 0
        used = set()       # 用哈希表记录每个元素
        for x in nums:
            if x - diff in used and x - diff * 2 in used:
                ans += 1
            used.add(x)
        return ans

"""方法二：三指针"""
class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        ans = 0
        i, j = 0, 1
        for x in nums:
            while nums[j] + diff < x:
                j += 1
            if nums[j] + diff > x:
                continue
            while nums[i] + diff * 2 < x:
                i += 1
            if nums[i] + diff * 2 == x:
                ans += 1
        return ans

if __name__ == "__main__":
    nums = [0,1,4,6,7,10]
    diff = 3
    sol = Solution()
    result = sol.arithmeticTriplets(nums, diff)
    print (result)