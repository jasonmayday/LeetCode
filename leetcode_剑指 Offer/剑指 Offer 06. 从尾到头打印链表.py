"""
输入一个链表的头节点，从尾到头反过来返回每个节点的值（用数组返回）。

示例 1：
    输入：head = [1,3,2]
    输出：[2,3,1]

限制：
    0 <= 链表长度 <= 10000

"""
from typing import List

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        
def listToLinkedList(list):
    head = ListNode(list[0])
    cur = head
    for i in range(1, len(list)):
        cur.next = ListNode(list[i])
        cur = cur.next
    return head

""" 方法一：递归法"""
class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        while head:
            return self.reversePrint(head.next) + [head.val]
        return []   # 则返回空列表；


""" 方法二：辅助栈法"""
class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        stack = []
        while head:
            stack.append(head.val)  # 把节点的数字逐个加入栈
            head = head.next
        return stack[::-1]


if __name__ == "__main__":
    head = listToLinkedList([1,3,2])
    sol = Solution()
    result = sol.reversePrint(head)
    print (result)