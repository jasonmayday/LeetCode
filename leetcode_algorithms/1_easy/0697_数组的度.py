"""
https://leetcode-cn.com/problems/degree-of-an-array/

给定一个非空且只包含非负数的整数数组 nums，数组的度的定义是指数组里任一元素出现频数的最大值。

你的任务是在 nums 中找到与 nums 拥有相同大小的度的最短连续子数组，返回其长度。

示例 1：
    输入：[1, 2, 2, 3, 1]
    输出：2
    解释：
        输入数组的度是2，因为元素1和2的出现频数最大，均为2.
        连续子数组里面拥有相同度的有如下所示:
        [1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
        最短连续子数组[2, 2]的长度为2，所以返回2.

示例 2：
    输入：[1,2,2,3,1,4,2]
    输出：6

提示：
    nums.length 在1到 50,000 区间范围内。
    nums[i] 是一个在 0 到 49,999 范围内的整数。

数组的度：数组中各元素出现次数的最大值。对于示例二 [1,2,2,3,1,4,2] ：
数组中各元素出现的次数为： 1 出现 2 次， 2 出现 3 次， 3 出现 1 次， 4 出现 1 次，
所以数组的度为 3（就是元素 2 出现的次数）。

题目要求的是与 nums 拥有相同大小的度的最短连续子数组的长度。
比如对于示例二 [1,2,2,3,1,4,2]，数组的度为 3，
它的度为 3 的最短连续子数组是 [2,2,3,1,4,2] ，返回该子数组长度 6。

"""
from typing import List
import collections

"""字典（哈希表）计数，字典的 key 是元素，value 是该元素出现的次数。"""
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        left = dict()   # 使用 left 保存每个元素在数组中第一次出现的位置
        right = dict()  # 使用 right 保存每个元素在数组中最后一次出现的位置
        counter = collections.Counter()     # 使用 counter 保存每个元素出现的次数。
        for i, num in enumerate(nums):
            if num not in left:
                left[num] = i
            right[num] = i
            counter[num] += 1
        degree = max(counter.values())      # 数组的度 degree 等于 counter.values() 的最大值
        res = len(nums)
        for k, v in counter.items():        # 对counter再次遍历：
            if v == degree:     # 如果元素 k 出现的次数等于 degree，则找出元素 k 最后一次出现的位置 和 第一次出现的位置，计算两者之差+1，即为子数组长度
                res = min(res, right[k] - left[k] + 1)  # 对所有出现次数等于 degree 的子数组的最短长度，取 min
        return res

if __name__ == "__main__":      
    nums = [1, 2, 2, 3, 1]
    sol = Solution()
    result = sol.findShortestSubArray(nums)
    print(result)