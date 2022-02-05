"""
https://leetcode-cn.com/problems/insertion-sort-list/

给定单个链表的头 head ，使用 插入排序 对链表进行排序，并返回 排序后链表的头 。

插入排序 算法的步骤:
    1. 插入排序是迭代的，每次只移动一个元素，直到所有元素可以形成一个有序的输出列表。
    2. 每次迭代中，插入排序只从输入数据中移除一个待排序的元素，找到它在序列中适当的位置，并将其插入。
    3. 重复直到所有输入数据插入完为止。

下面是插入排序算法的一个图形示例。部分排序的列表(黑色)最初只包含列表中的第一个元素。每次迭代时，从输入数据中删除一个元素(红色)，并就地插入已排序的列表中。

对链表进行插入排序。

示例 1：
    输入: head = [4,2,1,3]
    输出: [1,2,3,4]

示例 2：
    输入: head = [-1,5,3,4,0]
    输出: [-1,0,3,4,5]

提示：
    列表中的节点数在 [1, 5000]范围内
    -5000 <= Node.val <= 5000

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

""" 从前往后找插入点
    维护一个有序序列，初始时有序序列只有一个元素，每次将一个新的元素插入到有序序列中，将有序序列的长度增加 11，直到全部元素都加入到有序序列中。 """
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        
        dummyHead = ListNode(0) # 创建哑节点 
        dummyHead.next = head   # 引入哑节点是为了便于在 head 节点之前插入节点
        
        lastSorted = head   # 维护 lastSorted 为链表的已排序部分的最后一个节点，初始时 lastSorted = head。
        curr = head.next    # 维护 curr 为待插入的元素，初始时 curr = head.next。

        while curr:         # 比较 lastSorted 和 curr 的节点值。
            if lastSorted.val <= curr.val:      # 待插入的元素 比 之前的末尾元素 大，说明 curr 应该位于 lastSorted 之后
                lastSorted = lastSorted.next    # 将 lastSorted 后移一位，curr 变成新的 lastSorted。（不做调换）
            else:                               # 待插入的元素 比 之前的末尾元素 小
                prev = dummyHead                # 从链表的头节点开始：
                while prev.next.val <= curr.val:
                    prev = prev.next            # 往后遍历链表中的节点，寻找插入 curr 的位置
                lastSorted.next = curr.next
                curr.next = prev.next
                prev.next = curr                # 令 prev 为插入 curr 的位置的前一个节点，完成对 curr 的插入：
            curr = lastSorted.next      # 此时 curr 为下一个待插入的元素。
                                        # 重复 while curr 之后的操作，直到 curr 变成空，排序结束。
        return dummyHead.next   # dummyHead.next 为排序后的链表的头节点。


if __name__ == "__main__":
    head = listToLinkedList([-1,5,3,4,0])
    sol = Solution()
    result = sol.insertionSortList(head)
    print (printLinkedList(result))