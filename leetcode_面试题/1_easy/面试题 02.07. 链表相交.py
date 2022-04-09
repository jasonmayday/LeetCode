'''
https://leetcode-cn.com/problems/intersection-of-two-linked-lists-lcci/

给你两个单链表的头节点 headA 和 headB ，请你找出并返回两个单链表相交的起始节点。如果两个链表没有交点，返回 null 。

图示两个链表在节点 c1 开始相交：

A:        |a1| → |a2|
                     ↘
                      |c1| → |c2| → |c3|
                     ↗
B: |b1| → |b2| → |b3|

题目数据 保证 整个链式结构中不存在环。

注意，函数返回结果后，链表必须 保持其原始结构 。

示例 1：
https://assets.leetcode.com/uploads/2018/12/13/160_example_1.png
    输入：intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2, skipB = 3
    输出：Intersected at '8'
    解释：相交节点的值为 8 （注意，如果两个链表相交则不能为 0）。
    从各自的表头开始算起，链表 A 为 [4,1,8,4,5]，链表 B 为 [5,0,1,8,4,5]。
    在 A 中，相交节点前有 2 个节点；在 B 中，相交节点前有 3 个节点。

示例 2：
https://assets.leetcode.com/uploads/2018/12/13/160_example_2.png
    输入：intersectVal = 2, listA = [0,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
    输出：Intersected at '2'
    解释：相交节点的值为 2 （注意，如果两个链表相交则不能为 0）。
    从各自的表头开始算起，链表 A 为 [0,9,1,2,4]，链表 B 为 [3,2,4]。
    在 A 中，相交节点前有 3 个节点；在 B 中，相交节点前有 1 个节点。

示例 3：
https://assets.leetcode.com/uploads/2018/12/13/160_example_3.png
    输入：intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
    输出：null
    解释：从各自的表头开始算起，链表 A 为 [2,6,4]，链表 B 为 [1,5]。
    由于这两个链表不相交，所以 intersectVal 必须为 0，而 skipA 和 skipB 可以是任意值。
    这两个链表不相交，因此返回 null 。
 
提示：
    listA 中节点数目为 m
    listB 中节点数目为 n
    0 <= m, n <= 3 * 10^4
    1 <= Node.val <= 10^5
    0 <= skipA <= m
    0 <= skipB <= n
    如果 listA 和 listB 没有交点，intersectVal 为 0
    如果 listA 和 listB 有交点，intersectVal == listA[skipA + 1] == listB[skipB + 1]

本题与主站 160 题相同：https://leetcode-cn.com/problems/intersection-of-two-linked-lists/

'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def create_linked_list(arr):
    head = ListNode(arr[0])
    cur = head
    for i in range(1, len(arr)):
        cur.next = ListNode(arr[i])
        cur = cur.next
    return head

def print_linked_list(head):
    cur = head
    res = []
    while cur:
        res.append(cur.val)
        cur = cur.next
    return res

""" 解法1：双指针
    A和B两个链表长度可能不同，但是A+B和B+A的长度是相同的，所以遍历A+B和遍历B+A一定是同时结束。 
    如果A,B相交的话A和B有一段尾巴是相同的，所以两个遍历的指针一定会同时到达交点 如果A,B不相交的话两个指针就会同时到达A+B（B+A）的尾节点
"""
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        cur1 = headA  # cur1指向链表A的头结点
        cur2 = headB  # cur2指向链表B的头结点
        # 让 cur1, cur2 指针都走一遍 headA, headB 两个链表, cur1, cur2 相遇的地方就是两个链表相交的地方.
        while cur1 != cur2:
            if cur1:
                cur1 = cur1.next   # cur1 指向 headA, 一步一步往 next 走, 走到结尾 null 时, 跳到 headB 继续往后遍历
            else:
                cur1 = headB       # 当 curr1 到达链表的尾部时，将它重定位到链表 B 的头结点

            if cur2:
                cur2 = cur2.next   # cur2 指向 headB, 一步一步往 next 走, 走到结尾 null 时, 跳到 headA 继续往后遍历
            else:
                cur2 = headA       # 当 curr2 到达链表的尾部时，将它重定位到链表 A 的头结点。

        return cur1

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        A, B = headA, headB
        while A != B:
            A = A.next if A else headB
            B = B.next if B else headA
        return A

if __name__ == "__main__":
    a = [4,1,8,4,5]
    b = [5,0,1,8,4,5]
    head_a = create_linked_list(a)
    head_b = create_linked_list(b)
    head_a.next.next = head_b.next.next.next   # skipA = 2, skipB = 3，在 '8' 处相交
    sol = Solution()
    result = sol.getIntersectionNode(head_a, head_b)
    print (print_linked_list(result))
