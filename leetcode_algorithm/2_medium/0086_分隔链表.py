"""
https://leetcode-cn.com/problems/partition-list/

给你一个链表的头节点 head 和一个特定值 x ，请你对链表进行分隔，使得所有 小于 x 的节点都出现在 大于或等于 x 的节点之前。

你应当 保留 两个分区中每个节点的初始相对位置。

示例 1：
    输入：head = [1,4,3,2,5,2], x = 3
    输出：[1,2,2,4,3,5]
    
    1 → 4 → 3 → 2 → 5 → 2
            ↓
              → → → 
                    ↓
    1 → 2 → 2 → 4 → 3 → 5

示例 2：
    输入：head = [2,1], x = 2
    输出：[1,2]
 
提示：
    链表中节点的数目在范围 [0, 200] 内
    -100 <= Node.val <= 100
    -200 <= x <= 200

"""

'''单链表的结点'''
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

# 传入链表头节点，以数组形式返回
def printLinkedList(head):
    cur = head
    list = []
    while cur:
        list.append(cur.val)
        cur = cur.next
    return list

""" 解法：用两个链表,一个链表放小于x的节点,一个链表放大于等于x的节点
    最后,拼接这两个链表."""

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        dummy1 = ListNode()
        dummy2 = ListNode()
        p1 = dummy1     # 一个链表放小于x的节点
        p2 = dummy2     # 一个链表放大于等于x的节点
        while head:             # 条件：如果还有数字，[1,4,3,2,5,2]
            if head.val < x:    # 如果小于 x
                p1.next = head  # 把数字放到 p1
                p1 = p1.next
            else:               # 如果大于 x
                p2.next = head  # 把数字放到 p2
                p2 = p2.next
            head = head.next    # 继续判断下一个数字，直到没有 head
        print(printLinkedList(dummy1.next))     # [1, 2, 2]
        print(printLinkedList(dummy2.next))     # [4, 3, 5, 2]
        p1.next = dummy2.next   # 
        p2.next = None          # 链表的最后都需要指向None，代表链表的结束。
        return dummy1.next

if __name__ == "__main__":
    head = listToLinkedList ([1,4,3,2,5,2])
    x = 3
    sol = Solution()
    result = sol.partition(head, x)     # [1, 2, 2, 4, 3, 5]
    print(printLinkedList(result))