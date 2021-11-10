'''
https://leetcode-cn.com/problems/balanced-binary-tree/

给定一个二叉树，判断它是否是高度平衡的二叉树。

本题中，一棵高度平衡二叉树定义为：

一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1 。

示例 1：
    输入：root = [3,9,20,null,null,15,7]
    输出：true

示例 2：
    输入：root = [1,2,2,3,3,null,null,4,4]
    输出：false

示例 3：
    输入：root = []
    输出：true
 
提示：
    树中的节点数在范围 [0, 5000] 内
    -10^4 <= Node.val <= 10^4

'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 利用题目给的列表建一个树
class BiTree(object):
    def __init__(self, data_list):
        # 初始化即将传入的列表的迭代器
        self.it = iter(data_list)

    def createBiTree(self, bt=None):    
        try:
            # 步进获取下一个元素
            next_data = next(self.it)
            # 如果当前列表元素为'#', 则认为其为 None
            if next_data is "#":
                bt = None
            else:
                bt = TreeNode(next_data)
                bt.left = self.createBiTree(bt.left)
                bt.right = self.createBiTree(bt.right)
        except Exception as e:
            print(e)
        return bt

# https://leetcode-cn.com/problems/balanced-binary-tree/solution/balanced-binary-tree-di-gui-fang-fa-by-jin40789108/

# 方法一：自顶向下的递归      
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def height(root: TreeNode) -> int:
            if not root:
                return 0
            return max(height(root.left), height(root.right)) + 1

        if not root:
            return True
        return abs(height(root.left) - height(root.right)) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)

# 方法二：自底向上的递归
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def height(root: TreeNode) -> int:
            if not root:
                return 0
            leftHeight = height(root.left)
            rightHeight = height(root.right)
            if leftHeight == -1 or rightHeight == -1 or abs(leftHeight - rightHeight) > 1:
                return -1
            else:
                return max(leftHeight, rightHeight) + 1

        return height(root) >= 0

if __name__ == "__main__":
    data = [1,2,2,3,3,None,None,4,4]
    data_list = list(data)
    btree = BiTree(data_list)
    root = btree.createBiTree()

    sol = Solution()
    result = sol.isBalanced(root)
    print (result)