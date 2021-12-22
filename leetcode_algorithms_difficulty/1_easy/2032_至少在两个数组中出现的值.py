"""
https://leetcode-cn.com/problems/two-out-of-three/

给你三个整数数组 nums1、nums2 和 nums3 ，请你构造并返回一个 与这三个数组都不同的 数组，且由 至少 在 两个 数组中出现的所有值组成。数组中的元素可以按 任意 顺序排列。

示例 1：
    输入：nums1 = [1,1,3,2], nums2 = [2,3], nums3 = [3]
    输出：[3,2]
    解释：至少在两个数组中出现的所有值为：
    - 3 ，在全部三个数组中都出现过。
    - 2 ，在数组 nums1 和 nums2 中出现过。

示例 2：
    输入：nums1 = [3,1], nums2 = [2,3], nums3 = [1,2]
    输出：[2,3,1]
    解释：至少在两个数组中出现的所有值为：
    - 2 ，在数组 nums2 和 nums3 中出现过。
    - 3 ，在数组 nums1 和 nums2 中出现过。
    - 1 ，在数组 nums1 和 nums3 中出现过。

示例 3：
    输入：nums1 = [1,2,2], nums2 = [4,3,3], nums3 = [5]
    输出：[]
    解释：不存在至少在两个数组中出现的值。

提示：
    1 <= nums1.length, nums2.length, nums3.length <= 100
    1 <= nums1[i], nums2[j], nums3[k] <= 100

"""
from typing import List
from collections import Counter

"""解法1：使用HashSet排除掉重复的元素"""
class Solution:
    def twoOutOfThree(self, nums1, nums2, nums3):
        nums = [0] * 101
        for n in nums1, nums2, nums3:
            for i in set(n):    # 使用HashSet排除掉重复的元素。
                nums[i] += 1
        return [idx for idx, v in enumerate(nums) if v > 1]

"""解法2：使用Counter统计"""
class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        set1 = set(nums1)
        set2 = set(nums2)
        set3 = set(nums3)
        count1 = Counter(set1)
        count2 = Counter(set2)
        count3 = Counter(set3)
        count = count1 + count2 + count3    # {3: 3, 2: 2, 1: 1}
        return [key for key, val in count.items() if val > 1] 

"""解法3：先set去重，然后 & 操作找同时存在的"""
class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        s1, s2, s3 = set(nums1), set(nums2), set(nums3)
        return list((s1 & s2) | (s1 & s3) | (s2 & s3))


if __name__ == "__main__":
    nums1 = [1,1,3,2]
    nums2 = [2,3]
    nums3 = [3]
    sol = Solution()
    result = sol.twoOutOfThree(nums1, nums2, nums3)
    print(result)