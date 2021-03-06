"""
https://leetcode-cn.com/problems/he-bing-liang-ge-pai-xu-de-lian-biao-lcof/

输入两个递增排序的链表，合并这两个链表并使新链表中的节点仍然是递增排序的。

示例1：
    输入：1->2->4, 1->3->4
    输出：1->1->2->3->4->4

限制：
    0 <= 链表长度 <= 1000

注意：本题与主站 21 题相同：https://leetcode-cn.com/problems/merge-two-sorted-lists/

"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 将传入的数组转化为链表
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
    res = []
    while cur:
        res.append(cur.val)
        cur = cur.next
    return res

""" 解法1：递归 """
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:     # 如果 l1 或者 l2 一开始就是空链表，那么没有任何操作需要合并，所以我们只需要返回非空链表。
            return l2
        elif l2 is None:
            return l1
        elif l1.val < l2.val:  # 判断 l1 和 l2 哪一个链表的头节点的值更小
            l1.next = self.mergeTwoLists(l1.next, l2)  # 递归地决定下一个添加到结果里的节点。# 如果两个链表有一个为空，递归结束。
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2

""" 解法2：迭代 """
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        prehead = ListNode(-1)    # 设定一个哨兵节点 prehead ，这可以在最后让我们比较容易地返回合并后的链表。
        prev = prehead            # 维护一个 prev 指针，我们需要做的是调整它的 next 指针。
        
        while l1 and l2:
            if l1.val <= l2.val:  # 如果 l1 当前节点的值小于等于 l2：
                prev.next = l1    # 就把 l1 当前的节点接在 prev 节点的后面
                l1 = l1.next      # 同时将 l1 指针往后移一位。
            
            else:                 # 如果 l1 当前节点的值大于 l2：
                prev.next = l2    # 就把 l2 当前的节点接在 prev 节点的后面
                l2 = l2.next      # 同时将 l2 指针往后移一位。
            
            prev = prev.next      # 不管我们将哪一个元素接在了后面，我们都需要把 prev 向后移一位。

        # 合并后 l1 和 l2 最多只有一个还未被合并完，我们直接将链表末尾指向未合并完的链表即可
        prev.next = l1 if l1 is not None else l2

        return prehead.next     # 合并链表在伪头节点 prehead 之后，因此返回 prehead.next 即可。

if __name__ == "__main__":
    l1 = create_linked_list([1, 2, 4])
    l2 = create_linked_list([2, 3, 4])
    sol = Solution()
    sorted_lists = sol.mergeTwoLists(l1, l2)
    print(print_linked_list(sorted_lists))
