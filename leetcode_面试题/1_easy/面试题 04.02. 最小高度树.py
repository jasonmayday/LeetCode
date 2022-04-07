"""
https://leetcode-cn.com/problems/minimum-height-tree-lcci/

给定一个有序整数数组，元素各不相同且按升序排列，编写一个算法，创建一棵高度最小的二叉搜索树。

示例:
    给定有序数组: [-10,-3,0,5,9],

    一个可能的答案是：[0,-3,9,-10,null,5]，它可以表示下面这个高度平衡二叉搜索树：

          0
         / \
       -3   9
       /   /
     -10  5

本题与主站 108 题相同：：https://leetcode-cn.com/problems/convert-sorted-array-to-binary-search-tree/

"""

from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

""" 递归 """
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return
        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[: mid])
        root.right = self.sortedArrayToBST(nums[mid + 1: ])
        
        return root

""" 递归 """
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:

        def make_tree(left, right):     # 只和长度有关
            # 首先判定我们的区间是否合理，即left_index要 <= right_index
            # 当相等时，只有root会产生，不会产生左右小树
            if left > right:
                return None
            
            mid = (left + right) // 2   # 总是选择中间位置左边的数字作为根节点
            root = TreeNode(nums[mid])  # 做一个小树的 root
            
            root.left = make_tree(left, mid - 1)    # 递归，最中间数字左边的段落再做一棵树
            root.right = make_tree(mid + 1, right)
            return root
        
        return make_tree(0, len(nums)-1)    # 左闭右闭区间
        # 可以看到整个题解只和index有关，和数组里的具体数字无关，
        # 因为题目给出的“有序数列”帮助我们满足了“二叉搜索树”的条件。
    
if __name__ == "__main__":
    nums = [-10,-3,0,5,9]
    sol = Solution()
    result = sol.sortedArrayToBST(nums)
    print (str(result))
