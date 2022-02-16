"""
https://leetcode-cn.com/problems/product-of-array-except-self/

给你一个整数数组 nums，返回 数组 answer ，其中 answer[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积 。

题目数据 保证 数组 nums之中任意元素的全部前缀元素和后缀的乘积都在  32 位 整数范围内。

请不要使用除法，且在 O(n) 时间复杂度内完成此题。

示例 1:
    输入: nums = [1,2,3,4]
    输出: [24,12,8,6]

示例 2:
    输入: nums = [-1,1,0,-3,3]
    输出: [0,0,9,0,0]

提示：
    2 <= nums.length <= 10^5
    -30 <= nums[i] <= 30
    保证 数组 nums之中任意元素的全部前缀元素和后缀的乘积都在  32 位 整数范围内

进阶：你可以在 O(1) 的额外空间复杂度内完成这个题目吗？（ 出于对空间复杂度分析的目的，输出数组不被视为额外空间。）

"""

"""
这似乎是一个简单的问题，可以在线性时间和空间内解决。先计算给定数组所有元素的乘积，然后对数组中的每个元素 x，将总的乘积除以 x 来求得除自身值的以外数组的乘积。

然而这样的解决方法有一个问题，就是如果输入数组中出现 0，那么这个方法就失效了。而且在问题中说明了不允许使用除法运算。这增加了这个问题的难度。
"""
from typing import List

""" 乘积 = 当前数左边的乘积 * 当前数右边的乘积"""
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        
        k = 1   # 刚开始左边没有元素，所以 k = 1
        for i in range(len(nums)):
            res.append(k)
            k = k * nums[i]         # 此时 res[i] 存储的是 下标 i 左侧所有元素乘积    [1, 1, 2, 6] 
        
        k = 1   # 刚开始右边没有元素，所以 k = 1
        for i in range(len(nums))[::-1]:
            res[i] = res[i]* k  # k 为 下标 i 元素右边所有数字的乘积。
            k = k * nums[i]     # 此时数组等于左边的 * 该数右边的。所以计算下一个结果时需要将当前值乘到 k 上
        
        return res

""" 左右乘积列表 """         
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        
        # L 和 R 分别表示左右两侧的乘积列表
        L, R, res = [0]*length, [0]*length, [0]*length
        
        L[0] = 1            # L[i] 为索引 i 左侧所有元素的乘积，L[0]左侧没有元素，所以 L[0] = 1
        for i in range(1, length):
            L[i] = nums[i-1] * L[i-1]   # 更新左侧元素的乘积
        
        R[length-1] = 1     # R[i] 为索引 i 右侧所有元素的乘积，R[length-1] 右侧没有元素，所以 R[length-1] = 1
        for i in reversed(range(length - 1)):
            R[i] = nums[i+1] * R[i+1]   # 更新右侧元素的乘积

        
        for i in range(length):     # 对于索引 i
            res[i] = L[i] * R[i]    # 除 nums[i] 之外其余各元素的乘积就是左侧所有元素的乘积乘以右侧所有元素的乘积
        
        return res
         

if __name__ == "__main__":
    nums = [1,2,3,4]
    sol = Solution()
    result = sol.productExceptSelf(nums)
    print (result)  