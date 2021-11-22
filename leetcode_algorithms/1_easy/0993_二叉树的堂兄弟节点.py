"""
https://leetcode-cn.com/problems/cousins-in-binary-tree/

在二叉树中，根节点位于深度 0 处，每个深度为 k 的节点的子节点位于深度 k+1 处。

如果二叉树的两个节点深度相同，但 父节点不同 ，则它们是一对堂兄弟节点。

我们给出了具有唯一值的二叉树的根节点 root ，以及树中两个不同节点的值 x 和 y 。

只有与值 x 和 y 对应的节点是堂兄弟节点时，才返回 true 。否则，返回 false。

示例 1：
    输入：root = [1,2,3,4], x = 4, y = 3
    输出：false
    
示例 2：
    输入：root = [1,2,3,null,4,null,5], x = 5, y = 4
    输出：true

示例 3：
    输入：root = [1,2,3,null,4], x = 2, y = 3
    输出：false

提示：
    二叉树的节点数介于 2 到 100 之间。
    每个节点的值都是唯一的、范围为 1 到 100 的整数。

"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def list_to_binarytree(nums):
    def level(index):
        if index >= len(nums) or nums[index] is None:
            return None
        root = TreeNode(nums[index])
        root.left = level(2 * index + 1)
        root.right = level(2 * index + 2)
        return root
    return level(0)

"""DFS"""
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        x_depth, x_parent, y_depth, y_parent = None, None, None, None
        # 从根节点开始，对树进行一次遍历，在遍历的过程中维护「深度」以及「父节点」这两个信息。
        def dfs(root, parent, x, y, depth):
            nonlocal x_depth, x_parent, y_depth, y_parent
            
            if root is None:
                return 
            
            # 判断 x, y 是否等于当前节点的值, 是的话更新 x 或者 y 的深度和parent
            if root.val == x:       # 当我们遍历到 x 或 y 节点时，就将「深度」以及「父节点」信息记录下来
                x_depth = depth 
                x_parent = parent 
            if root.val == y:
                y_depth = depth
                y_parent = parent

            dfs(root.left, root, x, y, depth+1)
            dfs(root.right, root, x, y, depth+1)

        dfs(root, None, x, y, 0)
        # 最后保证 x, y的深度一样, 但是parent节点不一样, 这样才是堂兄弟
        return x_depth == y_depth and x_parent != y_parent

"""BFS"""
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        x_depth, x_parent, y_depth, y_parent = None, None, None, None

        level = 0
        # 保存node和node的parent节点
        queue = [(root, None)]

        # 为什么python这样也能检查queue是否为空呢? 
        # python 会检查一个变量的boolean值, 如果不是bool类型, 则检查他的size,
        # size = 0 返回 False, 其余均返回 True
        while queue:
            queueLen = len(queue)
            level += 1
            for i in range(queueLen):
                # 队列操作先进先出, pop(0)弹出最早进入的值
                current, parent = queue.pop(0)

                # 判断节点值, 更新x 或者 y 的深度和parent
                if current.val == x:
                    x_depth = level
                    x_parent = parent
                if current.val == y:
                    y_depth = level
                    y_parent = parent

                if current.left:
                    queue.append((current.left, current))
                if current.right:
                    queue.append((current.right, current))

        # 最后保证 x, y的深度一样, 但是parent节点不一样, 这样才是堂兄弟
        return x_depth == y_depth and x_parent != y_parent

if __name__ == "__main__":
    root = list_to_binarytree([1,2,3,None,4,None,5])
    x = 5
    y = 4
    
    sol = Solution()
    result = sol.isCousins(root,x,y)
    print(result)
    