"""
给定一个二叉搜索树, 找到该树中两个指定节点的最近公共祖先。

百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”

例如，给定如下二叉搜索树:  root = [6,2,8,0,4,7,9,null,null,3,5]

示例 1:
    输入: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
    输出: 6 
    解释: 节点 2 和节点 8 的最近公共祖先是 6。

示例 2:
    输入: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
    输出: 2
    解释: 节点 2 和节点 4 的最近公共祖先是 2, 因为根据定义最近公共祖先节点可以为节点本身。

说明:
    所有节点的值都是唯一的。
    p、q 为不同节点且均存在于给定的二叉搜索树中。
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
        root.left = level(2 * index + 1)
        root.right = level(2 * index + 2)
        return root
    return level(0)

""" 解法：递归
    树为二叉搜索树，左树比当前节点小，右树比当前节点大。可以想到，我们可以容易的判断p,q在当前节点的哪一侧。"""
class Solution:    
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':   # 从root开始遍历
        if p.val < root.val and q.val < root.val:               # 如果p、q都比当前节点值小（都在当前节点的左侧）
            return self.lowestCommonAncestor(root.left, p ,q)   # 再从root.left往下层递归
        elif p.val > root.val and q.val > root.val:             # 如果p、q都比当前节点值大（都在当前节点的右侧）
            return self.lowestCommonAncestor(root.right, p ,q)  # 再从root.right往下层递归
        else:                                                   # 如在两侧，则返回当前节点
            return root


if __name__ == "__main__":
    nums = [6,2,8,0,4,7,9,None,None,3,5]
    root = list_to_binarytree(nums)

    p = TreeNode(2)
    q = TreeNode(8)

    sol = Solution()
    result = sol.lowestCommonAncestor(root, p, q)
    print(result)