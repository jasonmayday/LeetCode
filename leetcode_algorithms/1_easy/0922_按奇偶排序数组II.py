"""
https://leetcode-cn.com/problems/sort-array-by-parity-ii/

给定一个非负整数数组 A， A 中一半整数是奇数，一半整数是偶数。

对数组进行排序，以便当 A[i] 为奇数时，i 也是奇数；当 A[i] 为偶数时， i 也是偶数。

你可以返回任何满足上述条件的数组作为答案。

示例：
    输入：[4,2,5,7]
    输出：[4,5,2,7]
    解释：[4,7,2,5]，[2,5,4,7]，[2,7,4,5] 也会被接受。

提示：
    2 <= A.length <= 20000
    A.length % 2 == 0
    0 <= A[i] <= 1000

"""
from typing import List

"""方法1: 两个辅助数组"""
class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)   # 初始化一个数组存放答案
        evenIndex = 0           # 偶数下标
        oddIndex = 1            # 奇数下标
        for i in range(len(nums)):
            if nums[i] % 2:     # 奇数
                res[oddIndex] = nums[i]     # 把该奇数放到新数组的 i 位置
                oddIndex += 2               # 下标加2，新下标还是奇数
            else:               # 偶数
                res[evenIndex] = nums[i]    # 把该偶数放到新数组的 i 位置
                evenIndex += 2              # 下标加2，新下标还是偶数
        return res

"""方法2: 在原数组上修改"""
class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        oddIndex = 1
        for i in range(0, len(nums), 2):    # 遍历步长为2，从0开始，所以都为偶数位
            if nums[i] % 2:                 # 偶数位遇到奇数
                while nums[oddIndex] % 2:   # 奇数位找偶数
                    oddIndex += 2
                nums[i], nums[oddIndex] = nums[oddIndex], nums[i]
        return nums

if __name__ == "__main__":
    nums = [1,3,6]
    k = 3
    sol = Solution()
    result = sol.sortArrayByParityII(nums)
    print (result)