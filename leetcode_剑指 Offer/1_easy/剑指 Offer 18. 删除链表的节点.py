"""
https://leetcode-cn.com/problems/shan-chu-lian-biao-de-jie-dian-lcof/

给定单向链表的头指针和一个要删除的节点的值，定义一个函数删除该节点。

返回删除后的链表的头节点。

注意：此题对比原题有改动

示例 1:
    输入: head = [4,5,1,9], val = 5
    输出: [4,1,9]
    解释: 给定你链表中值为 5 的第二个节点，那么在调用了你的函数之后，该链表应变为 4 -> 1 -> 9.

示例 2:
    输入: head = [4,5,1,9], val = 1
    输出: [4,5,9]
    解释: 给定你链表中值为 1 的第三个节点，那么在调用了你的函数之后，该链表应变为 4 -> 5 -> 9.

说明：
    题目保证链表中节点的值互不相同
    若使用 C 或 C++ 语言，你不需要 free 或 delete 被删除的节点

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

"""迭代法"""
class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        if head.val == val:     # 当应删除头节点 head 时
            return head.next    # 直接返回之后的 head.next 即可。
        pre = head          # 初始化
        cur = head.next
        while cur and cur.val != val:   # 定位节点： 当还有节点，且节点不等于目标值时，继续遍历
            pre = cur       # 保存当前节点索引，即 pre = cur 。
            cur = cur.next  # 遍历下一节点，即 cur = cur.next 。
        if cur:                     # 删除节点： 若 cur 指向某节点，
            pre.next = cur.next     # 修改节点指向：执行 pre.next = cur.next，跳过目标节点
        return head     # 返回值： 返回链表头部节点 head 即可。

if __name__ == "__main__":
    head = [4,5,1,9]
    val = 5

    sol = Solution()
    NewLinkedList = sol.deleteNode(head, val)
    print (print_linked_list(NewLinkedList))