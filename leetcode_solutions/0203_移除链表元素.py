"""
https://leetcode-cn.com/problems/remove-linked-list-elements/

给你一个链表的头节点 head 和一个整数 val ，请你删除链表中所有满足 Node.val == val 的节点，并返回 新的头节点 。

示例 1：
    输入：head = [1,2,6,3,4,5,6], val = 6
    输出：[1,2,3,4,5]

示例 2：
    输入：head = [], val = 1
    输出：[]

示例 3：
    输入：head = [7,7,7,7], val = 7
    输出：[]

提示：
    列表中的节点数目在范围 [0, 10^4] 内
    1 <= Node.val <= 50
    0 <= val <= 50

"""
class ListNode:   # 节点类
    def __init__(self, val = 0, next = None):  # 初始化节点
        self.val = val     # val存放数据元素
        self.next = next   # 保存当前节点中下一个节点的引用
        # 每个节点包含两个部分，一部分存放数据变量的val，另一部分存放下一个节点的位置信息next。
    
    def __str__(self):
        # 测试基本功能，输出字符串
        return str(self.val)

'''将传入的数组转化为链表'''
def create_linked_list(list):
    head = ListNode(list[0])
    cur = head
    for i in range(1, len(list)):
        cur.next = ListNode(list[i])
        cur = cur.next
    return head

# 传入链表头节点，以数组形式返回
def print_linked_list(head):
    cur = head
    list = []
    while cur:
        list.append(cur.val)
        cur = cur.next
    return list


"""递归法"""
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if head is None:
            return head
        # removeElement 方法会返回下一个 Node 节点
        head.next = self.removeElements(head.next, val) # 递归程序会先一路遍历来到节点尾部
        if head.val == val:
            next_node = head.next # 从后往前把val符合的节点进行删除
        else:
            next_node = head
        return next_node

"""迭代法"""
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode()  # 新增一个dummy节点, 方便遍历和最后返回结果
        dummy.next = head
        p = dummy
        while p is not None:                    # 向前探一个节点，检查是否等于val
            if p.next and p.next.val == val:    # 如果 val 相等
                p.next = p.next.next            # 跳过 p.next 节点
            else:
                p = p.next
        return dummy.next

if __name__ == "__main__":
    head = create_linked_list([1,2,6,3,4,5,6])
    val = 6

    sol = Solution()
    NewLinkedList = sol.removeElements(head, val)
    print (print_linked_list(NewLinkedList))