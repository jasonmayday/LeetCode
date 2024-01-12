"""
https://leetcode-cn.com/problems/number-of-students-doing-homework-at-a-given-time/

给你两个整数数组 startTime（开始时间）和 endTime（结束时间），并指定一个整数 queryTime 作为查询时间。

已知，第 i 名学生在 startTime[i] 时开始写作业并于 endTime[i] 时完成作业。

请返回在查询时间 queryTime 时正在做作业的学生人数。形式上，返回能够使 queryTime 处于区间 [startTime[i], endTime[i]]（含）的学生人数。

示例 1：
    输入：startTime = [1,2,3], endTime = [3,2,7], queryTime = 4
    输出：1
    解释：一共有 3 名学生。
    第一名学生在时间 1 开始写作业，并于时间 3 完成作业，在时间 4 没有处于做作业的状态。
    第二名学生在时间 2 开始写作业，并于时间 2 完成作业，在时间 4 没有处于做作业的状态。
    第三名学生在时间 3 开始写作业，预计于时间 7 完成作业，这是是唯一一名在时间 4 时正在做作业的学生。

示例 2：
    输入：startTime = [4], endTime = [4], queryTime = 4
    输出：1
    解释：在查询时间只有一名学生在做作业。

示例 3：
    输入：startTime = [4], endTime = [4], queryTime = 5
    输出：0

示例 4：
    输入：startTime = [1,1,1,1], endTime = [1,3,2,4], queryTime = 7
    输出：0

示例 5：
    输入：startTime = [9,8,7,6,5,4,3,2,1], endTime = [10,10,10,10,10,10,10,10,10], queryTime = 5
    输出：5

提示：
    startTime.length == endTime.length
    1 <= startTime.length <= 100
    1 <= startTime[i] <= endTime[i] <= 1000
    1 <= queryTime <= 1000

"""
from typing import List
from bisect import bisect_left, bisect_right

"""方法一：枚举"""
class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        return sum((startTime[i] <= queryTime <= endTime[i]) for i in range(len(startTime)))

class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        res = 0
        for i in range(len(startTime)):
            if startTime[i] <= queryTime <= endTime[i]:
                res += 1
        return res

""" 方法二：差分数组
    对差分数组求前缀和，可以得到统计出 t 时刻正在做作业的人数"""
class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        maxEndTime = max(endTime)
        if queryTime > maxEndTime:
            return 0
        cnt = [0] * (maxEndTime + 2)    # 初始化差分数组 cnt 每个元素都为 0
        for start, end in zip(startTime, endTime):
            # print ([start, end])
            cnt[start] += 1     # 在每个学生的起始时间处 cnt[startTime[i]] 加 1，
            cnt[end + 1] -= 1   # 在每个学生的结束时间处 cnt[endTime[i]+1] 减 1
        # print (cnt) # [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, -9]
        return sum(cnt[:queryTime + 1])

""" 方法三：二分查找
    对于每个学生的作业时间 [startTime[i],endTime[i]]，
    一定满足 startTime[i] ≤ endTime[i]。
    如果第 i 名学生在 queryTime 时正在作业，则一定满足 startTime[i] ≤ queryTime ≤ endTime[i]。
    设起始时间小于等于 queryTime 的学生集合为 lessStart，设结束时间小于 queryTime 的学生集合为 lessEnd，
    则根据上述推理可以知道 lessEnd ∈ lessStart，我们从 lessStart 去除 lessEnd 的子集部分即为符合条件的学生集合。
    因此我们通过二分查找找到始时间小于等于 queryTime 的学生人数，然后减去结束时间小于 queryTime 的学生人数，最终结果即为符合条件要求。
"""
class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        startTime.sort()
        endTime.sort()
        return bisect_right(startTime, queryTime) - bisect_left(endTime, queryTime)

if __name__ == "__main__":
    startTime = [9,8,7,6,5,4,3,2,1]
    endTime = [10,10,10,10,10,10,10,10,10]
    queryTime = 5
    sol = Solution()
    result = sol.busyStudent(startTime, endTime, queryTime)
    print (result)