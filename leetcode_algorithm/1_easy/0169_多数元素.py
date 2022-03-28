"""
https://leetcode-cn.com/problems/majority-element/

给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数 大于 ⌊ n/2 ⌋ 的元素。

你可以假设数组是非空的，并且给定的数组总是存在多数元素。

示例 1：
    输入：[3,2,3]
    输出：3

示例 2：
    输入：[2,2,1,1,1,2,2]
    输出：2
 
进阶：
    尝试设计时间复杂度为 O(n)、空间复杂度为 O(1) 的算法解决此问题。

"""
import random
import collections
from typing import List

""" 方法1：哈希表
    使用哈希映射（HashMap）来存储每个元素以及出现的次数。对于哈希映射中的每个键值对，键表示一个元素，值表示该元素出现的次数。"""
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = collections.Counter(nums)
        return max(counts.keys(), key = counts.get)

""" 方法2：排序"""
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()                     # 将数组 nums 中的所有元素按排序，
        return nums[len(nums) // 2]     # 那么下标为 n/2 的元素（下标从 0 开始）一定是众数

""" 方法3：随机化
    因为超过 ⌊ n/2 ⌋ 的数组下标被众数占据了，这样我们随机挑选一个下标对应的元素并验证，有很大的概率能找到众数。"""
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority_count = len(nums) // 2 # 出现一半的次数
        while True:
            candidate = random.choice(nums) # 随机挑选一个下标，检查它是否是众数
            if sum(1 for elem in nums if elem == candidate) > majority_count:
                return candidate

""" 方法4：分治 """

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        def majority_element_rec(lo, hi) -> int:
            # base case; the only element in an array of size 1 is the majority
            # element.
            if lo == hi:
                return nums[lo]

            # recurse on left and right halves of this slice.
            mid = (hi - lo) // 2 + lo
            left = majority_element_rec(lo, mid)
            right = majority_element_rec(mid + 1, hi)

            # if the two halves agree on the majority element, return it.
            if left == right:
                return left

            # otherwise, count each element and return the "winner".
            left_count = sum(1 for i in range(lo, hi + 1) if nums[i] == left)
            right_count = sum(1 for i in range(lo, hi + 1) if nums[i] == right)

            return left if left_count > right_count else right

        return majority_element_rec(0, len(nums) - 1)

""" 方法5：Boyer-Moore 摩尔投票算法"""
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate

if __name__ == "__main__":
    nums = [2,2,1,1,1,2,2]
    sol = Solution()
    result = sol.majorityElement(nums)
    print(result)