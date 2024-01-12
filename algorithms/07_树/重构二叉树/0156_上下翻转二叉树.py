"""
https://leetcode-cn.com/problems/binary-tree-upside-down/

给你一个二叉树的根节点 root ，请你将此二叉树上下翻转，并返回新的根节点。

你可以按下面的步骤翻转一棵二叉树：
    原来的左子节点变成新的根节点
    原来的根节点变成新的右子节点
    原来的右子节点变成新的左子节点

上面的步骤逐层进行。题目数据保证每个右节点都有一个同级节点（即共享同一父节点的左节点）且不存在子节点。

示例 1：
    输入：root = [1,2,3,4,5]
    输出：[4,5,2,null,null,3,1]

示例 2：
    输入：root = []
    输出：[]

示例 3：
    输入：root = [1]
    输出：[1]

提示：
    树中节点数目在范围 [0, 10] 内
    1 <= Node.val <= 10
    树中的每个右节点都有一个同级节点（即共享同一父节点的左节点）
    树中的每个右节点都没有子节点

"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

""" 递归 """
class Solution:
    def upsideDownBinaryTree(self, root: TreeNode) -> TreeNode:
        if not root or not root.left:   # 节点为空，或左子节点为空
            return root
        new_root = self.upsideDownBinaryTree(root.left)     # 处理左子树（左子树翻转后，返回的根节点，也就是二叉树翻转后的根节点）
        root.left.right = root          # 处理根节点，根节点变成其左子节点的右节点
        root.left.left = root.right     # 根节点的右子节点变成其左子节点的左子节点
        root.left = None                # 将根节点的左右子节点置空
        root.right = None
        return new_root

""" 迭代法 类似反转链表 """
class Solution:
    def upsideDownBinaryTree(self, root: TreeNode) -> TreeNode:
        parent = None
        parent_right = None
        cur = root

        while cur:
            cur_left = cur.left
            cur_right = cur.right    # 存下来cur的左右节点 因为后面重新指向获取不到原来的左右节点了

            cur.left = parent_right
            cur.right = parent

            parent = cur
            parent_right = cur_right
            cur = cur_left
        # 当cur为空，parent为最左下角的节点
        return parent

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    sol = Solution()
    result = sol.upsideDownBinaryTree(root)
    print(result)