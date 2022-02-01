"""
https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

给定两个整数数组 preorder 和 inorder ，其中 preorder 是二叉树的先序遍历， inorder 是同一棵树的中序遍历，请构造二叉树并返回其根节点。

示例 1:
    输入: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
    输出: [3,9,20,null,null,15,7]

示例 2:
    输入: preorder = [-1], inorder = [-1]
    输出: [-1]

提示:
    1 <= preorder.length <= 3000
    inorder.length == preorder.length
    -3000 <= preorder[i], inorder[i] <= 3000
    preorder 和 inorder 均 无重复 元素
    inorder 均出现在 preorder
    preorder 保证 为二叉树的前序遍历序列
    inorder 保证 为二叉树的中序遍历序列

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

''' 前序遍历 (Pre-Order Traversal) ：根结点 ---> 左子树 ---> 右子树
    中序遍历 (In -Order Traversal) ：左子树 ---> 根结点 ---> 右子树
    https://pic.leetcode-cn.com/beff309937462b352940c1925de8ff50c22b65bada872cf286b0228a45054ea2-2.jpg
    '''


""" 方法一：递归 """
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        
        def recur_func(inorder):
            x = preorder.pop(0)     # 每次取前序列表最左端的元素
            node = TreeNode(x)      # 用该元素生成一个 node（根节点）
            idx = inorder.index(x)  # 找到该元素在中序列表中的索引
            left_l = inorder[:idx]          # 用该元素分割中序列表（中序遍历的中间元素把树两边分割）
            right_l = inorder[idx+1:]
            node.left = recur_func(left_l) if left_l else None      # 递归的处理前序数组左边和中序数组左边
            node.right = recur_func(right_l) if right_l else None   # 递归的处理前序数组右边和中序数组右边
            # 一直探索到最底层的最左端的叶子，然后从下往上一层层返回
            return node

        if not preorder or not inorder:     # 终止条件:前序和中序数组为空
            return None
        
        return recur_func(inorder)


""" 方法一：递归 """
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        
        def myBuildTree(preorder_left: int, preorder_right: int, inorder_left: int, inorder_right: int):
            if preorder_left > preorder_right:
                return None
            preorder_root = preorder_left   # 前序遍历中的第一个节点就是根节点
            inorder_root = index[preorder[preorder_root]]   # 在中序遍历中定位根节点
            root = TreeNode(preorder[preorder_root])        # 先把根节点建立出来
            size_left_subtree = inorder_root - inorder_left # 得到左子树中的节点数目
            
            # 递归地构造左子树，并连接到根节点
            # 先序遍历中「从 左边界+1 开始的 size_left_subtree」个元素就对应了中序遍历中「从 左边界 开始到 根节点定位-1」的元素
            root.left = myBuildTree(preorder_left + 1, preorder_left + size_left_subtree, inorder_left, inorder_root - 1)
            
            # 递归地构造右子树，并连接到根节点
            # 先序遍历中「从 左边界+1+左子树节点数目 开始到 右边界」的元素就对应了中序遍历中「从 根节点定位+1 到 右边界」的元素
            root.right = myBuildTree(preorder_left + size_left_subtree + 1, preorder_right, inorder_root + 1, inorder_right)
            return root
        
        n = len(preorder)
        index = {element: i for i, element in enumerate(inorder)}   # 构造哈希映射，帮助我们快速定位根节点
        return myBuildTree(0, n - 1, 0, n - 1)

""" 方法二：迭代 """
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return None

        root = TreeNode(preorder[0])    # 前序遍历中的第一个节点就是根节点
        stack = [root]      # 用一个栈 stack 来维护「当前节点的所有还没有考虑过右子树的祖先节点」，栈顶就是当前节点。也就是说，只有在栈中的节点才可能连接一个新的右子树。
        inorderIndex = 0    # 用一个指针 index 指向中序遍历的某个位置，初始值为 0
        for i in range(1, len(preorder)):
            preorderVal = preorder[i]
            node = stack[-1]
            if node.val != inorder[inorderIndex]:
                node.left = TreeNode(preorderVal)
                stack.append(node.left)
            else:
                while stack and stack[-1].val == inorder[inorderIndex]:
                    node = stack.pop()
                    inorderIndex += 1
                node.right = TreeNode(preorderVal)
                stack.append(node.right)

        return root


if __name__ == "__main__":
    preorder = [3,9,20,15,7]
    inorder = [9,3,15,20,7]
    sol = Solution()
    result = sol.buildTree(preorder,inorder)
    print (printBFS(result))