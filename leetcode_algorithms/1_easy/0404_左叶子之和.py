"""
https://leetcode-cn.com/problems/sum-of-left-leaves

计算给定二叉树的所有左叶子之和。

示例：

    3
   / \
  9  20
    /  \
   15   7

在这个二叉树中，有两个左叶子，分别是 9 和 15，所以返回 24

"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        #测试基本功能，输出字符串
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

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        self.res = 0
        def dfs(node):
            if not node:
                return None
            if node.left and not node.left.left and not node.left.right: # 判断是否为左子节点，是否同时又是叶子节点
                self.res += node.left.val # 统计结果
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return self.res

'''递归, 后序遍历（左右中）'''
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:    # 确定终止条件
            return 0
        
        left_left_leaves_sum = self.sumOfLeftLeaves(root.left)  # 左
        right_left_leaves_sum = self.sumOfLeftLeaves(root.right) # 右
        
        cur_left_leaf_val = 0
        if root.left and not root.left.left and not root.left.right: 
            cur_left_leaf_val = root.left.val  # 中
            
        return cur_left_leaf_val + left_left_leaves_sum + right_left_leaves_sum

'''迭代'''
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        stack = []
        if root: 
            stack.append(root)
        res = 0
        while stack: 
            cur_node = stack.pop()
            if cur_node.left and not cur_node.left.left and not cur_node.left.right: 
                res += cur_node.left.val    # # 每次都把当前节点的左节点加进去. 
                
            if cur_node.left: 
                stack.append(cur_node.left)
            if cur_node.right: 
                stack.append(cur_node.right)
        return res

if __name__ == "__main__":
    nums = [3,9,20,None,None,15,7]
    root = list_to_binarytree(nums)

    sol = Solution()
    result = sol.sumOfLeftLeaves(root)
    print(result)