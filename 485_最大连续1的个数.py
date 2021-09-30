'''
https://leetcode-cn.com/problems/max-consecutive-ones/

给定一个二进制数组， 计算其中最大连续 1 的个数。

示例：
输入：[1,1,0,1,1,1]
输出：3
解释：开头的两位和最后的三位都是连续 1 ，所以最大连续 1 的个数是 3.

'''

from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxCount = count = 0

        for i, num in enumerate(nums):
            if num == 1:
                count += 1  # 两个值相加，然后返回值给符号左侧的变量。在这里 count = count + 1
            else:
                maxCount = max(maxCount, count)
                count = 0
        
        maxCount = max(maxCount, count)
        return maxCount

sol = Solution()
result = sol.findMaxConsecutiveOnes([1,1,0,1,1,1,0,0,1,1])
print(result)