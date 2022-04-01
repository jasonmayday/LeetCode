"""
https://leetcode-cn.com/problems/4sum/

给你一个由 n 个整数组成的数组 nums ，和一个目标值 target 。
请你找出并返回满足下述全部条件且不重复的四元组 [nums[a], nums[b], nums[c], nums[d]] （若两个四元组元素一一对应，则认为两个四元组重复）：
    0 <= a, b, c, d < n
    a、b、c 和 d 互不相同
    nums[a] + nums[b] + nums[c] + nums[d] == target

你可以按 任意顺序 返回答案 。

示例 1：
    输入：nums = [1,0,-1,0,-2,2], target = 0
    输出：[[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

示例 2：
    输入：nums = [2,2,2,2,2], target = 8
    输出：[[2,2,2,2]]

提示：
    1 <= nums.length <= 200
    -10^9 <= nums[i] <= 10^9
    -10^9 <= target <= 10^9

"""
from typing import List

"""排序+双指针"""
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        quadruplets = list()            # 定义一个返回值
        if not nums or len(nums) < 4:
            return quadruplets
        
        nums.sort()
        length = len(nums)
        
        # 定义4个指针i, j, left, right。  i 从 0 开始遍历,j 从 i+1 开始遍历,留下 left 和 right 作为双指针
        for i in range(length - 3):
            if i > 0 and nums[i] == nums[i - 1]: # 当i的值与前面的值相等时忽略
                continue
            # 获取当前最小值,如果最小值比目标值大,说明后面越来越大的值根本没戏
            if nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target:
                break # 这里使用的break,直接退出此次循环,因为后面的数只会更大
            # 获取当前最大值,如果最大值比目标值小,说明后面越来越小的值根本没戏,忽略
            if nums[i] + nums[length - 3] + nums[length - 2] + nums[length - 1] < target:
                continue # 这里使用continue,继续下一次循环,因为下一次循环有更大的数
            # 第二层循环j,初始值指向i+1
            for j in range(i + 1, length - 2):
                if j > i + 1 and nums[j] == nums[j - 1]: # 当j的值与前面的值相等时忽略
                    continue
                if nums[i] + nums[j] + nums[j + 1] + nums[j + 2] > target:
                    break
                if nums[i] + nums[j] + nums[length - 2] + nums[length - 1] < target:
                    continue
                left, right = j + 1, length - 1
                # 双指针遍历,如果等于目标值,left++并去重,right--并去重,当当前和大于目标值时right--,当当前和小于目标值时left++
                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]
                    if total == target:
                        quadruplets.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1 # left先+1之后,和它前面的left-1进行比较,若后+1,则和它后面的left+1进行比较
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        right -= 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                    elif total < target:
                        left += 1
                    else:
                        right -= 1
        
        return quadruplets

if __name__ == "__main__":
    nums = [1,0,-1,0,-2,2]
    target = 0
    sol = Solution()
    result = sol.fourSum(nums, target)
    print (result)