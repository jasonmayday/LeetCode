'''
https://leetcode-cn.com/problems/path-sum/

给你二叉树的根节点 root 和一个表示目标和的整数 targetSum ，判断该树中是否存在 根节点到叶子节点 的路径，这条路径上所有节点值相加等于目标和 targetSum 。

叶子节点 是指没有子节点的节点。

示例 1：
    输入：root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
    输出：true

示例 2：
    输入：root = [1,2,3], targetSum = 5
    输出：false

示例 3：
    输入：root = [1,2], targetSum = 0
    输出：false

提示：
    树中节点的数目在范围 [0, 5000] 内
    -1000 <= Node.val <= 1000
    -1000 <= targetSum <= 1000

'''
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

"""DFS"""
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root: return False
        if not root.left and not root.right:
            return sum == root.val
        return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)



if __name__ == "__main__":
    root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22

    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(8)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    
    targetSum = 22

    sol = Solution()
    result = sol.hasPathSum(root)
    print (result)  
    '''
        3
       / \
      9   20
         / \
        15  7
    ''' 