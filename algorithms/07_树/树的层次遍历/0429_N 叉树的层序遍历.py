"""
https://leetcode-cn.com/problems/n-ary-tree-level-order-traversal/

给定一个 N 叉树，返回其节点值的层序遍历。（即从左到右，逐层遍历）。

树的序列化输入是用层序遍历，每组子节点都由 null 值分隔（参见示例）。

示例 1：
    输入：root = [1,null,3,2,4,null,5,6]
            1
          ↙ ↓ ↘
        3   2   4
       ↙ ↘
      5   6
    输出：[[1],[3,2,4],[5,6]]

示例 2：
    输入：root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
    输出：[[1],[2,3,4,5],[6,7,8,9,10],[11,12,13],[14]]
 
提示：
    树的高度不会超过 1000
    树的节点总数在 [0, 10^4] 之间

"""
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

from typing import List

""" 迭代法 """
class Solution:
    def levelOrder(self, root):
        res = []
        if not root:
            return res
        queue = [root]        # 队列初始化
        while queue:
            lenQue = len(queue) # 先获取队列长度，因为后面队列会变化
            sub = []            # 每层的子列表
            for i in range(lenQue):   # 遍历每层
                node = queue.pop(0)   # 获取队列首元素
                sub.append(node.val)  # 把该层的元素添加进去
                if node.children:     #
                    queue.extend(node.children)   # 扩展队列下一层级元素，注意用extend
            res.append(sub)
        return res
"""
            1
          ↙ ↓ ↘
        3   2   4
       ↙ ↘
      5   6
    输出：[[1],[3,2,4],[5,6]]
"""

""" 递归法 """
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        res = []
        self.level(root, 1, res)    # 从深度1开始
        return res
    
    def level(self,root: 'Node', depth, res):   # 为了让递归的过程中的同一层的节点放在同一个列表中，需要记录深度depth
        if root == None:
            return []
        if len(res) < depth:    # 若当前行对应的列表不存在，
            res.append([])      # 加一个空列表
        res[depth - 1].append(root.val) # 将当前节点的值加入当前行的 res 中
        for child in root.children:     # 递归处理子树
            self.level(child, depth + 1, res)   # 层数加一，记录下一层

""" BFS """
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:    # 首先判断root是否有内容，如果没有则输出[]
            return []
        queue = [root]  # 设置列表queue, 存放节点
        res = []        # 设置列表res, 存放值
        while queue:    # 开始循环，
            res.append(node.val for node in queue)  # 通过for循环将queue里面的值分离出来一次性加入res中，
            queue = [child for node in queue for child in node.children]    #queue队列通过两个for循环，前面一个取出queue的节点，后一个将取出的节点再取子节点，然后得到queue
        return res      # 最后循环结束输出res