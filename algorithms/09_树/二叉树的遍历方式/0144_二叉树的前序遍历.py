'''
给定一个二叉树，返回它的 前序 遍历。

示例:

输入: [1,null,2,3]  
  1
    \
     2
    /
   3 

输出: [1,2,3]

进阶: 递归算法很简单，你可以通过迭代算法完成吗？

'''
# 后序遍历：按照访问左子树——右子树——根节点

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
'''
       1
     ↙   ↘
   2       3
 ↙  ↘    ↙  ↘
4    5   6    7
                ↘
                  8
'''

'''前序遍历 (Pre-Order Traversal) ：根结点 ---> 左子树 ---> 右子树'''

""" 递归 """
class Solution(object):
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        def preorder(root):
            if root:
                res.append(root.val)
                preorder(root.left)
                preorder(root.right)
        preorder(root)
        return res

""" 迭代 """
class Solution(object):
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

if __name__ == "__main__":
    sol = Solution()
    result = sol.preorderTraversal(root)
    print (result)  