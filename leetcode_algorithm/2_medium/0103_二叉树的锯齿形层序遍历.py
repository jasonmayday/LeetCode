"""
https://leetcode-cn.com/problems/binary-tree-zigzag-level-order-traversal/

给你二叉树的根节点 root ，返回其节点值的 锯齿形层序遍历 。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。

示例 1：
    输入：root = [3,9,20,null,null,15,7]
    输出：[[3],[20,9],[15,7]]

示例 2：
    输入：root = [1]
    输出：[[1]]

示例 3：
    输入：root = []
    输出：[]

提示：
    树中节点数目在范围 [0, 2000] 内
    -100 <= Node.val <= 100

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


""" 迭代实现 BFS (广度优先搜索) """
class Solution(object):
    def zigzagLevelOrder(self, root):
        if not root:
            return []
        queue = deque()     # 定义一个双端队列，初始时候将根节点放入队列
        queue.append(root)
        index = 1           # 定义 index (层数)，用来控制输出的方向的，是正向输出，还是反向输出
        res = []
        while queue:
            size = len(queue)       # 获取queue的长度，因为队列的长度是在不断变化的，这里需先确定要遍历多少次
            tmp = []                # 每一层的列表
            for _ in range(size):
                node = queue.popleft()
                tmp.append(node.val)
                if node.left:               
                    queue.append(node.left)     # 如果左节点不为空，则继续放入队列中
                if node.right:              
                    queue.append(node.right)    # 如果右节点不为空，则继续放入队列中
            if (index & 1) == 1:        # 当index为奇数时，
                res.append(tmp)         # 就正向输出
            else:                       # 当index偶位数时，
                res.append(tmp[::-1])   # 就反向输出，即先调用一次reverse，再保存
            index += 1
        return res

""" 递归实现 DFS (深度优先搜索) """
class Solution(object):
    def zigzagLevelOrder(self, root):
        if not root:
            return []
        res = []
        
        def dfs(root, index):   # index 为层数
            if not root:        # 遍历的终止条件
                return
            if len(res) < index:      # 没有对应的第 index 层数组时：
                res.append(deque())   # 创建第 index 层数组
            if index % 2:                           # 偶数层
                res[index - 1].append(root.val)     # 答案中第 index 层加入答案
            else:                                   # 奇数层
                res[index - 1].appendleft(root.val) # 答案中第 index 层加入答案（加入到list最左边，相当于反向加入）
            dfs(root.left, index + 1)   # 递归左子树
            dfs(root.right, index + 1)  # 递归右子树
            
        dfs(root, 1)
        return [list(q) for q in res]

if __name__ == "__main__":
    root = list_to_binarytree([3,9,20,None,None,15,7])
    '''
           3
         ↙   ↘
       9       20
              ↙  ↘
             15    7
    '''
    sol = Solution()
    result = sol.zigzagLevelOrder(root)
    print(result)