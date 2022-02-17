class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution():

    def rob(self, root):

        # 说明：
        # 1.由于房屋是树状的，因此，我们可以使用遍历树的传统方法进行遍历(前序、中序、后续)
        # 2.简单的思路是，从树低进行往上遍历，拿到最优的打劫值。可以选用后续遍历
        # 3.得到每一节点的最优值，最后选取最优的结果

        # 1.dp[i]代表该节点及以下拿到的最多的钱
        # 2.动态方程：
        #   2.1 dp[0]代表不偷该节点拿到最多的钱，则儿子节点偷不偷都ok。dp[0] = max(left[0], left[1]) + max(right[0], right[1])
        #   2.2 dp[1]代表偷了该节点拿到最多的钱，则儿子节点都不能被偷。dp[1] = var + left[0] + right[0]
        # 3.初始化：当前树的形状为空的时候，直接返回dp[0, 0]
        def postTrasval(root):
            dp = [0, 0]
            if not root:
                return dp
            left = postTrasval(root.left)
            right = postTrasval(root.right)

            dp[0] = max(left[0], left[1]) + max(right[0], right[1])
            dp[1] = root.val + left[0] + right[0]

            return dp

        dp = postTrasval(root)
        return max(dp[0], dp[1])


if __name__ == '__main__':
    # initial tree structure
    T = TreeNode(3)
    T.left = TreeNode(2)
    T.right = TreeNode(3)
    T.left.right = TreeNode(3)
    T.right.right = TreeNode(1)

    # The solution to the Question
    s = Solution()
    print(s.rob(T))