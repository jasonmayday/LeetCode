
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    ''' 广度优先（ Breath First Search）层次遍历
        递归不好实现广度优先（层序）遍历，如果不是题目要求，使用迭代实现BFS（层序）遍历。
        使用队列实现树的层次遍历
        '''
    
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        def helper(root, depth):
            if not root:
                return []
            if len(res) == depth:
                res.append([]) # start the current depth
            res[depth].append(root.val) # fulfil the current depth
            if  root.left:
                helper(root.left, depth + 1) # process child nodes for the next depth
            if  root.right:
                helper(root.right, depth + 1)
        helper(root, 0)
        return res

 
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        if not root:
            return []
        
        def bfs(index, r):
            if len(res) < index:    # 假设res是[ [1],[2,3] ]， index是3，就再插入一个空list放到res中
                res.append([])      # 将当前节点的值加入到res中，index代表当前层，假设index是3，节点值是99
			
            # res是[ [1],[2,3] [4] ]，加入后res就变为 [ [1],[2,3] [4,99] ]
            res[index-1].append(r.val)
            # 递归的处理左子树，右子树，同时将层数index+1
            if r.left:
                bfs(index+1,r.left)
            if r.right:
                bfs(index+1,r.right)
        bfs(1, root)
        return res


    ''' DFS
        深度优先遍历 Depth First Search，主要有三种子方法:
        前序遍历
        中序遍历
        后序遍历'''

    ''' 前序遍历 (Pre-Order Traversal) ：根结点 ---> 左子树 ---> 右子树'''
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        def preorder(root):
            if root:
                res.append(root.val)    # 执行操作
                preorder(root.left)
                preorder(root.right)
        preorder(root)
        return res

    '''中序遍历 (In-Order Traversal) ：左子树 ---> 根结点 ---> 右子树'''
    '''二叉搜索树采用中序遍历，就是一个有序数组'''
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        def inorder(root):
            if root:
                inorder(root.left)
                res.append(root.val)    # 执行操作
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
                res.append(root.val)    # 执行操作
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
    '''
           1
         ↙   ↘
       2       3
     ↙  ↘    ↙  ↘
    4    5   6    7
                    ↘
                      8
    '''
    sol = Solution()

    result1 = sol.preorderTraversal(root)
    result2 = sol.inorderTraversal(root)
    result3 = sol.postorderTraversal(root)
    result4 = sol.levelOrder(root)

    print ("前序遍历结果: ", result1) 
    print ("中序遍历结果: ", result2) 
    print ("后序遍历结果: ", result3)
    print ("层次遍历结果: ", result4) 



"""
    先序遍历：
    def dfs(root):
        if not root:
            return
        执行操作
        dfs(root.left)
        dfs(root.right)
        
    中序遍历：
    def dfs(root):
        if not root:
            return
        dfs(root.left)
        执行操作
        dfs(root.right)
        
    后序遍历：
    def dfs(root):
        if not root:
            return
        dfs(root.left)
        dfs(root.right)
        执行操作
"""




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

