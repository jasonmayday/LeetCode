'''

给你一个非空数组，返回此数组中 第三大的数 。如果不存在，则返回数组中最大的数。

示例 1：
    输入：[3, 2, 1]
    输出：1
    解释：第三大的数是 1 。

示例 2：
    输入：[1, 2]
    输出：2
    解释：第三大的数不存在, 所以返回最大的数 2 。

示例 3：
    输入：[2, 2, 3, 1]
    输出：1
    解释：注意，要求返回第三大的数，是指在所有不同数字中排第三大的数。
    此例中存在两个值为 2 的数，它们都排第二。在所有不同数字中排第三大的数为 1 。

'''
from typing import List

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums.sort(reverse = True)
        diff = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                diff += 1
                if diff == 3:  # 此时 nums[i] 就是第三大的数
                    return nums[i]
        return nums[0]

if __name__ == "__main__":
    nums = [3, 5, 8, 91, 76, 2, 6, 2, 52, 7, 2, 1]
    sol = Solution()
    result = sol.thirdMax(nums)
    print (result)