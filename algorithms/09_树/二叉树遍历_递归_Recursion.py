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

class Solution(object):
    '''广度优先（ Breath First Search）层次遍历'''
    #  使用队列实现树的层次遍历

    '''深度优先遍历 Depth First Search，DFS，主要有三种子方法:
       前序遍历
       中序遍历
       后序遍历'''

    '''前序遍历 (Pre-Order Traversal) ：根结点 ---> 左子树 ---> 右子树'''
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        def preorder(root):
            if root:
                res.append(root.val)
                preorder(root.left)
                preorder(root.right)
        preorder(root)
        return res

    '''中序遍历 (In-Order Traversal) ：左子树 ---> 根结点 ---> 右子树'''
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        def inorder(root):
            if root:
                inorder(root.left)
                res.append(root.val)
                inorder(root.right)
        inorder(root)
        return res    

    '''后序遍历 (Post-Order Traversal) ：左子树 ---> 右子树 ---> 根结点'''
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        def postorder(root):
            if root:
                postorder(root.left)
                postorder(root.right)
                res.append(root.val)
        postorder(root)
        return res

if __name__ == "__main__":  
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    root.right.right.right = TreeNode(8)

    sol = Solution()

    result1 = sol.preorderTraversal(root)
    result2 = sol.inorderTraversal(root)
    result3 = sol.postorderTraversal(root)

    print ("前序遍历结果: ", result1) 
    print ("中序遍历结果: ", result2) 
    print ("后序遍历结果: ", result3) 
 










'''
    # 另一个版本的递归实现
    # 前序递归
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)
    
    # 中序递归 
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []    
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
    
    # 后序递归
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []      
        return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]
'''

