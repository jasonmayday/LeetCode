"""
https://leetcode-cn.com/problems/linked-list-random-node/

给你一个单链表，随机选择链表的一个节点，并返回相应的节点值。每个节点 被选中的概率一样 。

实现 Solution 类：
    Solution(ListNode head) 使用整数数组初始化对象。
    int getRandom() 从链表中随机选择一个节点并返回该节点的值。链表中所有节点被选中的概率相等。

示例：
    输入
    ["Solution", "getRandom", "getRandom", "getRandom", "getRandom", "getRandom"]
    [[[1, 2, 3]], [], [], [], [], []]
    输出
    [null, 1, 3, 2, 2, 3]

    解释
    Solution solution = new Solution([1, 2, 3]);
    solution.getRandom(); // 返回 1
    solution.getRandom(); // 返回 3
    solution.getRandom(); // 返回 2
    solution.getRandom(); // 返回 2
    solution.getRandom(); // 返回 3
    // getRandom() 方法应随机返回 1、2、3中的一个，每个元素被返回的概率相等。

提示：
    链表中的节点数在范围 [1, 10^4] 内
    -10^4 <= Node.val <= 10^4
    至多调用 getRandom 方法 10^4 次

进阶：
    如果链表非常大且长度未知，该怎么处理？
    你能否在不使用额外空间的情况下解决此问题？

"""
import random

def listToLinkedList(list):
    head = ListNode(list[0])
    cur = head
    for i in range(1, len(list)):
        cur.next = ListNode(list[i])
        cur = cur.next
    return head

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

""" 方法一：记录所有链表元素"""
class Solution:
    def __init__(self, head: ListNode):
        self.arr = []   # 用一个数组记录链表中的所有元素
        while head:
            self.arr.append(head.val)
            head = head.next

    def getRandom(self) -> int:
        return random.choice(self.arr)  # 随机选择链表的一个节点，就变成在数组中随机选择一个元素。

""" 方法二：蓄水池抽样 """
class Solution:
    def __init__(self, head: ListNode):
        self.head = head

    def getRandom(self) -> int:
        node = self.head
        i = 1
        ans = 0
        while node:
            if random.randrange(i) == 0:  # 1/i 的概率选中（替换为答案）
                ans = node.val
            i += 1
            node = node.next
        return ans

if __name__ == "__main__":
    solution = Solution(listToLinkedList([1, 2, 3]))
    print(solution.getRandom())    # 返回 1
    print(solution.getRandom())    # 返回 3
    print(solution.getRandom())    # 返回 2
    print(solution.getRandom())    # 返回 2
    print(solution.getRandom())    # 返回 3