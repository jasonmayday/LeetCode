"""
https://leetcode-cn.com/problems/two-sum-iv-input-is-a-bst/

给定一个二叉搜索树 root 和一个目标结果 k，如果 BST 中存在两个元素且它们的和等于给定的目标结果，则返回 true。

示例 1：
	    5
	   / \
	  3   6
	 / \   \ 
	2   4   7
    输入: root = [5,3,6,2,4,null,7], k = 9
    输出: true

示例 2：
	    5
	   / \
	  3   6
	 / \   \ 
	2   4   7
    输入: root = [5,3,6,2,4,null,7], k = 28
    输出: false

示例 3：
    输入: root = [2,1,3], k = 4
    输出: true

示例 4：
    输入: root = [2,1,3], k = 1
    输出: false

示例 5：
    输入: root = [2,1,3], k = 3
    输出: true
 
提示:
    二叉树的节点个数的范围是  [1, 10^4].
    -10^4 <= Node.val <= 10^4
    root 为二叉搜索树
    -10^5 <= k <= 10^5

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

"""二叉搜索树中旬遍历得到有序数组 双指针查找"""
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        nums = []
        '''中序遍历 (In-Order Traversal) ：左子树 ---> 根结点 ---> 右子树'''
        '''二叉搜索树采用中序遍历，就是一个有序数组'''
        def mid_order(root):
            if root:
                mid_order(root.left)
                nums.append(root.val)
                mid_order(root.right)
        mid_order(root)
        l, r = 0, len(nums) - 1
        while l < r:
            if nums[l] + nums[r] == k:
                return True
            elif nums[l] + nums[r] > k:
                r -= 1
            else:
                l += 1
        return False

if __name__ == "__main__":
    root = list_to_binarytree([5,3,6,2,4,None,7])
    k = 9
    sol = Solution()
    result = sol.findTarget(root, k)
    print (result)


