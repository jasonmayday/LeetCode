"""
https://leetcode.cn/problems/longest-univalue-path/

给定一个二叉树的 root ，返回 最长的路径的长度 ，这个路径中的 每个节点具有相同值 。 这条路径可以经过也可以不经过根节点。

两个节点之间的路径长度 由它们之间的边数表示。

示例 1:
    输入：root = [5,4,5,1,1,5]
    输出：2

示例 2:
    输入：root = [1,4,5,4,4,5]
    输出：2

提示:
    树的节点数的范围是 [0, 10^4] 
    -1000 <= Node.val <= 1000
    树的深度将不超过 1000
    
"""
class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
        
def list_to_binarytree(nums):
    def level(index):
        if index >= len(nums) or nums[index] is None:
            return None
        root = TreeNode(nums[index])
        root.left = level(2 * index + 1)    # 往左递推  # 从根开始一直到最左，直至为空
        root.right = level(2 * index + 2)   # 往右回溯  # 再返回上一个根，回溯右
        return root     # 再返回根
    return level(0)

"""方法一：深度优先搜索"""
class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        ans = 0
        def dfs(node: TreeNode) -> int:
            if node is None:
                return 0
            left = dfs(node.left)   # 对于当前搜索的结点 root，我们分别获取它左结点的最长同值有向路径长度 left，
            right = dfs(node.right) # 右结点的最长同值有向路径长度 right。
            
            if node.left and node.left.val == node.val: # 如果结点 root 的左结点非空且结点 root 的值与它的左结点的值相等，
                left1 = left + 1    # 那么结点 root 的左最长同值有向路径长度 left1 = left + 1 
            else: left1 = 0         # 否则 left1 = 0

            
            if node.right and node.right.val == node.val:   # 如果结点 root 的右结点非空且结点 root 的值与它的右结点的值相等，
                right1 = right + 1  # 那么结点 root 的右最长同值有向路径长度 right1 = right + 1
            else: right1 = 0        # 否则 right1 = 0
            
            nonlocal ans
            ans = max(ans, left1 + right1)
            return max(left1, right1)
        
        dfs(root)
        return ans

class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        if not root: return 0
        def dfs(node):
            nonlocal ans
            left = (node.val==node.left.val)*dfs(node.left) if node.left else 0 
            # 接收左边节点返回的以左边节点为端点的最长路径，并且只有当存在左节点且左节点和当前节点值一样时才有效 否则为0
            right = (node.val==node.right.val)*dfs(node.right) if node.right else 0
            # 接收右边节点返回的以右边节点为端点的最长路径，与左节点同理
            ans = max(ans,left+right+1)
            # 讨论子-父-子结构的路径长度
            return max(left,right)+1
            # 向父节点返回以当前节点为端点的路径长度
        ans = 0
        dfs(root)
        return ans-1
        # 我们统计的是端点数 题目要求边数故减一

if __name__ == "__main__":
    root = list_to_binarytree([5,4,5,1,1,5])
    sol = Solution()
    result = sol.longestUnivaluePath(root)
    print(result)