"""
https://leetcode-cn.com/problems/two-furthest-houses-with-different-colors/

街上有 n 栋房子整齐地排成一列，每栋房子都粉刷上了漂亮的颜色。给你一个下标从 0 开始且长度为 n 的整数数组 colors ，其中 colors[i] 表示第  i 栋房子的颜色。

返回 两栋 颜色 不同 房子之间的 最大 距离。

第 i 栋房子和第 j 栋房子之间的距离是 abs(i - j) ，其中 abs(x) 是 x 的绝对值。

示例 1：
    输入：colors = [1,1,1,6,1,1,1]
    输出：3
    解释：上图中，颜色 1 标识成蓝色，颜色 6 标识成红色。
        两栋颜色不同且距离最远的房子是房子 0 和房子 3 。
        房子 0 的颜色是颜色 1 ，房子 3 的颜色是颜色 6 。两栋房子之间的距离是 abs(0 - 3) = 3 。
        注意，房子 3 和房子 6 也可以产生最佳答案。

示例 2：
    输入：colors = [1,8,3,8,3]
    输出：4
    解释：上图中，颜色 1 标识成蓝色，颜色 8 标识成黄色，颜色 3 标识成绿色。
        两栋颜色不同且距离最远的房子是房子 0 和房子 4 。
        房子 0 的颜色是颜色 1 ，房子 4 的颜色是颜色 3 。两栋房子之间的距离是 abs(0 - 4) = 4 。

示例 3：
    输入：colors = [0,1]
    输出：1
    解释：两栋颜色不同且距离最远的房子是房子 0 和房子 1 。
        房子 0 的颜色是颜色 0 ，房子 1 的颜色是颜色 1 。两栋房子之间的距离是 abs(0 - 1) = 1 。

提示：
    n == colors.length
    2 <= n <= 100
    0 <= colors[i] <= 100
    生成的测试数据满足 至少 存在 2 栋颜色不同的房子

"""

from typing import List

"""方法1：枚举"""
class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        n = len(colors)
        res = 0
        for i in range(n):  # 遍历两栋房子下标并维护最远距离
            for j in range(i + 1, n):
                if colors[i] != colors[j]:
                    res = max(res, j - i)
        return res
    
"""方法2：枚举的一行写法"""
class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        n = len(colors)
        return max(j - i for i in range(n) for j in range(i + 1, n) if colors[i] != colors[j])

"""方法3：贪心算法"""
class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        if colors[0] != colors[-1]:     # 如果第一栋和最后一栋颜色不同
            return len(colors) - 1      # 直接返回答案
        ans = 0
        for i in range(1, len(colors) - 1):
            if colors[0] != colors[i]:
                ans = max(i,ans)
            if colors[-1] != colors[i]:
                ans = max(len(colors) - 1 - i,ans)
        return ans 

if __name__ == "__main__":
    colors = [1,1,1,6,1,1,1]
    sol = Solution()
    result = sol.maxDistance(colors)
    print (result)