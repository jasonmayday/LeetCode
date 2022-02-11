"""
https://leetcode-cn.com/problems/0jQkd0/

在 「力扣挑战赛」 开幕式的压轴节目 「无人机方阵」中，每一架无人机展示一种灯光颜色。 无人机方阵通过两种操作进行颜色图案变换：

    调整无人机的位置布局
    切换无人机展示的灯光颜色

给定两个大小均为 N*M 的二维数组 source 和 target 表示无人机方阵表演的两种颜色图案，由于无人机切换灯光颜色的耗能很大，请返回从 source 到 target 最少需要多少架无人机切换灯光颜色。

注意： 调整无人机的位置布局时无人机的位置可以随意变动。

示例 1：
    输入：source = [[1,3],[5,4]], target = [[3,1],[6,5]]
    输出：1
    解释：
        最佳方案为
        将 [0,1] 处的无人机移动至 [0,0] 处；
        将 [0,0] 处的无人机移动至 [0,1] 处；
        将 [1,0] 处的无人机移动至 [1,1] 处；
        将 [1,1] 处的无人机移动至 [1,0] 处，其灯光颜色切换为颜色编号为 6 的灯光；
        因此从source 到 target 所需要的最少灯光切换次数为 1。

示例 2：
    输入：source = [[1,2,3],[3,4,5]], target = [[1,3,5],[2,3,4]]
    输出：0
    解释：
        仅需调整无人机的位置布局，便可完成图案切换。因此不需要无人机切换颜色

提示：
    n == source.length == target.length
    m == source[i].length == target[i].length
    1 <= n, m <=100
    1 <= source[i][j], target[i][j] <=10^4

"""
from typing import List
from collections import Counter

class Solution:
    def minimumSwitchingTimes(self, source: List[List[int]], target: List[List[int]]) -> int:
        c1 = Counter(sum(source,[]))    # {1: 1, 3: 1, 5: 1, 4: 1}
        c2 = Counter(sum(target,[]))    # {3: 1, 1: 1, 6: 1, 5: 1}
        res = 0
        for i in set(c2)|set(c1): 
            res += abs(c2[i] - c1[i])
        return res // 2

"""计数，可以随意变换位置，只要计算不能匹配的颜色个数"""
class Solution:
    def minimumSwitchingTimes(self, source: List[List[int]], target: List[List[int]]) -> int:
        dict = {}
        for i in source:
            for j in i:
                if j not in dict:
                    dict[j] = 0
                dict[j] += 1
        ans = 0
        for i in target:
            for j in i:
                if j not in dict:
                    ans += 1
                elif dict[j] > 0:
                    dict[j] -= 1
                else:
                    ans += 1
        return ans


if __name__ == "__main__":
    source = [[1,3],[5,4]]
    target = [[3,1],[6,5]]
    sol = Solution()
    result = sol.minimumSwitchingTimes(source, target)
    print(result)