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
    # 前序遍历 (Pre-Order Traversal) ：根结点 ---> 左子树 ---> 右子树
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        def preorder(root):
            if root:
                res.append(root.val)
                preorder(root.left)
                preorder(root.right)
        preorder(root)
        return res

    # 中序遍历 (In-Order Traversal) ：左子树 ---> 根结点 ---> 右子树
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        def inorder(root):
            if root:
                inorder(root.left)
                res.append(root.val)
                inorder(root.right)
        inorder(root)
        return res    

    # 后序遍历 (Post-Order Traversal) ：左子树 ---> 右子树 ---> 根结点
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        def postorder(root):
            if root:
                postorder(root.left)
                postorder(root.right)
                res.append(root.val)
        postorder(root)
        return res

    '''
    如果是在树中用BFS与DFS，因为一个节点顶多有两个子节点，我们已经明确知道这个节点除了子节点以外不会再有相邻节点，
    因此在搜索过程中也不会遇到重复的节点，所以不需要加集合searched。
    只需要按照BFS与DFS的思想与所用数据结构，遍历即可。

    而如果要再图中使用DFS或者BFS，需要加一个集合searched，里面是已经遍历过的点。
    '''
    # 层次遍历（广度优先 Breath First Search）
    def BFS(self, root: TreeNode) -> List[int]:
        res = []
        if root is None: # 递归结束条件：节点是None，结束函数调用
            return
        else:
            queue = [root]
            while queue:
                currentNode = queue.pop(0)
                res.append(currentNode.val)
                if currentNode.left:
                    queue.append(currentNode.left)
                if currentNode.right:
                    queue.append(currentNode.right)
        return res


    # 深度优先（Deep First Search）
    def DFS(self, root: TreeNode) -> List[int]:
        res = []
        if root is None: # 递归结束条件：节点是None，结束函数调用
            return
        else:
            stack = [root]
            while stack:
                currentNode = stack.pop()
                res.append(currentNode.val)
                if currentNode.right:
                    stack.append(currentNode.right)
                if currentNode.left:
                    stack.append(currentNode.left)
        return res

if __name__ == "__main__":
    sol = Solution()
    result1 = sol.preorderTraversal(root)
    result2 = sol.inorderTraversal(root)
    result3 = sol.postorderTraversal(root)
    result4 = sol.BFS(root)
    result5 = sol.DFS(root)
    print ("前序遍历结果: ", result1) 
    print ("中序遍历结果: ", result2) 
    print ("后序遍历结果: ", result3) 
    print ("广度优先结果: ", result4) 
    print ("深度优先结果: ", result5) 










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

