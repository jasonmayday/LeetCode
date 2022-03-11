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
        ans = []
        def dfs(node: 'Node'):
            if node is None:
                return
            for ch in node.children:
                dfs(ch)
            ans.append(node.val)
        dfs(root)
        return ans

"""迭代"""
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if root is None:
            return []
        ans = []
        st = []
        nextIndex = defaultdict(int)
        node = root
        while st or node:
            while node:
                st.append(node)
                if not node.children:
                    break
                nextIndex[node] = 1
                node = node.children[0]
            node = st[-1]
            i = nextIndex[node]
            if i < len(node.children):
                nextIndex[node] = i + 1
                node = node.children[i]
            else:
                ans.append(node.val)
                st.pop()
                del nextIndex[node]
                node = None
        return ans

""" 迭代优化 """
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if root is None:
            return []
        ans = []
        st = [root]
        vis = set()
        while st:
            node = st[-1]
            # 如果当前节点为叶子节点或者当前节点的子节点已经遍历过
            if len(node.children) == 0 or node in vis:
                ans.append(node.val)
                st.pop()
                continue
            st.extend(reversed(node.children))
            vis.add(node)
        return ans
    
""" 利用前序遍历反转 """
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if root is None:
            return []
        ans = []
        st = [root]
        while st:
            node = st.pop()
            ans.append(node.val)
            st.extend(node.children)
        ans.reverse()
        return ans
