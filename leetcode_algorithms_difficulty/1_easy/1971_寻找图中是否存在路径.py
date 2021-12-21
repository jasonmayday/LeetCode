"""
https://leetcode-cn.com/problems/find-if-path-exists-in-graph/

有一个具有 n个顶点的 双向 图，其中每个顶点标记从 0 到 n - 1（包含 0 和 n - 1）。图中的边用一个二维整数数组 edges 表示，其中 edges[i] = [ui, vi] 表示顶点 ui 和顶点 vi 之间的双向边。 每个顶点对由 最多一条 边连接，并且没有顶点存在与自身相连的边。

请你确定是否存在从顶点 start 开始，到顶点 end 结束的 有效路径 。

给你数组 edges 和整数 n、start和end，如果从 start 到 end 存在 有效路径 ，则返回 true，否则返回 false 。

示例 1：
    输入：n = 3, edges = [[0,1],[1,2],[2,0]], start = 0, end = 2
    输出：true
    解释：存在由顶点 0 到顶点 2 的路径:
    - 0 → 1 → 2 
    - 0 → 2

示例 2：
    输入：n = 6, edges = [[0,1],[0,2],[3,5],[5,4],[4,3]], start = 0, end = 5
    输出：false
    解释：不存在由顶点 0 到顶点 5 的路径.

提示:
    1 <= n <= 2 * 10^5
    0 <= edges.length <= 2 * 10^5
    edges[i].length == 2
    0 <= ui, vi <= n - 1
    ui != vi
    0 <= start, end <= n - 1
    不存在双向边
    不存在指向顶点自身的边
    通过次数1,139提交次数2,286

"""
from typing import List

class Solution:
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        e_list = [-1] * n
        e_dict = {}
        for edge in edges:
            left, right = edge
            # 左右均没出现过
            if e_list[left] == e_list[right] == -1:
                e_list[left] = e_list[right] = left
                e_dict[left] = set(edge)
            # 左没出现过
            elif e_list[left] == -1:
                e_list[left] = e_list[right]
                e_dict[e_list[right]].add(left)
            # 右没出现过
            elif e_list[right] == -1:
                e_list[right] = e_list[left]
                e_dict[e_list[left]].add(right)
            # 都出现过且不能联通
            elif e_list[left] != e_list[right]:
                cur_right = e_list[right]
                for e in e_dict[cur_right]:
                    e_list[e] = e_list[left]
                e_dict[e_list[left]].update(e_dict.pop(cur_right))
            if e_list[start] == e_list[end] != -1:
                return True
        return e_list[start] == e_list[end]

if __name__ == "__main__":
    n = 6
    edges = [[0,1],[0,2],[3,5],[5,4],[4,3]]
    start = 0
    end = 5
    sol = Solution()
    result = sol.validPath(n, edges, start, end)
    print(result)