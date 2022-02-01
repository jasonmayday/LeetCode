"""
https://leetcode-cn.com/problems/path-sum-ii/

给你二叉树的根节点 root 和一个整数目标和 targetSum ，找出所有 从根节点到叶子节点 路径总和等于给定目标和的路径。

叶子节点 是指没有子节点的节点。

示例 1：
    输入：root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
    输出：[[5,4,11,2],[5,8,4,5]]

示例 2：
    输入：root = [1,2,3], targetSum = 5
    输出：[]

示例 3：
    输入：root = [1,2], targetSum = 0
    输出：[]

提示：
    树中节点总数在范围 [0, 5000] 内
    -1000 <= Node.val <= 1000
    -1000 <= targetSum <= 1000

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
    
from typing import List
from collections import deque

""" 深度优先搜索 DFS """
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        ret = list()
        path = list()
        
        def dfs(root: TreeNode, targetSum: int):
            if not root:
                return
            path.append(root.val)
            targetSum -= root.val
            if not root.left and not root.right and targetSum == 0:
                ret.append(path[:])
            dfs(root.left, targetSum)
            dfs(root.right, targetSum)
            path.pop()
        
        dfs(root, targetSum)
        return ret

""" 广度优先搜索 BFS """
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        res = []
        que = deque()   # 使用队列，同时保存(将要处理的节点，路径，路径和)
        que.append((root, [], 0)) # 将要处理的节点，路径，路径和
        while que:
            node, path, pathSum = que.popleft()
            if not node: # 如果是空节点，不处理
                continue
            if not node.left and not node.right:    # 如果是叶子节点
                if node.val + pathSum == sum:       # 加上叶子节点后，路径和等于sum
                    res.append(path + [node.val])   # 保存路径
            que.append((node.left, path + [node.val], pathSum + node.val))      # 处理左子树
            que.append((node.right, path + [node.val], pathSum + node.val))     # 处理右子树
        return res


if __name__ == "__main__":
    root = list_to_binarytree([5,4,8,11,None,13,4,7,2,None,None,5,1])
    targetSum = 22
    sol = Solution()
    result = sol.pathSum(root, targetSum)
    print (result)