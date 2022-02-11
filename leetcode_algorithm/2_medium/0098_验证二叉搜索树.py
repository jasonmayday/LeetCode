"""
https://leetcode-cn.com/problems/validate-binary-search-tree/

给你一个二叉树的根节点 root ，判断其是否是一个有效的二叉搜索树。

有效 二叉搜索树定义如下：
    节点的左子树只包含 小于 当前节点的数。
    节点的右子树只包含 大于 当前节点的数。
    所有左子树和右子树自身必须也是二叉搜索树。

示例 1：
    输入：root = [2,1,3]
    输出：true

示例 2：
    输入：root = [5,1,4,null,null,3,6]
    输出：false
    解释：根节点的值是 5 ，但是右子节点的值是 4 。

提示：
    树中节点数目范围在[1, 10^4] 内
    -2^31 <= Node.val <= 2^31 - 1

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
        root.left = level(2 * index + 1)    # 往左递推  # 从根开始一直到最左，直至为空
        root.right = level(2 * index + 2)   # 往右回溯  # 再返回上一个根，回溯右
        return root     # 再返回根
    return level(0)


""" 方法1：因为二叉搜索树中序遍历是递增的, 左子树 ---> 根结点 ---> 右子树
    所以我们可以中序遍历判断前一数是否小于后一个数."""
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        res = []
        
        def inorder(root):
            if not root:
                return 
            inorder(root.left)
            res.append(root.val)
            inorder(root.right)
            
        inorder(root)
        return res == sorted(res) and len(set(res)) == len(res)
    
""" 方法2 """
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        self.pre = None
        
        def isBST(root):
            if not root:
                return True
            if not isBST(root.left):
                return False
            if self.pre and self.pre.val >= root.val:
                return False
            self.pre = root
            # print(root.val)
            return  isBST(root.right)
        
        return isBST(root)

if __name__ == "__main__":
    root = list_to_binarytree([5,1,4,None,None,3,6])
    sol = Solution()
    result = sol.isValidBST(root)
    print(result)