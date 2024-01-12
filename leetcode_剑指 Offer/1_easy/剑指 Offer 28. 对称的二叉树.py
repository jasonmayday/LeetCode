"""
https://leetcode-cn.com/problems/dui-cheng-de-er-cha-shu-lcof/

请实现一个函数，用来判断一棵二叉树是不是对称的。如果一棵二叉树和它的镜像一样，那么它是对称的。

例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

    1
   / \
  2   2
 / \ / \
3  4 4  3
但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:

    1
   / \
  2   2
   \   \
   3    3

示例 1：
    输入：root = [1,2,2,3,4,4,3]
    输出：true

示例 2：
    输入：root = [1,2,2,null,3,null,3]
    输出：false

限制：
    0 <= 节点个数 <= 1000

注意：本题与主站 101 题相同：https://leetcode-cn.com/problems/symmetric-tree/

"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

""" 递归实现 """
class Solution(object):
	def isSymmetric(self, root: TreeNode) -> bool:
		if not root:
			return True
		def dfs(left, right):	# 调用递归函数，比较左节点，右节点
			# 递归的终止条件:
			if not (left or right):     # 两个节点有一个为空
				return True
			if not (left and right):    # 两个节点都为空
				return False
			if left.val != right.val:	# 两个节点的值不相等
				return False
			return dfs(left.left, right.right) and dfs(left.right, right.left)	# 如果相当，比较 left 的左节点和 right 的右节点，再比较 left 的右节点和 right 的左节点
		return dfs(root.left, root.right)	# 调用递归函数，从比较根节点的左节点，右节点开始

""" 队列实现 """
class Solution(object):
	def isSymmetric(self, root: TreeNode) -> bool:
		if not root or not (root.left or root.right):
			return True
		# 用队列保存节点
		queue = [root.left,root.right]
		while queue:
			# 从队列中取出两个节点(left 和 right)，再比较这两个节点
			left = queue.pop(0)
			right = queue.pop(0)
			
			if not (left or right):		# 如果两个节点都为空就继续循环
				continue
			if not (left and right):	# 如果两个节点有一个为空就返回false
				return False
			if left.val != right.val:	# 如果左右节点不相等就返回false
				return False
			
			queue.append(left.left)		# 将左节点的左子树放入队列
			queue.append(right.right)	# 将右节点的右子树放入队列
			queue.append(left.right)	# 将左节点的右子树放入队列
			queue.append(right.left)	# 将右节点的左子树放入队列
		return True

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(3)

    sol = Solution()
    result = sol.isSymmetric(root)
    print (result)
    '''
        1
       / \
      2   2
     / \ / \
    3  4 4  3
    '''
    
