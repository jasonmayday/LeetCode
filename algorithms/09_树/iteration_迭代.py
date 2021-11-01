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
    # 在节点达到null层时进行判断
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res,stack = [],[]       # 利用栈进行临时存储
        while stack or root:    # stack为空且node为null时，说明遍历结束
            while root:         # 可以进入左子树时，先访问，再进入
                res.append(root.val)    # 首先访问该节点（先序），之后顺序入栈右子树，左子树
                stack.append(root)
                root = root.left
            root = stack.pop()
            root = root.right   # 否则进入栈中节点的右子树
        return res
        
    # 中序遍历 (In-Order Traversal)：左子树 ---> 根结点 ---> 右子树
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res,stack = [],[]       # 利用栈进行临时存储
        while stack or root:    # stack为空且root为null时，说明已经遍历结束
            while root:         # 可以深入左子树
                stack.append(root)
                root = root.left
            root = stack.pop()     # 否则访问栈中节点，并深入右子树
            res.append(root.val)   
            root = root.right
        return res
        
    # 后序遍历 (Post-Order Traversal)：左子树 ---> 右子树 ---> 根结点
    # 后序遍历：左 → 右 → 根，前序遍历：根 → 左 → 右。
    # 后序遍历翻转后为根 → 右 → 左，与前序遍历相比仅仅左右顺序调换。
    # 在前序遍历中，把left 和 right的顺序调换，然后输出反转的树即可。
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



