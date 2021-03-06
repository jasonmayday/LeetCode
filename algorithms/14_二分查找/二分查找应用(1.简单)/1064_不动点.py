"""
https://leetcode-cn.com/problems/fixed-point/

给定已经按 升序 排列、由不同整数组成的数组 arr，返回满足 arr[i] == i 的最小索引 i。如果不存在这样的 i，返回 -1。

示例 1：
    输入：arr = [-10,-5,0,3,7]
    输出：3
    解释：对于给定的数组，arr[0] = -10，arr[1] = -5，arr[2] = 0，arr[3] = 3，因此输出为 3 。

示例 2：
    输入：arr = [0,2,5,8,17]
    输出：0
    解释：arr[0] = 0，因此输出为 0 。

示例 3：
    输入：arr = [-10,-5,3,4,7,9]
    输出：-1
    解释：不存在这样的 i 满足 arr[i] = i，因此输出为 -1 。

提示：
    1 <= arr.length < 10^4
    -10^9 <= arr[i] <= 10^9

"""
from typing import List

""" 二分法 """
class Solution:
    def fixedPoint(self, arr: List[int]) -> int:
        left = 0
        right = len(arr) - 1
        while left < right:
            mid = (left + right) // 2
            if arr[mid] >= mid:
                right = mid
            else:
                left = mid + 1
        return left if arr[left] == left else -1

if __name__ == "__main__":
    arr = [-10,-5,0,3,7]
    sol = Solution()
    result = sol.fixedPoint(arr)
    print(result)