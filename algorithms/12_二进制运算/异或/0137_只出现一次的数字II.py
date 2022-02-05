"""
https://leetcode-cn.com/problems/single-number-ii/

给你一个整数数组 nums ，除某个元素仅出现 一次 外，其余每个元素都恰出现 三次 。请你找出并返回那个只出现了一次的元素。

示例 1：
    输入：nums = [2,2,3,2]
    输出：3

示例 2：
    输入：nums = [0,1,0,1,0,1,99]
    输出：99

提示：
    1 <= nums.length <= 3 * 10^4
    -2^31 <= nums[i] <= 2^31 - 1
    nums 中，除某个元素仅出现 一次 外，其余每个元素都恰出现 三次

进阶：
    你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？

"""
from typing import List
from collections import Counter

    
""" 方法1：依次确定每一个二进制位
    由于数组中的元素都在 int（即 32 位整数）范围内，因此我们可以依次计算答案的每一个二进制位是 0 还是 1"""
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for i in range(32):
            total = sum((num >> i) & 1 for num in nums) # 使用位运算得到 x 的第 i 个二进制位, 并将它们相加
            if total % 3:                               # 再对 3 取余
                # Python 这里对于最高位需要特殊判断
                if i == 31:
                    ans -= (1 << i)
                else:
                    ans |= (1 << i)
        return ans

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        b1,b2 = 0,0 # 出现一次的位，和两次的位
        for n in nums:
            b1 = (b1 ^ n) & ~ b2 # 既不在出现一次的b1，也不在出现两次的b2里面，我们就记录下来，出现了一次，再次出现则会抵消
            b2 = (b2 ^ n) & ~ b1 # 既不在出现两次的b2里面，也不再出现一次的b1里面(不止一次了)，记录出现两次，第三次则会抵消
        return b1

if __name__ == "__main__":
    nums = [0,1,0,1,0,1,99]
    sol = Solution()
    result = sol.singleNumber(nums)
    print(result)