"""
https://leetcode-cn.com/problems/clone-graph/

给你无向 连通 图中一个节点的引用，请你返回该图的 深拷贝（克隆）。

图中的每个节点都包含它的值 val（int） 和其邻居的列表（list[Node]）。

    class Node {
        public int val;
        public List<Node> neighbors;
    }

测试用例格式：

简单起见，每个节点的值都和它的索引相同。例如，第一个节点值为 1（val = 1），第二个节点值为 2（val = 2），以此类推。该图在测试用例中使用邻接列表表示。

邻接列表 是用于表示有限图的无序列表的集合。每个列表都描述了图中节点的邻居集。

给定节点将始终是图中的第一个节点（值为 1）。你必须将 给定节点的拷贝 作为对克隆图的引用返回。

示例 1：
    输入：adjList = [[2,4],[1,3],[2,4],[1,3]]
    输出：[[2,4],[1,3],[2,4],[1,3]]
    解释：
        图中有 4 个节点。
        节点 1 的值是 1，它有两个邻居：节点 2 和 4 。
        节点 2 的值是 2，它有两个邻居：节点 1 和 3 。
        节点 3 的值是 3，它有两个邻居：节点 2 和 4 。
        节点 4 的值是 4，它有两个邻居：节点 1 和 3 。

示例 2：
    输入：adjList = [[]]
    输出：[[]]
    解释：输入包含一个空列表。该图仅仅只有一个值为 1 的节点，它没有任何邻居。

示例 3：
    输入：adjList = []
    输出：[]
    解释：这个图是空的，它不含任何节点。

示例 4：
    输入：adjList = [[2],[1]]
    输出：[[2],[1]]

提示：
    节点数不超过 100 。
    每个节点值 Node.val 都是唯一的，1 <= Node.val <= 100。
    无向图是一个简单图，这意味着图中没有重复的边，也没有自环。
    由于图是无向的，如果节点 p 是节点 q 的邻居，那么节点 q 也必须是节点 p 的邻居。
    图是连通图，你可以从给定节点访问到所有节点。

"""
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
        
''' 深拷贝，所有的节点都要新建一遍，然后重建它们之间的关系
    图的深拷贝是在做什么，对于一张图而言，它的深拷贝即构建一张与原图结构，值均一样的图，但是其中的节点不再是原来图节点的引用。
    因此，为了深拷贝出整张图，我们需要知道整张图的结构以及对应节点的值。
'''

""" DFS (深度遍历)
    A - B     ABCD
    |   |   
    D - C
"""
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        visited = {}    # 使用一个哈希表存储所有已被访问和克隆的节点 (避免陷入死循环)
                        # 哈希表中的 key 是原始图中的节点，value 是克隆图中的对应节点。
        def dfs(node):
            # print(node.val)
            if not node:
                return
            if node in visited:         # 如果该节点已经被访问过了
                return visited[node]    # 则直接从哈希表中取出对应的克隆节点返回
            clone = Node(node.val, [])  # 克隆节点，注意到为了深拷贝我们不会克隆它的邻居的列表
            visited[node] = clone       # 哈希表存储被访问和克隆的节点
            for n in node.neighbors:    # 遍历该节点的邻居并更新克隆节点的邻居列表
                clone.neighbors.append(dfs(n))
            return clone

        return dfs(node)


""" BFS (广度遍历)
    A - B     ABDC
    |   |   
    D - C
"""
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        from collections import deque
        visited = {}    # 使用一个哈希表存储所有已被访问和克隆的节点 (避免陷入死循环)
                        # 哈希表中的 key 是原始图中的节点，value 是克隆图中的对应节点。
        def bfs(node):
            # print(node.val)
            if not node:
                return
            clone = Node(node.val, [])  
            visited[node] = clone       # 克隆第一个节点并存储到哈希表中
            queue = deque()
            queue.appendleft(node)      # 将题目给定的节点添加到队列
            
            while queue:                # 广度优先搜索
                tmp = queue.pop()       # 取出队列的头节点
                for n in tmp.neighbors: # 遍历该节点的邻居（BFS的核心）
                    if n not in visited:                # 如果没有被访问过
                        visited[n] = Node(n.val, [])    # 就克隆并存储在哈希表中
                        queue.appendleft(n)             # 将邻居节点加入队列中
                    visited[tmp].neighbors.append(visited[n])   # 更新当前节点的邻居列表
            return clone

        return bfs(node)

if __name__ == '__main__':
    ns = [Node(i, []) for i in range(0, 5)]
    ns[1].neighbors = [ns[2], ns[4]]    # 1 - 2 
    ns[2].neighbors = [ns[1], ns[3]]    # |   |
    ns[3].neighbors = [ns[2], ns[4]]    # 4 - 3
    ns[4].neighbors = [ns[3], ns[1]]
    
    sol = Solution()
    res = sol.cloneGraph(ns[1])
    