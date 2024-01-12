"""
https://leetcode-cn.com/problems/house-robber-iii/

小偷又发现了一个新的可行窃的地区。这个地区只有一个入口，我们称之为 root 。

除了 root 之外，每栋房子有且只有一个“父“房子与之相连。一番侦察之后，聪明的小偷意识到“这个地方的所有房屋的排列类似于一棵二叉树”。 如果 两个直接相连的房子在同一天晚上被打劫 ，房屋将自动报警。

给定二叉树的 root 。返回 在不触动警报的情况下 ，小偷能够盗取的最高金额 。

示例 1:
    输入: root = [3,2,3,null,3,null,1]
    输出: 7 
    解释: 小偷一晚能够盗取的最高金额 3 + 3 + 1 = 7

示例 2:
    输入: root = [3,4,5,1,3,null,1]
    输出: 9
    解释: 小偷一晚能够盗取的最高金额 4 + 5 = 9

提示：
    树的节点数在 [1, 10^4] 范围内
    0 <= Node.val <= 10^4

"""

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

""" 动态规划 + 后序遍历 """
class Solution():
    def rob(self, root: TreeNode) -> int:
        # 从树低进行往上遍历，拿到最优的打劫值。可以选用后续遍历，得到每一节点的最优值，最后选取最优的结果
        def postTrasval(root):
            dp = [0, 0]     # dp 数组 下标为0记录不偷该节点所得到的的最大金钱，下标为1记录偷该节点所得到的的最大金钱。 [不偷，偷]
            if not root:    # 确定终止条件: 在遍历的过程中，如果遇到空节点的话，很明显，无论偷还是不偷都是0，所以就返回
                return dp
            left = postTrasval(root.left)   # 通过递归左节点，得到左节点偷与不偷的金钱。
            right = postTrasval(root.right) # 通过递归右节点，得到右节点偷与不偷的金钱。
            
            # dp[i]代表该节点及以下拿到的最多的钱
            dp[0] = max(left) + max(right)          # dp[0]代表不偷该节点拿到最多的钱，则取左右子树中最大的值
            dp[1] = root.val + left[0] + right[0]   # dp[1]代表偷了该节点拿到最多的钱，则左右子树都不能偷

            return dp

        dp = postTrasval(root)  # [6,7]
        return max(dp[0], dp[1])


if __name__ == '__main__':
    houses = TreeNode(3)
    houses.left = TreeNode(2)
    houses.right = TreeNode(3)
    houses.left.right = TreeNode(3)
    houses.right.right = TreeNode(1)
    
    sol = Solution()
    result = sol.rob(houses)
    print (result)