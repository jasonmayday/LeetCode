"""
https://leetcode-cn.com/problems/heaters/

冬季已经来临。 你的任务是设计一个有固定加热半径的供暖器向所有房屋供暖。

在加热器的加热半径范围内的每个房屋都可以获得供暖。

现在，给出位于一条水平线上的房屋 houses 和供暖器 heaters 的位置，请你找出并返回可以覆盖所有房屋的最小加热半径。

说明：所有供暖器都遵循你的半径标准，加热的半径也一样。

示例 1:
    输入: houses = [1,2,3], heaters = [2]
    输出: 1
    解释: 仅在位置2上有一个供暖器。如果我们将加热半径设为1，那么所有房屋就都能得到供暖。

示例 2:
    输入: houses = [1,2,3,4], heaters = [1,4]
    输出: 1
    解释: 在位置1, 4上有两个供暖器。我们需要将加热半径设为1，这样所有房屋就都能得到供暖。

示例 3：
    输入：houses = [1,5], heaters = [2]
    输出：3

提示：
    1 <= houses.length, heaters.length <= 3 * 10^4
    1 <= houses[i], heaters[i] <= 10^9

"""
from typing import List
import bisect

"""方法一：排序 + 二分查找 (二分的对象就是半径)"""
class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        left = 0    # 二分法左区间：最少为0，当房屋和取暖器重叠的时候
        right = max(houses[-1], heaters[-1])    # 二分法右区间：最多为最大坐标

        def can_heat(radius):       # 判断指定半径是否能覆盖完
            last_right = 0          # 上一次能够加热的最右端坐标
            for heater in heaters:  # 遍历每个取暖器
                left = bisect.bisect_left(houses, heater - radius)          # 二分查询取暖器加热半径能够覆盖最左边的房子编号
                if left > last_right:   # 如果最左边不能跟上一次最右边重叠，
                    return False        # 表示不能覆盖加热
                last_right = bisect.bisect_right(houses, heater + radius)   # 更新当前取暖器加热半径能够覆盖最右边的房子编号
                if last_right >= len(houses):       # 如果已经到达最后一个房子
                    return True                     # 表示已经全部覆盖完了
            return False

        # 二分法模板
        while left <= right:
            mid = left + (right - left) // 2
            if can_heat(mid):       # 如果能覆盖 
                right = mid - 1     # 说明还可以尝试减小半径
            else:
                left = mid + 1      # 不能吃完，则增大半径
        return left


"""方法二：排序 + 双指针"""
class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        ans = 0
        houses.sort()
        heaters.sort()
        j = 0
        for i, house in enumerate(houses):
            curDistance = abs(house - heaters[j])
            while j + 1 < len(heaters) and abs(houses[i] - heaters[j]) >= abs(houses[i] - heaters[j + 1]):
                j += 1
                curDistance = min(curDistance, abs(houses[i] - heaters[j]))
            ans = max(ans, curDistance)
        return ans

if __name__ == "__main__":
    houses = [1,2,3,4]
    heaters = [1,4]
    sol = Solution()
    result = sol.findRadius(houses, heaters)
    print (result) 