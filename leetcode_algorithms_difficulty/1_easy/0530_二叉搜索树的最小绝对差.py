"""
https://leetcode-cn.com/problems/minimum-absolute-difference-in-bst/

给你一个二叉搜索树的根节点 root ，返回 树中任意两不同节点值之间的最小差值 。

差值是一个正数，其数值等于两值之差的绝对值。

示例 1：
    输入：root = [4,2,6,1,3]
    输出：1

示例 2：
    输入：root = [1,0,48,null,null,12,49]
    输出：1

提示：
    树中节点的数目范围是 [2, 10^4]
    0 <= Node.val <= 10^5

"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        #测试基本功能，输出字符串
        return str(self.val)

def list_to_binarytree(nums):
    def level(index):
        if index >= len(nums) or nums[index] is None:
            return None
        root = TreeNode(nums[index])
        root.left = level(2 * index + 1)
        root.right = level(2 * index + 2)
        return root
    return level(0)

# 二叉搜索树采用中序遍历，其实就是一个有序数组。
"""递归"""
class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        res = []   
        r = float("inf")
        def inorder(root):           # 递归进行中序遍历的函数
            if root:
                inorder(root.left)
                res.append(root.val)
                inorder(root.right)
            return res    
        inorder(root)                # 执行函数，将二叉搜索树转化为有序的数组
        
        for i in range(len(res)-1):  # 统计有序数组的最小差值
            r = min(abs(res[i] - res[i+1]), r)
        return r

"""迭代法-中序遍历"""
class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        stack = []
        cur = root
        pre = None
        result = float('inf')
        while cur or stack:
            if cur: # 指针来访问节点，访问到最底层
                stack.append(cur)
                cur = cur.left
            else: # 逐一处理节点
                cur = stack.pop()
                if pre: # 当前节点和前节点的值的差值
                    result = min(result, cur.val - pre.val)
                pre = cur
                cur = cur.right
        return result

if __name__ == "__main__":
    nums = [1,0,48,None,None,12,49]
    root = list_to_binarytree(nums)

    sol = Solution()
    result = sol.getMinimumDifference(root)
    print(result)