'''
给定一个二叉树，返回它的 后序 遍历。

示例:

输入: [1,null,2,3]  
   1
    \
     2
    /
   3 

输出: [3,2,1]

进阶: 递归算法很简单，你可以通过迭代算法完成吗？

'''
# 后序遍历：按照访问左子树——右子树——根节点

from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

""" 递归 """
class Solution(object):
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        def postorder(root):
            if root:
                postorder(root.left)
                postorder(root.right)
                res.append(root.val)
        postorder(root)
        return res

""" 迭代 """
class Solution(object):
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

if __name__ == "__main__":
    
    '''
           1
         ↙   ↘
       2       3
     ↙  ↘    ↙  ↘
    4    5   6    7
                    ↘
                      8
    '''
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    root.right.right.right = TreeNode(8)

    sol = Solution()
    result = sol.postorderTraversal(root)
    print (result)  