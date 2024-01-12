"""
https://leetcode-cn.com/problems/diameter-of-binary-tree/

给定一棵二叉树，你需要计算它的直径长度。一棵二叉树的直径长度是任意两个结点路径长度中的最大值。这条路径可能穿过也可能不穿过根结点。

示例 :
给定二叉树

          1
         / \
        2   3
       / \     
      4   5   
     / \   \
    6   7   8
   /         \
  9          10
返回 6, 它的长度是路径 [9,6,4,2,5,8,10]。

注意：两结点之间的路径长度是以它们之间边的数目表示。

"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

"""深度优先搜索"""
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.ans = 1
        def depth(node):                # 任意一条路径均可以被看作由某个节点为起点，从其左子树和右子树向下遍历的路径拼接得到。
            if not node:                # 访问到空节点了，返回 0
                return 0
            L = depth(node.left)        # 左子树为根的子树的深度
            R = depth(node.right)       # 右子树为根的子树的深度
            self.ans = max(self.ans, L + R + 1)     # 计算 该节点为起点的路径经过节点数的最大值，即 L+R+1，如果更大则更新 ans
            return max(L, R) + 1    # 返回该节点为根的子树的深度
        depth(root)
        return self.ans - 1         # 求直径（即求路径长度的最大值）等效于求路径经过节点数的最大值减一

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.left.left.left = TreeNode(6)
    root.left.left.right = TreeNode(7)
    root.left.right.right = TreeNode(8)
    root.left.left.left.left = TreeNode(9)
    root.left.right.right.right = TreeNode(10)

    sol = Solution()
    result = sol.diameterOfBinaryTree(root)
    print(result)
    






