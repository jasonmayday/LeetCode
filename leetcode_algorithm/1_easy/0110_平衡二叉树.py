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

def list_to_binarytree(nums):
    def level(index):
        if index >= len(nums) or nums[index] is None:
            return None
        root = TreeNode(nums[index])
        root.left = level(2 * index + 1)
        root.right = level(2 * index + 2)
        return root
    return level(0)


""" 后序遍历 + 剪枝 （从底至顶）
    对二叉树做后序遍历：左子树 -> 右子树 -> 根结点，先访问左子树再访问右子树，在比较左右子树
    从底至顶返回子树最大高度，若判定某子树不是平衡树则 “剪枝” ，直接向上返回。"""
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def recur(root):
            if not root:
                return 0    # 递归终止条件1：当越过叶子节点时，返回高度 0
            
            left = recur(root.left)
            if left == -1:
                return -1   # 递归终止条件2：当左子树高度 == -1 时，代表此子树的左子树不是平衡树，因此直接返回 -1
            
            right = recur(root.right)
            if right == -1:
                return -1   # 递归终止条件3：当右子树高度 == -1 时，代表此子树的右子树不是平衡树，因此直接返回 -1
            
            if abs(left - right) <= 1:      # 递归返回值：当节点 root 左 / 右子树的高度差 <= 1
                return max(left, right) + 1 # 则返回以节点 root 为根节点的子树的最大高度，即节点 root 的左右子树中最大高度加 1
            else:                           # 当节点 root 左/右子树的高度差 ≥ 2:
                return -1                   # 则返回 -1，代表 此子树不是平衡树
        
        return recur(root) != -1    # 若 recur(root) != -1 ，则说明此树平衡，返回 true ；否则返回 false

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
            return -1       # 递归终止条件3：当右子树高度 == -1 时，代表此子树的右子树不是平衡树，因此直接返回 -1
        
        if abs(left - right) <= 1:          # 递归返回值：当节点root 左 / 右子树的高度差 <= 1
            return max(left, right) + 1     # 则返回以节点root为根节点的子树的最大高度，即节点 root 的左右子树中最大高度加 1
        else:                               # 当节点root 左/右子树的高度差 ≥ 2:
            return -1                       # 则返回 -1，代表 此子树不是平衡树

""" 先序遍历 + 判断深度 （从顶至底）
    构造一个获取当前子树的深度的函数 depth(root) """
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def depth(root: TreeNode) -> int:   # 计算树 root 的深度
            if not root:    # 当 root 为空，即越过叶子节点，则返回高度 0
                return 0
            return max(depth(root.left), depth(root.right)) + 1   # 终止条件： 当 root 为空，即越过叶子节点，则返回高度 0

        if not root:        # 若树根节点 root 为空，则直接返回 true
            return True
        # 所有子树都需要满足平衡树性质，因此者使用 and 逻辑
        #               判断 当前子树 是否是平衡树              and        先序遍历递归，判断当前子树的左(右)子树是否是平衡树
        return abs(depth(root.left) - depth(root.right)) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)

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

if __name__ == "__main__":
    root = list_to_binarytree([1,2,2,3,3,None,None,4,4])
    sol = Solution()
    result = sol.isBalanced(root)
    print (result)