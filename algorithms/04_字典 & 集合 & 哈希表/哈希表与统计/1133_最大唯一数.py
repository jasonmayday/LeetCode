"""
https://leetcode-cn.com/problems/largest-unique-number/

给你一个整数数组 A，请找出并返回在该数组中仅出现一次的最大整数。

如果不存在这个只出现一次的整数，则返回 -1。

示例 1：
    输入：[5,7,3,9,4,9,8,3,1]
    输出：8
    解释：
    数组中最大的整数是 9，但它在数组中重复出现了。而第二大的整数是 8，它只出现了一次，所以答案是 8。

示例 2：
    输入：[9,9,8,8]
    输出：-1
    解释：
    数组中不存在仅出现一次的整数。

提示：
    1 <= A.length <= 2000
    0 <= A[i] <= 1000

"""
from typing import List

class Solution:
    def largestUniqueNumber(self, A: List[int]) -> int:
        from collections import Counter
        ans = -1
        for key, count in Counter(A).items():
            if count == 1:
                ans = max(ans, key)     # 更新答案
        return ans

class Solution(object):
    def largestUniqueNumber(self, A: List[int]) -> int:
        hash = {}
        for num in A:
            if num not in hash:
                hash[num] = 1
            else:
                hash[num] += 1
        max_value = -1
        for num in hash:
            if hash[num] == 1:
                max_value = max(num, max_value)
        return max_value