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

"""方法1：自顶向下的递归"""
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def height(root: TreeNode) -> int:
            if not root:    # 当 root 为空，即越过叶子节点，则返回高度 0
                return 0
            return max(height(root.left), height(root.right)) + 1   # 终止条件： 当 root 为空，即越过叶子节点，则返回高度 0

        if not root:        # 若树根节点 root 为空，则直接返回 true
            return True
        # 所有子树都需要满足平衡树性质，因此者使用 and 逻辑
        #               判断 当前子树 是否是平衡树                and        先序遍历递归，判断当前子树的左(右)子树是否是平衡树
        return abs(height(root.left) - height(root.right)) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)

"""方法1：自顶向下的递归（另一种写法）"""
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        return abs(self.depth(root.left) - self.depth(root.right)) <= 1 and \
            self.isBalanced(root.left) and self.isBalanced(root.right)              # 三者全部成立才为True

    def depth(self, root):
        if not root: 
            return 0
        return max(self.depth(root.left), self.depth(root.right)) + 1

"""方法2：自底向上的递归"""
"""对二叉树做后序遍历：左子树 -> 右子树 -> 根结点，先访问左子树再访问右子树，在比较左右子树
   从底至顶返回子树最大高度，若判定某子树不是平衡树则 “剪枝” ，直接向上返回。"""
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        return self.recur(root) != -1       # 若 recur(root) != -1 ，则说明此树平衡，返回 true ；否则返回 false

    def recur(self, root):
        if not root: 
            return 0        # 递归终止条件1：当越过叶子节点时，返回高度 0
        
        left = self.recur(root.left)
        if left == -1: 
            return -1       # 递归终止条件2：当左子树高度 == -1 时，代表此子树的左子树不是平衡树，因此直接返回 -1
        
        right = self.recur(root.right)
        if right == -1: 
            return -1       # 递归终止条件2：当右子树高度 == -1 时，代表此子树的右子树不是平衡树，因此直接返回 -1
        
        if abs(left - right) < 2:           # 递归返回值：当节点root 左 / 右子树的高度差 < 2
            return max(left, right) + 1     # 则返回以节点root为根节点的子树的最大高度，即节点 root 的左右子树中最大高度加 1
        else:                               # 当节点root 左/右子树的高度差 ≥ 2:
            return -1                       # 则返回 -1，代表 此子树不是平衡树

if __name__ == "__main__":
    data = [1,2,2,3,3,None,None,4,4]
    data_list = list(data)
    btree = BiTree(data_list)
    root = btree.createBiTree()
    
    sol = Solution()
    result = sol.isBalanced(root)
    print (result)