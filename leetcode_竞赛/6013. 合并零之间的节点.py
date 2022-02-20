"""

6013. 合并零之间的节点

给你一个链表的头节点 head ，该链表包含由 0 分隔开的一连串整数。链表的 开端 和 末尾 的节点都满足 Node.val == 0 。

对于每两个相邻的 0 ，请你将它们之间的所有节点合并成一个节点，其值是所有已合并节点的值之和。然后将所有 0 移除，修改后的链表不应该含有任何 0 。

返回修改后链表的头节点 head 。

示例 1：
    输入：head = [0,3,1,0,4,5,2,0]
    输出：[4,11]
    解释：
        上图表示输入的链表。修改后的链表包含：
        - 标记为绿色的节点之和：3 + 1 = 4
        - 标记为红色的节点之和：4 + 5 + 2 = 11

示例 2：
    输入：head = [0,1,0,3,0,2,2,0]
    输出：[1,3,4]
    解释：
        上图表示输入的链表。修改后的链表包含：
        - 标记为绿色的节点之和：1 = 1
        - 标记为红色的节点之和：3 = 3
        - 标记为黄色的节点之和：2 + 2 = 4

提示：
    列表中的节点数目在范围 [3, 2 * 10^5] 内
    0 <= Node.val <= 1000
    不 存在连续两个 Node.val == 0 的节点
    链表的 开端 和 末尾 节点都满足 Node.val == 0

"""

class ListNode:   # 节点类
    def __init__(self, val = 0, next = None):  # 初始化节点
        self.val = val     # val存放数据元素
        self.next = next   # 保存当前节点中下一个节点的引用
        # 每个节点包含两个部分，一部分存放数据变量的val，另一部分存放下一个节点的位置信息next。
    
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


class Solution:
    def removeNthFromEnd(self, head: ListNode) -> ListNode:


if __name__ == "__main__":
    head = listToLinkedList ([0,3,1,0,4,5,2,0])
    sol = Solution()
    result = sol.removeNthFromEnd(head)
    print (printLinkedList(result))