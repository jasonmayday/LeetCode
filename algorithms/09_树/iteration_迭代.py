'''
       1
     ↙   ↘
   2       3
 ↙  ↘    ↙  ↘
4    5   6    7
                ↘
                  8
'''

from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
root.right.right.right = TreeNode(8)

class Solution(object):
    # 前序遍历 (Pre-Order Traversal)：根结点 ---> 左子树 ---> 右子树
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res,stack = [],[]
        while stack or root:
            while root:
                res.append(root.val)
                stack.append(root)
                root = root.left
            root = stack.pop()
            root = root.right
        return res
        
    # 中序遍历 (In-Order Traversal)：左子树 ---> 根结点 ---> 右子树
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res,stack = [],[]
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            res.append(root.val)
            root = root.right
        return res
        
    # 后序遍历 (Post-Order Traversal)：左子树 ---> 右子树 ---> 根结点
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res,stack = [],[]
        while stack or root:
            while root:
                res.append(root.val)
                stack.append(root)
                root = root.right
            root = stack.pop()
            root = root.left
        return res[::-1]

sol = Solution()
result1 = sol.preorderTraversal(root)
result2 = sol.inorderTraversal(root)
result3 = sol.postorderTraversal(root)
print ("前序遍历结果: ", result1) 
print ("中序遍历结果: ", result2) 
print ("后序遍历结果: ", result3)  



