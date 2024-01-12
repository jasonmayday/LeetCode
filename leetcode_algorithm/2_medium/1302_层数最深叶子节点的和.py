"""
https://leetcode.cn/problems/deepest-leaves-sum/

给你一棵二叉树的根节点 root ，请你返回 层数最深的叶子节点的和 。

示例 1：
    输入：root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
    输出：15
    
          1
         / \
        2   3
       / \   \
      4   5   6
     /         \
    7           8

示例 2：
    输入：root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
    输出：19

提示：
    树中节点数目在范围 [1, 10^4] 之间。
    1 <= Node.val <= 100

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

""" 方法一：深度优先搜索
    从根节点开始遍历整个二叉树，遍历每个节点时需要记录该节点的层数，规定根节点在第 0 层。
    遍历过程中维护最大层数与最深节点之和。"""
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        maxLevel = -1   # 最大层数
        ans = 0         # 初始化 层数最深的叶子节点的和
        def dfs(node: TreeNode, level: int) -> None:
            if node is None:
                return
            nonlocal maxLevel, ans
            if level > maxLevel:    # 如果当前节点的层数大于最大层数, 则之前遍历到的节点都不是层数最深的节点
                maxLevel = level    # 因此用当前节点的层数更新最大层数
                ans = node.val      # 并将最深节点之和更新为当前节点值；
            elif level == maxLevel:     # 如果当前节点的层数等于最大层数，
                ans += node.val         # 则将当前节点值加到最深节点之和。
            dfs(node.left, level + 1)   # 对当前节点的左右子节点继续深度优先搜索。
            dfs(node.right, level + 1)
        dfs(root, 0)
        return ans

""" 方法二：广度优先搜索
    使用广度优先搜索时，对二叉树层序遍历。
    此时不需要维护最大层数，只需要确保每一轮遍历的节点是同一层的全部节点，则最后一轮遍历的节点是全部最深节点。"""
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        q = deque([root])   # 初始时，将根节点加入队列，此时队列中只有一个节点，是同一层的全部节点。
        while q:            # 遍历层数
            ans = 0
            for _ in range(len(q)):
                node = q.popleft()  # 每一轮遍历时，首先得到队列中的节点个数 size，从队列中取出 size 个节点，则这 size 个节点是同一层的全部节点，
                ans += node.val
                if node.left:           # 第 x 层的每个节点的子节点都在第 x+1 层，将子节点加入队列，
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return ans                  # 分别计算每一层的节点之和，则遍历结束时的节点之和即为层数最深叶子节点的和。

if __name__ == "__main__":
    root = list_to_binarytree([1,2,3,4,5,None,6,7,None,None,None,None,8])
    sol = Solution()
    result = sol.deepestLeavesSum(root)
    print(result)