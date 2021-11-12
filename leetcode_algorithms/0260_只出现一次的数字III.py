'''
https://leetcode-cn.com/problems/single-number-iii/

给定一个整数数组 nums，其中恰好有两个元素只出现一次，其余所有元素均出现两次。 找出只出现一次的那两个元素。你可以按 任意顺序 返回答案。

进阶：你的算法应该具有线性时间复杂度。你能否仅使用常数空间复杂度来实现？

示例 1：
输入：nums = [1,2,1,3,2,5]
输出：[3,5]
解释：[5, 3] 也是有效的答案。

示例 2：
输入：nums = [-1,0]
输出：[-1,0]

示例 3：
输入：nums = [0,1]
输出：[1,0]

提示：
2 <= nums.length <= 3 * 104
-231 <= nums[i] <= 231 - 1
除两个只出现一次的整数外，nums 中的其他数字都出现两次

'''
nums = [1,2,1,3,2,5]

from typing import List
from collections import Counter

'''
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        freq = Counter(nums)
        return [num for num, occ in freq.items() if occ == 1]
'''

'''
异或解法：
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        single_number = 0
        for num in nums:
            single_number ^= num
        return single_number

'''
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        res = []                          # 新建一个数组
        hashmap = {}                      # 新建一个哈希表
        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1  # 用哈希表记录每个数出现的次数   # get()方法语法：dict.get(key, default=None)
        for num in hashmap:
            if hashmap[num] == 1:                   # 遍历哈希表，将次数为1的加入到结果中
                res.append(num)
        return res

sol = Solution()
result = sol.singleNumber(nums)
print (result)