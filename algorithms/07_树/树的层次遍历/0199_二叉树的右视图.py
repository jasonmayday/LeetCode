"""
https://leetcode-cn.com/problems/binary-tree-right-side-view/

给定一个二叉树的 根节点 root，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。

示例 1:
    输入: [1,2,3,null,5,null,4]
    输出: [1,3,4]

示例 2:
    输入: [1,null,3]
    输出: [1,3]

示例 3:
    输入: []
    输出: []

提示:
    二叉树的节点个数的范围是 [0,100]
    -100 <= Node.val <= 100 

"""

from typing import List
from collections import deque

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def list_to_binarytree(nums):
    def level(index):
        if index >= len(nums) or nums[index] is None:
            return None
        root = TreeNode(nums[index])
        root.left = level(2 * index + 1)    # 往左递推  # 从根开始一直到最左，直至为空
        root.right = level(2 * index + 2)   # 往右回溯  # 再返回上一个根，回溯右
        return root     # 再返回根
    return level(0)


"""
           1            ←
         ↙   ↘
       2       3        ←
        ↘        ↘
         5        4     ←
"""

""" BFS + 迭代 
    对二叉树进行层次遍历，那么对于每层来说，最右边的结点一定是最后被遍历到的。"""
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root: return []
        res = []

        def bfs(root):
            queue = [root]
            while queue:
                nxt = []        # 存储当前层的子节点列表
                res.append(queue[-1].val)       # 把每一层遍历到的最后一个（最右边）加入答案列表
                for node in queue:              # 对当前层的每个节点遍历
                    if node.left:               # 如果左子节点存在，入 nxt 队列
                        nxt.append(node.left)
                    if node.right:              # 如果右子节点存在，入 nxt 队列
                        nxt.append(node.right)
                queue = nxt                     # 后把queue更新成下一层的结点，继续遍历下一层
        
        bfs(root)
        return res


""" DFS + 递归 """
class Solution:
    """ 根结点 ---> 左子树 ---> 右子树
        能保证每层最后一个遍历的到的元素一定是最右边的元素"""
    def rightSideView(self, root: TreeNode) -> List[int]:
        res = []
        def dfs(root, depth):
            if not root:
                return 
            if len(res) <= depth:
                res.append(0)           # 每向下一层就直接先插入一个0占位
            res[depth] = root.val       # 层数即为答案的下标数
            dfs(root.left, depth + 1)   # 遍历下一层，
            dfs(root.right, depth + 1)  # 每层最后一个遍历的到的元素一定是最右边的元素（可能是有左子树的右节点也可能是没有右子树的左节点）
        
        dfs(root, 0)
        return res
    
    """ 根结点 ---> 右子树 ---> 左子树
        遍历到新的一层时先把第一个元素加入答案（右边的）"""
    def rightSideView(self, root: TreeNode) -> List[int]:
        res = []
        def dfs(root, depth):
            if not root:
                return []
            if len(res) <= depth:
                res.append(root.val)
            dfs(root.right, depth + 1)
            dfs(root.left, depth + 1) 

        dfs(root, 0)
        return res

if __name__ == "__main__":
    root = list_to_binarytree([1,2,3,None,5,None,4])
    sol = Solution()
    result = sol.rightSideView(root)
    print (result)