"""
https://leetcode-cn.com/problems/all-elements-in-two-binary-search-trees/

给你 root1 和 root2 这两棵二叉搜索树。请你返回一个列表，其中包含 两棵树 中的所有整数并按 升序 排序。.

示例 1：
    输入：root1 = [2,1,4], root2 = [1,0,3]
    输出：[0,1,1,2,3,4]

示例 2：
    输入：root1 = [1,null,8], root2 = [8,1]
    输出：[1,1,8,8]

提示：
    每棵树的节点数在 [0, 5000] 范围内
    -105 <= Node.val <= 105

"""
from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    
    def __str__(self):
        # 测试基本功能，输出字符串
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

""" 方法一：中序遍历 + 归并 """
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def inorder(node: TreeNode, res: List[int]):
            if node:
                inorder(node.left, res)
                res.append(node.val)
                inorder(node.right, res)

        nums1, nums2 = [], []
        inorder(root1, nums1)
        inorder(root2, nums2)

        merged = []
        p1, n1 = 0, len(nums1)
        p2, n2 = 0, len(nums2)
        while True:
            if p1 == n1:
                merged.extend(nums2[p2:])
                break
            if p2 == n2:
                merged.extend(nums1[p1:])
                break
            if nums1[p1] < nums2[p2]:
                merged.append(nums1[p1])
                p1 += 1
            else:
                merged.append(nums2[p2])
                p2 += 1
        return merged

if __name__ == "__main__":
    root1 = list_to_binarytree([2,1,4])
    root2 = list_to_binarytree([1,0,3])
    sol = Solution()
    result = sol.getAllElements(root1, root2)
    print (result)