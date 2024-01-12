"""
https://leetcode-cn.com/problems/sum-root-to-leaf-numbers/

给你一个二叉树的根节点 root ，树中每个节点都存放有一个 0 到 9 之间的数字。
每条从根节点到叶节点的路径都代表一个数字：
    例如，从根节点到叶节点的路径 1 -> 2 -> 3 表示数字 123 。

计算从根节点到叶节点生成的 所有数字之和 。

叶节点 是指没有子节点的节点。

示例 1：
    输入：root = [1,2,3]
    输出：25
    解释：
    从根到叶子节点路径 1->2 代表数字 12
    从根到叶子节点路径 1->3 代表数字 13
    因此，数字总和 = 12 + 13 = 25

示例 2：
    输入：root = [4,9,0,5,1]
    输出：1026
    解释：
    从根到叶子节点路径 4->9->5 代表数字 495
    从根到叶子节点路径 4->9->1 代表数字 491
    从根到叶子节点路径 4->0 代表数字 40
    因此，数字总和 = 495 + 491 + 40 = 1026

提示：
    树中节点的数目在范围 [1, 1000] 内
    0 <= Node.val <= 9
    树的深度不超过 10

"""
from collections import deque

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

"""递归 + 回溯"""
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        res = 0
        path = []   # 使用数组方便进行回溯
        
        def backtrace(root):
            nonlocal res
            if not root: return # 节点空则返回
            path.append(root.val)
            if not root.left and not root.right: # 遇到了叶子节点
                res += get_sum(path)
            if root.left: # 左子树不空
                backtrace(root.left)
            if root.right: # 右子树不空
                backtrace(root.right)
            path.pop()

        def get_sum(arr):
            s = 0
            for i in range(len(arr)):
                s = s * 10 + arr[i]
            return s

        backtrace(root)
        return res

""" 深度优先搜索 """
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        
        def dfs(root: TreeNode, prevTotal: int) -> int:
            if not root:
                return 0
            total = prevTotal * 10 + root.val
            if not root.left and not root.right:    # 如果遇到叶子节点
                return total                        # 则将叶子节点对应的数字加到数字之和
            else:                                                       # 如果当前节点不是叶子节点
                return dfs(root.left, total) + dfs(root.right, total)   # 则计算其子节点对应的数字，然后对子节点递归遍历。

        return dfs(root, 0)

""" 广度优先搜索 """
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if not root:
            return 0

        total = 0                       # 需要维护两个队列
        nodeQueue = deque([root])       # 存储节点
        numQueue = deque([root.val])    # 存储节点对应的数字
        
        while nodeQueue:                # 每次从两个队列分别取出一个节点和一个数字
            node = nodeQueue.popleft()  # 将根节点加入队列
            num = numQueue.popleft()    # 将根节点的值加入队列
            left = node.left
            right = node.right
            if not left and not right:  # 如果当前节点是叶子节点，
                total += num            # 则将该节点对应的数字加到数字之和
            else:                           # 如果当前节点不是叶子节点
                if left:    
                    nodeQueue.append(left)                  # 将子节点和子节点对应的数字分别加入两个队列
                    numQueue.append(num * 10 + left.val)    # 根据当前节点对应的数字和子节点的值计算子节点对应的数字
                if right:
                    nodeQueue.append(right)
                    numQueue.append(num * 10 + right.val)

        return total


if __name__ == "__main__":
    root = list_to_binarytree([4,9,0,5,1])
    sol = Solution()
    result = sol.sumNumbers(root)
    print (result)