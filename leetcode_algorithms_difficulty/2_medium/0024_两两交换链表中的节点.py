"""
https://leetcode-cn.com/problems/swap-nodes-in-pairs/

给你一个链表，两两交换其中相邻的节点，并返回交换后链表的头节点。你必须在不修改节点内部的值的情况下完成本题（即，只能进行节点交换）。

示例 1：
    输入：head = [1,2,3,4]
    输出：[2,1,4,3]

示例 2：
    输入：head = []
    输出：[]

示例 3：
    输入：head = [1]
    输出：[1]

提示：
    链表中节点的数目在范围 [0, 100] 内
    0 <= Node.val <= 100

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


"""方法一：递归"""
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        newHead = head.next
        head.next = self.swapPairs(newHead.next)
        newHead.next = head
        return newHead

if __name__ == "__main__":
    head = listToLinkedList([1,2,3,4])
    sol = Solution()
    result = sol.swapPairs(head)
    print (printLinkedList(result))