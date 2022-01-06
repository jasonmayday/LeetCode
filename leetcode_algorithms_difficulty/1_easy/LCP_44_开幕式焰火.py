"""
https://leetcode-cn.com/problems/sZ59z6/

「力扣挑战赛」开幕式开始了，空中绽放了一颗二叉树形的巨型焰火。
给定一棵二叉树 root 代表焰火，节点值表示巨型焰火这一位置的颜色种类。请帮小扣计算巨型焰火有多少种不同的颜色。

示例 1：
    输入：root = [1,3,2,1,null,2]
    输出：3
    解释：焰火中有 3 个不同的颜色，值分别为 1、2、3

示例 2：
    输入：root = [3,3,3]
    输出：1
    解释：焰火中仅出现 1 个颜色，值为 3

提示：
    1 <= 节点个数 <= 1000
    1 <= Node.val <= 1000

"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.val)   

"""递归构建"""
def list_to_binarytree(nums):
    def level(index):
        if index >= len(nums) or nums[index] is None:
            return None
        root = TreeNode(nums[index])
        root.left = level(2 * index + 1)    # 往左递推  从根开始一直到最左，直至为空
        root.right = level(2 * index + 2)   # 往右回溯  再返回上一个根，回溯右
        return root     # 再返回根
    return level(0)

class Solution:
    def numColor(self, root: TreeNode) -> int:
        color = set()
        
        def dfs(root):
            if not root: return
            color.add(root.val)
            dfs(root.left)
            dfs(root.right)
        
        dfs(root)
        return len(color)

if __name__ == "__main__":
    root = list_to_binarytree([1,3,2,1,None,2])
    sol = Solution()
    result = sol.numColor(root)
    print(result)