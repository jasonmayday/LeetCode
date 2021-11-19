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
    '''前序遍历 (Pre-Order Traversal)：根结点 ---> 左子树 ---> 右子树'''
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
        
    '''中序遍历 (In-Order Traversal)：左子树 ---> 根结点 ---> 右子树'''
    """二叉搜索树采用中序遍历，就是一个有序数组。"""
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
        
    '''后序遍历 (Post-Order Traversal)：左子树 ---> 右子树 ---> 根结点'''
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


    '''
    如果是在树中用BFS与DFS，因为一个节点顶多有两个子节点，我们已经明确知道这个节点除了子节点以外不会再有相邻节点，
    因此在搜索过程中也不会遇到重复的节点，所以不需要加集合searched。
    只需要按照BFS与DFS的思想与所用数据结构，遍历即可。

    而如果要再图中使用DFS或者BFS，需要加一个集合searched，里面是已经遍历过的点。
    '''
    
    ''' 层次遍历（广度优先 Breath First Search）
        每次都从左到右、从上到下的去遍历一个图，那么就需要把一行中最左边先进来的先输出，最右边后进来的后输出。所以会用到队列。'''
    def BFS(self, root: TreeNode) -> List[int]:
        res = []         
        if root is None:
            return
        else:
            queue = [root] # 每次输出一行，所用数据结构为队列
            while queue:
                currentNode = queue.pop(0)   # 弹出元素
                res.append(currentNode.val)  # 打印元素值
                if currentNode.left:
                    queue.append(currentNode.left)
                if currentNode.right:
                    queue.append(currentNode.right)
        return res


    ''' 深度优先 (Deep First Search)
        从图的最上边先按照一条道深挖到最下面，在挖到底以后就需要再逐个返回到上面的顶点，再去遍历父节点是不是还有别的子节点。后进先出的模式，所以需要用到栈。'''
    def DFS(self, root: TreeNode) -> List[int]:
        res = []
        if root is None: 
            return
        else:
            stack = [root] # 每次深挖到底，所用数据结构为栈
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


