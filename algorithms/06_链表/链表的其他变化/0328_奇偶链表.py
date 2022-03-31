"""
https://leetcode-cn.com/problems/odd-even-linked-list/

给定单链表的头节点 head ，将所有索引为奇数的节点和索引为偶数的节点分别组合在一起，然后返回重新排序的列表。

第一个节点的索引被认为是 奇数 ， 第二个节点的索引为 偶数 ，以此类推。

请注意，偶数组和奇数组内部的相对顺序应该与输入时保持一致。

你必须在 O(1) 的额外空间复杂度和 O(n) 的时间复杂度下解决这个问题。

示例 1:
    输入: head = [1,2,3,4,5]
    输出: [1,3,5,2,4]

示例 2:
    输入: head = [2,1,3,5,6,4,7]
    输出: [2,3,6,7,1,5,4]

提示:
    n ==  链表中的节点数
    0 <= n <= 10^4
    -10^6 <= Node.val <= 10^6

"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
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

""" 分段双指针 """
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        evenHead = head.next    # head 的后一个节点是偶数链表的头节点。
        odd  = head             # 原始链表的头节点 head 也是奇数链表的头节点以及结果链表的头节点
        even = evenHead         # evenHead 是偶数链表的头节点。
        while even and even.next:   # 维护两个指针 odd 和 even 分别指向奇数节点和偶数节点. 先更新奇数节点, 然后更新偶数节点。
            odd.next = even.next    # 更新奇数节点时，奇数节点的后一个节点需要指向偶数节点的后一个节点
            odd = odd.next          # 然后令 odd = odd.next, 此时 odd 变成 even 的后一个节点。
            even.next = odd.next    # 更新偶数节点时，偶数节点的后一个节点需要指向奇数节点的后一个节点，
            even = even.next        # 然后令 even = even.next，此时 even 变成 odd 的后一个节点。
        odd.next = evenHead     # 最后将偶数链表连接在奇数链表之后
        return head

if __name__ == "__main__":
    head = listToLinkedList([1,2,3,4,5])
    sol = Solution()
    result = sol.oddEvenList(head)
    print (printLinkedList(result))