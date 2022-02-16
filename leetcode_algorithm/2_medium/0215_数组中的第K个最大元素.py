"""
https://leetcode-cn.com/problems/kth-largest-element-in-an-array/

给定整数数组 nums 和整数 k，请返回数组中第 k 个最大的元素。

请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。

示例 1:
    输入: [3,2,1,5,6,4] 和 k = 2
    输出: 5

示例 2:
    输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
    输出: 4

提示：
    1 <= k <= nums.length <= 10^4
    -10^4 <= nums[i] <= 10^4

"""
import heapq
from typing import List

""" 堆排序
    维护一个大小为k的最小堆，堆顶是这k个数里的最小的，遍历完数组后返回堆顶元素即可"""
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)
        return heap[0]

if __name__ == "__main__":
    nums = [3,2,3,1,2,4,5,5,6]
    k = 4
    sol = Solution()
    result = sol.findKthLargest(nums, k)
    print (result)