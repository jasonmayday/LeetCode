'''
https://leetcode-cn.com/problems/er-cha-shu-de-shen-du-lcof/

输入一棵二叉树的根节点，求该树的深度。从根节点到叶节点依次经过的节点（含根、叶节点）形成树的一条路径，最长路径的长度为树的深度。

示例：
    给定二叉树 [3,9,20,null,null,15,7]，

      3
     / \
    9  20
      /  \
     15   7

    返回它的最大深度 3 。

提示：
    节点总数 <= 10000

注意：本题与主站 104 题相同：https://leetcode-cn.com/problems/maximum-depth-of-binary-tree/

'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

""" 递归 + 深度优先搜索 """
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:    # 节点为空，高度为 0
            return 0
        left_height = self.maxDepth(root.left)      # 递归计算左子树的最大深度
        right_height = self.maxDepth(root.right)    # 递归计算右子树的最大深度
        return max(left_height, right_height) + 1   # 二叉树的最大深度 = 子树的最大深度 + 1（1 是根节点）

""" 迭代 + 深度优先搜索 """
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root == None:    # 节点为空，高度为 0
            return 0
        queue = [root]      # 初始化队列和层次
        depth = 0
        while queue:        # 当队列不为空
            n = len(queue)  # 当前层的节点数
            
            for i in range(n):  # 弹出当前层的所有节点，并将所有子节点入队列
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            depth += 1
        return depth        # 二叉树最大层次即为二叉树最深深度

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(3)

    sol = Solution()
    result = sol.maxDepth(root)
    print (result)
    '''
        1
       / \
      2   2
     / \ / \
    3  4 4  3
    '''