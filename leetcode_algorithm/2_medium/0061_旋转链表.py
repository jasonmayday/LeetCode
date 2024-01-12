"""
https://leetcode-cn.com/problems/rotate-list/

给你一个链表的头节点 head ，旋转链表，将链表每个节点向右移动 k 个位置。

示例 1：
    输入：head = [1,2,3,4,5], k = 2
    输出：[4,5,1,2,3]

示例 2：
    输入：head = [0,1,2], k = 4
    输出：[2,0,1]

提示：
    链表中节点的数目在范围 [0, 500] 内
    -100 <= Node.val <= 100
    0 <= k <= 2 * 10^9

"""

'''单链表的结点'''
class ListNode:   # 节点类
    def __init__(self, val = 0, next = None):  # 初始化节点
        self.val = val     # val存放数据元素
        self.next = next   # 保存当前节点中下一个节点的引用
        # 每个节点包含两个部分，一部分存放数据变量的val，另一部分存放下一个节点的位置信息next。
    
    def __str__(self):
        #测试基本功能，输出字符串
        return str(self.val)

'''根据输入的列表创建链表'''
def listToLinkedList(list):
    head = ListNode(list[0])
    cur = head
    for i in range(1, len(list)):
        cur.next = ListNode(list[i])
        cur = cur.next
    return head

# 传入链表头节点，以数组形式返回
def printLinkedList(head):
    cur = head
    list = []
    while cur:
        list.append(cur.val)
        cur = cur.next
    return list

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if k == 0 or not head or not head.next:
            return head
        
        """ 首先计算出链表的长度 n """
        n = 1               # 初始化链表长度为 1
        cur = head          # 初始化指针为头节点 head
        while cur.next:     # 当节点仍有下一节点相连时
            cur = cur.next  # 指针递进
            n += 1          # 长度统计 +1
        
        """ 当向右移动的次数 k ≥ n 时，我们仅需要向右移动 k mod n 次即可 """
        if (add := n - k % n) == n: # 因为每 n 次移动都会让链表变为原状。新链表的最后一个节点为原链表的第 (n−1) − (k mod n) 个节点（从 0 开始计数）
            return head             # 如果 k 刚好为 n 的整数倍数，新链表将于原链表相同
        
        """ 处理逻辑 """
        cur.next = head     # 将最后一位指向第一位，当前链表闭合为环
        while add:          # 将指针 cur 指向新链表的最后一个节点位置
            cur = cur.next
            add -= 1
        
        ret = cur.next      # 此时 ret 为移动 k 位后新链表的头
        cur.next = None     # 将环断开
        return ret          # 返回新链表

if __name__ == "__main__":
    head = listToLinkedList([1,2,3,4,5])
    k = 2
    sol = Solution()
    result = sol.rotateRight(head, k)
    print (printLinkedList(result))