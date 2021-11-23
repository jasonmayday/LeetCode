"""
https://leetcode-cn.com/problems/range-sum-of-bst/

给定二叉搜索树的根结点 root，返回值位于范围 [low, high] 之间的所有结点的值的和。

示例 1：
    输入：root = [10,5,15,3,7,null,18], low = 7, high = 15
    输出：32

示例 2：
    输入：root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
    输出：23

提示：
    树中节点数目在范围 [1, 2 * 10^4] 内
    1 <= Node.val <= 10^5
    1 <= low <= high <= 10^5
    所有 Node.val 互不相同

"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def list_to_binarytree(nums):
    def level(index):
        if index >= len(nums) or nums[index] is None:
            return None
        root = TreeNode(nums[index])
        root.left = level(2 * index + 1)
        root.right = level(2 * index + 2)
        return root
    return level(0)

from collections import deque

'''DFS'''
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        if not root:
            return 0
        if root.val > high: # root 节点的值大于 high
            return self.rangeSumBST(root.left, low, high)
            # 由于二叉搜索树右子树上所有节点的值均大于根节点的值，即均大于 high，故无需考虑右子树，返回左子树的范围和。
        if root.val < low:  # root 节点的值小于 low
            return self.rangeSumBST(root.right, low, high)
            # 由于二叉搜索树左子树上所有节点的值均小于根节点的值，即均小于 low，故无需考虑左子树，返回右子树的范围和。
        return root.val + self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high)

'''递归,中序遍历'''
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        self.cur = 0
        def dfs(node):
            if node.left:
                dfs(node.left)
            if node.val > high:         # \
                return                  #  \ 需要执行的操作：
            if node.val >= low:         #  / 大于 high 的无需考虑
                self.cur += node.val    # /  大于 low 的把值加入
            if node.right:
                dfs(node.right)
        dfs(root)
        return self.cur

if __name__ == "__main__":
    root = list_to_binarytree([10,5,15,3,7,13,18,1,None,6])
    low = 6
    high = 10
    sol = Solution()
    result = sol.rangeSumBST(root, low, high)
    print (result)