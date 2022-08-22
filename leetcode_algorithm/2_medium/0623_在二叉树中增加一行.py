"""
https://leetcode.cn/problems/add-one-row-to-tree/

给定一个二叉树的根 root 和两个整数 val 和 depth ，在给定的深度 depth 处添加一个值为 val 的节点行。

注意，根节点 root 位于深度 1 。

加法规则如下:
    给定整数 depth，对于深度为 depth - 1 的每个非空树节点 cur ，创建两个值为 val 的树节点作为 cur 的左子树根和右子树根。
    cur 原来的左子树应该是新的左子树根的左子树。
    cur 原来的右子树应该是新的右子树根的右子树。
    如果 depth == 1 意味着 depth - 1 根本没有深度，那么创建一个树节点，值 val 作为整个原始树的新根，而原始树就是新根的左子树。

示例 1:
    输入: root = [4,2,6,3,1,5], val = 1, depth = 2
    输出: [4,1,1,2,null,null,6,3,1,5]

示例 2:
    输入: root = [4,2,null,3,1], val = 1, depth = 3
    输出:  [4,2,null,1,1,3,null,null,1]

提示:
    节点数在 [1, 10^4] 范围内
    树的深度在 [1, 10^4]范围内
    -100 <= Node.val <= 100
    -10^5 <= val <= 10^5
    1 <= depth <= the depth of tree + 1

"""
from typing import List

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
        
def list_to_binarytree(nums):
    def level(index):
        if index >= len(nums) or nums[index] is None:
            return None
        root = TreeNode(nums[index])
        root.left = level(2 * index + 1)    # 往左递推  # 从根开始一直到最左，直至为空
        root.right = level(2 * index + 2)   # 往右回溯  # 再返回上一个根，回溯右
        return root     # 再返回根
    return level(0)

# 层序遍历把结果展示出来
def levelOrder(root: TreeNode) -> List[List[int]]:
    res = []
    if not root:
        return []
    
    def bfs(index, r):
        if len(res) < index:    # 假设res是[ [1],[2,3] ]， index是3，就再插入一个空list放到res中
            res.append([])      # 将当前节点的值加入到res中，index代表当前层，假设index是3，节点值是99
        
        # res是[ [1],[2,3] [4] ]，加入后res就变为 [ [1],[2,3] [4,99] ]
        res[index-1].append(r.val)
        # 递归的处理左子树，右子树，同时将层数index+1
        if r.left:
            bfs(index+1,r.left)
        if r.right:
            bfs(index+1,r.right)
    bfs(1, root)
    return res



""" 方法一：深度优先搜索"""
class Solution:
    def addOneRow(self, root: TreeNode, val: int, depth: int) -> TreeNode:
        if root == None:
            return
        if depth == 1:
            return TreeNode(val, root, None)
        if depth == 2:
            root.left = TreeNode(val, root.left, None)
            root.right = TreeNode(val, None, root.right)
        else:
            root.left = self.addOneRow(root.left, val, depth - 1)
            root.right = self.addOneRow(root.right, val, depth - 1)
        return root

""" 方法二：广度优先搜索"""
class Solution:
    def addOneRow(self, root: TreeNode, val: int, depth: int) -> TreeNode:
        if depth == 1:
            return TreeNode(val, root, None)
        curLevel = [root]
        for _ in range(1, depth - 1):
            tmpt = []
            for node in curLevel:
                if node.left:
                    tmpt.append(node.left)
                if node.right:
                    tmpt.append(node.right)
            curLevel = tmpt
        for node in curLevel:
            node.left = TreeNode(val, node.left, None)
            node.right = TreeNode(val, None, node.right)
        return root

if __name__ == "__main__":
    root = list_to_binarytree([4,2,6,3,1,5])
    val = 1
    depth = 2
    sol = Solution()
    result = sol.addOneRow(root, val, depth)
    print(levelOrder(result))   # [[4], [1, 1], [2, 6], [3, 1, 5]]