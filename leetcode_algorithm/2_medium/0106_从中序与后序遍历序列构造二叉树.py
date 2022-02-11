"""
https://leetcode-cn.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/

给定两个整数数组 inorder 和 postorder ，其中 inorder 是二叉树的中序遍历， postorder 是同一棵树的后序遍历，请你构造并返回这颗 二叉树 。

示例 1:
    输入：inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
    输出：[3,9,20,null,null,15,7]

示例 2:
    输入：inorder = [-1], postorder = [-1]
    输出：[-1]

提示:
    1 <= inorder.length <= 3000
    postorder.length == inorder.length
    -3000 <= inorder[i], postorder[i] <= 3000
    inorder 和 postorder 都由 不同 的值组成
    postorder 中每一个值都在 inorder 中
    inorder 保证是树的中序遍历
    postorder 保证是树的后序遍历

"""
from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.val)  

def printBFS(root):
    res = []         
    if root is None:
        return
    else:
        queue = [root] # 每次输出一行，所用数据结构为队列
        while queue:
            currentNode = queue.pop(0)   # 弹出元素
            res.append(currentNode.val)  # 打印元素值
            if currentNode.left:
                queue.append(currentNode.left)
            if currentNode.right:
                queue.append(currentNode.right)
    return res

''' 中序遍历 (In - Order Traversal)：左子树 ---> 根结点 ---> 右子树
    后序遍历 (Post-Order Traversal)：左子树 ---> 右子树 ---> 根结点
    《后序遍历的最后一个元素一定是根结点》
'''

""" 方法一：递归 """
class Solution(object):
    def buildTree(self, inorder, postorder):
        if not (inorder and postorder):
            return None
        
        def helper(inor,post):
            if not post:
                return None
            root = TreeNode(post[-1])   # 根据后序数组的最后一个元素，创建根节点
            idx = inor.index(post[-1])  # 在中序数组中查找值等于【后序数组最后一个元素】的下标
            
            # 确定这个下标i后，将中序数组分成两部分，后序数组分成两部
            root.left = helper(inor[:idx],post[:idx])       # 递归处理中序数组左边，后序数组左边
            root.right = helper(inor[idx+1:],post[idx:-1])  # 递归处理中序数组右边，后序数组右边
            return root
        
        return helper(inorder, postorder)


if __name__ == "__main__":
    inorder = [9,3,15,20,7]
    postorder = [9,15,7,20,3]
    sol = Solution()
    result = sol.buildTree(inorder, postorder)
    print (printBFS(result))    # [3,9,20,15,7]