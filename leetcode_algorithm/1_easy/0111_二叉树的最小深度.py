'''
https://leetcode-cn.com/problems/minimum-depth-of-binary-tree/

给定一个二叉树，找出其最小深度。

最小深度是从根节点到最近叶子节点的最短路径上的节点数量。

说明：叶子节点是指没有子节点的节点。

示例 1：
    输入：root = [3,9,20,null,null,15,7]
    输出：2

示例 2：
    输入：root = [2,null,3,null,4,null,5,null,6]
    输出：5

提示：
    树中节点数的范围在 [0, 10^5] 内
    -1000 <= Node.val <= 1000

'''
import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

"""深度优先搜索：递归法
   遍历整棵树，记录最小深度。
   对于每一个非叶子节点，我们只需要分别计算其左右子树的最小叶子节点深度。这样就将一个大问题转化为了小问题，可以递归地解决该问题。"""
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        if not root.left and not root.right:
            return 1
        
        min_depth = 10**9
        
        if root.left:
            min_depth = min(self.minDepth(root.left), min_depth)    # 获得左子树的最小高度
        if root.right:
            min_depth = min(self.minDepth(root.right), min_depth)   # 获得右子树的最小高度
        
        return min_depth + 1

"""广度优先搜索：迭代法
   当我们找到一个叶子节点时，直接返回这个叶子节点的深度。广度优先搜索的性质保证了最先搜索到的叶子节点的深度一定最小。"""
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        que = collections.deque([(root, 1)])
        while que:
            node, depth = que.popleft()
            if not node.left and not node.right:
                return depth
            if node.left:
                que.append((node.left, depth + 1))
            if node.right:
                que.append((node.right, depth + 1))
        
        return 0

if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    sol = Solution()
    result = sol.minDepth(root)
    print (result)
    '''
        3
       / \
      9   20
         / \
        15  7
    '''