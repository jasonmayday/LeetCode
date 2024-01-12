"""
https://leetcode-cn.com/problems/corporate-flight-bookings/

这里有 n 个航班，它们分别从 1 到 n 进行编号。

有一份航班预订表 bookings ，表中第 i 条预订记录 bookings[i] = [firsti, lasti, seatsi] 意味着在从 firsti 到 lasti （包含 firsti 和 lasti ）的 每个航班 上预订了 seatsi 个座位。

请你返回一个长度为 n 的数组 answer，里面的元素是每个航班预定的座位总数。

示例 1：
    输入：bookings = [[1,2,10],[2,3,20],[2,5,25]], n = 5
    输出：[10,55,45,25,25]
    解释：
        航班编号        1   2   3   4   5
        预订记录 1 ：   10  10
        预订记录 2 ：       20  20
        预订记录 3 ：       25  25  25  25
        总座位数：      10  55  45  25  25
        因此，answer = [10,55,45,25,25]

示例 2：
    输入：bookings = [[1,2,10],[2,2,15]], n = 2
    输出：[10,25]
    解释：
        航班编号        1   2
        预订记录 1 ：   10  10
        预订记录 2 ：       15
        总座位数：      10  25
        因此，answer = [10,25]

提示：
    1 <= n <= 2 * 10^4
    1 <= bookings.length <= 2 * 10^4
    bookings[i].length == 3
    1 <= firsti <= lasti <= n
    1 <= seatsi <= 10^4

"""
from typing import List

""" 差分数组
    一个预订记录实际上代表了一个区间的增量。我们的任务是将这些增量叠加得到答案。因此，我们可以使用差分解决本题。"""
class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        nums = [0] * n  # 差分数组  [0, 0, 0, 0, 0]
        for left, right, inc in bookings:
            nums[left - 1] += inc   # 注意下标需要调整
            if right < n:           # 当 r 为 n 时，我们无需修改 d[r]，因为这个位置溢出了下标范围
                nums[right] -= inc
        # [10,  0, -10,   0, 0]
        # [10, 20, -10, -20, 0]
        # [10, 45, -10, -20, 0]
        for i in range(1, n):
            nums[i] += nums[i - 1]
        return nums # [10,55,45,25,25]

if __name__ == "__main__":
    bookings = [[1,2,10],[2,3,20],[2,5,25]]
    n = 5
    sol = Solution()
    result = sol.corpFlightBookings(bookings, n)
    print(result)