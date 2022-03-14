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
    2 <= nums.length <= 3 * 10^4
    -2^31 <= nums[i] <= 2^31 - 1
    除两个只出现一次的整数外，nums 中的其他数字都出现两次

'''


from typing import List
from collections import Counter

""" 哈希表：Counter函数 """
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        return [num for (num, occ) in count.items() if occ == 1]
    
    
""" 哈希表 """
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


""" 异或
    0 ^ a = a
    a ^ a = 0
"""
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        for num in nums:    # 先遍历数组对所有数异或
            xor ^= num      # 得到两个只出现一次的数的异或结果 xor = 3 ^ 5 = 6  0b 110
        rightOne = xor & - xor  # 通过eor & - eor取得eor的最右边的1，，令其为 rightOne
        res = 0                 # 因为两个数对应位不同异或后该位才会为1，所以rightOne对应位在两个数中一定是一个为0，一个为1，这是在为后面分组做准备
        for num in nums:            # 再遍历数组，每个数和rightOne与
            if num & rightOne != 0: # 将所有数分成与运算后为0和为1两组，要找的两个数分别在两组
                res ^= num          # 把其中一组的所有数异或
        return [res, res ^ xor]     # 得到其中一个要找的数res，另一个数即为res ^ eor


if __name__ == "__main__":
    nums = [1,2,1,3,2,5]
    sol = Solution()
    result = sol.singleNumber(nums)
    print (result)