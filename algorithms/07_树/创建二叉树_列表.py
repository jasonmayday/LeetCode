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
    
    def __str__(self):
        # 测试基本功能，输出字符串
        return str(self.val)

"""递归构建"""
def list_to_binarytree(nums):
    def level(index):
        if index >= len(nums) or nums[index] is None:
            return None
        root = TreeNode(nums[index])
        root.left = level(2 * index + 1)    # 往左递推  # 从根开始一直到最左，直至为空
        root.right = level(2 * index + 2)   # 往右回溯  # 再返回上一个根，回溯右
        return root     # 再返回根
    return level(0)

"""迭代构建"""
def list_to_binarytree(nums):
    if not nums:
        return
    root=TreeNode(nums[0])
    seq=[root]
    i=1
    while i<len(nums):
        node=seq.pop(0)
        node.left=TreeNode(nums[i])
        if nums[i]:
            seq.append(node.left)
        node.right=TreeNode(nums[i+1])
        i+=1
        if i<len(nums):
            node.right=TreeNode(nums[i])
            if nums[i]:
                seq.append(node.right)
        i+=1
    return root

def printBFS(root):
    res = []
    if root is None:
        return
    else:
        queue = [root] # 每次输出一行，所用数据结构为队列
        while queue:
            currentNode = queue.pop(0)   # 弹出元素
            res.append(currentNode.val)  # 打印元素值
            if currentNode.left:
                queue.append(currentNode.left)
            if currentNode.right:
                queue.append(currentNode.right)
    return res
    
if __name__ == "__main__":
    nums = [5,4,8,11,None,13,4,7,2,None,None,None,1]
    root = list_to_binarytree(nums)
    print (printBFS(root))
    