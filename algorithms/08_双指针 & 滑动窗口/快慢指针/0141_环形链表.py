'''
给定一个链表，判断链表中是否有环。

如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。 为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。注意：pos 不作为参数进行传递，仅仅是为了标识链表的实际情况。

如果链表中存在环，则返回 true 。 否则，返回 false 。

进阶：
    你能用 O(1)（即，常量）内存解决此问题吗？

示例 1：
    输入：head = [3,2,0,-4], pos = 1
    输出：true
    解释：链表中有一个环，其尾部连接到第二个节点。

示例 2：
    输入：head = [1,2], pos = 0
    输出：true
    解释：链表中有一个环，其尾部连接到第一个节点。

示例 3：
    输入：head = [1], pos = -1
    输出：false
    解释：链表中没有环。
 
提示：
    链表中节点的数目范围是 [0, 10^4]
    -10^5 <= Node.val <= 10^5
    pos 为 -1 或者链表中的一个 有效索引 。

'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

"""哈希表"""
# 遍历所有节点，每次遍历到一个节点时，判断该节点此前是否被访问过。
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        seen = set()            # 使用哈希表来存储所有已经访问过的节点
        while head:
            if head in seen:
                return True     # 到达一个节点，如果该节点已经存在于哈希表中，则说明该链表是环形链表
            seen.add(head)      # 否则就将该节点加入哈希表中
            head = head.next
        return False

"""快慢指针"""
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next:
            return False
        
        slow = head         # 初始时慢指针在位置 head
        fast = head.next    # 初始时快指针在位置 head.next

        while slow != fast:
            if not fast or not fast.next:
                return False
            slow = slow.next        # 慢指针每次只移动一步
            fast = fast.next.next   # 快指针每次移动两步
        
        return True

if __name__ == "__main__":
    head = [3,2,0,-4]
    pos = 1
    sol = Solution()
    result = sol.hasCycle(head)
    print(result)