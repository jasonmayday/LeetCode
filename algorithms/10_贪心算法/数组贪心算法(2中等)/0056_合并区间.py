"""
https://leetcode-cn.com/problems/merge-intervals/

以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi] 。请你合并所有重叠的区间，并返回一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间。

示例 1：
    输入：intervals = [[1,3],[2,6],[8,10],[15,18]]
    输出：[[1,6],[8,10],[15,18]]
    解释：区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].

示例 2：
    输入：intervals = [[1,4],[4,5]]
    输出：[[1,5]]
    解释：区间 [1,4] 和 [4,5] 可被视为重叠区间。

提示：
    1 <= intervals.length <= 10^4
    intervals[i].length == 2
    0 <= starti <= endi <= 10^4

"""
from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])    # 按照区间的左端点排序
        merged = []     # 用数组 merged 存储最终的答案
        for interval in intervals: 
            # 如果列表为空，或者当前区间与上一区间不重合，直接添加
            if not merged or merged[-1][1] < interval[0]:   # merged[-1][1] 为 merged 数组中最后一个区间的右端
                merged.append(interval)
            
            else:   # 否则的话，它们重合，我们就可以与上一区间进行合并
                merged[-1][1] = max(merged[-1][1], interval[1])     # 用当前区间的右端点更新数组 merged 中最后一个区间的右端点，将其置为二者的较大值。
        return merged

""" 贪心算法
    排序之后局部最优：每次合并都取最大的右边界，这样就可以合并更多的区间了
    整体最优：合并所有重叠的区间。"""
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 0:
            return intervals
        intervals.sort(key=lambda x: x[0])  # 按照区间的左端点排序  [[1, 3], [2, 6], [8, 10], [15, 18]]
        result = []
        result.append(intervals[0])         # 先把第一个区间添加进答案 [1, 3]
        for i in range(1, len(intervals)):  # 遍历之后的区间
            last = result[-1]               # 上一个区间
            if last[1] >= intervals[i][0]:  # 如果上一个区间的右边 >= 要遍历的区间的左边 （3>2）
                result[-1] = [last[0], max(last[1], intervals[i][1])]   # 合并区间
            else:
                result.append(intervals[i])
        return result

if __name__ == "__main__":
    intervals = [[1,3],[2,6],[8,10],[15,18]]
    sol = Solution()
    result = sol.merge(intervals)
    print (result)