'''

给定一个二叉树，找出其最大深度。

二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。

说明: 叶子节点是指没有子节点的节点。

示例：
给定二叉树 [3,9,20,null,null,15,7]，

      3
     / \
    9  20
      /  \
     15   7

返回它的最大深度 3 。

'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

"""深度优先搜索"""
class Solution:
    def maxDepth(self, root):
        if root is None: 
            return 0 
        else:                                           # 如果我们知道了左子树和右子树的最大深度 ll 和 rr，那么该二叉树的最大深度即为 max(l,r)+1
            left_height = self.maxDepth(root.left)      # 而左子树和右子树的最大深度又可以以同样的方式进行计算。
            right_height = self.maxDepth(root.right)    # 先递归计算出其左子树和右子树的最大深度
            return max(left_height, right_height) + 1
            

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