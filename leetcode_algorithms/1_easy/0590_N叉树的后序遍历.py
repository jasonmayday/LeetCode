"""
https://leetcode-cn.com/problems/n-ary-tree-preorder-traversal/

给定一个 N 叉树，返回其节点值的 后序遍历 。

N 叉树 在输入中按层序遍历进行序列化表示，每组子节点由空值 null 分隔（请参见示例）。

进阶：
    递归法很简单，你可以使用迭代法完成此题吗?

示例 1：
    输入：root = [1,null,3,2,4,null,5,6]
    输出：[5,6,3,2,4,1]

示例 2：
    输入：root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
    输出：[2,6,14,11,7,3,12,8,4,13,9,10,5,1]

提示：
    N 叉树的高度小于或等于 1000
    节点总数在范围 [0, 10^4] 内

"""
from typing import List


"""递归"""
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        def dfs(root: 'Node') -> None:
            for child in root.children:
                dfs(child)
            value.append(root.val)
        
        value = []
        if root:
            dfs(root)
        return value

"""迭代"""
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        value, s = [], []
        cur = root
        while s or cur:
            while cur:
                s.append((cur, 0))
                if cur.children:
                    cur = cur.children[0]
                else:
                    cur = None
            cur, c = s.pop()
            if not cur.children or c >= len(cur.children):
                value.append(cur.val)
                cur = None
            else:
                c += 1
                s.append((cur, c))
                if c < len(cur.children):
                    cur = cur.children[c]
                else:
                    cur = None
        return value

