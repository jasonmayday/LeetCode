"""
https://leetcode-cn.com/problems/longest-consecutive-sequence/

给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。

请你设计并实现时间复杂度为 O(n) 的算法解决此问题。

示例 1：
    输入：nums = [100,4,200,1,3,2]
    输出：4
    解释：最长数字连续序列是 [1, 2, 3, 4]。它的长度为 4。

示例 2：
    输入：nums = [0,3,7,2,5,8,4,6,0,1]
    输出：9

提示：
    0 <= nums.length <= 10^5
    -10^9 <= nums[i] <= 10^9

"""
from typing import List

""" 哈希表 """
class Solution(object):
    def longestConsecutive(self, nums):
        hash_dict = dict()  # 用哈希表存储每个端点值对应连续区间的长度
        max_length = 0
        
        for num in nums:                    # 遍历数字
            if num not in hash_dict:        # (若数已在哈希表中：跳过不做处理) 若是新数加入：
                left = hash_dict.get(num - 1, 0)    # 获取当前数的最左边连续长度,没有的话就更新为0
                right = hash_dict.get(num + 1, 0)   # 获取当前数的最右边连续长度,没有的话就更新为0
                cur_length = 1 + left + right       # 计算当前数的区间长度（比如左右都没有连续的数字，则当前区间长度为1）
                hash_dict[num] = cur_length         # 把当前数加入哈希表，代表当前数字出现过
                
                if cur_length > max_length:     # 如果当前区间长度 大于 之前的最长序列
                    max_length = cur_length     # 更新最大长度 max_length 的值
                
                hash_dict[num - left] = cur_length  # 更新最左端点的值，如果left=n存在，那么证明当前数的前n个都存在哈希表中
                hash_dict[num + right] = cur_length # 更新最右端点的值，如果right=n存在，那么证明当前数的后n个都存在哈希表中
                                                    # 此时 [num-left，num-right] 范围的值都连续存在哈希表中了
        return max_length
    
    
""" 哈希表 """
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_length = 0
        num_set = set(nums)     # 集合去重

        for num in num_set:             # 遍历数字
            if num - 1 not in num_set:    # 如果 (数字-1) 不在集合中
                current_num = num       # 把该数字作为当前数字
                cur_length = 1          # 当前连续序列长度初始化为 1

                while current_num + 1 in num_set:
                    current_num += 1
                    cur_length += 1

                max_length = max(max_length, cur_length)

        return max_length


if __name__ == "__main__":
    nums = [100,4,200,1,3,2]
    sol = Solution()
    result = sol.longestConsecutive(nums)
    print (result)
    