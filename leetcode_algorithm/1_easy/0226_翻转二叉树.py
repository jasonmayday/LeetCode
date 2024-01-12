"""
https://leetcode-cn.com/problems/invert-binary-tree/

给你一棵二叉树的根节点 root ，翻转这棵二叉树，并返回其根节点。

示例 1：

    输入：root = [4,2,7,1,3,6,9]
    输出：[4,7,2,9,6,3,1]

         4
       /   \
      2     7
     / \   / \
    1   3 6   9

    输出：

         4
       /   \
      7     2
     / \   / \
    9   6 3   1
    
示例 2：
    输入：root = [2,1,3]
    输出：[2,3,1]

示例 3：
    输入：root = []
    输出：[]

提示：
    树中节点数目范围在 [0, 100] 内
    -100 <= Node.val <= 100

"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    
    def __str__(self):
        # 测试基本功能，输出字符串
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

""" 方法一：递归，深度优先遍历，从叶子节点先开始翻转。"""
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:        # 递归函数的终止条件，节点为空时返回
            return None
        root.left, root.right = right, left # 将当前节点的左右子树交换
        left = self.invertTree(root.left)   # 递归交换当前节点的 左子树
        right = self.invertTree(root.right) # 递归交换当前节点的 右子树
        return root

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:        # 递归函数的终止条件，节点为空时返回
            return None
        root.left, root.right = root.right, root.left   # 将当前节点的左右子树交换
        self.invertTree(root.left)                      # 递归交换当前节点的 左子树
        self.invertTree(root.right)                     # 递归交换当前节点的 右子树
        return root

""" 迭代 """
class Solution(object):
	def invertTree(self, root):
		if not root:
			return None
		queue = [root]  # 先将根节点放入到队列中，然后将二叉树中的节点逐层放入队列中，再迭代处理队列中的元素
		while queue:
			tmp = queue.pop(0)
			tmp.left,tmp.right = tmp.right,tmp.left     # 每次都从队列中拿一个节点，并交换这个节点的左右子树
			if tmp.left:
				queue.append(tmp.left)      # 如果当前节点的左子树不为空，则放入队列等待后续处理
			if tmp.right:
				queue.append(tmp.right)     # 如果当前节点的右子树不为空，则放入队列等待后续处理
		return root     # 返回处理完的根节点


if __name__ == "__main__":
    nums = [4,2,7,1,3,6,9]
    root = list_to_binarytree(nums)
    print (printBFS(root))
    
    sol = Solution()
    newTree = sol.invertTree(root)
    print(printBFS(newTree))
    