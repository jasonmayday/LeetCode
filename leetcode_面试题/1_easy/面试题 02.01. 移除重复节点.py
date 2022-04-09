"""
https://leetcode-cn.com/problems/remove-duplicate-node-lcci/

编写代码，移除未排序链表中的重复节点。保留最开始出现的节点。

示例1:
    输入：[1, 2, 3, 3, 2, 1]
    输出：[1, 2, 3]

示例2:
    输入：[1, 1, 1, 1, 2]
    输出：[1, 2]

提示：
    链表长度在[0, 20000]范围内。
    链表元素在[0, 20000]范围内。

进阶：
    如果不得使用临时缓冲区，该怎么解决？

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

""" 传入链表头节点，以数组形式返回"""
def printLinkedList(head):
    cur = head
    list = []
    while cur:
        list.append(cur.val)
        cur = cur.next
    return list

""" 方法一：哈希表"""
class Solution:
    def removeDuplicateNodes(self, head: ListNode) -> ListNode:
        if not head:
            return head
        occurred = {head.val}
        pos = head
        # 枚举前驱节点
        while pos.next:
            # 当前待删除节点
            cur = pos.next
            if cur.val not in occurred:
                occurred.add(cur.val)
                pos = pos.next
            else:
                pos.next = pos.next.next
        return head

class Solution:
    def removeDuplicateNodes(self, head: ListNode) -> ListNode:
        if not head:        # 如果head里本来就没东西，那就返回head本身
            return head
        r = head            # r是head的代言人，负责迭代和更新，head负责原地不动
        record = {head.val} # record负责储存看见过的值。现在已经储存了第一个值
        while r and r.next: # 只要r接下来还有东西，就看看下一个东西是不是已经在record当中
            # 这里判断时要同时符合这两个条件，因为如果r已经是None了，判断r.next会报错，所以每次得先判断r
            if r.next.val not in record:    # 如果下一环的值没被储存过,不用对head作任何修改
                record.add(r.next.val)      # 在record中添加这个值
                r = r.next # 并且让r进入下一环
            else: # 如果下一环的值已经见过了
                r.next = r.next.next # 直接让r的下一环变为下下环，即把r.next这一环删了
                # 这里不用再写"r=r.next"让r进入下一环，原因是r.next已经更改了，要重新进入loop判断现在的r.next(即原来的r.next.next)是否已经遇见过
        return head

if __name__ == "__main__":
    head = listToLinkedList([1, 2, 3, 3, 2, 1])
    sol = Solution()
    result = sol.removeDuplicateNodes(head)
    print(printLinkedList(result))