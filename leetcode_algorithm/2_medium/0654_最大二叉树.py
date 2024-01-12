"""
https://leetcode.cn/problems/maximum-binary-tree/

给定一个不重复的整数数组 nums 。 最大二叉树 可以用下面的算法从 nums 递归地构建:

    1. 创建一个根节点，其值为 nums 中的最大值。
    2. 递归地在最大值 左边 的 子数组前缀上 构建左子树。
    3. 递归地在最大值 右边 的 子数组后缀上 构建右子树。

返回 nums 构建的 最大二叉树 。

示例 1：
    输入：nums = [3,2,1,6,0,5]
    输出：[6,3,5,null,2,0,null,null,1]
    解释：递归调用如下所示：
    - [3,2,1,6,0,5] 中的最大值是 6 ，左边部分是 [3,2,1] ，右边部分是 [0,5] 。
        - [3,2,1] 中的最大值是 3 ，左边部分是 [] ，右边部分是 [2,1] 。
            - 空数组，无子节点。
            - [2,1] 中的最大值是 2 ，左边部分是 [] ，右边部分是 [1] 。
                - 空数组，无子节点。
                - 只有一个元素，所以子节点是一个值为 1 的节点。
        - [0,5] 中的最大值是 5 ，左边部分是 [0] ，右边部分是 [] 。
            - 只有一个元素，所以子节点是一个值为 0 的节点。
            - 空数组，无子节点。

示例 2：
    输入：nums = [3,2,1]
    输出：[3,null,2,null,1]

提示：
    1 <= nums.length <= 1000
    0 <= nums[i] <= 1000
    nums 中的所有整数 互不相同

"""
from typing import List
    
class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

# 层序遍历把结果展示出来
def levelOrder(root: TreeNode) -> List[List[int]]:
    res = []
    if not root:
        return []
    
    def bfs(index, r):
        if len(res) < index:    # 假设res是[ [1],[2,3] ]， index是3，就再插入一个空list放到res中
            res.append([])      # 将当前节点的值加入到res中，index代表当前层，假设index是3，节点值是99
        
        # res是[ [1],[2,3] [4] ]，加入后res就变为 [ [1],[2,3] [4,99] ]
        res[index-1].append(r.val)
        # 递归的处理左子树，右子树，同时将层数index+1
        if r.left:
            bfs(index+1,r.left)
        if r.right:
            bfs(index+1,r.right)
    bfs(1, root)
    return res

""" 方法一：递归"""
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        def construct(left: int, right: int) -> TreeNode:   # 用递归函数表示对数组 nums 中从 left 到 right 的元素构建一棵树。
            if left > right:
                return None
            
            max = left  # 先假定最左为最大值，
            for i in range(left + 1, right + 1):    # 再找到最大值的下标
                if nums[i] > nums[max]:
                    max = i
        
            node = TreeNode(nums[max])      # 确定了根节点的值，为nums中的最大值。
            node.left = construct(left, max - 1)    # 递归左子树
            node.right = construct(max + 1, right)  # 递归右子树
            return node
        
        return construct(0, len(nums) - 1)  # 从第一个数找到最后一个数

""" 方法二：单调栈"""
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        n = len(nums)
        stk = list()
        left, right = [-1] * n, [-1] * n
        tree = [None] * n

        for i in range(n):
            tree[i] = TreeNode(nums[i])
            while stk and nums[i] > nums[stk[-1]]:
                right[stk[-1]] = i
                stk.pop()
            if stk:
                left[i] = stk[-1]
            stk.append(i)
        
        root = None
        for i in range(n):
            if left[i] == right[i] == -1:
                root = tree[i]
            elif right[i] == -1 or (left[i] != -1 and nums[left[i]] < nums[right[i]]):
                tree[left[i]].right = tree[i]
            else:
                tree[right[i]].left = tree[i]
        
        return root

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        n = len(nums)
        stk = list()
        tree = [None] * n

        for i in range(n):
            tree[i] = TreeNode(nums[i])
            while stk and nums[i] > nums[stk[-1]]:
                tree[i].left = tree[stk[-1]]
                stk.pop()
            if stk:
                tree[stk[-1]].right = tree[i]
            stk.append(i)
        
        return tree[stk[0]]

if __name__ == "__main__":
    nums = [3,2,1,6,0,5]
    sol = Solution()
    result = sol.constructMaximumBinaryTree(nums)
    print(levelOrder(result))