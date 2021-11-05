'''
https://leetcode-cn.com/problems/missing-number/

给定一个包含 [0, n] 中 n 个数的数组 nums ，找出 [0, n] 这个范围内没有出现在数组中的那个数。

示例 1：
    输入：nums = [3,0,1]
    输出：2
    解释：n = 3，因为有 3 个数字，所以所有的数字都在范围 [0,3] 内。2 是丢失的数字，因为它没有出现在 nums 中。

示例 2：
    输入：nums = [0,1]
    输出：2
    解释：n = 2，因为有 2 个数字，所以所有的数字都在范围 [0,2] 内。2 是丢失的数字，因为它没有出现在 nums 中。

示例 3：
    输入：nums = [9,6,4,2,3,5,7,0,1]
    输出：8
    解释：n = 9，因为有 9 个数字，所以所有的数字都在范围 [0,9] 内。8 是丢失的数字，因为它没有出现在 nums 中。

示例 4：
    输入：nums = [0]
    输出：1
    解释：n = 1，因为有 1 个数字，所以所有的数字都在范围 [0,1] 内。1 是丢失的数字，因为它没有出现在 nums 中。

提示：
    n == nums.length
    1 <= n <= 10^4
    0 <= nums[i] <= n
    nums 中的所有数字都 独一无二

'''
from typing import List

class Solution:
    # 解法1：排序
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()                       # 将数组排序
        for i, num in enumerate(nums):    # enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中。
            if num != i:                  # 根据数组中每个下标处的元素是否和下标相等，得到丢失的数字。
                return i
        return num

    # 解法2：哈希集合
    def missingNumber(self, nums: List[int]) -> int:
        s = set(nums)                     # 遍历数组 nums，将数组中的每个元素加入哈希集合
        for i in range(len(nums) + 1):    # 依次检查从 0 到 n 的每个整数是否在哈希集合中
            if i not in s:                # 不在哈希集合中的数字即为丢失的数字
                return i

    # 解法3：哈希集合
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        total = n * (n + 1) // 2          # 将从 0 到 n 的全部整数之和记为 total，根据高斯求和公式，有 total = n*(n+1)/2
        arrSum = sum(nums)                # 将数组 nums 的元素之和记为 arrSum，则 arrSum 比 total 少了丢失的一个数字
        return total - arrSum             # 因此丢失的数字即为 total 与 arrSum 之差


if __name__ == "__main__":
    nums = [9,6,4,2,3,5,7,0,1]
    sol = Solution()
    result = sol.missingNumber(nums)
    print (result) 