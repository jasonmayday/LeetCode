"""
https://leetcode-cn.com/problems/gas-station/

在一条环路上有 N 个加油站，其中第 i 个加油站有汽油 gas[i] 升。

你有一辆油箱容量无限的的汽车，从第 i 个加油站开往第 i+1 个加油站需要消耗汽油 cost[i] 升。你从其中的一个加油站出发，开始时油箱为空。

如果你可以绕环路行驶一周，则返回出发时加油站的编号，否则返回 -1。

说明: 
    如果题目有解，该答案即为唯一答案。
    输入数组均为非空数组，且长度相同。
    输入数组中的元素均为非负数。

示例 1:
    输入: 
        gas  = [1,2,3,4,5]
        cost = [3,4,5,1,2]

    输出: 3

    解释:
        从 3 号加油站(索引为 3 处)出发，可获得 4 升汽油。此时油箱有 = 0 + 4 = 4 升汽油
        开往 4 号加油站，此时油箱有 4 - 1 + 5 = 8 升汽油
        开往 0 号加油站，此时油箱有 8 - 2 + 1 = 7 升汽油
        开往 1 号加油站，此时油箱有 7 - 3 + 2 = 6 升汽油
        开往 2 号加油站，此时油箱有 6 - 4 + 3 = 5 升汽油
        开往 3 号加油站，你需要消耗 5 升汽油，正好足够你返回到 3 号加油站。
        因此，3 可为起始索引。

示例 2:
    输入: 
        gas  = [2,3,4]
        cost = [3,4,3]

    输出: -1

    解释:
        你不能从 0 号或 1 号加油站出发，因为没有足够的汽油可以让你行驶到下一个加油站。
        我们从 2 号加油站出发，可以获得 4 升汽油。 此时油箱有 = 0 + 4 = 4 升汽油
        开往 0 号加油站，此时油箱有 4 - 3 + 2 = 3 升汽油
        开往 1 号加油站，此时油箱有 3 - 3 + 3 = 3 升汽油
        你无法返回 2 号加油站，因为返程需要消耗 4 升汽油，但是你的油箱只有 3 升汽油。
        因此，无论怎样，你都不可能绕环路行驶一周。

"""
from typing import List

""" 解法1：暴力方法 """
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):    # 如果 gas 总和小于 cost 总和，则不可能行驶一圈
            return -1
        leng = len(gas)
        for i in range(leng):       # 从 i = 0 出发的例子开始，逐个试验
            if gas[i] < cost[i]:    # i 下标为起点
                continue
            total = 0
            for j in range(i, i + leng):    # 遍历环路一周，j 为汽车行驶的当前下标
                j %= leng                   # 因为是环路，所以要取模
                total += gas[j] - cost[j]   # 更新当前汽油量
                if total < 0:
                    break
            else:
                return i
        return -1


""" 解法2：贪心算法 """
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):    # 如果 gas 总和小于 cost 总和，则不可能行驶一圈
            return -1
        start = 0   # 起始下标
        total = 0   # 初始化油量
        for i in range(len(gas)):
            total += gas[i] - cost[i]
            if total < 0:
                total = 0
                start = i + 1
        return start


""" 解法3：双指针 """
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        circ = len(gas)     # 环的长度
        start, cur = 0, 0   # 起始点假设为 0，当前在 0 节点。
        oil = gas[0]        # 初始化油量，把 0 节点的油都灌进去。

        # 当 cur + 1 == start 时说明到了终点，所以没有考虑终点到起点（两者相邻）所用的油。
        while (cur + 1) % circ != start:
            
            if oil < cost[cur]:                   # 如果油不够开往下一节点。
                start = (start - 1) % circ        # 说明以 start 为起始节点不行，将 start 前一位假设为起始节点。
                oil += (gas[start] - cost[start]) # 重置油量：新的起始点里面的油全都抱走，同时要计算从新的起始点到旧的的起始点（它的下一节点）所消耗的油。

            else:                       # 如果够开往下一节点
                oil -= cost[cur]        # 把消耗的油减掉。
                cur = (cur + 1) % circ  # 去下一个节点。
                oil += gas[cur]         # 把新节点的油抱走。
        
        if oil - cost[cur] >= 0:    # 返回时判断一下在终点时的油能否开到起点。
            return start
        else:
            return -1


if __name__ == "__main__":
    gas  = [1,2,3,4,5]
    cost = [3,4,5,1,2]
    sol = Solution()
    result = sol.canCompleteCircuit(gas, cost)
    print(result)