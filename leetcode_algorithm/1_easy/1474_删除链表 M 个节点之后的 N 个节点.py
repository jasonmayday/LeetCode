"""
https://leetcode-cn.com/problems/delete-n-nodes-after-m-nodes-of-a-linked-list/

给定链表 head 和两个整数 m 和 n. 遍历该链表并按照如下方式删除节点:

    开始时以头节点作为当前节点.
    保留以当前节点开始的前 m 个节点.
    删除接下来的 n 个节点.
    重复步骤 2 和 3, 直到到达链表结尾.

在删除了指定结点之后, 返回修改过后的链表的头节点.

示例 1:
    输入: head = [1,2,3,4,5,6,7,8,9,10,11,12,13], m = 2, n = 3
    输出: [1,2,6,7,11,12]
    解析: 保留前(m = 2)个结点,  也就是以黑色节点表示的从链表头结点开始的结点(1 ->2).
        删除接下来的(n = 3)个结点(3 -> 4 -> 5), 在图中以红色结点表示.
        继续相同的操作, 直到链表的末尾.
        返回删除结点之后的链表的头结点.

示例 2:
    输入: head = [1,2,3,4,5,6,7,8,9,10,11], m = 1, n = 3
    输出: [1,5,9]
    解析: 返回删除结点之后的链表的头结点.

示例 3:
    输入: head = [1,2,3,4,5,6,7,8,9,10,11], m = 3, n = 1
    输出: [1,2,3,5,6,7,9,10,11]

示例 4:
    输入: head = [9,3,7,7,9,10,8,2], m = 1, n = 2
    输出: [9,7,8]

提示:
    链表中节点数目在范围 [1, 10^4] 内
    1 <= Node.val <= 10^6
    1 <= m, n <= 1000

进阶: 你能通过 就地 修改链表的方式解决这个问题吗?

"""

class ListNode:   # 节点类
    def __init__(self, val = 0, next = None):  # 初始化节点
        self.val = val     # val存放数据元素
        self.next = next   # 保存当前节点中下一个节点的引用

def listToLinkedList(list):
    head = ListNode(list[0])
    cur = head
    for i in range(1, len(list)):
        cur.next = ListNode(list[i])
        cur = cur.next
    return head

def printLinkedList(head):
    cur = head
    list = []
    while cur:
        list.append(cur.val)
        cur = cur.next
    return list


""" 解法1：递归 """
class Solution:
    def deleteNodes(self, head: ListNode, m: int, n: int) -> ListNode:
        if not head:
            return None
        a = b = head
        keep = m
        remo = n
        while (keep-1) and a.next:     # 条件：
            a, b = a.next, b.next
            keep -= 1
        while remo and b.next:
            b = b.next
            remo -= 1
        a.next = self.deleteNodes(b.next, m, n)
        return head

""" 迭代 """
class Solution:
    def deleteNodes(self, head: ListNode, m: int, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        cur = dummy
        while cur.next:
            p = m
            q = n
            while p > 0 and cur.next:
                p -= 1
                cur = cur.next
            while q > 0 and cur.next:
                q -= 1
                cur.next = cur.next.next   # 直接改变cur的后继结点。
        return dummy.next


if __name__ == "__main__":
    head = listToLinkedList([1,2,3,4,5,6,7,8,9,10,11,12,13])
    m = 2                 # [1,2,      6,7,       11,12]
    n = 3
    sol = Solution()
    result = sol.deleteNodes(head, m, n)
    print(printLinkedList(result))