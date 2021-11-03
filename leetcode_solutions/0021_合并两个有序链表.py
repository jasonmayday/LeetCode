'''
https://leetcode-cn.com/problems/merge-two-sorted-lists/

将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

示例 1：
输入：l1 = [1,2,4], l2 = [1,3,4]
https://assets.leetcode.com/uploads/2020/10/03/merge_ex1.jpg
1 → 2 → 4
1 → 3 → 4
1 → 1 → 2 → 3 → 4 → 4
输出：[1,1,2,3,4,4]

示例 2：
输入：l1 = [], l2 = []
输出：[]

示例 3：
输入：l1 = [], l2 = [0]
输出：[0]

提示：
两个链表的节点数目范围是 [0, 50]
-100 <= Node.val <= 100
l1 和 l2 均按 非递减顺序 排列

'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 将传入的数组转化为链表
def create_linked_list(arr):
    head = ListNode(arr[0])
    cur = head
    for i in range(1, len(arr)):
        cur.next = ListNode(arr[i])
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

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1: return l2  # 终止条件，直到两个链表都空
        if not l2: return l1
        if l1.val <= l2.val:  # 递归调用
            l1.next = self.mergeTwoLists(l1.next,l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1,l2.next)
            return l2

if __name__ == "__main__":
    head1 = create_linked_list([1, 2, 4])
    head2 = create_linked_list([1, 3, 4])
    solution = Solution()
    sorted_lists = solution.mergeTwoLists(head1, head2)
    print(print_linked_list(sorted_lists))

