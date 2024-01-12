"""
https://leetcode-cn.com/problems/missing-number-in-arithmetic-progression/

在某个数组 arr 中，值符合等差数列的数值规律：在 0 <= i < arr.length - 1 的前提下，arr[i+1] - arr[i] 的值都相等。

我们会从该数组中删除一个 既不是第一个 也 不是最后一个的值，得到一个新的数组  arr。

给你这个缺值的数组 arr，返回 被删除的那个数 。

示例 1：
    输入：arr = [5,7,11,13]
    输出：9
    解释：原来的数组是 [5,7,9,11,13]。

示例 2：
    输入：arr = [15,13,12]
    输出：14
    解释：原来的数组是 [15,14,13,12]。

提示：
    3 <= arr.length <= 1000
    0 <= arr[i] <= 10^5
    给定的数组 保证 是一个有效的数组。

"""
from typing import List

""" 等差数列求和 """
class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        n = len(arr)
        origin_sum = (arr[0] + arr[-1]) * (n + 1) // 2
        cur_sum = sum(arr)
        return origin_sum - cur_sum

""" 公差 + 二分查找 """
class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        d = (arr[-1] - arr[0]) // len(arr)
        if d == 0:
            return arr[0]
        left, right = 0, len(arr)-1
        mid = (left + right) // 2
        while mid != left:
            if arr[mid] - arr[left] == (mid - left) * d:
                left = mid
            else:
                right = mid
            mid = (left + right) // 2
        return arr[mid] + d


if __name__ == "__main__":
    arr = [5,7,11,13]
    sol = Solution()
    result = sol.missingNumber(arr)
    print(result)