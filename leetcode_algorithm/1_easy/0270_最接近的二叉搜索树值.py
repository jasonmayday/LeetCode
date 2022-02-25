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
        def inorder(r: TreeNode):
            return inorder(r.left) + [r.val] + inorder(r.right) if r else []
        return min(inorder(root), key = lambda x: abs(target - x))


"""方法二：迭代"""
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        stack, pred = [], float('-inf')
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            
            if pred <= target and target < root.val:
                return min(pred, root.val, key = lambda x: abs(target - x))

            pred = root.val
            root = root.right

        return pred

if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    sol = Solution()
    result = sol.minDepth(root)
    print (result)  
    '''
        3
       / \
      9   20
         / \
        15  7
    ''' 