"""
给你一个整数数组 nums 。数组中唯一元素是那些只出现 恰好一次 的元素。

请你返回 nums 中唯一元素的 和 。

示例 1：
    输入：nums = [1,2,3,2]
    输出：4
    解释：唯一元素为 [1,3] ，和为 4 。

示例 2：
    输入：nums = [1,1,1,1,1]
    输出：0
    解释：没有唯一元素，和为 0 。

示例 3 ：
    输入：nums = [1,2,3,4,5]
    输出：15
    解释：唯一元素为 [1,2,3,4,5] ，和为 15 。

提示：
    1 <= nums.length <= 100
    1 <= nums[i] <= 100

"""
from typing import List
from collections import Counter

""" 使用哈希表统计次数""" 
class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        dict = {}
        for i in nums:
            if i in dict:
                dict[i] += 1
            else:
                dict[i] = 1
        res = 0
        for j in dict:
            if dict[j] == 1:
                res += j
        return res
    
""" 使用Counter功能记录每个元素的出现次数""" 
class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        return sum(num for (num, time) in Counter(nums).items() if time == 1)

if __name__ == "__main__":
    nums = [1,2,3,2]
    sol = Solution()
    result = sol.sumOfUnique(nums)
    print(result)