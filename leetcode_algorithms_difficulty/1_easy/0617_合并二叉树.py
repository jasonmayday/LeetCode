"""
https://leetcode-cn.com/problems/merge-two-binary-trees/

给定两个二叉树，想象当你将它们中的一个覆盖到另一个上时，两个二叉树的一些节点便会重叠。

你需要将他们合并为一个新的二叉树。合并的规则是如果两个节点重叠，那么将他们的值相加作为节点合并后的新值，否则不为 NULL 的节点将直接作为新二叉树的节点。

示例 1:
输入: 
	Tree 1                     Tree 2                  
          1                         2                             
         / \                       / \                            
        3   2                     1   3                        
       /                           \   \                      
      5                             4   7                  
输出: 
合并后的树:
	     3
	    / \
	   4   5
	  / \   \ 
	 5   4   7
注意: 合并必须从两个树的根节点开始。

"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
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

def BFS(root):
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

'''深度优先搜索'''
class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1:
            return t2
        if not t2:
            return t1
        # 从根节点开始同时遍历两个二叉树，并将对应的节点进行合并。
        merged = TreeNode(t1.val + t2.val)                  # 从根节点开始，数字等于原来两个根节点相加
        merged.left = self.mergeTrees(t1.left, t2.left)     # 递归的过程，对左子树进行合并
        merged.right = self.mergeTrees(t1.right, t2.right)  # 递归的过程，对右子树进行合并
        return merged

if __name__ == "__main__":
    t1 = list_to_binarytree([1,3,2,5])
    t2 = list_to_binarytree([2,1,3,None,4,None,7])
    sol = Solution()
    newTree = sol.mergeTrees(t1,t2)
    print (BFS(newTree))

