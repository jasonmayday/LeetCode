"""
https://leetcode-cn.com/problems/sum-of-root-to-leaf-binary-numbers/

给出一棵二叉树，其上每个结点的值都是 0 或 1 。每一条从根到叶的路径都代表一个从最高有效位开始的二进制数。例如，如果路径为 0 -> 1 -> 1 -> 0 -> 1，那么它表示二进制数 01101，也就是 13 。

对树上的每一片叶子，我们都要找出从根到该叶子的路径所表示的数字。

返回这些数字之和。题目数据保证答案是一个 32 位 整数。

示例 1：
    输入：root = [1,0,1,0,1,0,1]
    输出：22
    解释：(100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22

示例 2：
    输入：root = [0]
    输出：0

示例 3：
    输入：root = [1]
    输出：1

示例 4：
    输入：root = [1,1]
    输出：3

提示：
    树中的结点数介于 1 和 1000 之间。
    Node.val 为 0 或 1 。

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

""" DFS + 前序遍历 """
class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        def pre_order(node, parent_sum):
            sum = 0             # 初始化 sum 值
            if node == None:    # 节点为空，直接返回 sum
                return sum
            cur = (parent_sum << 1) | node.val
            if node.left == None and node.right == None:    
                sum += cur      # leaf 节点，将 cur 添加到 sum
                return sum      # 直接返回，不需要后续操作
            sum += pre_order(node.left, cur)    # 返回 left, right
            sum += pre_order(node.right, cur)
            return sum          # 返回结果
        return pre_order(root, 0)

class Solution(object):
    def sumRootToLeaf(self, root):
        return self.helper(root, 0)
    
    def helper(self, root, base):
        if root == None:
            return 0
        if root.left == None and root.right == None:
            return 2 * base + root.val
        base = 2 * base + root.val
        return self.helper(root.left, base) + self.helper(root.right, base)


if __name__ == "__main__":      
    root = list_to_binarytree([1,0,1,0,1,0,1])
    sol = Solution()
    result = sol.sumRootToLeaf(root)
    print(result)