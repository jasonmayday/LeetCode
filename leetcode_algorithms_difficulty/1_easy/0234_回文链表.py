"""
https://leetcode-cn.com/problems/palindrome-linked-list/
给你一个单链表的头节点 head ，请你判断该链表是否为回文链表。如果是，返回 true ；否则，返回 false 。

示例 1：
    输入：head = [1,2,2,1]
    输出：true

示例 2：
    输入：head = [1,2]
    输出：false
 

提示：
    链表中节点数目在范围[1, 10^5] 内
    0 <= Node.val <= 9

"""
class ListNode:
    def __init__(self, val = 0, next = None):  # 初始化节点
        self.val = val     # val存放数据元素
        self.next = next   # 保存当前节点中下一个节点的引用
    
    def __str__(self):
        return str(self.val)    # 测试基本功能，输出字符串

def create_linked_list(list):
    head = ListNode(list[0])
    cur = head
    for i in range(1, len(list)):
        cur.next = ListNode(list[i])
        cur = cur.next
    return head

"""解法1：将值复制到数组中后用双指针法"""
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        vals = []   # 新建一个数组列表
        current_node = head     # 我们用 currentNode 指向当前节点
        while current_node is not None:         # 当 currentNode = null 时停止循环。
            vals.append(current_node.val)       # 每次迭代向数组添加 currentNode.val
            current_node = current_node.next    # 并更新 currentNode
        return vals == vals[::-1]       # 列表与反转的列表相等时，返回 True

if __name__ == "__main__":
    head = create_linked_list([1,2,2,1])
    sol = Solution()
    result = sol.isPalindrome(head)
    print(result)