"""
https://leetcode-cn.com/problems/construct-string-from-binary-tree/

你需要采用前序遍历的方式，将一个二叉树转换成一个由括号和整数组成的字符串。

空节点则用一对空括号 "()" 表示。而且你需要省略所有不影响字符串与原始二叉树之间的一对一映射关系的空括号对。

示例 1:
    输入: 二叉树: [1,2,3,4]
          1
         / \
        2   3
       /    
      4     
    输出: "1(2(4))(3)"

    解释: 原本将是“1(2(4)())(3())”，
    在你省略所有不必要的空括号对之后，
    它将是“1(2(4))(3)”。

示例 2:
    输入: 二叉树: [1,2,3,null,4]
          1
         / \
        2   3
         \  
          4 

    输出: "1(2()(4))(3)"
    
    解释: 和第一个示例相似，
    除了我们不能省略第一个对括号来中断输入和输出之间的一对一映射关系。


"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

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

'''解法1'''
class Solution:
    def tree2str(self, t: TreeNode) -> str:
        def preorder(root):
            if not root:
                return ''
            if not root.left and root.right:        # 左边为空，右边不为空时，需要加一个空括号保证映射关系
                return str(root.val)+'()'+'('+preorder(root.right)+')'
            if root.left and not root.right:        # 左边不为空，右边为空时，需要加一个空括号保证映射关系
                return str(root.val)+'('+preorder(root.left)+')'
            if not root.left and not root.right:    # 左右都为空时
                return str(root.val)
            return str(root.val) + '('+preorder(root.left)+')'+'('+preorder(root.right)+')'
        return preorder(t)

'''解法2'''
class Solution:
    def tree2str(self, t: TreeNode) -> str:
        if not t:
            return ''
        left = '('+self.tree2str(t.left)+')' if (t.left or t.right) else ''
        right = '('+self.tree2str(t.right)+')' if t.right else ''
        return str(t.val) +left + right

if __name__ == "__main__":
    root = list_to_binarytree([1,2,3,None,None,12,49])
    sol = Solution()
    result = sol.tree2str(root)
    print(result)