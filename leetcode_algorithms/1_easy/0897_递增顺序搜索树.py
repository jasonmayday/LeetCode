'''
https://leetcode-cn.com/problems/increasing-order-search-tree/

给你一棵二叉搜索树，请你 按中序遍历 将其重新排列为一棵递增顺序搜索树，使树中最左边的节点成为树的根节点，并且每个节点没有左子节点，只有一个右子节点。

示例 1：
https://assets.leetcode.com/uploads/2020/11/17/ex1.jpg
输入：root = [5,3,6,2,4,null,8,1,null,null,null,7,9]
输出：[1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]

示例 2：
https://assets.leetcode.com/uploads/2020/11/17/ex2.jpg
输入：root = [5,1,7]
输出：[1,null,5,null,7]

提示：
树中节点数的取值范围是 [1, 100]
0 <= Node.val <= 1000

'''

#  中序遍历：左子树 ---> 根结点 ---> 右子树

#  先中序遍历，把结果放在数组中；
#  然后修改数组中每个节点的左右指针：把节点的左指针设置为 null，把节点的右指针设置为数组的下一个节点。

#  下面的代码中，使用了 dummy （哑节点），它一般在链表题中出现。
#  在链表题目中，我们为了防止链表的头结点发生变化之后，不好维护头结点，我们设置 dummy 从而保证头结点不变。
#  这个题目中设置了 dummy ，从而保证了在新的树中，dummy 是根节点，最终返回的时候，要返回的是 dummy.right。



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(6)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right.right = TreeNode(8)
root.left.left.left = TreeNode(1)
root.right.right.left = TreeNode(7)
root.right.right.right = TreeNode(9)

class Solution(object):
    def increasingBST(self, root: TreeNode) -> TreeNode:
        self.res = []
        self.inOrder(root)
        if not self.res:
            return 
        dummy = TreeNode(-1)
        cur = dummy
        for node in self.res:
            node.left = node.right = None
            cur.right = node
            cur = cur.right
        return dummy.right
    
    def inOrder(self, root):
        if not root:
            return
        self.inOrder(root.left)
        self.res.append(root)
        self.inOrder(root.right)

if __name__ == "__main__":
    sol = Solution()
    result = sol.increasingBST(root)
    print (result)  