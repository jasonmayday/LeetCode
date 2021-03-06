"""
https://leetcode-cn.com/problems/intersection-of-two-arrays

给定两个数组，编写一个函数来计算它们的交集。

示例 1：
    输入：nums1 = [1,2,2,1], nums2 = [2,2]
    输出：[2]

示例 2：
    输入：nums1 = [4,9,5], nums2 = [9,4,9,8,4]
    输出：[9,4]

说明：
    输出结果中的每个元素一定是唯一的。
    我们可以不考虑输出结果的顺序。

"""
from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result_set = set()
        set1 = set(nums1)
        for num in nums2:
            if num in set1:
                result_set.add(num) # set1里出现的nums2元素 存放到结果
        return result_set

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))    # 两个数组先变成集合，求交集后还原为数组

if __name__ == "__main__":
    nums1 = [4,9,5]
    nums2 = [9,4,9,8,4]
    sol = Solution()
    result = sol.intersection(nums1, nums2)
    print (result)