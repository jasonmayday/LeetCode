"""
https://leetcode-cn.com/problems/last-stone-weight/

有一堆石头，每块石头的重量都是正整数。

每一回合，从中选出两块 最重的 石头，然后将它们一起粉碎。假设石头的重量分别为 x 和 y，且 x <= y。那么粉碎的可能结果如下：
    如果 x == y，那么两块石头都会被完全粉碎；
    如果 x != y，那么重量为 x 的石头将会完全粉碎，而重量为 y 的石头新重量为 y-x。

最后，最多只会剩下一块石头。返回此石头的重量。如果没有石头剩下，就返回 0。

示例：
    输入：[2,7,4,1,8,1]
    输出：1
    解释：
    先选出 7 和 8，得到 1，所以数组转换为 [2,4,1,1,1]，
    再选出 2 和 4，得到 2，所以数组转换为 [2,1,1,1]，
    接着是 2 和 1，得到 1，所以数组转换为 [1,1,1]，
    最后选出 1 和 1，得到 0，最终数组转换为 [1]，这就是最后剩下那块石头的重量。
 
提示：
    1 <= stones.length <= 30
    1 <= stones[i] <= 1000
    
"""
from typing import List
import heapq

# https://docs.python.org/zh-cn/3/library/heapq.html

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-stone for stone in stones] # 因为python只支持小顶堆，所以在入堆的时候我们要添加的是数据的相反数
        heapq.heapify(heap)                 # 初始化，将list x 转换成堆

        # 模拟
        while len(heap) > 1:
            x = heapq.heappop(heap)     # x,y 为当前最大值
            y = heapq.heappop(heap)     # 弹出并返回 heap 的最小的元素（最大值的相反数即为最小值）
            if x != y:
                heapq.heappush(heap, x-y)   # 将 item 放入堆中

        if heap:                # 如果剩下一个元素
            return -heap[0]     # 返回该元素的相反数
        return 0                # 如果没有元素，返回 0

if __name__ == "__main__":
    n = 4
    trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
    sol = Solution()
    result = sol.findJudge(n,trust)
    print(result)