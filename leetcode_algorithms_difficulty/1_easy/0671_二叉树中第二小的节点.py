"""
https://leetcode-cn.com/problems/second-minimum-node-in-a-binary-tree/

给定一个非空特殊的二叉树，每个节点都是正数，并且每个节点的子节点数量只能为 2 或 0。如果一个节点有两个子节点的话，那么该节点的值等于两个子节点中较小的一个。

更正式地说，root.val = min(root.left.val, root.right.val) 总成立。

给出这样的一个二叉树，你需要输出所有节点中的第二小的值。如果第二小的值不存在的话，输出 -1 。

示例 1：
    输入：root = [2,2,5,null,null,5,7]
    输出：5
    解释：最小的值是 2 ，第二小的值是 5 。

示例 2：
    输入：root = [2,2,2]
    输出：-1
    解释：最小的值是 2, 但是不存在第二小的值。
 
提示：
    树中节点数目在范围 [1, 25] 内
    1 <= Node.val <= 231 - 1
    对于树中每个节点 root.val == min(root.left.val, root.right.val)

"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    
    def __str__(self):
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

class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        if not root or not root.left:
            return -1
        # 我们知道root.val是最小值，那么
        # 第二小的值存在于 更小的子节点那一边的子树的第二小的值 或 更大的子节点 之中
        left = root.left.val if root.val != root.left.val else self.findSecondMinimumValue(root.left)
        right = root.right.val if root.val != root.right.val else self.findSecondMinimumValue(root.right)

        return min(left, right) if left != -1 and right != -1 else max(left, right)

if __name__ == "__main__":
    root = list_to_binarytree([2,2,5,None,None,5,7])
    sol = Solution()
    result = sol.findSecondMinimumValue(root)
    print(result)