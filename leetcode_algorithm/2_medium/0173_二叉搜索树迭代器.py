"""
https://leetcode-cn.com/problems/binary-search-tree-iterator/

实现一个二叉搜索树迭代器类BSTIterator ，表示一个按中序遍历二叉搜索树（BST）的迭代器：
    BSTIterator(TreeNode root) 初始化 BSTIterator 类的一个对象。BST 的根节点 root 会作为构造函数的一部分给出。指针应初始化为一个不存在于 BST 中的数字，且该数字小于 BST 中的任何元素。
    boolean hasNext() 如果向指针右侧遍历存在数字，则返回 true ；否则返回 false 。
    int next()将指针向右移动，然后返回指针处的数字。

注意，指针初始化为一个不存在于 BST 中的数字，所以对 next() 的首次调用将返回 BST 中的最小元素。

你可以假设 next() 调用总是有效的，也就是说，当调用 next() 时，BST 的中序遍历中至少存在一个下一个数字。

示例：
    输入
        ["BSTIterator", "next", "next", "hasNext", "next", "hasNext", "next", "hasNext", "next", "hasNext"]
        [[[7, 3, 15, null, null, 9, 20]], [], [], [], [], [], [], [], [], []]
    输出
        [null, 3, 7, true, 9, true, 15, true, 20, false]

    解释
        BSTIterator bSTIterator = new BSTIterator([7, 3, 15, null, null, 9, 20]);
        bSTIterator.next();    // 返回 3
        bSTIterator.next();    // 返回 7
        bSTIterator.hasNext(); // 返回 True
        bSTIterator.next();    // 返回 9
        bSTIterator.hasNext(); // 返回 True
        bSTIterator.next();    // 返回 15
        bSTIterator.hasNext(); // 返回 True
        bSTIterator.next();    // 返回 20
        bSTIterator.hasNext(); // 返回 False

提示：
    树中节点的数目在范围 [1, 10^5] 内
    0 <= Node.val <= 10^6
    最多调用 10^5 次 hasNext 和 next 操作

进阶：
    你可以设计一个满足下述条件的解决方案吗？next() 和 hasNext() 操作均摊时间复杂度为 O(1) ，并使用 O(h) 内存。其中 h 是树的高度。

"""
from collections import deque

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
    def __str__(self):
        return str(self.val)
    
def list_to_binarytree(nums):
    def level(index):
        if index >= len(nums) or nums[index] is None:
            return None
        root = TreeNode(nums[index])
        root.left = level(2 * index + 1)    # 往左递推  # 从根开始一直到最左，直至为空
        root.right = level(2 * index + 2)   # 往右回溯  # 再返回上一个根，回溯右
        return root     # 再返回根
    return level(0)


""" 方法一：提前保存全部节点"""
class BSTIterator(object):

    def __init__(self, root):
        self.queue = deque()
        self.inOrder(root)
    
    def inOrder(self, root):    # 中序遍历（递归）
        if not root:
            return
        self.inOrder(root.left)
        self.queue.append(root.val) # 把节点保存到双端列表中
        self.inOrder(root.right)

    def next(self):
        return self.queue.popleft()

    def hasNext(self):
        return len(self.queue) > 0  # 双端列表不为空，说明还有节点


""" 方法二：迭代时计算 next 节点"""
class BSTIterator(object):

    def __init__(self, root):
        self.stack = []     # 把递归转成迭代，基本想法就是用栈
        while root:                     # 构造方法：一路到底，
            self.stack.append(root)     # 把根节点和它的所有左节点放到栈中；
            root = root.left

    def next(self):
        cur = self.stack.pop()          # 调用 next() 方法：弹出栈顶的节点
        node = cur.right                # 如果它有右子树，
        while node:                     # 则对右子树一路到底，
            self.stack.append(node)     # 把它和它的所有左节点放到栈中。
            node = node.left
        return cur.val

    def hasNext(self):
        return len(self.stack) > 0


if __name__ == "__main__":
    bSTIterator = BSTIterator(list_to_binarytree([7, 3, 15, None, None, 9, 20]))
    print (bSTIterator.next())      # 返回 3
    print (bSTIterator.next())      # 返回 7
    print (bSTIterator.hasNext())   # 返回 True
    print (bSTIterator.next())      # 返回 9
    print (bSTIterator.hasNext())   # 返回 True
    print (bSTIterator.next())      # 返回 15
    print (bSTIterator.hasNext())   # 返回 True
    print (bSTIterator.next())      # 返回 20
    print (bSTIterator.hasNext())   # 返回 False
