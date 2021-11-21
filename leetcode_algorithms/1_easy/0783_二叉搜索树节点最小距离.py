"""
https://leetcode-cn.com/problems/minimum-distance-between-bst-nodes/

给你一个二叉搜索树的根节点 root ，返回 树中任意两不同节点值之间的最小差值 。

差值是一个正数，其数值等于两值之差的绝对值。

示例 1：
    输入：root = [4,2,6,1,3]
    输出：1

示例 2：
    输入：root = [1,0,48,null,null,12,49]
    输出：1

提示：
    树中节点的数目范围是 [2, 100]
    0 <= Node.val <= 10^5

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

'''方法一：中序遍历, 递归'''
class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        arr = []   
        res = float("inf")    # 求最小值，所以初始化为正无穷
        def inorder(root):  # 把二叉搜索树转换成有序数组
            if not root: return None
            if root.left: inorder(root.left)    # 左子树
            arr.append(root.val)                # 中子树
            if root.right: inorder(root.right)  # 右子树
            return arr
            
        inorder(root)
        for i in range(len(arr)-1):  # 统计有序数组的最小差值
            res = min(abs(arr[i] - arr[i+1]), res)
        return res


'''方法二：中序遍历, 迭代'''
class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        stack = []
        cur = root
        pre = None
        result = float('inf')   # 求最小值，所以初始化为正无穷
        while cur or stack:
            if cur: # 指针来访问节点，访问到最底层
                stack.append(cur)
                cur = cur.left
            else: # 逐一处理节点
                cur = stack.pop()
                if pre: # 当前节点和前节点的值的差值
                    result = min(result, cur.val - pre.val)

if __name__ == "__main__":
    nums = [1,0,48,None,None,12,49]
    root = list_to_binarytree(nums)

    sol = Solution()
    result = sol.minDiffInBST(root)
    print(result)
    
    
    