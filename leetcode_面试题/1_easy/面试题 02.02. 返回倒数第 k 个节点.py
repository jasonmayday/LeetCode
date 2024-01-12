"""
https://leetcode-cn.com/problems/kth-node-from-end-of-list-lcci/

实现一种算法，找出单向链表中倒数第 k 个节点。返回该节点的值。

注意：本题相对原题稍作改动

示例：
    输入： 1->2->3->4->5 和 k = 2
    输出： 4

说明：
    给定的 k 保证是有效的。

"""

""" 单链表的结点"""
class ListNode:   # 节点类
    def __init__(self, val = 0, next = None):  # 初始化节点
        self.val = val     # val存放数据元素
        self.next = next   # 保存当前节点中下一个节点的引用

    def __str__(self):
        return str(self.val)

''' 根据输入的列表创建链表 '''
def listToLinkedList(list):
    head = ListNode(list[0])
    cur = head
    for i in range(1, len(list)):
        cur.next = ListNode(list[i])
        cur = cur.next
    return head

""" 快慢指针 """
class Solution:
    def kthToLast(self, head: ListNode, k: int) -> int:
        fast = head     # 初始化双指针都指向头节点 head
        slow = head
        while k > 0:
            fast = fast.next    # fast 先走
            k -= 1              # 每走一步 k 减一，直到 k = 1
        while fast != None:
            fast = fast.next    # fast 走到尽头
            slow = slow.next    # 因为之前 fast 走过，所以slow 比 fast 少走 k-1 步
        return slow.val         # slow 最后在的位置就是倒数第 k 个

if __name__ == "__main__":
    head = listToLinkedList([1, 2, 3, 4, 5])
    k = 2
    sol = Solution()
    result = sol.kthToLast(head, k)
    print(result)