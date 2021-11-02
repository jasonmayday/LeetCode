class ListNode:
    def __init__(self, val = 0, next=None):
        self.val = val     # 保存当前节点的值
        self.next = next   # 保存当前节点中下一个节点的引用

l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(4)

l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)
print(l1)