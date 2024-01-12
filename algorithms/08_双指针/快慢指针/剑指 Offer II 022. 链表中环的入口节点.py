"""
https://leetcode-cn.com/problems/linked-list-cycle-ii/

给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。

如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。 
为了表示给定链表中的环，评测系统内部使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。
如果 pos 是 -1，则在该链表中没有环。
注意：pos 不作为参数进行传递，仅仅是为了标识链表的实际情况。

不允许修改 链表。

示例 1：
    输入：head = [3,2,0,-4], pos = 1
    输出：返回索引为 1 的链表节点
    解释：链表中有一个环，其尾部连接到第二个节点。

示例 2：
    输入：head = [1,2], pos = 0
    输出：返回索引为 0 的链表节点
    解释：链表中有一个环，其尾部连接到第一个节点。

示例 3：
    输入：head = [1], pos = -1
    输出：返回 null
    解释：链表中没有环。

提示：
    链表中节点的数目范围在范围 [0, 10^4] 内
    -10^5 <= Node.val <= 10^5
    pos 的值为 -1 或者链表中的一个有效索引
 
进阶：
    你是否可以使用 O(1) 空间解决此题？

"""

""" 快慢双指针
    https://leetcode-cn.com/problems/linked-list-cycle-ii/solution/linked-list-cycle-ii-kuai-man-zhi-zhen-shuang-zhi-/ """
class Solution(object):
    def detectCycle(self, head):
        fast = head
        slow = head     # 若有环，两指针一定会相遇。因为每走 1 轮，fast 与 slow 的间距 +1，fast 终会追上 slow；
        while True:
            if not (fast and fast.next):    # fast 指针走过链表末端，说明链表无环
                return
            fast = fast.next.next   # fast 每轮走 2 步
            slow = slow.next        # slow 每轮走 1 步
            if fast == slow:    # 当 fast == slow 时，两指针在环中 第一次相遇
                break
        fast = head             # 第一次相遇后，将fast指针重新 指向链表头部节点，slow指针 位置不变
        while fast != slow:
            fast = fast.next    # slow 和 fast 同时每轮向前走 1 步；
            slow = slow.next
        return fast     # 两指针第二次重合后，此时 同时指向链表环入口 。返回 slow 或 fast 指针指向的节点。

