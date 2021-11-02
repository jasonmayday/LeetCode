'''
https://leetcode-cn.com/problems/merge-two-sorted-lists/

将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

示例 1：
输入：l1 = [1,2,4], l2 = [1,3,4]
https://assets.leetcode.com/uploads/2020/10/03/merge_ex1.jpg
1 → 2 → 4
1 → 3 → 4
1 → 1 → 2 → 3 → 4 → 4
输出：[1,1,2,3,4,4]

示例 2：
输入：l1 = [], l2 = []
输出：[]

示例 3：
输入：l1 = [], l2 = [0]
输出：[0]

提示：
两个链表的节点数目范围是 [0, 50]
-100 <= Node.val <= 100
l1 和 l2 均按 非递减顺序 排列

'''
# Definition for singly-linked list.
class ListNode:   # 节点类
    def __init__(self, val = 0, next = None):  # 初始化节点
        self.val = val     # 保存当前节点的值
        self.next = next   # 保存当前节点中下一个节点的引用
        # 每个节点包含两个部分，一部分存放数据变量的data，另一部分存放下一个节点的位置信息next。

class Linkedlist(): # 链表类
    def __init__(self): # 初始化链表
        self.head = None  # 头节点
        self.length = 0   # 链表长度






l1 = [1,2,4]
l2 = [1,3,4]    

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(4)
node1.next = node2
node2.next = node3

# 递归
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2

sol = Solution()
result = sol.mergeTwoLists(l1, l2)
print(result)