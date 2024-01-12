"""
https://leetcode-cn.com/problems/kLl5u1/

给定一个已按照 升序排列  的整数数组 numbers ，请你从数组中找出两个数满足相加之和等于目标数 target 。

函数应该以长度为 2 的整数数组的形式返回这两个数的下标值。numbers 的下标 从 0 开始计数 ，所以答案数组应当满足 0 <= answer[0] < answer[1] < numbers.length 。

假设数组中存在且只存在一对符合条件的数字，同时一个数字不能使用两次。

示例 1：
    输入：numbers = [1,2,4,6,10], target = 8
    输出：[1,3]
    解释：2 与 6 之和等于目标数 8 。因此 index1 = 1, index2 = 3 。

示例 2：
    输入：numbers = [2,3,4], target = 6
    输出：[0,2]

示例 3：
    输入：numbers = [-1,0], target = -1
    输出：[0,1]

提示：
    2 <= numbers.length <= 3 * 10^4
    -1000 <= numbers[i] <= 1000
    numbers 按 递增顺序 排列
    -1000 <= target <= 1000
    仅存在一个有效答案
 
注意：本题与主站 167 题相似（下标起点不同）：https://leetcode-cn.com/problems/two-sum-ii-input-array-is-sorted/

"""
from typing import List

""" 二分查找"""
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            low  = i + 1
            high = len(numbers) - 1
            while low <= high:
                mid = (low + high) // 2                 # 可以首先固定第一个数
                if numbers[mid] == target - numbers[i]: # 然后寻找第二个数，第二个数等于目标值减去第一个数的差
                    return [i, mid]
                elif numbers[mid] > target - numbers[i]:
                    high = mid - 1
                else:
                    low = mid + 1
        return [-1, -1]

""" 双指针"""
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        low, high = 0, len(numbers) - 1             # 初始时两个指针分别指向第一个元素位置和最后一个元素的位置
        while low < high:
            total = numbers[low] + numbers[high]    # 每次计算两个指针指向的两个元素之和
            if total == target:                     # 如果两个元素之和等于目标值
                return [low, high]                  # 则发现了唯一解
            elif total < target:                    # 如果两个元素之和小于目标值
                low += 1                            # 则将左侧指针右移一位
            else:                                   # 如果两个元素之和大于目标值
                high -= 1                           # 则将右侧指针左移一位
        return [-1, -1]

if __name__ == "__main__":
    numbers = [2,7,11,15]
    target = 9
    sol = Solution()
    result = sol.twoSum(numbers, target)
    print(result)