"""
https://leetcode-cn.com/problems/course-schedule-ii/

现在你总共有 numCourses 门课需要选，记为 0 到 numCourses - 1。给你一个数组 prerequisites ，其中 prerequisites[i] = [ai, bi] ，表示在选修课程 ai 前 必须 先选修 bi 。
    例如，想要学习课程 0 ，你需要先完成课程 1 ，我们用一个匹配来表示：[0,1] 。

返回你为了学完所有课程所安排的学习顺序。可能会有多个正确的顺序，你只要返回 任意一种 就可以了。如果不可能完成所有课程，返回 一个空数组 。

示例 1：
    输入：numCourses = 2, prerequisites = [[1,0]]
    输出：[0,1]
    解释：总共有 2 门课程。要学习课程 1，你需要先完成课程 0。因此，正确的课程顺序为 [0,1] 。

示例 2：
    输入：numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
    输出：[0,2,1,3]
    解释：总共有 4 门课程。要学习课程 3，你应该先完成课程 1 和课程 2。并且课程 1 和课程 2 都应该排在课程 0 之后。
    因此，一个正确的课程顺序是 [0,1,2,3] 。另一个正确的排序是 [0,2,1,3] 。

示例 3：
    输入：numCourses = 1, prerequisites = []
    输出：[0]

提示：
    1 <= numCourses <= 2000
    0 <= prerequisites.length <= numCourses * (numCourses - 1)
    prerequisites[i].length == 2
    0 <= ai, bi < numCourses
    ai != bi
    所有[ai, bi] 互不相同

"""
from typing import List
from collections import defaultdict, deque

""" 方法1：拓扑排序（广度优先遍历）"""
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        adj = defaultdict(list)         # 邻接表。
        indegrees = [0] * numCourses    # 入度表。
        res = []

        for cur, pre in prerequisites:  # [ai, bi] 表示如果要学习课程 ai 则 必须 先学习课程  bi 。
            adj[pre].append(cur)        # 把所有顺序加入图中
            indegrees[cur] += 1
        
        queue = []                      # 借助一个队列 queue，将所有入度为 0 的节点入队
        for i in range(numCourses):     # 首先遍历一遍课程，
            if indegrees[i] == 0:       # 把所有入度为 0 的结点加入队列
                queue.append(i)
                
        while queue:            # 当 queue 非空时
            pre = queue.pop(0)  # 从队首取出一个节点
            res.append(pre)     # 放入答案中
            
            for cur in adj[pre]:            # 遍历邻接表
                indegrees[cur] -= 1         # 将节点对应所有邻接节点 cur 的入度 -1（并不是真正从邻接表中删除此节点 pre）
                if indegrees[cur] == 0:     # 当入度 −1后邻接节点 cur 的入度为 0
                    queue.append(cur)       # 说明 cur 所有的前驱节点已经被 “删除”，此时将 cur 入队。

        if len(res) != numCourses:   # 若整个课程安排图是有向无环图（即可以安排），则所有节点一定都入队并出队过，即完成拓扑排序。
            return []                   # 因此，如果答案长度 不等于 课程个数，不可能完成所有课程，返回 空数组
            
        return res


""" 方法二：深度优先遍历
    通过 DFS 判断图中是否有环"""
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)   # 存储有向图
        visited = [0] * numCourses  # 标记每个节点的状态：0 = 未搜索，1 = 搜索中，2 = 已完成
        result = list()             # 用数组来模拟栈，下标 0 为栈底，n-1 为栈顶
        valid = True                # 判断有向图中是否有环

        for cur, pre in prerequisites:  # [ai, bi] 表示如果要学习课程 ai 则 必须 先学习课程  bi 。
            graph[pre].append(cur)      # 把所有顺序加入图中
        
        def dfs(u: int):
            nonlocal valid
            visited[u] = 1  # 将节点标记为「搜索中」
            for v in graph[u]:      # 搜索其相邻节点 # 只要发现有环，立刻停止搜索
                if visited[v] == 0: # 如果「未搜索」
                    dfs(v)          # 那么使用dfs搜索相邻节点
                    if not valid:
                        return
                elif visited[v] == 1:   # 如果「搜索中」说明找到了环
                    valid = False
                    return
            
            visited[u] = 2      # 将节点标记为「已完成」
            result.append(u)    # 将节点入栈
        
        for i in range(numCourses):     # 每次挑选一个「未搜索」的节点，开始进行深度优先搜索
            if valid and not visited[i]:
                dfs(i)
        
        if not valid:
            return list()
        
        # 如果没有环，那么就有拓扑排序
        return result[::-1]     # 注意下标 0 为栈底，因此需要将数组反序输出

    

if __name__ == "__main__":
    numCourses = 6
    prerequisites = [[5,3],[5,4],[3,0],[3,1],[4,1],[4,2]]
    sol = Solution()
    result = sol.findOrder(numCourses, prerequisites)
    print (result)