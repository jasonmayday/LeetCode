"""
https://leetcode-cn.com/problems/set-mismatch/

集合 s 包含从 1 到 n 的整数。不幸的是，因为数据错误，导致集合里面某一个数字复制了成了集合里面的另外一个数字的值，导致集合 丢失了一个数字 并且 有一个数字重复 。

给定一个数组 nums 代表了集合 S 发生错误后的结果。

请你找出重复出现的整数，再找到丢失的整数，将它们以数组的形式返回。

示例 1：
    输入：nums = [1,2,2,4]
    输出：[2,3]

示例 2：
    输入：nums = [1,1]
    输出：[1,2]
 
提示：
    2 <= nums.length <= 10^4
    1 <= nums[i] <= 10^4
    
"""

'''解法1: 纯数学'''
class Solution:
    def findErrorNums(self, nums):
        length = len(nums), 
        total = sum(set(nums))
        return [sum(nums) - total, (1 + length) * length // 2 - total]

'''解法1: 循环数组'''
class Solution:
    def findErrorNums(self, nums):
        length = len(nums)
        repeat = lose = -1
        nums.sort()     # 对数组进行排序
        if nums[0] != 1:                    # 丢失数字情况 1
            lose = 1                        # 当nums[0] != 1，丢失的数字是1
        elif nums[-1] != length:            # 丢失数字情况 2
            lose = length                   # 当nums[-1] != len(nums), 丢失的数字是len(nums)
        for i in range(1, length):
            if nums[i] == nums[i - 1]:      # 重复数字情况，只有一种情况
                repeat = nums[i]            # 重复的数字是 nums[i] == nums[i - 1]
            if nums[i] - nums[i - 1] == 2:  # 丢失数字情况 3
                lose = nums[i] - 1          # 当nums[i + 1] - nums[i] = 2时，丢失的数字为nums[i] + 1
        return [repeat, lose]

'''解法3: 哈希表'''
from collections import Counter
class Solution:
    def findErrorNums(self, nums):
        ln = len(nums)
        dic = Counter(nums)
        repeat = lose = -1
        for i in range(1, ln + 1):
            tmp = dic.get(i, 0)
            if tmp == 0:
                lose = i
            elif tmp == 2:
                repeat = i
        return [repeat, lose]

if __name__ == "__main__":
    nums = [1,2,2,4]
    sol = Solution()
    result = sol.findErrorNums(nums)
    print (result)