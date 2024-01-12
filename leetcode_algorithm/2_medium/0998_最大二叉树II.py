"""
https://leetcode.cn/problems/maximum-binary-tree-ii/

最大树 定义：一棵树，并满足：其中每个节点的值都大于其子树中的任何其他值。

给你最大树的根节点 root 和一个整数 val 。

就像 之前的问题 那样，给定的树是利用 Construct(a) 例程从列表 a（root = Construct(a)）递归地构建的：

    如果 a 为空，返回 null 。
    否则，令 a[i] 作为 a 的最大元素。创建一个值为 a[i] 的根节点 root 。
    root 的左子树将被构建为 Construct([a[0], a[1], ..., a[i - 1]]) 。
    root 的右子树将被构建为 Construct([a[i + 1], a[i + 2], ..., a[a.length - 1]]) 。
    返回 root 。

请注意，题目没有直接给出 a ，只是给出一个根节点 root = Construct(a) 。

假设 b 是 a 的副本，并在末尾附加值 val。题目数据保证 b 中的值互不相同。

返回 Construct(b) 。

示例 1：
    输入：root = [4,1,3,null,null,2], val = 5
    输出：[5,4,null,1,3,null,null,2]
    解释：a = [1,4,2,3], b = [1,4,2,3,5]

示例 2：
    输入：root = [5,2,4,null,1], val = 3
    输出：[5,2,4,null,1,null,3]
    解释：a = [2,1,5,4], b = [2,1,5,4,3]

示例 3：
    输入：root = [5,2,3,null,1], val = 4
    输出：[5,2,4,null,1,3]
    解释：a = [2,1,5,3], b = [2,1,5,3,4]

提示：
    树中节点数目在范围 [1, 100] 内
    1 <= Node.val <= 100
    树中的所有值 互不相同
    1 <= val <= 100

"""
from typing import List

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
        root.left = level(2 * index + 1)    # 往左递推  # 从根开始一直到最左，直至为空
        root.right = level(2 * index + 2)   # 往右回溯  # 再返回上一个根，回溯右
        return root     # 再返回根
    return level(0)

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

"""方法一：遍历右子节点"""
class Solution:
    def insertIntoMaxTree(self, root: TreeNode, val: int) -> TreeNode:
        parent, cur = None, root
        while cur:
            if val > cur.val:   # 如果根节点的值小于给定的整数 val，那么新的树会以 val 作为根节点，并将原来的树作为新的根节点的左子树。
                if not parent:  # 我们就可以停止遍历，构造一个新的节点，以 val 为值且以 cur 为左子树。
                    return TreeNode(val, root, None)
                node = TreeNode(val, cur, None)
                parent.right = node
                return root         # 我们将该节点作为 parent 的新的右节点，并返回根节点作为答案即可。
            else:               # 否则，我们从根节点开始不断地向右子节点进行遍历。
                parent = cur
                cur = cur.right
        
        parent.right = TreeNode(val)
        return root

if __name__ == "__main__":
    root = list_to_binarytree([4,1,3,None,None,2])
    val = 5
    sol = Solution()
    result = sol.insertIntoMaxTree(root, val)
    print(levelOrder(result))