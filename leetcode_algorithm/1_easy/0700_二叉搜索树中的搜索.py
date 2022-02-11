"""
https://leetcode-cn.com/problems/search-in-a-binary-search-tree

给定二叉搜索树（BST）的根节点和一个值。 你需要在BST中找到节点值等于给定值的节点。 返回以该节点为根的子树。 如果节点不存在，则返回 NULL。

例如，

给定二叉搜索树:

        4
       / \
      2   7
     / \
    1   3

和值: 2

你应该返回如下子树:

      2     
     / \   
    1   3
在上述示例中，如果要找的值是 5，但因为没有节点值为 5，我们应该返回 NULL。

"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.val)   

def list_to_binarytree(nums):
    def level(index):
        if index >= len(nums) or nums[index] is None:
            return None
        root = TreeNode(nums[index])
        root.left = level(2 * index + 1)
        root.right = level(2 * index + 2)
        return root
    return level(0)

"""方法一：递归"""
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if root is None or val == root.val:
            return root
        if val < root.val:                          # 如果要找的值小于当前值
            return self.searchBST(root.left, val)   # 搜索左子树
        else:                                       # 如果要找的值大于当前值
            return self.searchBST(root.right, val)  # 搜索右子树

"""方法二：迭代"""
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        while root is not None and root.val != val:             # 如果根节点不空，且根节点不是目的节点 
            if val < root.val:      # 如果 val < root.val，
                root = root.left    # 进入根节点的左子树查找
            else:                   # 如果 val > root.val，
                root = root.right   # 进入根节点的右子树查找
        return root

if __name__ == "__main__":
    root = list_to_binarytree([2,2,5,None,None,5,7])
    val = 5
    sol = Solution()
    result = sol.searchBST(root, val)
    print(result)