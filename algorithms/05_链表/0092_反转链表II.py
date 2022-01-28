"""
https://leetcode-cn.com/problems/reverse-linked-list-ii/

给你单链表的头指针 head 和两个整数 left 和 right ，其中 left <= right 。请你反转从位置 left 到位置 right 的链表节点，返回 反转后的链表 。

示例 1：
    输入：head = [1,2,3,4,5], left = 2, right = 4
    输出：[1,4,3,2,5]

示例 2：
    输入：head = [5], left = 1, right = 1
    输出：[5]

提示：
    链表中节点数目为 n
    1 <= n <= 500
    -500 <= Node.val <= 500
    1 <= left <= right <= n

进阶： 你可以使用一趟扫描完成反转吗？

"""

class ListNode:   # 节点类
    def __init__(self, val = 0, next = None):  # 初始化节点
        self.val = val     # val存放数据元素
        self.next = next   # 保存当前节点中下一个节点的引用
        # 每个节点包含两个部分，一部分存放数据变量的val，另一部分存放下一个节点的位置信息next。
    
    def __str__(self):
        #测试基本功能，输出字符串
        return str(self.val)

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


"""" 穿针引线 """
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        '''反转一段链表的函数'''
        def reverse_linked_list(head: ListNode):    # 2 → 3 → 4 变成 4 → 3 → 3
            pre = None
            cur = head
            while cur:
                next = cur.next
                cur.next = pre
                pre = cur
                cur = next

        dummy = ListNode(0)     # 创建 dummy 节点 0
        dummy.next = head       # 把 dummy 节点添加到链表开头   0 → 1 → 2 → 3 → 4 → 5
        pre = dummy
        
        # 第 1 步：从虚拟头节点走 left - 1 步，来到 left 节点的前一个节点
        for _ in range(left - 1):
            pre = pre.next

        # 第 2 步：从 pre 再走 right - left + 1 步，来到 right 节点
        right_node = pre
        for _ in range(right - left + 1):
            right_node = right_node.next
        
        # 第 3 步：切断出一个子链表（截取链表）
        left_node = pre.next
        curr = right_node.next

        # 注意：切断链接
        pre.next = None
        right_node.next = None

        # 第 4 步：同第 206 题，反转链表的子区间
        reverse_linked_list(left_node)
        
        # 第 5 步：接回到原来的链表中
        pre.next = right_node
        left_node.next = curr
        return dummy.next


""" 一次遍历「穿针引线」反转链表（头插法）
    在需要反转的区间里，每遍历到一个节点，让这个新节点来到反转部分的起始位置 """
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        count = 1
        dummy = ListNode(0)     # 创建 dummy 节点 0
        dummy.next = head       # 把 dummy 节点添加到链表开头   0 → 1 → 2 → 3 → 4 → 5
        pre = dummy     # 指向 left 左边元素的指针 pre ，它表示未翻转的链表，需要把当前要翻转的链表结点放到 pre 之后。
        
        while pre.next and count < left:    # pre 找到第一个反转之位置的一个节点    [1]
            pre = pre.next
            count += 1
            
        cur = pre.next  # cur 指向当前要翻转的链表结点，也就是 pre 的下一个节点
        tail = cur      # tail 指向已经翻转的链表的结尾，用它来把已翻转的链表和剩余链表进行拼接。
        while cur and count <= right:
            nxt = cur.next      # nxt 指向 cur.next ，表示下一个要被翻转的链表结点。
            cur.next = pre.next
            pre.next = cur      # 把 [cur 节点] 和 [pre 之后一位的节点] 交换
            tail.next = nxt
            cur = nxt
            count += 1
        return dummy.next


if __name__ == "__main__":
    head = listToLinkedList([1,2,3,4,5])
    left = 2
    right = 4
    sol = Solution()
    result = sol.reverseBetween(head, left, right)
    print(printLinkedList(result))