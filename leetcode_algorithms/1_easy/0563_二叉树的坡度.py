"""
https://leetcode-cn.com/problems/binary-tree-tilt

给定一个二叉树，计算 整个树 的坡度 。

一个树的 节点的坡度 定义即为，该节点左子树的节点之和和右子树节点之和的 差的绝对值 。如果没有左子树的话，左子树的节点之和为 0 ；没有右子树的话也是一样。空结点的坡度是 0 。

整个树 的坡度就是其所有节点的坡度之和。

示例 1：
    输入：root = [1,2,3]
    输出：1
    解释：
    节点 2 的坡度：|0-0| = 0（没有子节点）
    节点 3 的坡度：|0-0| = 0（没有子节点）
    节点 1 的坡度：|2-3| = 1（左子树就是左子节点，所以和是 2 ；右子树就是右子节点，所以和是 3 ）
    坡度总和：0 + 0 + 1 = 1

示例 2：
    输入：root = [4,2,9,3,5,null,7]
    输出：15
    解释：
    节点 3 的坡度：|0-0| = 0（没有子节点）
    节点 5 的坡度：|0-0| = 0（没有子节点）
    节点 7 的坡度：|0-0| = 0（没有子节点）
    节点 2 的坡度：|3-5| = 2（左子树就是左子节点，所以和是 3 ；右子树就是右子节点，所以和是 5 ）
    节点 9 的坡度：|0-7| = 7（没有左子树，所以和是 0 ；右子树正好是右子节点，所以和是 7 ）
    节点 4 的坡度：|(3+5+2)-(9+7)| = |10-16| = 6（左子树值为 3、5 和 2 ，和是 10 ；右子树值为 9 和 7 ，和是 16 ）
    坡度总和：0 + 0 + 0 + 2 + 7 + 6 = 15

示例 3：
    输入：root = [21,7,14,1,1,2,2,3,3]
    输出：9
 
提示：
    树中节点数目的范围在 [0, 10^4] 内
    -1000 <= Node.val <= 1000

"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    
    def __str__(self):
        #测试基本功能，输出字符串
        return str(self.val)   

"""从传入的列表构建二叉树"""
def list_to_binarytree(nums):
    def level(index):
        if index >= len(nums) or nums[index] is None:
            return None
        root = TreeNode(nums[index])
        root.left = level(2 * index + 1)    # 往左递推  # 从根开始一直到最左，直至为空
        root.right = level(2 * index + 2)   # 往右回溯  # 再返回上一个根，回溯右
        return root     # 再返回根
    return level(0)

'''解法1'''
class Solution:
    def findTilt(self, root: TreeNode) -> int:
        def dfs(node):      # 返回节点和，累积坡度
            if not node:
                return 0, 0
            l_sum, l_diff = dfs(node.left)      # 递归求解子问题
            r_sum, r_diff = dfs(node.right)     # 递归求解子问题
            return l_sum + r_sum + node.val, l_diff + r_diff + abs(r_sum - l_sum)   # 跟节点的节点和，累积坡度与子问题的递归关系（合并子问题，形成原问题的解）
        return dfs(root)[1]

'''解法2'''
class Solution:
    def findTilt(self, root: TreeNode) -> int:
        res  = 0
        def dfs(root):      # 返回节点和，累积坡度
            nonlocal res    # 用nonlocal记录全局信息
            if not root: 
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            res += abs(left - right)
            return root.val + left + right
        dfs(root)
        return res

'''解法3'''
class Solution:
    def __init__(self):
        self.ans = 0

    def findTilt(self, root: TreeNode) -> int:
        self.dfs(root)
        return self.ans

    def dfs(self, node):
        if not node:
            return 0
        sum_left = self.dfs(node.left)
        sum_right = self.dfs(node.right)
        self.ans += abs(sum_left - sum_right)
        return sum_left + sum_right + node.val

if __name__ == "__main__":
    nums = [4,2,9,3,5,None,7]
    root = list_to_binarytree(nums)

    sol = Solution()
    result = sol.findTilt(root)
    print(result)

    