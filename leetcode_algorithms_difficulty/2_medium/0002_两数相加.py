"""
给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。

请你将两个数相加，并以相同形式返回一个表示和的链表。

你可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例 1：
    输入：l1 = [2,4,3], l2 = [5,6,4]
    输出：[7,0,8]
    解释：342 + 465 = 807.

示例 2：
    输入：l1 = [0], l2 = [0]
    输出：[0]

示例 3：
    输入：l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
    输出：[8,9,9,9,0,0,0,1]

提示：
    每个链表中的节点数在范围 [1, 100] 内
    0 <= Node.val <= 9
    题目数据保证列表表示的数字不含前导零

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

"""解法1"""
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(l1.val + l2.val)    # 先将l1和l2头节点的值加起来赋值给新链表的头节点
        cur = head                          # 从头部开始遍历
        while l1.next or l2.next:           # 遍历两个链表，只要有一个链表还没有遍历到末尾，就继续遍历
            l1 = l1.next if l1.next else ListNode()
            l2 = l2.next if l2.next else ListNode()
            cur.next = ListNode(l1.val + l2.val + cur.val // 10)    # 每次遍历生成一个当前节点cur的下一个节点，其值为两链表对应节点的和再加上当前节点cur产生的进位
            cur.val = cur.val % 10
            cur = cur.next      # 更新进位后的当前节点cur的值
        if cur.val >= 10:       # 循环结束后，因为首位可能产生进位
            cur.next = ListNode(cur.val // 10)  # 因此如果cur.val是两位数的话，新增一个节点
            cur.val = cur.val % 10
        return head             # 返回头节点

"""解法2"""
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = p = ListNode(None)          # 创建一个结点值为 None 的头结点, dummy 和 p 指向头结点, dummy 用来最后返回, p 用来遍历
        s = 0                               # 初始化进位 s 为 0
        while l1 or l2 or s:                # 循环条件：l1 或者l2（没有遍历完成），s(进位)不为0
            # 如果 l1 或 l2 存在, 则取l1的值 + l2的值 + s(s初始为0, 如果下面有进位1, 下次加上)
            s += (l1.val if l1 else 0) + (l2.val if l2 else 0)  
            p.next = ListNode(s % 10)       # p.next 指向新链表, 用来创建一个新的链表
            p = p.next                      # p 向后遍历
            s //= 10                        # 有进位情况则取模, eg. s = 18, 18 // 10 = 1
            l1 = l1.next if l1 else None    # 如果l1存在, 则向后遍历, 否则为 None
            l2 = l2.next if l2 else None    # 如果l2存在, 则向后遍历, 否则为 None
        return dummy.next   # 返回 dummy 的下一个节点, 因为 dummy 指向的是空的头结点, 下一个节点才是新建链表的后序节点


if __name__ == "__main__":
    l1 = listToLinkedList ([2,4,3])
    l2 = listToLinkedList ([5,6,4])
    sol = Solution()
    result = sol.addTwoNumbers(l1, l2)
    print (printLinkedList(result))