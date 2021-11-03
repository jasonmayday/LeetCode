'''
https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list/

存在一个按升序排列的链表，给你这个链表的头节点 head ，请你删除所有重复的元素，使每个元素 只出现一次 。

返回同样按升序排列的结果链表。

示例 1：
1 → 1 → 2
    ⇩ 
  1 → 2
输入：head = [1,1,2]
输出：[1,2]

示例 2：
1 → 1 → 2 → 3 → 3
        ⇩ 
    1 → 2 → 3
输入：head = [1,1,2,3,3]
输出：[1,2,3]

提示：
链表中节点数目在范围 [0, 300] 内
-100 <= Node.val <= 100
题目数据保证链表已经按升序排列

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
    def deleteDuplicates(self, head) -> ListNode:
        # 解法一：递归
        if not head or not head.next: return head
        head.next=self.deleteDuplicates(head.next)
        if head.val==head.next.val:
            head.next = head.next.next
        return head

class Solution:
    def deleteDuplicates(self, head) -> ListNode:        
        # 解法二：遍历
        dummy = ListNode(next=head)
        while head:
            while head.next and head.val==head.next.val:
                head.next = head.next.next
            head = head.next
        return dummy.next

if __name__ == "__main__":
    head = create_linked_list([1, 1, 2, 3, 3])
    sol = Solution()
    result = sol.deleteDuplicates(head)
    print(print_linked_list(result))


