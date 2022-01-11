"""
https://leetcode-cn.com/problems/3sum/

给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有和为 0 且不重复的三元组。

注意：答案中不可以包含重复的三元组。

示例 1：
    输入：nums = [-1,0,1,2,-1,-4]
    输出：[[-1,-1,2],[-1,0,1]]

示例 2：
    输入：nums = []
    输出：[]

示例 3：
    输入：nums = [0]
    输出：[]

提示：
    0 <= nums.length <= 3000
    -10^5 <= nums[i] <= 10^5

"""
from typing import List

"""方法1：排序 + 双指针"""
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        ans = list()
        
        for a in range(n):      # 枚举 a
            if a > 0 and nums[a] == nums[a - 1]:    # 需要和上一次枚举的数不相同
                continue                            # 所以对于重复元素：跳过
            c = n - 1       # c 对应的指针初始指向数组的最右端
            target = -nums[a]
            for b in range(a + 1, n):   # 枚举 b
                if b > a + 1 and nums[b] == nums[b - 1]:        # 需要和上一次枚举的数不相同
                    continue
                while b < c and nums[b] + nums[c] > target:     # 需要保证 b 的指针在 c 的指针的左侧
                    c -= 1      # 向左移动指针，直到 a+b+c 不大于 0
                if b == c:      # 如果指针重合
                    break       # 随着 b 后续的增加，就不会有满足 a+b+c=0 并且 b<c 的 c 了，可以退出循环
                if nums[b] + nums[c] == target:
                    ans.append([nums[a], nums[b], nums[c]])
        return ans
    
"""方法2：排序 + 双指针"""
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        res = []
        
        for i in range(n):      # 枚举 a（剩下的操作都是建立在这个 a 值的基础上）
            if (nums[i] > 0):   # 若 nums[i] > 0
                return res      # 因为已经排序好，所以后面不可能有三个数加和等于 0，直接返回结果。
            if (i > 0 and nums[i] == nums[i - 1]):      # 需要和上一次枚举的数不相同
                continue                                # 所以对于重复元素：跳过
            L = i + 1   # 左指针初始为 i 右边一位
            R = n - 1   # 右指针初始为最后一位
            while(L < R):
                if(nums[i] + nums[L] + nums[R] == 0):           # 当有a+b+c = 0 时
                    res.append([nums[i], nums[L], nums[R]])     # 把数组加入答案
                    while(L < R and nums[L] == nums[L + 1]):    # 然后判断左界和右界是否和下一位置重复，去除重复解。并同时将 L,R 移到下一位置，寻找新的解
                        L = L + 1
                    while(L < R and nums[R] == nums[R - 1]):
                        R = R - 1
                    L = L + 1
                    R = R - 1
                elif(nums[i] + nums[L] + nums[R] > 0):      # 若和大于 0，说明 nums[R] 太大，R 左移
                    R = R - 1
                else:                                       # 若和小于 0，说明 nums[L] 太小，L 右移
                    L = L + 1
        return res

if __name__ == "__main__":
    nums = [-1,0,1,2,-1,-4]
    sol = Solution()
    result = sol.threeSum(nums)
    print (result)