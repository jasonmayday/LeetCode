"""
https://leetcode-cn.com/problems/minimum-height-trees/

树是一个无向图，其中任何两个顶点只通过一条路径连接。 换句话说，一个任何没有简单环路的连通图都是一棵树。

给你一棵包含 n 个节点的树，标记为 0 到 n - 1 。给定数字 n 和一个有 n - 1 条无向边的 edges 列表（每一个边都是一对标签），其中 edges[i] = [ai, bi] 表示树中节点 ai 和 bi 之间存在一条无向边。

可选择树中任何一个节点作为根。当选择节点 x 作为根节点时，设结果树的高度为 h 。在所有可能的树中，具有最小高度的树（即，min(h)）被称为 最小高度树 。

请你找到所有的 最小高度树 并按 任意顺序 返回它们的根节点标签列表。

树的 高度 是指根节点和叶子节点之间最长向下路径上边的数量。
 

示例 1：
    输入：n = 4, edges = [[1,0],[1,2],[1,3]]
    输出：[1]
    解释：如图所示，当根是标签为 1 的节点时，树的高度是 1 ，这是唯一的最小高度树。

示例 2：
    输入：n = 6, edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]
    输出：[3,4]

提示：
    1 <= n <= 2 * 10^4
    edges.length == n - 1
    0 <= ai, bi < n
    ai != bi
    所有 (ai, bi) 互不相同
    给定的输入 保证 是一棵树，并且 不会有重复的边

"""
from typing import List
from collections import defaultdict, deque

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 2:
            return [0,1]
        if n == 1:
            return [0]

        ''' 简单无向图：套路是建图并遍历，建立邻接表。
            邻接表为 map,其值为 list, 它的 size 就是入度数
            0
            |
            1
           / \
          2   3     '''
        adjs = defaultdict(list)            # defaultdict写法很有用
        for edge in edges:                  # 图的邻接表表示法, 基本是模板
            adjs[edge[0]].append(edge[1])   # 1:{2}
            adjs[edge[1]].append(edge[0])   # 2:{1}
        print('adjs: ', adjs)               # {1: [0, 2, 3], 0: [1], 2: [1], 3: [1]}

        ''' BFS 队列: 初始队列放入初始元素, size = 1 的为叶子, 入队'''
        queue = deque() # 固定写法
        for key, value in adjs.items():
            if len(value) == 1:
                queue.append(key)   # 把仅于一个节点连接的节点加入queue
        print('queue: ', queue)     # deque([0, 2, 3])

        ''' BFS 两个大循环 '''
        while(queue): # 固定写法
            size = len(queue)  # 固定写法
            n = n - size

            for _ in range(size):
                v = queue.popleft()
                v_adj = adjs[v].pop() # v的邻接仅一个,弹出即删除
                adjs[v_adj].remove(v) # 在v的邻接元素的邻接列表里删除v
                if len(adjs[v_adj]) == 1:
                    queue.append(v_adj)

            if n == 1:
                return [queue.popleft()]
            if n == 2:
                return [queue.popleft(), queue.popleft()]

if __name__ == "__main__":
    n = 4
    edges = [[1,0],[1,2],[1,3]]
    sol = Solution()
    result = sol.findMinHeightTrees(n, edges)
    print (result)
