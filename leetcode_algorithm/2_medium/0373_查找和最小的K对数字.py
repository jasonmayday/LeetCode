"""
https://leetcode-cn.com/problems/find-k-pairs-with-smallest-sums/

给定两个以升序排列的整数数组 nums1 和 nums2 , 以及一个整数 k 。

定义一对值 (u,v)，其中第一个元素来自 nums1，第二个元素来自 nums2 。

请找到和最小的 k 个数对 (u1,v1),  (u2,v2)  ...  (uk,vk) 。

示例 1:
    输入: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
    输出: [1,2],[1,4],[1,6]
    解释: 返回序列中的前 3 对数：
        [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]

示例 2:
    输入: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
    输出: [1,1],[1,1]
    解释: 返回序列中的前 2 对数：
         [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]

示例 3:
    输入: nums1 = [1,2], nums2 = [3], k = 3
    输出: [1,3],[2,3]
    解释: 也可能序列中所有的数对都被返回:[1,3],[2,3]
 
提示:
    1 <= nums1.length, nums2.length <= 10^4
    -10^9 <= nums1[i], nums2[i] <= 10^9
    nums1, nums2 均为升序排列
    1 <= k <= 1000

"""
from typing import List
from heapq import heappop
from heapq import heappush

"""方法一：优先队列"""
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        m, n = len(nums1), len(nums2)
        ans = []
        pq = [(nums1[i] + nums2[0], i, 0) for i in range(min(k, m))]
        while pq and len(ans) < k:
            _, i, j = heappop(pq)
            ans.append([nums1[i], nums2[j]])
            if j + 1 < n:
                heappush(pq, (nums1[i] + nums2[j + 1], i, j + 1))
        return ans
    
"""方法一：优先队列"""
class Solution:
    def kSmallestPairs(self, nums1, nums2, k):
        h = []
        def push(i, j):
            if i < len(nums1) and j < len(nums2):
                heappush(h, [nums1[i] + nums2[j], i, j])
        push(0, 0)
        pairs = []
        while h and len(pairs) < k:
            _, i, j = heappop(h)
            pairs.append([nums1[i], nums2[j]])
            push(i, j + 1)
            if j == 0: # 避免重复遍历
                push(i + 1, 0)
        return pairs
    
"""字典排序"""
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        len_1 , len_2 = len(nums1), len(nums2)
        dic = {}
        index = 0   # 该索引是为了记录是该和是两个数组中的哪两个元素的坐标
        for i in nums1:
            for j in nums2:
                dic[index] = i + j
                index += 1
        dic = dict(sorted(dic.items(), key=lambda item: item[1]))
        result = []
        if k > len_1 * len_2:
            k = len_1 * len_2
        for key in dic.keys():
            # u 在 nums1 中的位置
            i = key // len_2 
            # v 在 nums2 中的位置
            j = key % len_2 
            result.append([nums1[i], nums2[j]])
            k -= 1
            if k == 0:
                break
        return result

if __name__ == "__main__":
    nums1 = [1,7,11]
    nums2 = [2,4,6]
    k = 3
    sol = Solution()
    result = sol.kSmallestPairs(nums1, nums2, k)
    print (result) 