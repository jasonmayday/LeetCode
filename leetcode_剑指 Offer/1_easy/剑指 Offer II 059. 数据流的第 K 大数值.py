"""
https://leetcode-cn.com/problems/jBjn9C/

设计一个找到数据流中第 k 大元素的类（class）。注意是排序后的第 k 大元素，不是第 k 个不同的元素。

请实现 KthLargest 类：

    KthLargest(int k, int[] nums) 使用整数 k 和整数流 nums 初始化对象。
    int add(int val) 将 val 插入数据流 nums 后，返回当前数据流中第 k 大的元素。

示例：
    输入：
        ["KthLargest", "add", "add", "add", "add", "add"]
        [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
    输出：
        [null, 4, 5, 5, 8, 8]

    解释：
        KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
        kthLargest.add(3);   // return 4
        kthLargest.add(5);   // return 5
        kthLargest.add(10);  // return 5
        kthLargest.add(9);   // return 8
        kthLargest.add(4);   // return 8

提示：
    1 <= k <= 10^4
    0 <= nums.length <= 10^4
    -10^4 <= nums[i] <= 10^4
    -10^4 <= val <= 10^4
    最多调用 add 方法 10^4 次
    题目数据保证，在查找第 k 大元素时，数组中至少有 k 个元素

注意：本题与主站 703 题相同： https://leetcode-cn.com/problems/kth-largest-element-in-a-stream/

"""

from typing import List
import heapq

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        self.k = k
        for num in nums:
            heapq.heappush(self.heap, num)
            if len(self.heap) > k:
                heapq.heappop(self.heap)    # 非前 k 大的数据可以不存。

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]

if __name__ == "__main__":
    kthLargest = KthLargest(3, [4, 5, 8, 2])
    print(kthLargest.add(3))   # return 4
    print(kthLargest.add(5))   # return 5
    print(kthLargest.add(10))  # return 5
    print(kthLargest.add(9))   # return 8
    print(kthLargest.add(4))   # return 8