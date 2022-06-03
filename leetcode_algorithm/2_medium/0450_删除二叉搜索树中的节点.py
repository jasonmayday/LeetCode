"""
https://leetcode.cn/problems/delete-node-in-a-bst/

给定一个二叉搜索树的根节点 root 和一个值 key，删除二叉搜索树中的 key 对应的节点，并保证二叉搜索树的性质不变。返回二叉搜索树（有可能被更新）的根节点的引用。

一般来说，删除节点可分为两个步骤：
    首先找到需要删除的节点；
    如果找到了，删除它。

示例 1:
    输入：root = [5,3,6,2,4,null,7], key = 3
    输出：[5,4,6,2,null,null,7]
    解释：给定需要删除的节点值是 3，所以我们首先找到 3 这个节点，然后删除它。
    一个正确的答案是 [5,4,6,2,null,null,7], 如下图所示。
    另一个正确答案是 [5,2,6,null,4,null,7]。

示例 2:
    输入: root = [5,3,6,2,4,null,7], key = 0
    输出: [5,3,6,2,4,null,7]
    解释: 二叉树不包含值为 0 的节点

示例 3:
    输入: root = [], key = 0
    输出: []

提示:
    节点数的范围 [0, 10^4].
    -10^5 <= Node.val <= 10^5
    节点值唯一
    root 是合法的二叉搜索树
    -10^5 <= key <= 10^5

进阶： 要求算法时间复杂度为 O(h)，h 为树的高度。

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
        root.left = level(2 * index + 1)    # 往左递推  # 从根开始一直到最左，直至为空
        root.right = level(2 * index + 2)   # 往右回溯  # 再返回上一个根，回溯右
        return root     # 再返回根
    return level(0)

"""方法一：递归"""
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if root is None:
            return None
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        elif root.left is None or root.right is None:
            root = root.left if root.left else root.right
        else:
            successor = root.right
            while successor.left:
                successor = successor.left
            successor.right = self.deleteNode(root.right, successor.val)
            successor.left = root.left
            return successor
        return root

if __name__ == "__main__":
    root = list_to_binarytree ([5,3,6,2,4,None,7])
    key = 3
    sol = Solution()
    result = sol.deleteNode(root, key)
    print (result)