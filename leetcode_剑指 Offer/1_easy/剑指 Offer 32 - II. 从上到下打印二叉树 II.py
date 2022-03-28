"""
https://leetcode-cn.com/problems/cong-shang-dao-xia-da-yin-er-cha-shu-ii-lcof/

从上到下按层打印二叉树，同一层的节点按从左到右的顺序打印，每一层打印到一行。

例如:
给定二叉树: [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其层次遍历结果：

[
  [3],
  [9,20],
  [15,7]
]

提示：
    节点总数 <= 1000
    注意：本题与主站 102 题相同：https://leetcode-cn.com/problems/binary-tree-level-order-traversal/

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

from collections import deque
from typing import List

""" 解法1：迭代实现 BFS
    广度优先需要用队列作为辅助结构"""
class Solution(object):
	def levelOrder(self, root: TreeNode) -> List[List[int]]:
		if not root:
			return []
		res = []
		queue = [root]      # 首先拿出根节点，如果左子树/右子树不为空，就将他们放入队列中。
		while queue:
			size = len(queue)   # 获取当前队列的长度，这个长度相当于 当前这一层的节点个数
			tmp = []
			for _ in range(size):
				r = queue.pop(0)    # 将队列中的元素都拿出来(也就是获取这一层的节点)
				tmp.append(r.val)   # 放到临时 list 中
				if r.left:                  # 如果节点的左/右子树不为空
					queue.append(r.left)    # 也放入队列中
				if r.right:
					queue.append(r.right)
			res.append(tmp)     # 把每层遍历到的节点都放入到一个结果集中
		return res

""" 解法2：递归实现 DFS (深度优先搜索) """
class Solution(object):
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res = []

        def dfs(root, index):   # index 为层数
            if not root:        # 遍历的终止条件
                return
            if len(res) < index:      # 没有对应的第 index 层数组时：创建第 index 层数组
                res.append(deque())   # 假设res是[ [1],[2,3] ]， index是3，就再插入一个空list放到res中
            res[index - 1].append(root.val) # 答案中第 index 层加入答案
            dfs(root.left, index + 1)   # 递归左子树，同时将层数index+1
            dfs(root.right, index + 1)  # 递归右子树，同时将层数index+1
            
        dfs(root, 1)
        return [list(q) for q in res]

class Solution(object):
	def levelOrder(self, root: TreeNode) -> List[List[int]]:
		if not root:
			return []
		res = []
		def dfs(index,r):
			if len(res)<index:  # 没有对应的第 index 层数组时：创建第 index 层数组
				res.append([])  # 假设res是[ [1],[2,3] ]， index是3，就再插入一个空list放到res中
			# 将当前节点的值加入到res中，index代表当前层，假设index是3，节点值是99
			# res是[ [1],[2,3] [4] ]，加入后res就变为 [ [1],[2,3] [4,99] ]
			res[index-1].append(r.val)  # 答案中第 index 层加入答案
			if r.left:
				dfs(index+1,r.left)     # 递归左子树，同时将层数index+1
			if r.right:
				dfs(index+1,r.right)    # 递归右子树，同时将层数index+1
		dfs(1,root)
		return res

if __name__ == "__main__":
    root = list_to_binarytree([3,9,20,None,None,15,7])
    '''
           3
         ↙   ↘
       9       20
              ↙  ↘
             15    7
    '''
    sol = Solution()
    result = sol.levelOrder(root)
    print(result)

