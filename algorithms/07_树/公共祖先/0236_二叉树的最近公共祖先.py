"""
https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree/

给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。

百度百科中最近公共祖先的定义为：“对于有根树 T 的两个节点 p、q，最近公共祖先表示为一个节点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”

示例 1：
    输入：root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
    输出：3
    解释：节点 5 和节点 1 的最近公共祖先是节点 3 。

示例 2：
    输入：root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
    输出：5
    解释：节点 5 和节点 4 的最近公共祖先是节点 5 。因为根据定义最近公共祖先节点可以为节点本身。

示例 3：
    输入：root = [1,2], p = 1, q = 2
    输出：1

提示：
    树中节点数目在范围 [2, 10^5] 内。
    -10^9 <= Node.val <= 10^9
    所有 Node.val 互不相同 。
    p != q
    p 和 q 均存在于给定的二叉树中。
    
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    
    def __str__(self):
        #测试基本功能，输出字符串
        return str(self.val)

def list_to_binarytree(nums):
    def level(index):
        if index >= len(nums) or nums[index] is None:
            return None
        root = TreeNode(nums[index])
        root.left = level(2 * index + 1)    # 往左递推  # 从根开始一直到最左，直至为空
        root.right = level(2 * index + 2)   # 往右回溯  # 再返回上一个根，回溯右
        return root     # 再返回根
    return level(0)


""" 递归 + DFS """
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root or root == p or root == q:  # 终止条件：找到了节点p或者q，或者遇到空节点：
            return root                         # 如果找不到p或q就返回null, 如果找的到就返回该点
        left = self.lowestCommonAncestor(root.left, p, q)       # 如果左子树中有p或q,那么就会返回找到的点。或者p和q都有，就返回pq的公共点。或者p或q都没有就返回null。
        right = self.lowestCommonAncestor(root.right, p, q)     # 如果右子树中有p或q,那么就会返回找到的点。或者p和q都有，就返回pq的公共点。或者p或q都没有就返回null。
        if not left and not right:  # 当 left 和 right 同时为空（遍历到树底）：
            return                  # 说明 root 的左 / 右子树中都不包含 p,q ，(终止递归，向上返回)
        if not left:                # 当 left 为空 ，right 不为空 ：
            return right            # p,q 都不在 root 的左子树中，直接返回 right
        if not right:               # 当 left 不为空 ，right 为空 ：
            return left             # p,q 都不在 root 的右子树中，直接返回 left
        return root                 # 当 left 和 right 同时不为空 ：说明 p,q 分列在 root 的 异侧 （分别在 左 / 右子树），因此 root 为最近公共祖先，返回 （或者更新）root


if __name__ == "__main__":
    root = list_to_binarytree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
    p = TreeNode(5)
    q = TreeNode(1)
    sol = Solution()
    result = sol.lowestCommonAncestor(root, p, q)
    print(result)