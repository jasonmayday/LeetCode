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


'''定义节点'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class SingleLinkedList():
    def __init__(self):   # 初始化链表
        self.head = None  # 先初始化一个头节点为空
    
    def add_first(self, val):
        node = ListNode(val)    # 创建一个新节点
        node.next = self.head   # 新节点指针指向原头部节点
        self.head = node        # 头部节点指针修改为新节点


head = SingleLinkedList()
head.add_first(3)
head.add_first(3)
head.add_first(2)
head.add_first(1)
head.add_first(1)

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

sol = Solution()
result = sol.deleteDuplicates(head)
print (result)
