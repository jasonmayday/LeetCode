"""
你这个学期必须选修 numCourses 门课程，记为 0 到 numCourses - 1 。

在选修某些课程之前需要一些先修课程。 先修课程按数组 prerequisites 给出，其中 prerequisites[i] = [ai, bi] ，表示如果要学习课程 ai 则 必须 先学习课程  bi 。
    例如，先修课程对 [0, 1] 表示：想要学习课程 0 ，你需要先完成课程 1 。

请你判断是否可能完成所有课程的学习？如果可以，返回 true ；否则，返回 false 。

示例 1：
    输入：numCourses = 2, prerequisites = [[1,0]]
    输出：true
    解释：总共有 2 门课程。学习课程 1 之前，你需要完成课程 0 。这是可能的。

示例 2：
    输入：numCourses = 2, prerequisites = [[1,0],[0,1]]
    输出：false
    解释：总共有 2 门课程。学习课程 1 之前，你需要先完成​课程 0 ；并且学习课程 0 之前，你还应先完成课程 1 。这是不可能的。

提示：
    1 <= numCourses <= 10^5
    0 <= prerequisites.length <= 5000
    prerequisites[i].length == 2
    0 <= ai, bi < numCourses
    prerequisites[i] 中的所有课程对 互不相同

"""
from typing import List

""" 方法1：入度表（广度优先遍历）
    该方法的每一步总是输出当前无前趋（即入度为零）的顶点
    本题可约化为： 课程安排图是否是 有向无环图(DAG)。即课程间规定了前置条件，但不能构成任何环路，否则课程前置条件将不成立。
    思路是通过 拓扑排序 判断此课程安排图是否是 有向无环图(DAG) 。 
    拓扑排序原理： 
        对 DAG 的顶点进行排序，使得对每一条有向边 (u,v)，均有 u（在排序记录中）比 v 先出现。
        亦可理解为对某点 v 而言，只有当 v 的所有源点均出现了，v 才能出现。
    通过课程前置条件列表 prerequisites 可以得到课程安排图的 邻接表 adjacency，以降低算法时间复杂度，以下两种方法都会用到邻接表。
"""
class Solution(object):
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if len(prerequisites) == 0:     # 没有课程，当然可以完成课程的学习
            return True
        
        indegrees = [0 for _ in range(numCourses)]      # 入度表。[0, 0] 统计课程安排图中每个节点的入度，一开始全部为 0（入度为 0 说明不需要前置课程）
        adj = [set() for _ in range(numCourses)]        # 邻接表。注意：邻接表存放的是后继 cur 结点的集合

        for cur, pre in prerequisites:  # [ai, bi] 表示如果要学习课程 ai 则 必须 先学习课程  bi 。
            indegrees[cur] += 1         # indegrees = [0, 1]
            adj[pre].add(cur)

        queue = []                      # 借助一个队列 queue，将所有入度为 0 的节点入队
        for i in range(numCourses):     # 首先遍历一遍课程，
            if indegrees[i] == 0:       # 把所有入度为 0 的结点加入队列
                queue.append(i)
        
        counter = 0             # 拓扑排序出队次数
        while queue:            # 当 queue 非空时
            pre = queue.pop(0)  # 依次将队首节点出队，在课程安排图中删除此节点 pre
            counter += 1        # 在每次 pre 出队时，执行 counter +1

            for cur in adj[pre]:            # 并不是真正从邻接表中删除此节点 pre
                indegrees[cur] -= 1         # 而是将此节点对应所有邻接节点 cur 的入度 -1
                if indegrees[cur] == 0:     # 当入度 −1后邻接节点 cur 的入度为 0
                    queue.append(cur)       # 说明 cur 所有的前驱节点已经被 “删除”，此时将 cur 入队。

        return counter == numCourses    # 若整个课程安排图是有向无环图（即可以安排），则所有节点一定都入队并出队过，即完成拓扑排序。
                                        # 换个角度说，若课程安排图中存在环，一定有节点的入度始终不为 0
                                        # 因此，拓扑排序出队次数等于课程个数，返回 numCourses == 0 判断课程是否可以成功安排


""" 方法二：深度优先遍历
    通过 DFS 判断图中是否有环"""
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """ 借助一个标志列表 flags，用于判断每个节点 i （课程）的状态：
            未被 DFS 访问：i == 0
            已被其他节点启动的 DFS 访问：i == -1
            已被当前节点启动的 DFS 访问：i ==  1 
        """
        def dfs(i, adjacency, flags):       
            if flags[i] == -1:  # 当 flag[i] == -1，说明当前访问节点已被其他节点启动的 DFS 访问，
                return True     # 无需再重复搜索，直接返回 True
            if flags[i] == 1:   # 当 flag[i] == 1，说明在本轮 DFS 搜索中节点 i 被第 2 次访问，即 课程安排图有环
                return False    # 直接返回 False
            flags[i] = 1                            # 将当前访问节点 i 对应 flag[i] 置 1，即标记其被本轮 DFS 访问过
            for j in adjacency[i]:                  # 递归访问当前节点 i 的所有邻接节点 j
                if not dfs(j, adjacency, flags):    # 当发现环直接返回 False
                    return False        
            flags[i] = -1       # 当前节点所有邻接节点已被遍历，并没有发现环，则将当前节点 flag 置为 −1 
            return True         # 并返回 True

        adjacency = [[] for _ in range(numCourses)] # [[], [], [], [], [], []]
        flags = [0 for _ in range(numCourses)]      # [0, 0, 0, 0, 0, 0]

        for cur, pre in prerequisites:
            adjacency[pre].append(cur)
        for i in range(numCourses):             # 对 numCourses 个节点依次执行 DFS
            if not dfs(i, adjacency, flags):    # 判断每个节点起步 DFS 是否存在环
                return False                    # 若存在环直接返回 False
        return True                             # 若整个图 DFS 结束并未发现环，返回 True


if __name__ == "__main__":
    numCourses = 6
    prerequisites = [[5,3],[5,4],[3,0],[3,1],[4,1],[4,2]]
    sol = Solution()
    result = sol.canFinish(numCourses, prerequisites)
    print (result)