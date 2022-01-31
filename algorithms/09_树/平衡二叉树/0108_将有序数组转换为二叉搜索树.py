'''
给你一个整数数组 nums ，其中元素已经按 升序 排列，请你将其转换为一棵 高度平衡 二叉搜索树。

高度平衡 二叉树是一棵满足「每个节点的左右两个子树的高度差的绝对值不超过 1 」的二叉树。

示例 1：
    输入：nums = [-10,-3,0,5,9]
    输出：[0,-3,9,-10,null,5]
    解释：[0,-10,5,null,-3,null,9] 也将被视为正确答案：

示例 2：
    输入：nums = [1,3]
    输出：[3,1]
    解释：[1,3] 和 [3,1] 都是高度平衡二叉搜索树。

提示：
    1 <= nums.length <= 10^4
    -10^4 <= nums[i] <= 10^4
    nums 按 严格递增 顺序排列

'''
from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:

        def make_tree(left, right):     # 只和长度有关
            # 首先判定我们的区间是否合理，即left_index要<=right_index
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