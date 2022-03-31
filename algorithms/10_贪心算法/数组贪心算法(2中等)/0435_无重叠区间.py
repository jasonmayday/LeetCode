"""
https://leetcode-cn.com/problems/non-overlapping-intervals/

给定一个区间的集合 intervals ，其中 intervals[i] = [starti, endi] 。返回 需要移除区间的最小数量，使剩余区间互不重叠 。

示例 1:
    输入: intervals = [[1,2],[2,3],[3,4],[1,3]]
    输出: 1
    解释: 移除 [1,3] 后，剩下的区间没有重叠。

示例 2:
    输入: intervals = [ [1,2], [1,2], [1,2] ]
    输出: 2
    解释: 你需要移除两个 [1,2] 来使剩下的区间没有重叠。

示例 3:
    输入: intervals = [ [1,2], [2,3] ]
    输出: 0
    解释: 你不需要移除任何区间，因为它们已经是无重叠的了。

提示:
    1 <= intervals.length <= 10^5
    intervals[i].length == 2
    -5 * 10^4 <= starti < endi <= 5 * 10^4

"""
from typing import List

""" 方法一：动态规划
    题目的要求等价于「选出最多数量的区间，使得它们互不重叠」"""
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        intervals.sort()    # 将所有的 n 个区间按照左端点从小到大进行排序
        n = len(intervals)
        dp = [1]             # dpi 表示「以区间 i 为最后一个区间，可以选出的区间数量的最大值」

        for i in range(1, n):
            dp.append(max((dp[j] for j in range(i) if intervals[j][1] <= intervals[i][0]), default = 0) + 1)

        return n - max(dp)

""" 方法二：贪心"""
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        ans = 1
        if not intervals:
            return 0
        
        intervals.sort(key = lambda x: x[1])  # 按照右边界排序 [[1, 2], [2, 3], [1, 3], [3, 4]]
        
        n = len(intervals)
        right = intervals[0][1] # 首个边界的右端点，并实时更新维护上一个选择区间的右端点right
        
        for i in range(1, n):
            if intervals[i][0] >= right:    # 如果当前遍历到的区间 [li, ri] 与上一个区间不重合
                ans += 1                    # 我们可以不断地寻找右端点在首个区间右端点左侧的新区间，将首个区间替换成该区间。
                right = intervals[i][1]     # 那么当我们无法替换时，首个区间就是所有可以选择的区间中右端点最小的那个区间。
        
        return n - ans

if __name__ == "__main__":
    intervals = [[1,2],[2,3],[3,4],[1,3]]
    sol = Solution()
    result = sol.eraseOverlapIntervals(intervals)
    print (result)