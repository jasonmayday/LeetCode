"""
https://leetcode-cn.com/problems/two-sum-iv-input-is-a-bst/

给定一个二叉搜索树 root 和一个目标结果 k，如果 BST 中存在两个元素且它们的和等于给定的目标结果，则返回 true。

示例 1：
	    5
	   / \
	  3   6
	 / \   \
	2   4   7
    输入: root = [5,3,6,2,4,null,7], k = 9
    输出: true

示例 2：
	    5
	   / \
	  3   6
	 / \   \
	2   4   7
    输入: root = [5,3,6,2,4,null,7], k = 28
    输出: false

示例 3：
    输入: root = [2,1,3], k = 4
    输出: true

示例 4：
    输入: root = [2,1,3], k = 1
    输出: false

示例 5：
    输入: root = [2,1,3], k = 3
    输出: true
 
提示:
    二叉树的节点个数的范围是  [1, 10^4].
    -10^4 <= Node.val <= 10^4
    root 为二叉搜索树
    -10^5 <= k <= 10^5

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

from collections import deque

""" 方法一：DFS + 哈希表 """
class Solution:
    def __init__(self):
        self.hash = set()  # 初始化一个哈希表 hash

    def findTarget(self, root: TreeNode, k: int) -> bool:
        if root is None:                # 如果遍历完整棵树都不存在对应的元素，
            return False                # 那么该树上不存在两个和为 k 的节点。
        if k - root.val in self.hash:   # 对于一个值为 x 的节点，我们检查哈希表中是否存在 k−x 即可
            return True                 # 如果存在对应的元素，那么我们就可以在该树上找到两个节点的和为 k
        self.hash.add(root.val)         # 否则，我们将 x 放入到哈希表中。
        return self.findTarget(root.left, k) or self.findTarget(root.right, k)

""" 方法二：BFS + 哈希表 """
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        s = set()           # 用哈希表记录遍历过的节点的值，首先创建一个哈希表
        q = deque([root])   # 创建一个队列，将根节点加入队列中
        while q:
            node = q.popleft()      # 从队列中取出队头，假设其值为 x
            if k - node.val in s:   # 检查哈希表中是否存在 k−x
                return True         # 如果存在，返回 True
            s.add(node.val)         # 否则，将该节点的左右的非空子节点加入队尾
            if node.left:           # 重复以上步骤，直到队列为空
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return False                # 如果队列为空，说明树上不存在两个和为 k 的节点，返回 False。

""" 方法三：深度优先搜索 + 中序遍历 + 双指针
    中序遍历 (In-Order Traversal) ：左子树 ---> 根结点 ---> 右子树
    二叉搜索树采用中序遍历，就是一个升序数组"""
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        arr = []
        def inorderTraversal(node: TreeNode) -> None:
            if node:
                inorderTraversal(node.left)
                arr.append(node.val)
                inorderTraversal(node.right)
        inorderTraversal(root)

        left  = 0               # 使用两个指针分别指向数组的头尾
        right = len(arr) - 1
        while left < right:
            sum = arr[left] + arr[right]
            if sum == k:    # 当两个指针指向的元素之和等于 kk 时，返回 True。
                return True
            if sum < k:     # 当两个指针指向的元素之和小于 k 时，让左指针右移
                left += 1
            else:           # 当两个指针指向的元素之和大于 k 时，让右指针左移
                right -= 1
        return False        # 最终，当左指针和右指针重合时，树上不存在两个和为 k 的节点，返回 False。


if __name__ == "__main__":
    root = list_to_binarytree([5,3,6,2,4,None,7])
    k = 9
    sol = Solution()
    result = sol.findTarget(root, k)
    print (result)


