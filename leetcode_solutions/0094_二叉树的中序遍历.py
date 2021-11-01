'''
给定一个二叉树，返回它的 后序 遍历。

示例 1：
输入：root = [1,null,2,3]
输出：[1,3,2]

示例 2：
输入：root = []
输出：[]

示例 3：
输入：root = [1]
输出：[1]

示例 4：
输入：root = [1,2]
输出：[2,1]

示例 5：
输入：root = [1,null,2]
输出：[1,2]

提示：
树中节点数目在范围 [0, 100] 内
-100 <= Node.val <= 100

'''
# 中序遍历：左子树——根节点——右子树

# Definition for a binary tree node.
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
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        def postorder(root):
            if root:
                postorder(root.left)
                res.append(root.val)
                postorder(root.right)
        postorder(root)
        return res


sol = Solution()
result = sol.postorderTraversal(root)
print (result)  