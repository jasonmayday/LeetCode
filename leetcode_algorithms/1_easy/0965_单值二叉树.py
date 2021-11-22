"""
https://leetcode-cn.com/problems/univalued-binary-tree/

如果二叉树每个节点都具有相同的值，那么该二叉树就是单值二叉树。

只有给定的树是单值二叉树时，才返回 true；否则返回 false。

示例 1：
    输入：[1,1,1,1,1,null,1]
    输出：true

示例 2：
    输入：[2,2,2,5,2]
    输出：false
 
提示：
    给定树的节点数范围是 [1, 100]。
    每个节点的值都是整数，范围为 [0, 99] 。

"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def list_to_binarytree(nums):
    def level(index):
        if index >= len(nums) or nums[index] is None:
            return None
        root = TreeNode(nums[index])
        root.left = level(2 * index + 1)
        root.right = level(2 * index + 2)
        return root
    return level(0)

"""深度优先搜索"""
class Solution(object):
    def isUnivalTree(self, root):
        vals = []       # 获取这颗树中的所有节点的值

        def dfs(node):  # 深度优先搜索，前序搜索
            if node:
                vals.append(node.val)
                dfs(node.left)
                dfs(node.right)

        dfs(root)
        return len(set(vals)) == 1  # 判断所有节点的值是不是都相等

"""递归"""
class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        if not root: return True
        if root.left and root.left.val != root.val: return False
        if root.right and root.right.val != root.val: return False
        return self.isUnivalTree(root.left) and self.isUnivalTree(root.right)

if __name__ == "__main__":
    root = list_to_binarytree([1,1,1,1,1,None,1])
    sol = Solution()
    result = sol.isUnivalTree(root)
    print (result)