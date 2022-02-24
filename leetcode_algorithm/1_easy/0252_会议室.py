"""
https://leetcode-cn.com/problems/meeting-rooms/

给定一个会议时间安排的数组 intervals ，每个会议时间都会包括开始和结束的时间 intervals[i] = [starti, endi] ，请你判断一个人是否能够参加这里面的全部会议。

示例 1：
    输入：intervals = [[0,30],[5,10],[15,20]]
    输出：false

示例 2：
    输入：intervals = [[7,10],[2,4]]
    输出：true

提示：
    0 <= intervals.length <= 10^4
    intervals[i].length == 2
    0 <= starti < endi <= 10^6

"""
from typing import List

class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key = lambda x:x[0]) # 根据会议开始时间排序
        return all(intervals[i-1][1] <= intervals[i][0] for i in range(1, len(intervals)))

class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()
        for i in range(1,len(intervals)):
            if intervals[i][0] < intervals[i-1][1]:
                return False
        return True

if __name__ == "__main__":
    intervals = [[7,10],[2,4]]
    sol = Solution()
    result = sol.canAttendMeetings(intervals)
    print(result)