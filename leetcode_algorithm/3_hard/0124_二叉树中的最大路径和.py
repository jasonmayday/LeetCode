"""
路径 被定义为一条从树中任意节点出发，沿父节点-子节点连接，达到任意节点的序列。同一个节点在一条路径序列中 至多出现一次 。该路径 至少包含一个 节点，且不一定经过根节点。

路径和 是路径中各节点值的总和。

给你一个二叉树的根节点 root ，返回其 最大路径和 。

示例 1：
    输入：root = [1,2,3]
    输出：6
    解释：最优路径是 2 -> 1 -> 3 ，路径和为 2 + 1 + 3 = 6

示例 2：
    输入：root = [-10,9,20,null,null,15,7]
    输出：42
    解释：最优路径是 15 -> 20 -> 7 ，路径和为 15 + 20 + 7 = 42

提示：
    树中节点数目范围是 [1, 3 * 10^4]
    -1000 <= Node.val <= 1000

"""
from typing import List

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
""" 递归 """
class Solution:
    def __init__(self):
        self.maxSum = float("-inf")

    def maxPathSum(self, root: TreeNode) -> int:
        def maxGain(node):  # 该函数计算二叉树中的一个节点的最大贡献值
            if not node:
                return 0

            leftGain = max(maxGain(node.left), 0)       # 递归计算左右子节点的最大贡献值
            rightGain = max(maxGain(node.right), 0)     # 只有在最大贡献值大于 0 时，才会选取对应子节点，如果某条路径之和小于0，则使用0，代表不选这条路径
            
            Newpath = node.val + leftGain + rightGain   # 节点的最大路径和取决于该节点的值与该节点的左右子节点的最大贡献值

            self.maxSum = max(self.maxSum, Newpath)     # 更新答案
        
            return node.val + max(leftGain, rightGain)  # 返回节点的最大贡献值
   
        maxGain(root)
        return self.maxSum


"""

1. 「可以从任意节点出发, 到达任意节点」 的路径, 
   一定是先上升（ 0 ～ n 个）节点, 到达顶点, 后下降（ 0 ～ n 个）节点。
   我们可以通过枚举顶点的方式来枚举路径。
   
2. 我们枚举顶点时, 可以把路径分拆成3部分： 左侧路径、右侧路径和顶点。
   如下面的路径, 顶点为 20, 左侧路径为 6 -> 15, 右侧为 6 -> 7。
   
      -10
      / \
     9 [20]
       /  \
     [15] [7]
     /    / \
   [6]   4  [6]   

   以当前节点为顶点的路径中, 最大和为 两侧路径的最大和 + 节点的值。
   需要注意的是, 两侧路径也可能不选, 此时取 0。

3. 如何求两侧路径最大和？ 看一个类似问题：求数组的最大子数组和。
   动态规划： dp[i] 代表以 nums[i] 为结尾的子数组的最大和。
   转移方程： dp[i] = max(dp[i-1], 0) + nums[i]。

4. 在树上, 设 dp[C] 代表以当前节点为结尾的最大上升路径和, 
   则我们需要对节点的左右子树做一个选择, 有
   dp[C] = max(max(dp[L], 0), max(dp[R], 0)) + C.val
   式中, C,L,R 分别代指 当前节点、左子节点、右子节点。

5. 最后, 以当前节点为顶点的路径中, 最大的和为
   max(dp[L], 0) + max(dp[R], 0) + C.val。
   我们枚举顶点, 并记录最大答案。
"""

if __name__ == '__main__':
    tree = TreeNode(-10)
    tree.left = TreeNode(9)
    tree.right = TreeNode(20)
    tree.right.left = TreeNode(15)
    tree.right.right = TreeNode(7)
    
    sol = Solution()
    result = sol.maxPathSum(tree)
    print (result)