"""
https://leetcode-cn.com/problems/shu-zu-zhong-zhong-fu-de-shu-zi-lcof/

找出数组中重复的数字。

在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。请找出数组中任意一个重复的数字。

示例 1：
    输入：
    [2, 3, 1, 0, 2, 5, 3]
    输出：2 或 3

限制：
    2 <= n <= 100000

"""
from typing import List

from pyparsing import nums

""" 方法一： 先排序，然后看相邻元素是否有相同的，有直接return。
    不过很慢，时间O(nlogn)，空间O(1)"""
class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        nums.sort()
        pre = nums[0]
        n = len(nums)
        for index in range(1, n):
            if pre == nums[index]:
                return pre
            pre = nums[index]

""" 方法二：哈希表
    时间O(n)，空间O（n）"""
class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        repeatDict = {}
        for num in nums:
            if num not in repeatDict:   # 如果不在哈希表中，说明第一次出现
                repeatDict[num] = 1     # key为数字，value为次数，次数为1
            else:
                return num

class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        dic = set()
        for num in nums:
            if num in dic: return num
            dic.add(num)
        return -1

""" 方法三：原地交换
    时间复杂度O(n)，空间复杂度O(1)。
    即 在一个长度为 n 的数组 nums 里的所有数字都在 0 ~ n-1 的范围内 。 此说明含义：数组元素的 索引 和 值 是 一对多 的关系。
    因此，可遍历数组并通过交换操作，使元素的 索引 与 值 一一对应（即 nums[i] = inums[i]=i ）。因而，就能通过索引映射对应的值，起到与字典等价的作用。
"""
class Solution:
    def findRepeatNumber(self, nums) -> int:
        i = 0
        while i < len(nums):    # 遍历数组 nums，设索引初始值为 i=0 :
            if nums[i] == i:    # 若 nums[i] = i ： 说明此数字已在对应索引位置，无需交换，因此跳过；
                i += 1
                continue
            if nums[nums[i]] == nums[i]:    # 若 nums[nums[i]]=nums[i]：代表索引 nums[i] 处和索引 i 处的元素值都为 nums[i]
                return nums[i]              # 即找到一组重复值，返回此值 nums[i] ；
            nums[nums[i]], nums[i] = nums[i], nums[nums[i]] # 否则：交换索引为 i 和 nums[i] 的元素值，将此数字交换至对应索引位置。
        return -1


if __name__ == "__main__":
    nums = [2, 3, 1, 0, 2, 5, 3]
    sol = Solution()
    result = sol.findRepeatNumber(nums)
    print (result)