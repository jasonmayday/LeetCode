'''
https://leetcode-cn.com/problems/same-tree/

给你两棵二叉树的根节点 p 和 q ，编写一个函数来检验这两棵树是否相同。

如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。

示例 1：
    输入：p = [1,2,3], q = [1,2,3]
    输出：true

示例 2：
    输入：p = [1,2], q = [1,null,2]
    输出：false

示例 3：
    输入：p = [1,2,1], q = [1,1,2]
    输出：false
 
提示：
    两棵树上的节点数目都在范围 [0, 100] 内
    -10^4 <= Node.val <= 10^4

'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p is None or q is None:      # 递归终止条件：两个节点有None，如果两个节点都为None则返回True，否则返回False
            return p == q
        if p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)    # 递归条件：两个节点的val值相同，则递归判断他们的左子树、右子树是否相同
        return False    # 两个节点的val值不同，返回False

if __name__ == "__main__":
    p = TreeNode(1)
    p.left = TreeNode(2)
    p.right = TreeNode(3)

    q = TreeNode(1)
    q.left = TreeNode(2)
    q.right = TreeNode(3)

    sol = Solution()
    result = sol.isSameTree(p, q)
    print (result)  