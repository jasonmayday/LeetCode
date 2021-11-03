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
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

head = [1,1,2,3,3]

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next: 
            return head
        cur = head                        # 指针 cur 指向链表的头节点
        while cur.next:                   # 随后开始对链表进行遍历
            if cur.val == cur.next.val:
                cur.next = cur.next.next
            else: cur = cur.next

        return head

sol = Solution()
result = sol.deleteDuplicates(head)
print (result)