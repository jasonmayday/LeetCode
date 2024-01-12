"""
https://leetcode-cn.com/problems/unique-binary-search-trees-ii/

给你一个整数 n ，请你生成并返回所有由 n 个节点组成且节点值从 1 到 n 互不相同的不同 二叉搜索树 。可以按 任意顺序 返回答案。

示例 1：
    输入：n = 3
    输出：[[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]

示例 2：
    输入：n = 1
    输出：[[1]]

提示：
    1 <= n <= 8

"""
import functools
from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
    
    def __str__(self):
        return str(self.val)   

""" 递归 """
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n == 0:
            return []   # 空的时候，返回 [None]  而不是None  
        
        @functools.lru_cache(None)
        
        def helper(start, end):
            res = []
            if start > end:
                res.append(None)
            for val in range(start, end + 1):           # 枚举可行根节点，取遍 [start, end] 中的节点
                for left in helper(start, val - 1):     # 寻找左子树, 返回 根节点 val 左半部分[start, val-1] 所能构成的所有左子树 
                    for right in helper(val + 1, end):  # 寻找右子树, 返回 根节点 val 右半部分[val + 1, end] 所能构成的所有右子树 
                        root = TreeNode(val)
                        root.left = left
                        root.right = right
                        res.append(root)        # 保存 一种 { 左子树 | 根节点 | 右子树} 组合
            return res
        
        return helper(1, n)

"""解法2：回溯"""
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        def generateTrees(start, end):
            if start > end:
                return [None,]
            
            res = []
            for i in range(start, end + 1):  # 枚举可行根节点（注意：使用同一个根节点可能生成多种二叉搜索树）
                leftTrees = generateTrees(start, i - 1) # 获得所有可行的左子树集合
                rightTrees = generateTrees(i + 1, end)  # 获得所有可行的右子树集合
                
                for l in leftTrees:             # 从左子树集合中选出一棵左子树
                    for r in rightTrees:        # 从右子树集合中选出一棵右子树
                        currTree = TreeNode(i)  # 拼接到根节点上
                        currTree.left = l
                        currTree.right = r
                        res.append(currTree)
            return res
        
        return generateTrees(1, n) if n else []

if __name__ == "__main__":
    n = 4
    sol = Solution()
    result = sol.generateTrees(n)
    print (result)
    