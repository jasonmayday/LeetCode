"""
https://leetcode-cn.com/problems/shuffle-an-array/

给你一个整数数组 nums ，设计算法来打乱一个没有重复元素的数组。

实现 Solution class:
    Solution(int[] nums) 使用整数数组 nums 初始化对象
    int[] reset() 重设数组到它的初始状态并返回
    int[] shuffle() 返回数组随机打乱后的结果

示例：
    输入
        ["Solution", "shuffle", "reset", "shuffle"]
        [[[1, 2, 3]], [], [], []]
    
    输出
        [null, [3, 1, 2], [1, 2, 3], [1, 3, 2]]

    解释
        Solution solution = new Solution([1, 2, 3]);
        solution.shuffle();    // 打乱数组 [1,2,3] 并返回结果。任何 [1,2,3]的排列返回的概率应该相同。例如，返回 [3, 1, 2]
        solution.reset();      // 重设数组到它的初始状态 [1, 2, 3] 。返回 [1, 2, 3]
        solution.shuffle();    // 随机返回数组 [1, 2, 3] 打乱后的结果。例如，返回 [1, 3, 2]
 
提示：
    1 <= nums.length <= 200
    -10^6 <= nums[i] <= 10^6
    nums 中的所有元素都是 唯一的
    最多可以调用 5 * 10^4 次 reset 和 shuffle

"""
from typing import List
import random

'''Fisher–Yates算法'''
class Solution:
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.original = nums.copy()
        
    def __str__(self):
        return str(self.nums)
    
    def reset(self) -> List[int]:
        self.nums = self.original.copy()    # 返回初始化时的数组
        return self.nums

    def shuffle(self) -> List[int]:
        for i in range(len(self.nums)): # 循环 n 次，在第 i 次循环中（0 ≤ i < n）
            j = random.randrange(i, len(self.nums))                 # 在 [i,n) 中随机抽取一个下标 j
            self.nums[i], self.nums[j] = self.nums[j], self.nums[i] # 将第 i 个元素与第 j 个元素交换
        # nums[0 .. i−1] 的部分为乱序后的数组，其长度为 i
        # nums[i .. n−1] 的部分为待乱序的数组，其长度为 n-i
        return self.nums

if __name__ == "__main__":
    solution = Solution([1, 2, 3])
    solution.shuffle()
    print (solution)
    solution.reset()
    print (solution)
    solution.shuffle()
    print (solution)