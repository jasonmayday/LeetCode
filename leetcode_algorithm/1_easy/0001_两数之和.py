'''
https://leetcode-cn.com/problems/two-sum/

给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target 的那 两个 整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。

你可以按任意顺序返回答案。

示例 1：
    输入：nums = [2,7,11,15], target = 9
    输出：[0,1]
    解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。

示例 2：
    输入：nums = [3,2,4], target = 6
    输出：[1,2]

示例 3：
    输入：nums = [3,3], target = 6
    输出：[0,1]

提示：
    2 <= nums.length <= 10^4
    -10^9 <= nums[i] <= 10^9
    -10^9 <= target <= 10^9
    只会存在一个有效答案

进阶：你可以想出一个时间复杂度小于 O(n2) 的算法吗？
'''


from typing import List

""" 暴力枚举
    时间复杂度：O(N^2)
    空间复杂度：O(1)"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []

""" 哈希表
    时间复杂度：O(N)
    空间复杂度：O(N)"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashtable = dict()
        for i, num in enumerate(nums):
            if target - num in hashtable:             # 查询哈希表中是否存在 target-x
                return [hashtable[target - num], i]   # 若存在 target-x，返回
            hashtable[nums[i]] = i                    # 若不存在 target-x, 将当前数和索引放入哈希表
        return []

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(len(nums)):
            if target - nums[i] in dic:
                return dic[target - nums[i]], i
            dic[nums[i]] = i
        return []

if __name__ == "__main__":
    nums = [2,7,11,15]
    target = 9
    sol = Solution()
    result = sol.twoSum(nums, target)
    print (result)