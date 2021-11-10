'''
已知列表nums，将其转化为二叉树。举例：

nums = [3,9,20,None,None,15,7]，转化为二叉树后:

节点3的左子节点9，右子节点20，9的左右子节点都为None，20的左子节点15，右子节点7，参考下面：

        3
       / \
      9   20
         / \
        15  7

'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
class Tree:    
    def list_to_binarytree(nums):
        def level(index):
            if index >= len(nums) or nums[index] is None:
                return None

            root = TreeNode(nums[index])
            root.left = level(2 * index + 1)
            root.right = level(2 * index + 2)
            return root

        return level(0)

if __name__ == "__main__":
    nums = [5,4,8,11,None,13,4,7,2,None,None,None,1]
    tree = Tree()
    root = tree.list_to_binarytree(nums)
    