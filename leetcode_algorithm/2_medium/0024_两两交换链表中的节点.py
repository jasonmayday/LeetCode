"""
https://leetcode-cn.com/problems/swap-nodes-in-pairs/

给你一个链表，两两交换其中相邻的节点，并返回交换后链表的头节点。你必须在不修改节点内部的值的情况下完成本题（即，只能进行节点交换）。

示例 1：
    输入：head = [1,2,3,4]
    输出：[2,1,4,3]

示例 2：
    输入：head = []
    输出：[]

示例 3：
    输入：head = [1]
    输出：[1]

提示：
    链表中节点的数目在范围 [0, 100] 内
    0 <= Node.val <= 100

"""
'''单链表的结点'''
class ListNode:   # 节点类
    def __init__(self, val = 0, next = None):  # 初始化节点
        self.val = val     # val存放数据元素
        self.next = next   # 保存当前节点中下一个节点的引用
        # 每个节点包含两个部分，一部分存放数据变量的val，另一部分存放下一个节点的位置信息next。
    
    def __str__(self):
        #测试基本功能，输出字符串
        return str(self.val)

def listToLinkedList(list):
    head = ListNode(list[0])
    cur = head
    for i in range(1, len(list)):
        cur.next = ListNode(list[i])
        cur = cur.next
    return head

# 传入链表头节点，以数组形式返回
def printLinkedList(head):
    cur = head
    list = []
    while cur:
        list.append(cur.val)
        cur = cur.next
    return list


"""方法1：递归"""
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:   # 递归的终止条件是链表中没有节点，或者链表中只有一个节点
            return head                 # 假设链表是 1->2->3->4
        newHead = head.next             # 新的链表的头节点 为 原始链表的第二个节点  先保存新的头节点 2
        head.next = self.swapPairs(newHead.next)    # 继续递归，将其余节点进行两两交换，处理节点 3->4
                                                    # 当递归结束返回后，就变成了 4->3
		                                            # 于是head节点就指向了4，变成 1->4->3
        newHead.next = head             # 新的链表的第二个节点 为 原始链表的头节点  将2节点指向1
        return newHead
    
"""方法2：栈"""
class Solution(object):
	def swapPairs(self, head):
		if not (head and head.next):
			return head
		p = ListNode(-1)
		# 用stack保存每次迭代的两个节点
		# head指向新的p节点，函数结束时返回head.next即可
		cur,head,stack = head,p,[]
		while cur and cur.next:
			# 将两个节点放入stack中
			_,_ = stack.append(cur),stack.append(cur.next)
			# 当前节点往前走两步
			cur = cur.next.next
			# 从stack中弹出两个节点，然后用p节点指向新弹出的两个节点
			p.next = stack.pop()
			p.next.next = stack.pop()
			p = p.next.next
		# 注意边界条件，当链表长度是奇数时，cur就不为空
		if cur:
			p.next = cur
		else:
			p.next = None
		return head.next

if __name__ == "__main__":
    head = listToLinkedList([1,2,3,4])
    sol = Solution()
    result = sol.swapPairs(head)
    print (printLinkedList(result))