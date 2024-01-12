"""
https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-di-kda-jie-dian-lcof/

给定一棵二叉搜索树，请找出其中第 k 大的节点的值。

示例 1:

    输入: root = [3,1,4,null,2], k = 1
       3
      / \
     1   4
      \
       2
    输出: 4

示例 2:
    输入: root = [5,3,6,2,4,null,null,1], k = 3
           5
          / \
         3   6
        / \
       2   4
      /
     1
    输出: 4
 
限制：
    1 ≤ k ≤ 二叉搜索树元素个数

"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def list_to_binarytree(nums):
    def level(index):
        if index >= len(nums) or nums[index] is None:
            return None
        root = TreeNode(nums[index])
        root.left = level(2 * index + 1)
        root.right = level(2 * index + 2)
        return root
    return level(0)

""" 二叉搜索树的 中序遍历倒序 为 递减序列 。"""
class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        def dfs(root):
            if not root:
                return
            dfs(root.right) # 递归右子树
            if self.k == 0: # 若 k=0 ，代表已找到目标节点，
                return      # 无需继续遍历，因此直接返回；
            self.k -= 1     # 执行 k=k−1 （即从 k 减至 0 ）；
            if self.k == 0: # 若 k=0 ，代表当前节点为第 k 大的节点
                self.res = root.val # 记录结果
            dfs(root.left)  # 递归左子树

        self.k = k
        dfs(root)
        return self.res

if __name__ == "__main__":
    root = list_to_binarytree([[5,3,6,2,4,None,None,1]])
    k = 3
    sol = Solution()
    res = sol.kthLargest(root, k)
    print (res)
    '''
        1
       / \
      2   2
     / \ / \
    3  4 4  3
    '''