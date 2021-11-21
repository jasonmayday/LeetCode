"""
https://leetcode-cn.com/problems/middle-of-the-linked-list/

给定一个头结点为 head 的非空单链表，返回链表的中间结点。

如果有两个中间结点，则返回第二个中间结点。

示例 1：
    输入：[1,2,3,4,5]
    输出：此列表中的结点 3 (序列化形式：[3,4,5])
    返回的结点值为 3 。 (测评系统对该结点序列化表述是 [3,4,5])。
    注意，我们返回了一个 ListNode 类型的对象 ans，这样：
    ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, 以及 ans.next.next.next = NULL.

示例 2：
    输入：[1,2,3,4,5,6]
    输出：此列表中的结点 4 (序列化形式：[4,5,6])
    由于该列表有两个中间结点，值分别为 3 和 4，我们返回第二个结点。

提示：
    给定链表的结点数介于 1 和 100 之间。

"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __str__(self):
        #测试基本功能，输出字符串
        return str(self.val)

def create_linked_list(list):
    head = ListNode(list[0])
    cur = head
    for i in range(1, len(list)):
        cur.next = ListNode(list[i])
        cur = cur.next
    return head


''' 方法一：数组
    链表的缺点在于不能通过下标访问对应的元素。
    因此我们可以考虑对链表进行遍历，同时将遍历到的元素依次放入数组 arr 中。
    如果我们遍历到了 N 个元素，那么链表以及数组的长度也为 N，对应的中间节点即为 arr [N/2]。'''
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        arr = [head]
        while arr[-1].next:             # 如果新数组的最右边一个元素还有.next:
            arr.append(arr[-1].next)    # 把链表中的元素加到arr数组中
        return arr[len(arr) // 2]


''' 方法二：单指针法
    我们可以对方法一进行空间优化，省去数组 arr
    我们可以对链表进行两次遍历。
    第一次遍历时，我们统计链表中的元素个数 N；
    第二次遍历时，我们遍历到第 N/2 个元素（链表的首节点为第 0 个元素）时，将该元素返回即可。'''
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        n, cur = 0, head
        while cur:
            n += 1
            cur = cur.next
        k, cur = 0, head
        while k < n // 2:
            k += 1
            cur = cur.next
        return cur


''' 方法三：快慢指针法
    用两个指针 slow 与 fast 一起遍历链表。
    slow 一次走一步，fast 一次走两步。
    那么当 fast 到达链表的末尾时，slow 必然位于中间。'''
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow


if __name__ == "__main__":
    head = create_linked_list([5,5,5,10,20])
    sol = Solution()
    result = sol.middleNode(head)
    print(result)