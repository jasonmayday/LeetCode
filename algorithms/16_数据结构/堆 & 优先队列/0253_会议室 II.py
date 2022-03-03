"""
https://leetcode-cn.com/problems/meeting-rooms-ii/

给你一个会议时间安排的数组 intervals ，每个会议时间都会包括开始和结束的时间 intervals[i] = [starti, endi] ，返回 所需会议室的最小数量 。

示例 1：
    输入：intervals = [[0,30],[5,10],[15,20]]
    输出：2

示例 2：
    输入：intervals = [[7,10],[2,4]]
    输出：1

提示：
    1 <= intervals.length <= 10^4
    0 <= starti < endi <= 10^6

"""

from typing import List

""" 统计同时进行的会议 """
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        events = [(iv[0], 1) for iv in intervals] + [(iv[1], -1) for iv in intervals]
        print('events: ', events)   # [(0, 1), (5, 1), (15, 1), (30, -1), (10, -1), (20, -1)]
        events.sort()
        ans = 0
        cur = 0                 # 用cur表示当前进行的会议数量，
        for _, e in events:     # 遍历排序后的时间数组;
            cur += e            # 如果是开始时间，cur加一，如果是结束时间，cur减一
            ans = max(ans, cur)
        return ans

""" 优先队列
    首先按照开始时间排序，遍历会议，看当前会议的开始时间是否小于已经安排会议的最早结束时间，
        如果小于：则需增加会议室，同时添加当前结束时间到结束时间列表
        如果大于等于：则不需增加，但是需要将之前的最早结束时间替换为当前会议的结束时间
    因为每次都要找最早结束时间，所以我们用优先队列来存储结束时间列表 end_times
"""
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[0])   # 按照会议开始时间排序 [[0, 30], [5, 10], [15, 20]]
        n = len(intervals)
        end_times = [intervals[0][1]]
        ans = 1
        for i in range(1,n):
            if intervals[i][0] < end_times[0]:  # 会议开始时间比end_times中最早结束的还要早，需增加会议室
                ans += 1
                heapq.heappush(end_times, intervals[i][1])  # 把结束世界放入堆end_times中
            else:                               # 可以在最早结束的会议之后开始当前会议：
                heapq.heappop(end_times)        # 之前的最早结束时间变成当前会议结束的时间
                heapq.heappush(end_times, intervals[i][1])
        return ans

if __name__ == "__main__":
    intervals = [[0,30],[5,10],[15,20]]
    sol = Solution()
    result = sol.minMeetingRooms(intervals)
    print (result)