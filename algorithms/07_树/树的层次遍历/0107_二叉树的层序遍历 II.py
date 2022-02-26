"""
https://leetcode-cn.com/problems/binary-tree-level-order-traversal-ii/

给你二叉树的根节点 root ，返回其节点值 自底向上的层序遍历 。 （即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）

示例 1：
    输入：root = [3,9,20,null,null,15,7]
    输出：[[15,7],[9,20],[3]]

示例 2：
    输入：root = [1]
    输出：[[1]]

示例 3：
    输入：root = []
    输出：[]
 
提示：
    树中节点数目在范围 [0, 2000] 内
    -1000 <= Node.val <= 1000

"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.val)   

def list_to_binarytree(nums):
    def level(index):
        if index >= len(nums) or nums[index] is None:
            return None
        root = TreeNode(nums[index])
        root.left = level(2 * index + 1)    # 往左递推  # 从根开始一直到最左，直至为空
        root.right = level(2 * index + 2)   # 往右回溯  # 再返回上一个根，回溯右
        return root     # 再返回根
    return level(0)

from collections import deque
from typing import List

""" 解法1：迭代实现 BFS """
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res = []
        queue = [root]      # 首先拿出根节点，如果左子树/右子树不为空，就将他们放入队列中。
        while queue:
            size = len(queue)   # 获取当前队列的长度，这个长度相当于 当前这一层的节点个数
            tmp = []
            for _ in range(size):
                r = queue.pop(0)    # 将队列中的元素都拿出来(也就是获取这一层的节点)
                tmp.append(r.val)   # 放到临时 list 中
                if r.left:                  # 如果节点的左/右子树不为空
                    queue.append(r.left)    # 也放入队列中
                if r.right:
                    queue.append(r.right)
            res.append(tmp)     # 将临时 list 加入最终返回结果中
        return res[::-1]    # 翻转最终结果并返回


""" 解法2：递归实现 DFS """
class Solution(object):
    def levelOrderBottom(self, root):
        if not root:
            return []
        # 用来存放最终结果    
        res = []
        def dfs(root,index):
            if not root:
                return
            # 如果index大于res大小，说明这一层没有对应的集合，需要新创建    
            if index>len(res):
                res.append([])
            # 将当前层的元素直接放到对应层的末尾即可    
            res[index-1].append(root.val)
            # 继续遍历左右节点，同时将层高+1
            dfs(root.left,index+1)
            dfs(root.right,index+1)
        dfs(root,1)
        return res[::-1]


if __name__ == "__main__":
    root = list_to_binarytree([3,9,20,None,None,15,7])
    '''
           3
         ↙   ↘
       9       20
              ↙  ↘
             15    7
    '''
    sol = Solution()
    result = sol.levelOrderBottom(root)
    print(result)