"""
https://leetcode.cn/problems/serialize-and-deserialize-bst/

序列化是将数据结构或对象转换为一系列位的过程，以便它可以存储在文件或内存缓冲区中，或通过网络连接链路传输，以便稍后在同一个或另一个计算机环境中重建。

设计一个算法来序列化和反序列化 二叉搜索树 。 对序列化/反序列化算法的工作方式没有限制。 您只需确保二叉搜索树可以序列化为字符串，并且可以将该字符串反序列化为最初的二叉搜索树。

编码的字符串应尽可能紧凑。

示例 1：
    输入：root = [2,1,3]
    输出：[2,1,3]

示例 2：
    输入：root = []
    输出：[]

提示：
    树中节点数范围是 [0, 10^4]
    0 <= Node.val <= 10^4
    题目数据 保证 输入的树是一棵二叉搜索树。

"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

"""方法一：后序遍历"""
class Codec:
    def serialize(self, root: TreeNode) -> str:
        arr = []
        def postOrder(root: TreeNode) -> None:
            if root is None:
                return
            postOrder(root.left)
            postOrder(root.right)
            arr.append(root.val)
        postOrder(root)
        return ' '.join(map(str, arr))

    def deserialize(self, data: str) -> TreeNode:
        arr = list(map(int, data.split()))
        def construct(lower: int, upper: int) -> TreeNode:
            if arr == [] or arr[-1] < lower or arr[-1] > upper:
                return None
            val = arr.pop()
            root = TreeNode(val)
            root.right = construct(val, upper)
            root.left = construct(lower, val)
            return root
        return construct(-inf, inf)

""" 直接将其用先序遍历序列化，因为是二叉搜索树，所以排序后就是中序遍历，因此反序列化就转换成了105题的从先序与中序构造二叉树的问题。 """
class Codec:
    def serialize(self, root):
        def preorder(root):
            out = []
            if root:
                out += [str(root.val)]
                out += preorder(root.left)
                out += preorder(root.right)
            return out
        return ','.join(preorder(root))
        
    def deserialize(self, data):
        if not data:
            return None
        def buildTree(pre_o, in_o):
            if not pre_o:
                return None
            mid = pre_o[0]
            i = in_o.index(mid)
            root = TreeNode(mid)
            root.left = buildTree(pre_o[1:i + 1], in_o[:i])
            root.right = buildTree(pre_o[i + 1:], in_o[i + 1:])
            return root
        pre_o = list(map(int, data.split(',')))
        in_o = sorted(pre_o)
        return buildTree(pre_o, in_o)