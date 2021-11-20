"""
https://leetcode-cn.com/problems/average-of-levels-in-binary-tree/

给定一个非空二叉树, 返回一个由每层节点平均值组成的数组。

示例 1：
输入：
    3
   / \
  9  20
    /  \
   15   7
输出：[3, 14.5, 11]

解释：
第 0 层的平均值是 3 ,  第1层是 14.5 , 第2层是 11 。因此返回 [3, 14.5, 11] 。

提示：
    节点值的范围在32位有符号整数范围内。

"""
from typing import List

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

"""二叉树层平均值迭代解法：层序遍历的时候把一层求个总和在取一个均值"""
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        if not root:
            return []

        res = []
        queue = [root]
        
        while queue:
            cur = []    # 保存当前层的遍历值，因为queue保存的是TreeNode类型
            next = []   # 保存下一层的节点
            for node in queue:
                cur.append(node.val)
                if node.left:
                    next.append(node.left)
                if node.right:
                    next.append(node.right)
 
            '''记录平均值'''
            res.append(sum(cur)/len(cur))  
            queue = next  # 每次更新queue
        
        return res


if __name__ == "__main__":
    root = list_to_binarytree([3,9,20,None,None,15,7])
    sol = Solution()
    result = sol.averageOfLevels(root)
    print (result)
    

