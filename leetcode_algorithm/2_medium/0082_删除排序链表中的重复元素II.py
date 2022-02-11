"""
https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list-ii/

给定一个已排序的链表的头 head ， 删除原始链表中所有重复数字的节点，只留下不同的数字 。返回 已排序的链表 。

示例 1：
    输入：head = [1,2,3,3,4,4,5]
    输出：[1,2,5]

示例 2：
    输入：head = [1,1,1,2,3]
    输出：[2,3]

提示：
    链表中节点数目在范围 [0, 300] 内
    -100 <= Node.val <= 100
    题目数据保证链表已经按 升序 排列

"""

class ListNode:   # 节点类
    def __init__(self, val = 0, next = None):  # 初始化节点
        self.val = val     # val存放数据元素
        self.next = next   # 保存当前节点中下一个节点的引用
        # 每个节点包含两个部分，一部分存放数据变量的val，另一部分存放下一个节点的位置信息next。
    
    def __str__(self):
        #测试基本功能，输出字符串
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

""" 递归 """
class Solution:
    def deleteDuplicates(self, head, val = None) -> ListNode:
        if not head:
            return head
        # 情况 1（第一行）：和之前重复了
        # 情况 2（第二行）：和之后重复了
        if (val is not None and head.val == val) or \
           (head.next and head.val == head.next.val):
            return self.deleteDuplicates(head.next, head.val)
        head.next = self.deleteDuplicates(head.next, head.val)
        return head
    
""" 一次遍历
    由于给定的链表是排好序的，因此重复的元素在链表中出现的位置是连续的，
    因此我们只需要对链表进行一次遍历，就可以删除重复的元素。"""
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head
        dummy = ListNode(0, head)   # 由于链表的头节点可能会被删除，因此需要额外使用一个 dummy node 指向链表的头节点。
        cur = dummy                 # 指针 cur 指向链表的哑节点
        while cur.next and cur.next.next:               # 前提条件，接下来还有两个以上节点 
            if cur.next.val == cur.next.next.val:       # 如果当前 cur.next 与 cur.next.next 对应的元素相同
                x = cur.next.val                        # 记下这个元素值 xx
                while cur.next and cur.next.val == x:
                    cur.next = cur.next.next            # 不断将 cur.next 从链表中移除，直到 cur.next 为空节点或者其元素值不等于 x 为止
            else:                   # 如果当前 cur.next 与 cur.next.next 对应的元素不相同，那么说明链表中只有一个元素值为 cur.next 的节点，
                cur = cur.next      # 那么我们就可以将 cur 指向 cur.next。

        return dummy.next   # 返回链表的的哑节点的下一个节点 dummy.next 即可。

if __name__ == "__main__":
    head = listToLinkedList([1,2,3,3,4,4,5])
    sol = Solution()
    result = sol.deleteDuplicates(head)
    print(printLinkedList(result))