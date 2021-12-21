"""
https://leetcode-cn.com/problems/binary-tree-paths/

给你一个二叉树的根节点 root ，按 任意顺序 ，返回所有从根节点到叶子节点的路径。

叶子节点 是指没有子节点的节点。

示例 1：
    输入：root = [1,2,3,null,5]
    输出：["1->2->5","1->3"]

示例 2：
    输入：root = [1]
    输出：["1"]

提示：
    树中节点的数目在范围 [1, 100] 内
    -100 <= Node.val <= 100

"""
import collections
from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        #测试基本功能，输出字符串
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

"""方法1：深度优先搜索，递归"""
class Solution:
    def binaryTreePaths(self, root):
        def DFS(root, path):
            if root:
                path += str(root.val)
                if not root.left and not root.right:  # 当前节点是叶子节点
                    paths.append(path)  # 把路径加入到答案中
                else:
                    path += '->'  # 当前节点不是叶子节点，继续递归遍历
                    DFS(root.left, path)
                    DFS(root.right, path)
        paths = []
        DFS(root, '')
        return paths

"""方法2：广度优先搜索"""
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        paths = list()  # 维护一个队列，存储节点以及根到该节点的路径
        if not root:
            return paths

        node_queue = collections.deque([root])
        path_queue = collections.deque([str(root.val)])

        while node_queue:
            node = node_queue.popleft()
            path = path_queue.popleft()

            if not node.left and not node.right:
                paths.append(path)
            else:
                if node.left:
                    node_queue.append(node.left)
                    path_queue.append(path + '->' + str(node.left.val))
                
                if node.right:
                    node_queue.append(node.right)
                    path_queue.append(path + '->' + str(node.right.val))
        return paths

if __name__ == "__main__":
    nums = [5,4,8,11,None,13,4,7,2,None,None,None,1]
    root = list_to_binarytree(nums)

    sol = Solution()
    result = sol.binaryTreePaths(root)
    print(result)