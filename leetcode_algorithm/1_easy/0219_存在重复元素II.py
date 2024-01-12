'''
https://leetcode-cn.com/problems/contains-duplicate-ii/

给定一个整数数组和一个整数 k，判断数组中是否存在两个不同的索引 i 和 j，使得 nums [i] = nums [j]，并且 i 和 j 的差的 绝对值 不超过 k。

示例 1:
输入: nums = [1,2,3,1], k = 3
输出: true

示例 2:
输入: nums = [1,0,1,1], k = 1
输出: true

示例 3:
输入: nums = [1,2,3,1,2,3], k = 2
输出: false

'''

from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hash={}                              # 初始化哈希表hash
        for i in range(len(nums)):           # 遍历数组
            if (nums[i] not in hash):        # 若nums[i]不在hash中
                hash[nums[i]]=i              # 令nums[i]为key，value为当前的索引i。
            else:                            # 若nums[i]已存在
                if (i - hash[nums[i]] <= k): # 判断当前的索引和上一相同元素的索引差是否小于等于k。
                    return True              # 若满足，返回True
                else:
                    hash[nums[i]] = i        # 将索引更新为当前索引
        return False

if __name__ == "__main__":
    nums = [1,2,3,1,2,3]
    k = 2
    sol = Solution()
    result = sol.containsNearbyDuplicate(nums, k)
    print(result)