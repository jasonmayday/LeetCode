'''
https://leetcode-cn.com/problems/self-crossing/

给你一个整数数组 distance 。

从 X-Y 平面上的点 (0,0) 开始，先向北移动 distance[0] 米，然后向西移动 distance[1] 米，向南移动 distance[2] 米，向东移动 distance[3] 米，持续移动。也就是说，每次移动后你的方位会发生逆时针变化。

判断你所经过的路径是否相交。如果相交，返回 true ；否则，返回 false 。

示例 1：
https://assets.leetcode.com/uploads/2021/03/14/selfcross1-plane.jpg
┌───┐
│   │
└───┼──>
    │
输入：distance = [2,1,1,2]
输出：true

示例 2：
https://assets.leetcode.com/uploads/2021/03/14/selfcross2-plane.jpg
┌──────┐
│      │
│
│
└────────────>
输入：distance = [1,2,3,4]
输出：false

示例 3：
https://assets.leetcode.com/uploads/2021/03/14/selfcross3-plane.jpg
┌───┐
│   │
└───┼>
输入：distance = [1,1,1,1]
输出：true

提示：
1 <= distance.length <= 105
1 <= distance[i] <= 105

'''

distance = [2,1,1,2]

from typing import List
class Solution:
    def isSelfCrossing(self, distance: List[int]) -> bool:
        n = len(distance)
        for i in range(3, n):
            # 第 1 类路径交叉的情况
            if (distance[i] >= distance[i - 2]
                    and distance[i - 1] <= distance[i - 3]):
                return True

            # 第 2 类路径交叉的情况
            if i == 4 and (distance[3] == distance[1]
                           and distance[4] >= distance[2] - distance[0]):
                return True

            # 第 3 类路径交叉的情况
            if i >= 5 and (distance[i - 3] - distance[i - 5] <= distance[i - 1] <= distance[i - 3]
                           and distance[i] >= distance[i - 2] - distance[i - 4]
                           and distance[i - 2] > distance[i - 4]):
                return True
        return False

sol = Solution()
result = sol.isSelfCrossing(distance)
print (result) 
