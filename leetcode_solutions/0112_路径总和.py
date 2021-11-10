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

import collections

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Tree:    
    def list_to_binarytree(self, nums):
        def level(index):
            if index >= len(nums) or nums[index] is None:
                return None

            root = TreeNode(nums[index])
            root.left = level(2 * index + 1)
            root.right = level(2 * index + 2)
            return root

        return level(0)

"""BFS"""
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        que_node = collections.deque([root])
        que_val = collections.deque([root.val])
        while que_node:
            now = que_node.popleft()
            temp = que_val.popleft()
            if not now.left and not now.right:
                if temp == sum:
                    return True
                continue
            if now.left:
                que_node.append(now.left)
                que_val.append(now.left.val + temp)
            if now.right:
                que_node.append(now.right)
                que_val.append(now.right.val + temp)
        return False

"""递归"""
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        if not root.left and not root.right:
            return sum == root.val
        return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)

if __name__ == "__main__":
    nums = [5,4,8,11,None,13,4,7,2,None,None,None,1]
    tree = Tree()
    root = tree.list_to_binarytree(nums)
    
    targetSum = 22

    sol = Solution()
    result = sol.hasPathSum(root, targetSum)
    print (result)  