"""
https://leetcode-cn.com/problems/leaf-similar-trees/

请考虑一棵二叉树上所有的叶子，这些叶子的值按从左到右的顺序排列形成一个 叶值序列 。

举个例子，如上图所示，给定一棵叶值序列为 (6, 7, 4, 9, 8) 的树。

如果有两棵二叉树的叶值序列是相同，那么我们就认为它们是 叶相似 的。

如果给定的两个根结点分别为 root1 和 root2 的树是叶相似的，则返回 true；否则返回 false 。

示例 1：
    输入：root1 = [3,5,1,6,2,9,8,null,null,7,4], root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
    输出：true

示例 2：
    输入：root1 = [1], root2 = [1]
    输出：true

示例 3：
    输入：root1 = [1], root2 = [2]
    输出：false

示例 4：
    输入：root1 = [1,2], root2 = [2,2]
    输出：true

示例 5：
    输入：root1 = [1,2,3], root2 = [1,3,2]
    输出：false

提示：
    给定的两棵树可能会有 1 到 200 个结点。
    给定的两棵树上的值介于 0 到 200 之间。

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

""" 深度优先搜索，前序、后序均可。
    在深度优先搜索的过程中，我们总是先搜索当前节点的左子节点，再搜索当前节点的右子节点。
    如果我们搜索到一个叶节点，就将它的值放入序列中。
"""
    
""" 方法1：递归法"""
class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        nums1 = []
        nums2 = []
        def dfs(root,nums):
            if root and not root.left and not root.right:   # 当遍历到根节点时：
                nums.append(root.val)                       # 把数字加入到对应的数组中
            if root.left:                                   # 如果左
                dfs(root.left,nums)
            if root.right:
                dfs(root.right,nums)
            return nums
        return dfs(root1,nums1) == dfs(root2,nums2)
        
        
""" 方法2：迭代法"""
class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        res1 = []
        res2 = []
        self.dfs(root1, res1)
        self.dfs(root2, res2)
        return res1 == res2
        

    def dfs(self, root, result):
        stack = []
        current = root
        while current is not None or len(stack) > 0:
            # 相当于递归法中的 dfs(root.left), 优先把left节点都压入栈            
            while current:
                stack.append(current)
                current = current.left

            # left 节点都已经压完了, 从栈中取最近压入的 TreeNode
            current = stack.pop()

            if current.left is None and current.right is None:
                result.append(current.val)

            # 相当于递归法中的 dfs(root.right) 那一步
            current = current.right
      
if __name__ == "__main__":
    root1 = list_to_binarytree([3,5,1,6,2,9,8,None,None,7,4])
    root2 = list_to_binarytree([3,5,1,6,7,4,2,None,None,None,None,None,None,9,8])

    sol = Solution()
    result = sol.leafSimilar(root1,root2)
    print(result)