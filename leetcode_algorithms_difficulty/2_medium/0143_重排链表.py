"""
https://leetcode-cn.com/problems/reorder-list/

给定一个单链表 L 的头节点 head ，单链表 L 表示为：
L0 → L1 → … → Ln - 1 → Ln

请将其重新排列后变为：
L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …

不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

示例 1：
    输入：head = [1,2,3,4]
    输出：[1,4,2,3]

示例 2：
    输入：head = [1,2,3,4,5]
    输出：[1,5,2,4,3]

提示：
    链表的长度范围为 [1, 5 * 10^4]
    1 <= node.val <= 1000

"""
class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
    
    def __str__(self):
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

""" 方法1: 寻找链表中点 + 链表逆序 + 合并链表
    目标链表即为将原链表的左半端和反转后的右半端合并后的结果 """
class Solution:
    def reorderList(self, head: ListNode) -> None:
        if not head:
            return
        mid = self.middleNode(head)
        l1 = head       # 左半边
        l2 = mid.next   # 右半边
        mid.next = None # 最后一个节点的next不指向None的话，它的next就保留了原来的值，这样链表就形成环了
        l2 = self.reverseList(l2)
        self.mergeList(l1, l2)
        return l1
    
    ''' 找到原链表的中点，快慢指针'''    
    def middleNode(self, head: ListNode) -> ListNode:
        slow = fast = head  # 快慢指针均从头节点出发
        while fast.next and fast.next.next:
            slow = slow.next        # slow 一次走一步，fast 一次走两步。
            fast = fast.next.next   # 那么当 fast 到达链表的末尾时，slow 必然位于中间
        return slow
    
    ''' 将原链表的右半端反转(迭代法)'''
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head
        while curr:
            nextTemp = curr.next
            curr.next = prev
            prev = curr
            curr = nextTemp
        return prev
    
    ''' 将原链表的两端合并(交叉合并)''' 
    def mergeList(self, l1: ListNode, l2: ListNode):
        while l1 and l2:        # l1 = [1,2], l2 = [4,3]
            l1_tmp = l1.next
            l2_tmp = l2.next

            l1.next = l2
            l1 = l1_tmp

            l2.next = l1
            l2 = l2_tmp


""" 方法2: 栈 """
class Solution(object):
    def reorderList(self, head: ListNode) -> None:
        if not head:
            return None
        p = head
        stack = []
        while p:
            stack.append(p) # 把所有节点压入栈中
            p = p.next
        n = len(stack)
        count = (n - 1) // 2    # 找到中点前一个位置 
        p = head
        while count:
            tmp = stack.pop()   # 弹出栈顶
            tmp.next = p.next   # 与链头拼接
            p.next  = tmp
            p = tmp.next        # 移动一个位置
            count -= 1
        stack.pop().next = None
        
        return head


if __name__ == "__main__":
    head = listToLinkedList([1,2,3,4])
    sol = Solution()
    result = sol.reorderList(head)
    print (printLinkedList(result))