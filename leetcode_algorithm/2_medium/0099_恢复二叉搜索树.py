"""
https://leetcode-cn.com/problems/recover-binary-search-tree/

给你二叉搜索树的根节点 root ，该树中的 恰好 两个节点的值被错误地交换。请在不改变其结构的情况下，恢复这棵树 。

示例 1：
    输入：root = [1,3,null,null,2]
    输出：[3,1,null,null,2]
    解释：3 不能是 1 的左孩子，因为 3 > 1 。交换 1 和 3 使二叉搜索树有效。

示例 2：
    输入：root = [3,1,4,null,null,2]
    输出：[2,1,4,null,null,3]
    解释：2 不能在 3 的右子树中，因为 2 < 3 。交换 2 和 3 使二叉搜索树有效。
 
提示：
    树上节点的数目在范围 [2, 1000] 内
    -2^31 <= Node.val <= 2^31 - 1

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
        root.left = level(2 * index + 1)    # 往左递推  # 从根开始一直到最左，直至为空
        root.right = level(2 * index + 2)   # 往右回溯  # 再返回上一个根，回溯右
        return root     # 再返回根
    return level(0)

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

""" 解法1：二叉树搜索树的中序遍历
    中序遍历 (In-Order Traversal) ：左子树 ---> 根结点 ---> 右子树
    二叉搜索树采用中序遍历，就是一个有序数组"""
class Solution(object):
    def recoverTree(self, root):
        nodes = []
        # 中序遍历二叉树，并将遍历的结果保存到list中        
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            nodes.append(root)
            dfs(root.right)
        
        dfs(root)
        x = None        # x为前节点
        y = None        # y为后节点 （需要找到中序遍历后 前节点 > 后节点 的情况）
        pre = nodes[0]
        
        for i in range(1, len(nodes)):  # 扫面遍历的结果，找出可能存在错误交换的节点x和y
            if pre.val > nodes[i].val:
                y = nodes[i]
                if not x:
                    x = pre
            pre = nodes[i]
        if x and y:     # 如果x和y不为空，
            x.val,y.val = y.val,x.val   # 则交换这两个节点值，恢复二叉搜索树 

        
if __name__ == "__main__":
    nums = root = [1,3,None,None,2]
    root = list_to_binarytree(nums)
    print (printBFS(root))
    
    sol = Solution()
    newTree = sol.recoverTree(root)
    print(printBFS(newTree))
