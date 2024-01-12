"""
https://leetcode-cn.com/problems/top-k-frequent-elements/

给你一个整数数组 nums 和一个整数 k ，请你返回其中出现频率前 k 高的元素。你可以按 任意顺序 返回答案。

示例 1:
    输入: nums = [1,1,1,2,2,3], k = 2
    输出: [1,2]

示例 2:
    输入: nums = [1], k = 1
    输出: [1]

提示：
    1 <= nums.length <= 10^5
    k 的取值范围是 [1, 数组中不相同的元素的个数]
    题目数据保证答案唯一，换句话说，数组中前 k 个高频元素的集合是唯一的

进阶：你所设计算法的时间复杂度 必须 优于 O(n log n) ，其中 n 是数组大小。

"""
from typing import List
from collections import Counter
import heapq

""" 直接排序 """
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)   # {1: 3, 2: 2, 3: 1}
        return [item[0] for item in count.most_common(k)]
    
""" 堆排序 """
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)   # {1: 3, 2: 2, 3: 1}
        heap = [(val, key) for key, val in count.items()]
        return [item[1] for item in heapq.nlargest(k, heap)]
    
""" 堆排序 """
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        heap = []   # 定义一个小顶堆，大小为k
        for key, val in count.items():
            heapq.heappush(heap, (val, key))
            if len(heap) > k:           # 如果堆的大小大于了 k
                heapq.heappop(heap)     # 则队列弹出，保证堆的大小一直为 k
            # print (heap)     [(2, 2), (3, 1)]
        return [item[1] for item in heap]

if __name__ == "__main__":
    nums = [1,1,1,2,2,3]
    k = 2
    sol = Solution()
    result = sol.topKFrequent(nums, k)
    print (result)