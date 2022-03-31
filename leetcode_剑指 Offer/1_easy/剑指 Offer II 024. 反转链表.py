"""
https://leetcode-cn.com/problems/reverse-linked-list/

给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。

示例 1：
    输入：head = [1,2,3,4,5]
    输出：[5,4,3,2,1]

示例 2：
    输入：head = [1,2]
    输出：[2,1]

示例 3：
    输入：head = []
    输出：[]
 
提示：
    链表中节点的数目范围是 [0, 5000]
    -5000 <= Node.val <= 5000

进阶：链表可以选用迭代或递归方式完成反转。你能否用两种方法解决这道题？

注意：本题与主站 206 题相同： https://leetcode-cn.com/problems/reverse-linked-list/

"""

class ListNode:   # 节点类
    def __init__(self, val = 0, next = None):  # 初始化节点
        self.val = val     # val存放数据元素
        self.next = next   # 保存当前节点中下一个节点的引用
        # 每个节点包含两个部分，一部分存放数据变量的val，另一部分存放下一个节点的位置信息next。
    
    def __str__(self):
        # 测试基本功能，输出字符串
        return str(self.val)

'''将传入的数组转化为链表'''
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
    list = []
    while cur:
        list.append(cur.val)
        cur = cur.next
    return list

""" 双指针迭代 """
class Solution(object):
	def reverseList(self, head):
		pre = None      # 申请两个节点，pre 和 cur
		cur = head      # pre 指向 None，cur 指向头节点
		while cur:      # 遍历链表
			tmp = cur.next  # 记录当前节点的下一个节点
			cur.next = pre  # 然后将当前节点指向pre
			pre = cur   # pre和cur节点都前进一位
			cur = tmp
		return pre

""" 递归 """
class Solution(object):
	def reverseList(self, head):
		if (head == None or head.next == None): # 递归终止条件是当前为空，或者下一个节点为空
			return head
		cur = self.reverseList(head.next)   # 这里的 cur 就是最后一个节点
		head.next.next = head               # 如果链表是 1→2→3→4→5，那么此时的cur就是5，而head是4，head的下一个是5，下下一个是空，所以head.next.next 就是5→4
		head.next = None                    # 防止链表循环，需要将head.next设置为空
		return cur                          # 每层递归函数都返回cur，也就是最后一个节点

if __name__ == "__main__":
    head = create_linked_list([1,2,3,4,5,6,7])
    print (print_linked_list(head))

    sol = Solution()
    NewLinkedList = sol.reverseList(head)
    print (print_linked_list(NewLinkedList))