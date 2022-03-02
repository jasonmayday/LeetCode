"""
https://leetcode-cn.com/problems/grumpy-bookstore-owner/

有一个书店老板，他的书店开了 n 分钟。每分钟都有一些顾客进入这家商店。给定一个长度为 n 的整数数组 customers ，其中 customers[i] 是在第 i 分钟开始时进入商店的顾客的编号，所有这些顾客在第 i 分钟结束后离开。

在某些时候，书店老板会生气。 如果书店老板在第 i 分钟生气，那么 grumpy[i] = 1，否则 grumpy[i] = 0。

当书店老板生气时，那一分钟的顾客就会不满意，若老板不生气则顾客是满意的。

书店老板知道一个秘密技巧，能抑制自己的情绪，可以让自己连续 minutes 分钟不生气，但却只能使用一次。

请你返回 这一天营业下来，最多有多少客户能够感到满意 。
 

示例 1：
    输入：customers = [1,0,1,2,1,1,7,5], grumpy = [0,1,0,1,0,1,0,1], minutes = 3
    输出：16
    解释：书店老板在最后 3 分钟保持冷静。
    感到满意的最大客户数量 = 1 + 1 + 1 + 1 + 7 + 5 = 16.

示例 2：
    输入：customers = [1], grumpy = [0], minutes = 1
    输出：1

提示：
    n == customers.length == grumpy.length
    1 <= minutes <= n <= 2 * 10^4
    0 <= customers[i] <= 1000
    grumpy[i] == 0 or 1

"""
from typing import List

""" 滑动窗口 """
class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        N = len(customers)
        sum_ = 0
        for i in range(N):          # 所有不生气时间内的顾客总数
            if grumpy[i] == 0:
                sum_ += customers[i]

        unsatisfied = 0             # 统计生气的 minutes 分钟内，会让多少顾客不满意
        for i in range(minutes):    # 先计算起始的 [0, X) 区间
            if grumpy[i] == 1:
                unsatisfied += customers[i]
        res_keep = unsatisfied      # 初始化挽留的顾客数，为不满意的数量

        for i in range(minutes, N):                 # 然后利用滑动窗口，每次向右移动一步
            if grumpy[i] == 1:                      # 如果新进入窗口的元素是生气的，
                unsatisfied += customers[i]         # 累加不满意的顾客到滑动窗口中
            if grumpy[i - minutes] == 1:            # 如果离开窗口的元素是生气的，
                unsatisfied -= customers[i - minutes]   # 则从滑动窗口中减去该不满意的顾客数
            res_keep = max(res_keep, unsatisfied)       # 求所有窗口内不满意顾客的最大值(也就是可以挽留的最大值)
        return sum_ + res_keep                          # 最终结果是：不生气时的顾客总数 + 窗口X内挽留的因为生气被赶走的顾客数

if __name__ == "__main__":
    customers = [1,0,1,2,1,1,7,5]
    grumpy = [0,1,0,1,0,1,0,1]
    minutes = 3
    sol = Solution()
    result = sol.maxSatisfied(customers, grumpy, minutes)
    print(result)