"""
https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list/

给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。

示例 1：
    输入：head = [1,2,3,4,5], n = 2
    输出：[1,2,3,5]

示例 2：
    输入：head = [1], n = 1
    输出：[]

示例 3：
    输入：head = [1,2], n = 1
    输出：[1]

提示：
    链表中结点的数目为 sz
    1 <= sz <= 30
    0 <= Node.val <= 100
    1 <= n <= sz

进阶：你能尝试使用一趟扫描实现吗？

"""
class ListNode:   # 节点类
    def __init__(self, val = 0, next = None):  # 初始化节点
        self.val = val     # val存放数据元素
        self.next = next   # 保存当前节点中下一个节点的引用
        # 每个节点包含两个部分，一部分存放数据变量的val，另一部分存放下一个节点的位置信息next。
    
    def __str__(self):
        #测试基本功能，输出字符串
        return str(self.val)

'''根据输入的列表创建链表'''
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

"""方法一：计算链表长度"""
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        def getLength(head: ListNode) -> int:   # 从头节点开始对链表进行一次遍历，得到链表的长度
            length = 0
            while head:
                length += 1
                head = head.next
            return length
        
        dummy = ListNode(0, head)
        length = getLength(head)
        cur = dummy
        for i in range(1, length - n + 1):  # 从哑节点开始遍历 L−n+1 个节点
            cur = cur.next                  # 当遍历到第 L-n+1 个节点时，它的下一个节点就是我们需要删除的节点，
        cur.next = cur.next.next            # 把要删除的节点空过去：cur 直接指向 cur.next.next
        return dummy.next

"""方法二：栈"""
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0, head)
        stack = list()
        cur = dummy
        while cur:
            stack.append(cur)   # 遍历链表的同时将所有节点依次入栈
            cur = cur.next
        
        for i in range(n):      # 弹出栈的第 n 个节点就是需要删除的节点
            stack.pop()         # 并且目前栈顶的节点就是待删除节点的前驱节点

        prev = stack[-1]        # prev为弹出删除元素后的栈顶
        prev.next = prev.next.next  # 指向跳过原来删除的节点
        return dummy.next

"""方法三：双指针"""
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0, head)
        first = head    # 使用两个指针 first 和 second 同时对链表进行遍历，初始时 first 和 second 均指向头节点
        second = dummy
        for i in range(n):
            first = first.next

        while first:
            first = first.next
            second = second.next
        
        second.next = second.next.next
        return dummy.next


if __name__ == "__main__":
    head = listToLinkedList ([1,2,3,4,5])
    n = 2
    sol = Solution()
    result = sol.removeNthFromEnd(head, n)
    print (printLinkedList(result))