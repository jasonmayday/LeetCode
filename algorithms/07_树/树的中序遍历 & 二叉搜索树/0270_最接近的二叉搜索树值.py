"""
https://leetcode-cn.com/problems/closest-binary-search-tree-value/

给定一个不为空的二叉搜索树和一个目标值 target，请在该二叉搜索树中找到最接近目标值 target 的数值。

注意：
    给定的目标值 target 是一个浮点数
    题目保证在该二叉搜索树中只会存在一个最接近目标值的数

示例：

    输入: root = [4,2,5,1,3]，目标值 target = 3.714286

        4
       / \
      2   5
     / \
    1   3

    输出: 4

"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


""" 方法一：递归 + 线性搜索"""
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        def inorder(root: TreeNode):
            if root:
                return inorder(root.left) + [root.val] + inorder(root.right)
            else: return []
        return min(inorder(root), key = lambda x: abs(target - x))


""" 方法二：迭代"""
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        stack = []
        pred = float('-inf')    # 初始化一个空栈和设 pred 为一个很小的数字。
        while stack or root:
            while root:
                stack.append(root)
                root = root.left    # 为了要迭代构建一个中序序列，我们要尽可能的左移并将节点添加到栈中。
            root = stack.pop()      # 弹出栈顶元素

            if pred <= target and target < root.val:    # 若目标值在 pred 和 root.val 之间，
                return min(pred, root.val, key = lambda x: abs(target - x))     # 则最接近的元素在这两个元素之间。

            pred = root.val     # 设置 pred = root.val，
            root = root.right   # 且向右走一步 root = root.right。

        return pred

""" 方法三：二分搜索"""
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        closest = root.val
        while root:
            closest = min(root.val, closest, key = lambda x: abs(target - x))
            if target < root.val:
                root = root.left
            else:
                root = root.right
        return closest


if __name__ == "__main__":
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(5)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)

    target = 3.714286
    sol = Solution()
    result = sol.closestValue(root, target)
    print (result)
