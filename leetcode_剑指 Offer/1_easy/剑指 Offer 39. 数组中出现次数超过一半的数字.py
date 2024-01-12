"""
https://leetcode-cn.com/problems/shu-zu-zhong-chu-xian-ci-shu-chao-guo-yi-ban-de-shu-zi-lcof/

数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。

你可以假设数组是非空的，并且给定的数组总是存在多数元素。

示例 1:
    输入: [1, 2, 3, 2, 2, 2, 5, 4, 2]
    输出: 2

限制：
    1 <= 数组长度 <= 50000

注意：本题与主站 169 题相同：https://leetcode-cn.com/problems/majority-element/

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