"""
https://leetcode-cn.com/problems/number-of-ways-to-reconstruct-a-tree/

给你一个数组 pairs ，其中 pairs[i] = [xi, yi] ，并且满足：
    pairs 中没有重复元素
    xi < yi

令 ways 为满足下面条件的有根树的方案数：
    树所包含的所有节点值都在 pairs 中。
    一个数对 [xi, yi] 出现在 pairs 中 当且仅当 xi 是 yi 的祖先或者 yi 是 xi 的祖先。
    注意：构造出来的树不一定是二叉树。

两棵树被视为不同的方案当存在至少一个节点在两棵树中有不同的父节点。
请你返回：
    如果 ways == 0 ，返回 0 。
    如果 ways == 1 ，返回 1 。
    如果 ways > 1 ，返回 2 。

一棵 有根树 指的是只有一个根节点的树，所有边都是从根往外的方向。

我们称从根到一个节点路径上的任意一个节点（除去节点本身）都是该节点的 祖先 。根节点没有祖先。

示例 1：
    输入：pairs = [[1,2],[2,3]]
    输出：1
    解释：如上图所示，有且只有一个符合规定的有根树。

示例 2：
    输入：pairs = [[1,2],[2,3],[1,3]]
    输出：2
    解释：有多个符合规定的有根树，其中三个如上图所示。

示例 3：
    输入：pairs = [[1,2],[2,3],[2,4],[1,5]]
    输出：0
    解释：没有符合规定的有根树。

提示：
    1 <= pairs.length <= 10^5
    1 <= xi < yi <= 500
    pairs 中的元素互不相同。

"""
from typing import List

class Solution:
    def checkWays(self, pairs: List[List[int]]) -> int:
        edge = [[False for _ in range(501)] for _ in range(501)]    # 邻接矩阵
        adj = [set() for _ in range(501)]                           # 邻接表
        nodes = set()                                               # 点集
        
        for x, y in pairs:      # 初始化时，按照双向图
            edge[x][y] = True
            edge[y][x] = True
            adj[x].add(y)
            adj[y].add(x)
            nodes.add(x)
            nodes.add(y)
        nodes = list(nodes)
        nodes.sort(key = lambda x: -len(adj[x]))                    # 按出度降序排序
        n = len(nodes)
        if len(adj[nodes[0]]) != (n - 1):                           # 出度最大的点，出度不是 n-1
            return 0                                                # 没有符合条件的
        res = 1                                                     # 否则，res先置1
        start = 1           
        while start < n and len(adj[nodes[start]]) == n-1:
            res = 2                                                 # 若多个点的出度为n-1  结果为0或2
            start += 1                                              # 找到最后一个出度为n-1的idx
        for i in range(start):
            x = nodes[i]
            for y in adj[x]:                                        # y为x指向的点
                adj[y].remove(x)                                    # 只留x-->y，y指向x的remove掉
        for i in range(start, n):
            x = nodes[i]
            k = len(adj[x])                                         # x的出度
            for y in adj[x]:                                        # y为x指向的点
                if len(adj[y]) == k:                                # y的出度也为k,x与y可以互换
                    res = 2                                         # x与y出度相同，res为0或2，先置2
                adj[y].remove(x)                                    # 删除y指向x的指针（箭头）
                if k < len(set(adj[x]) | set(adj[y])):
                    # x指向的点的个数 < 儿子y和孙子指向的个数
                    return 0
        return res

if __name__ == "__main__":
    pairs = [[1,2],[2,3],[2,4],[1,5]]
    sol = Solution()
    result = sol.checkWays(pairs)
    print(result)