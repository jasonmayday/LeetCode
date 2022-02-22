"""
https://leetcode-cn.com/problems/count-complete-tree-nodes/

给你一棵 完全二叉树 的根节点 root ，求出该树的节点个数。

完全二叉树 的定义如下：在完全二叉树中，除了最底层节点可能没填满外，其余每层节点数都达到最大值，并且最下面一层的节点都集中在该层最左边的若干位置。若最底层为第 h 层，则该层包含 1~ 2h 个节点。

示例 1：
    输入：root = [1,2,3,4,5,6]
    输出：6

示例 2：
    输入：root = []
    输出：0

示例 3：
    输入：root = [1]
    输出：1

提示：
    树中节点的数目范围是[0, 5 * 10^4]
    0 <= Node.val <= 5 * 10^4
    题目数据保证输入的树是 完全二叉树

进阶：遍历树来统计节点是一种时间复杂度为 O(n) 的简单解决方案。你可以设计一个更快的算法吗？

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


""" 暴力递归
    每个节点都访问一下，看有多少个"""
class Solution:
    def countNodes(self, root: TreeNode) -> int:    
        return self.getNodesNum(root)
    
    def getNodesNum(self, cur): # 1. 确定递归函数的参数和返回值：（参数就是传入树的根节点，返回就返回以该节点为根节点二叉树的节点数量）
        if not cur:     # 2. 确定终止条件：
            return 0    # 如果为空节点的话，就返回0，表示节点数为0。
        leftNum = self.getNodesNum(cur.left)    # 3. 确定单层递归的逻辑：先求它的左子树的节点数量
        rightNum = self.getNodesNum(cur.right)  # 再求的右子树的节点数量
        treeNum = leftNum + rightNum + 1        # 最后取总和再加一 （加1是因为算上当前中间节点）
        return treeNum

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)


""" 利用完全二叉树的性质 
    如果整个树不是满二叉树，就递归其左右子树，直到遇到满二叉树为止，用公式计算这个子树（满二叉树）的节点数量。"""
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        left = root.left
        right = root.right
        leftHeight = 0  # 这里初始为0是有目的的，为了下面求指数方便
        rightHeight = 0
        while left:     # 求左子树深度
            left = left.left
            leftHeight += 1
        while right:    # 求右子树深度
            right = right.right
            rightHeight += 1
        if leftHeight == rightHeight:       # 情况1：满二叉树：可以直接用 (2^树深度 - 1) 来计算，注意这里根节点深度为1。
            return (2 << leftHeight) - 1    # 注意(2<<1) 相当于2^2，所以leftHeight初始为0
        # 情况2：最后一层叶子节点没有满。分别递归左右子树，递归到某一深度一定会有左子树或者右子树为满二叉树，然后依然可以按照情况1来计算。
        return self.countNodes(root.left) + self.countNodes(root.right) + 1 
    

if __name__ == "__main__":
    root = list_to_binarytree ([1,2,3,4,5,6])
    sol = Solution()
    result = sol.countNodes(root)
    print (result)