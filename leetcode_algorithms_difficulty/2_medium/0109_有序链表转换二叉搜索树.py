"""
https://leetcode-cn.com/problems/convert-sorted-list-to-binary-search-tree/

给定一个单链表，其中的元素按升序排序，将其转换为高度平衡的二叉搜索树。

本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。

示例:
    给定的有序链表： [-10, -3, 0, 5, 9],
    一个可能的答案是：[0, -3, 9, -10, null, 5], 它可以表示下面这个高度平衡二叉搜索树：

          0
         / \
       -3   9
       /   /
     -10  5

"""
class ListNode:   # 节点类
    def __init__(self, val = 0, next = None):  # 初始化节点
        self.val = val     # val存放数据元素
        self.next = next   # 保存当前节点中下一个节点的引用
        
    def __str__(self):
        return str(self.val)

def listToLinkedList(list):
    head = ListNode(list[0])
    cur = head
    for i in range(1, len(list)):
        cur.next = ListNode(list[i])
        cur = cur.next
    return head

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.val)

def printBFS(root):
    res = []         
    if root is None:
        return
    else:
        queue = [root] # 每次输出一行，所用数据结构为队列
        while queue:
            currentNode = queue.pop(0)   # 弹出元素
            res.append(currentNode.val)  # 打印元素值
            if currentNode.left:
                queue.append(currentNode.left)
            if currentNode.right:
                queue.append(currentNode.right)
    return res


""" 解法: 快慢指针找中点 """
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head:
            return head
        pre, slow, fast = None, head, head

        while fast and fast.next:
            fast = fast.next.next
            pre = slow
            slow = slow.next
        if pre:
            pre.next = None
        node = TreeNode(slow.val)
        if slow == fast:
            return node
        node.left = self.sortedListToBST(head)
        node.right = self.sortedListToBST(slow.next)
        return node


""" 解法: 快慢指针找中点 """
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        def findmid(head, tail):
            slow = head
            fast = head     # 初始时，快指针 fast 和慢指针 slow 均指向链表的左端点 left。
            while fast != tail and fast.next!= tail :   # 终止条件：快指针到达边界（即快指针到达右端点或快指针的下一个节点是右端点）
                fast = fast.next.next   # 将快指针 fast 向右移动两次的同时
                slow = slow.next        # 将慢指针 slow 向右移动一次
            return slow
        
        def buildTree(head, tail):  # 递归构造二叉搜索树
            if head == tail:    # 递归终止条件
                return
            node = findmid(head, tail)  # 找出了中位数节点之后，将其作为当前根节点的元素
            root = TreeNode(node.val)
            root.left = buildTree(head, node)       # 根节点左侧部分的链表对应的左子树
            root.right = buildTree(node.next, tail) # 根节点右侧部分的链表对应的右子树
            return root
            
        return buildTree(head, None)


if __name__ == "__main__":
    head = listToLinkedList([-10, -3, 0, 5, 9])
    sol = Solution()
    result = sol.sortedListToBST(head)
    print (printBFS(result))