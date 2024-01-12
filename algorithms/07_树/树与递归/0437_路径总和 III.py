"""
https://leetcode-cn.com/problems/path-sum-iii/

给定一个二叉树的根节点 root ，和一个整数 targetSum ，求该二叉树里节点值之和等于 targetSum 的 路径 的数目。

路径 不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。

示例 1：
    输入：root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
    输出：3
    解释：和等于 8 的路径有 3 条，如图所示。

示例 2：
    输入：root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
    输出：3

提示:
    二叉树的节点个数的范围是 [0,1000]
    -10^9 <= Node.val <= 10^9 
    -1000 <= targetSum <= 1000

"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def list_to_binarytree(nums):
    def level(index):
        if index >= len(nums) or nums[index] is None:
            return None
        root = TreeNode(nums[index])
        root.left = level(2 * index + 1)    # 往左递推  # 从根开始一直到最左，直至为空
        root.right = level(2 * index + 2)   # 往右回溯  # 再返回上一个根，回溯右
        return root     # 再返回根
    return level(0)

from collections import defaultdict

""" 方法一：深度优先搜索"""
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        def rootSum(root, targetSum):   # rootSum 函数返回以节点 p 为起点向下且满足路径总和为 val 的路径数目。
            if root is None:
                return 0
            res = 0
            if root.val == targetSum:
                res += 1
            res += rootSum(root.left, targetSum - root.val)     # 对节点 p 的左孩子节点 p1 求出 rootSum(p1, targetSum - val)
            res += rootSum(root.right, targetSum - root.val)    # 对节点 p 的右孩子节点 p1 求出 rootSum(p1, targetSum - val)
            return res
        
        if root is None:
            return 0
        res = rootSum(root, targetSum)  # 递归遍历二叉树的每个节点 p
        res += self.pathSum(root.left, targetSum)   # 然后将每个节点所有求的值进行相加求和返回。
        res += self.pathSum(root.right, targetSum)
        return res

""" 方法二: 前缀和"""
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        prefix = defaultdict(int)
        prefix[0] = 1   # 定义节点的前缀和为：由根结点到当前结点的路径上所有节点的和

        def dfs(root, curr):    # 先序遍历二叉树，记录下根节点 root 到当前节点 p 的路径上除当前节点以外所有节点的前缀和
            if not root:    # 空路径不经过任何节点，
                return 0    # 因此它的前缀和为 0
            res = 0
            curr += root.val
            res += prefix[curr - targetSum]
            prefix[curr] += 1
            res += dfs(root.left, curr)
            res += dfs(root.right, curr)
            prefix[curr] -= 1
            return res

        return dfs(root, 0)

if __name__ == "__main__":
    root = list_to_binarytree([10,5,-3,3,2,None,11,3,-2,None,1])
    targetSum = 8
    sol = Solution()
    result = sol.pathSum(root,targetSum)
    print (result)