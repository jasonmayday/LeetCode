'''

给定一个大小为 n 的整数数组，找出其中所有出现超过 ⌊ n/3 ⌋ 次的元素。

示例 1：
输入：[3,2,3]
输出：[3]

示例 2：
输入：nums = [1]
输出：[1]

示例 3：
输入：[1,1,1,3,3,2,2,2]
输出：[1,2]

'''
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        convene = {}       # 新建一个hash表来存储每个元素出现的次数
        n = len(nums) // 3 # 计算出众数次数
        result = []
        for num in nums:   # 遍历原始数组，如果hash里存在，则计数器+1
            if num in convene:
                convene[num] += 1 
            else:
                convene[num] = 1
            if convene[num] > n:   # 当前元素满足众数条件，直接将结果追加进result里
                result.append(num) # 重要！追加后记得将当前元素出现的次数置为最小值
                convene[num] = - len(nums) 
        return result

if __name__ == "__main__":
    nums = [1,1,1,3,3,2,2,2]
    sol = Solution()
    result = sol.majorityElement(nums)
    print(result)
