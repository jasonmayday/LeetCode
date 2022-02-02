"""
https://leetcode-cn.com/problems/flatten-binary-tree-to-linked-list/

给你二叉树的根结点 root ，请你将它展开为一个单链表：
    展开后的单链表应该同样使用 TreeNode ，其中 right 子指针指向链表中下一个结点，而左子指针始终为 null 。
    展开后的单链表应该与二叉树 先序遍历 顺序相同。

示例 1：
    输入：root = [1,2,5,3,4,null,6]
    输出：[1,null,2,null,3,null,4,null,5,null,6]

示例 2：
    输入：root = []
    输出：[]

示例 3：
    输入：root = [0]
    输出：[0]

提示：
    树中结点数在范围 [0, 2000] 内
    -100 <= Node.val <= 100

进阶：你可以使用原地算法（O(1) 额外空间）展开这棵树吗？

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

'''
           1
         ↙   ↘
       2       5
     ↙   ↘       ↘
    3     4        6
'''

""" 递归 + 前序遍历 """
class Solution:
    def flatten(self, root: TreeNode) -> None:
        preorderList = []   # 初始化先序遍历的列表

        def preorderTraversal(root: TreeNode):  # 先执行前序遍历
            if root:
                preorderList.append(root)
                preorderTraversal(root.left)
                preorderTraversal(root.right)
        
        preorderTraversal(root)
        
        length = len(preorderList)
        for i in range(1, length):
            prev = preorderList[i-1]
            curr = preorderList[i]
            prev.left = None
            prev.right = curr


""" 迭代 + 前序遍历 """
class Solution:
    def flatten(self, root: TreeNode) -> None:
        preorderList = []       # 初始化先序遍历的列表
        stack = []              # 利用栈进行临时存储
        node = root

        while node or stack:    # stack为空且node为null时，说明遍历结束
            while node:         # 可以进入左子树时，先访问，再进入
                preorderList.append(node)   # 首先访问该节点（先序），之后顺序入栈左子树
                stack.append(node)
                node = node.left
            node = stack.pop()
            node = node.right   # 否则进入栈中节点的右子树
        
        length = len(preorderList)
        for i in range(1, length):
            prev = preorderList[i-1]
            curr = preorderList[i]
            prev.left = None
            prev.right = curr


if __name__ == "__main__":
    root = list_to_binarytree([1,2,5,3,4,None,6])
    sol = Solution()
    result = sol.flatten(root)
    print (result)