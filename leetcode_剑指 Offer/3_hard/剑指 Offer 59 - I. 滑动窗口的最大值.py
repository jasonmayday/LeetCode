"""
https://leetcode-cn.com/problems/hua-dong-chuang-kou-de-zui-da-zhi-lcof/

给定一个数组 nums 和滑动窗口的大小 k，请找出所有滑动窗口里的最大值。

示例:
    输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
    输出: [3,3,5,5,6,7]
    解释:

    滑动窗口的位置                最大值
    ---------------               -----
    [1  3  -1] -3  5  3  6  7       3
     1 [3  -1  -3] 5  3  6  7       3
     1  3 [-1  -3  5] 3  6  7       5
     1  3  -1 [-3  5  3] 6  7       5
     1  3  -1  -3 [5  3  6] 7       6
     1  3  -1  -3  5 [3  6  7]      7

提示：
    你可以假设 k 总是有效的，在输入数组不为空的情况下，1 ≤ k ≤ 输入数组的大小。

注意：本题与主站 239 题相同：https://leetcode-cn.com/problems/sliding-window-maximum/

"""
from typing import List
from collections import deque
import heapq

"""方法一：优先队列（堆）"""
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        # 注意 Python 默认的优先队列是小根堆
        q = [(-nums[i], i) for i in range(k)]   # [(-1, 0), (-3, 1), (1, 2)]
        heapq.heapify(q)

        ans = [-q[0][0]]    # 存储二元组 (num, index)
        for i in range(k, n):
            heapq.heappush(q, (-nums[i], i))
            while q[0][1] <= i - k:
                heapq.heappop(q)
            ans.append(-q[0][0])
        
        return ans

""" 方法二：单调队列
    满足单调性的双端队列一般称作「单调队列」。"""

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums or k == 0:
            return []
        q = deque()
        
        ''' 未形成窗口'''
        for i in range(k):                  # 当滑动窗口向右移动时，我们需要把一个新的元素放入队列中
            while q and q[-1] < nums[i]:    # 为了保持 单调队列 的性质，不断地将(新的元素)与(队列队尾的元素)相比较，如果 新的元素 更大
                q.pop()                     # 那么 单调队列 队尾的元素就可以被永久地移除，直到队列为空或者新的元素小于队尾的元素。
            q.append(nums[i])       # deque 内的元素 非严格递减
        res = [q[0]]
        
        ''' 形成窗口后 '''
        for i in range(k, len(nums)):       
            if q[0] == nums[i - k]:
                q.popleft()
            while q and q[-1] < nums[i]:
                q.pop()
            q.append(nums[i])
            res.append(q[0])    # 第一个 滑动窗口 的答案
        return res

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        q = deque()
        
        ''' 未形成窗口'''
        for i in range(k):                      # 当滑动窗口向右移动时，我们需要把一个新的元素放入队列中
            while q and nums[i] >= nums[q[-1]]: # 为了保持 单调队列 的性质，不断地将(新的元素)与(队列队尾的元素)相比较，如果 新的元素 更大
                q.pop()                         # 那么 单调队列 队尾的元素就可以被永久地移除，直到队列为空或者新的元素小于队尾的元素。
            q.append(i)     # deque 内的元素 非严格递减

        ans = [nums[q[0]]]  # 第一个 滑动窗口 的答案
        
        ''' 形成窗口后 '''
        for i in range(k, n):
            while q and nums[i] >= nums[q[-1]]:
                q.pop()
            q.append(i)
            while q[0] <= i - k:
                q.popleft()
            ans.append(nums[q[0]])  # 每个窗口的最大值都在 单调队列 的 队首
        
        return ans
    

if __name__ == "__main__":
    nums = [1,3,-1,-3,5,3,6,7]
    k = 3
    sol = Solution()
    result = sol.maxSlidingWindow(nums, k)
    print(result)