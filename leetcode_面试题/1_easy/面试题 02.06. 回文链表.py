"""
https://leetcode-cn.com/problems/palindrome-linked-list-lcci/

编写一个函数，检查输入的链表是否是回文的。

示例 1：
    输入： 1->2
    输出： false

示例 2：
    输入： 1->2->2->1
    输出： true

进阶：
    你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？

"""

""" 单链表的结点"""
class ListNode:   # 节点类
    def __init__(self, val = 0, next = None):  # 初始化节点
        self.val = val     # val存放数据元素
        self.next = next   # 保存当前节点中下一个节点的引用

    def __str__(self):
        return str(self.val)

''' 根据输入的列表创建链表 '''
def listToLinkedList(list):
    head = ListNode(list[0])
    cur = head
    for i in range(1, len(list)):
        cur.next = ListNode(list[i])
        cur = cur.next
    return head


""" 方法一：将值复制到数组中 """
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        vals = []
        node = head
        while node is not None:
            vals.append(node.val)
            node = node.next
        return vals == vals[::-1]

""" 方法二：递归 """
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        self.front_pointer = head
        def recursively_check(current_node = head):
            if current_node is not None:
                if not recursively_check(current_node.next):
                    return False
                if self.front_pointer.val != current_node.val:
                    return False
                self.front_pointer = self.front_pointer.next
            return True

        return recursively_check()

""" 方法三：快慢指针"""
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head is None:
            return True

        # 找到前半部分链表的尾节点并反转后半部分链表
        first_half_end = self.end_of_first_half(head)
        second_half_start = self.reverse_list(first_half_end.next)

        # 判断是否回文
        result = True
        first_position = head
        second_position = second_half_start
        while result and second_position is not None:
            if first_position.val != second_position.val:
                result = False
            first_position = first_position.next
            second_position = second_position.next

        # 还原链表并返回结果
        first_half_end.next = self.reverse_list(second_half_start)
        return result

    def end_of_first_half(self, head):
        fast = head
        slow = head
        while fast.next is not None and fast.next.next is not None:
            fast = fast.next.next
            slow = slow.next
        return slow

    def reverse_list(self, head):
        previous = None
        current = head
        while current is not None:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        return previous


if __name__ == "__main__":
    head = listToLinkedList([1, 2, 2, 1])
    sol = Solution()
    result = sol.isPalindrome(head)
    print(result)