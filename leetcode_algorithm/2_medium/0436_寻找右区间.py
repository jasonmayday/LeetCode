"""
https://leetcode-cn.com/problems/find-right-interval/

给你一个区间数组 intervals ，其中 intervals[i] = [starti, endi] ，且每个 starti 都 不同 。

区间 i 的 右侧区间 可以记作区间 j ，并满足 startj >= endi ，且 startj 最小化 。

返回一个由每个区间 i 的 右侧区间 的最小起始位置组成的数组。如果某个区间 i 不存在对应的 右侧区间 ，则下标 i 处的值设为 -1 。

示例 1：
    输入：intervals = [[1,2]]
    输出：[-1]
    解释：集合中只有一个区间，所以输出-1。

示例 2：
    输入：intervals = [[3,4],[2,3],[1,2]]
    输出：[-1,0,1]
    解释：对于 [3,4] ，没有满足条件的“右侧”区间。
    对于 [2,3] ，区间[3,4]具有最小的“右”起点;
    对于 [1,2] ，区间[2,3]具有最小的“右”起点。

示例 3：
    输入：intervals = [[1,4],[2,3],[3,4]]
    输出：[-1,2,-1]
    解释：对于区间 [1,4] 和 [3,4] ，没有满足条件的“右侧”区间。
    对于 [2,3] ，区间 [3,4] 有最小的“右”起点。

提示：
    1 <= intervals.length <= 2 * 10^4
    intervals[i].length == 2
    -10^6 <= starti <= endi <= 10^6
    每个间隔的起点都 不相同

"""
from typing import List

""" hash + 排序 + 二分查找"""
class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
         
        def binarySearch(nums,target):  # 二分查找函数
            n = len(nums)
            if nums[n-1] < target:
                return float('inf')     # 刨除特例，返回inf，返回-1遇见区间为负的用例会踩坑
            l, r = 0, n - 1
            while l < r:
                mid = (l + r) >> 1
                if nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid
            # 这里返回 nums[l], 返回的是 starts 的值而不是下标
            # 例如 starts = [1,2,3] binareSearch(starts, 2) = 2 而不是下标1
            return nums[l]
        
        n = len(intervals)
        
        # 建立哈希表存储start的下标
        starts = []
        for i in intervals:
            starts.append(i[0])
        hashmap = {}
        for i in range(n):
            hashmap[starts[i]] = i
        
        starts.sort()   # 排序，后面二分查找

        res = [0] * n
        for i in range(n):
            val = binarySearch(starts,intervals[i][1])
            res[i] = hashmap[val] if val != float('inf') else -1
        return res

if __name__ == "__main__":
    intervals = [[1,4],[2,3],[3,4]]
    sol = Solution()
    result = sol.findRightInterval(intervals)
    print (result)