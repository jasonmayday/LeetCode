"""
https://leetcode-cn.com/problems/lian-biao-zhong-dao-shu-di-kge-jie-dian-lcof/

输入一个链表，输出该链表中倒数第k个节点。为了符合大多数人的习惯，本题从1开始计数，即链表的尾节点是倒数第1个节点。

例如，一个链表有 6 个节点，从头节点开始，它们的值依次是 1、2、3、4、5、6。这个链表的倒数第 3 个节点是值为 4 的节点。

示例：
    给定一个链表: 1->2->3->4->5, 和 k = 2.

    返回链表 4->5.

"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

""" 快慢指针
    我们将第一个指针 fast 指向链表的第 k+1 个节点，第二个指针 slow 指向链表的第一个节点，此时指针 fast 与 slow 二者之间刚好间隔 k 个节点。
    此时两个指针同步向后走，当第一个指针 fast 走到链表的尾部空节点时，则此时 slow 指针刚好指向链表的倒数k个节点。
"""

class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        fast = head
        slow = head
        while fast and k > 0:
            fast = fast.next    # 先将 fast 指向链表的头节点，然后向后走 k 步，则此时 fast 指针刚好指向链表的第 k+1 个节点。
            k = k - 1           # 剩下的步数，走一步少一步
        while fast:
            fast = fast.next
            slow = slow.next
        return slow

