"""
https://leetcode-cn.com/problems/sort-list/

给你链表的头结点 head ，请将其按 升序 排列并返回 排序后的链表 。

示例 1：
    输入：head = [4,2,1,3]
    输出：[1,2,3,4]

示例 2：
    输入：head = [-1,5,3,4,0]
    输出：[-1,0,3,4,5]

示例 3：
    输入：head = []
    输出：[]

提示：
    链表中节点的数目在范围 [0, 5 * 10^4] 内
    -10^5 <= Node.val <= 10^5

进阶：
    你可以在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序吗？

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

""" 归并排序（递归法） """
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:   # 递归结束条件
            return head
        
        slow = head         # 慢指针
        fast = head.next    # 快指针
        
        while fast and fast.next:   # 遍历到尽头
            slow = slow.next        # 每次慢指针走一步
            fast = fast.next.next   # 每次快指针走两步
            
        mid = slow.next     # 奇数个节点找到中点，偶数个节点找到中心左边的节点。
        slow.next = None    # 将链表切断。

        # 递归分割，直到每段只有两个元素
        left  = self.sortList(head) # 分割后的左半边递归
        right = self.sortList(mid)  # 分割后的右半边递归

        # 合并环节
        h = res = ListNode(0)   # 双指针法合并，建立辅助ListNode h 作为头部。
        while left and right:   # 设置两指针 left, right 分别指向两链表头部，比较两指针处节点值大小
            if left.val < right.val: 
                h.next = left
                left = left.next
            else:
                h.next = right
                right = right.next
                
            h = h.next  # 返回辅助ListNode h 作为头部的下个节点 h.next
            
        h.next = left if left else right
        return res.next


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        
        # 首先找到中间节点
        mid = self.middleNode(head) # middleNode函数中已经把中间节点和前面的节点分开了

        # 排序
        left = self.sortList(head)
        right = self.sortList(mid)

        # 合并有序链表
        return self.merge(left, right)

    # 寻找中间节点（使用快慢指针）
    def middleNode(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        dummyHead = ListNode(0)
        dummyHead.next = head
        pre = dummyHead
        slow = head
        fast = head
        while fast and fast.next:
            pre = slow
            slow = slow.next
            fast = fast.next.next
        
        pre.next = None   # 在这里把前半部分链表和后半部分链表断开
        return slow
        
    # 合并两个有序链表，这是剑指Offer25题
    def merge(self, l1, l2):
        if not l1:      # 奇数节点的链表会出现最后只有一个链表的情况
            return l2
        if not l2:
            return l1
        if l1.val <= l2.val:
            l1.next = self.merge(l1.next, l2)
            return l1
        else:
            l2.next = self.merge(l1, l2.next)
            return l2


""" 快速排序 """
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if head is None:
            return head

        # 分成三个链表，分别是比轴心数小，相等，大的数组成的链表
        big = None
        small = None
        equal = None
        cur = head
        while cur is not None:
            t = cur
            cur = cur.next
            if t.val < head.val:
                t.next = small
                small = t
            elif t.val > head.val:
                t.next = big
                big = t
            else:
                t.next = equal
                equal = t
        
        # 拆完各自排序即可，equal 无需排序
        big = self.sortList(big)
        small = self.sortList(small)

        ret = ListNode(None)
        cur = ret

        # 将三个链表组合成一起，这一步复杂度是 o(n)
        # 可以同时返回链表的头指针和尾指针加速链表的合并。
        for p in [small, equal, big]:
            while p is not None:
                cur.next = p
                p = p.next
                cur = cur.next
                cur.next = None
        return ret.next
            

if __name__ == "__main__":
    head = listToLinkedList([-1,5,3,4,0])
    sol = Solution()
    result = sol.sortList(head)
    print (printLinkedList(result))