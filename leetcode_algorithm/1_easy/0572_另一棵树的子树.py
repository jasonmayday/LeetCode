"""
https://leetcode-cn.com/problems/subtree-of-another-tree/

给你两棵二叉树 root 和 subRoot 。检验 root 中是否包含和 subRoot 具有相同结构和节点值的子树。如果存在，返回 true ；否则，返回 false 。

二叉树 tree 的一棵子树包括 tree 的某个节点和这个节点的所有后代节点。tree 也可以看做它自身的一棵子树。

示例 1：
    输入：root = [3,4,5,1,2], subRoot = [4,1,2]
    输出：true

示例 2：
    输入：root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
    输出：false

提示：
    root 树上的节点数量范围是 [1, 2000]
    subRoot 树上的节点数量范围是 [1, 1000]
    -10^4 <= root.val <= 10^4
    -10^4 <= subRoot.val <= 10^4

"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.val)   

"""递归构建"""
def list_to_binarytree(nums):
    def level(index):
        if index >= len(nums) or nums[index] is None:
            return None
        root = TreeNode(nums[index])
        root.left = level(2 * index + 1)    # 往左递推  # 从根开始一直到最左，直至为空
        root.right = level(2 * index + 2)   # 往右回溯  # 再返回上一个根，回溯右
        return root     # 再返回根
    return level(0)

class Solution(object):
    def isSubtree(self, s, t):
        if not s and not t:     # 两个 node 都为空为 True
            return True
        if not s or not t:      # 一方空，一方不空，为 False
            return False
        # 判断 t 是否为 s 的子树的三个条件是或的关系，即：
        # 1. 当前两棵树相等；
        # 2. 或者，t 是 s 的左子树；
        # 3. 或者，t 是 s 的右子树。
        return self.isSameTree(s, t) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
        
    def isSameTree(self, s, t):
        if not s and not t:     # 两个 node 都为空为 True
            return True
        if not s or not t:      # 一方空，一方不空，为 False
            return False
        # 判断两个树是否相等的三个条件是与的关系，即：
        # 1. 当前两个树的根节点值相等；
        # 2. 并且，s 的左子树和 t 的左子树相等；
        # 3. 并且，s 的右子树和 t 的右子树相等。
        return s.val == t.val and self.isSameTree(s.left, t.left) and self.isSameTree(s.right, t.right)
    
if __name__ == "__main__":
    s = list_to_binarytree([3,4,5,1,2])
    t = list_to_binarytree([4,1,2])
    sol = Solution()
    result = sol.isSubtree(s,t)
    print(result)