"""
https://leetcode-cn.com/problems/convert-binary-number-in-a-linked-list-to-integer/

给你一个单链表的引用结点 head。链表中每个结点的值不是 0 就是 1。已知此链表是一个整数数字的二进制表示形式。

请你返回该链表所表示数字的 十进制值 。

示例 1：
    输入：head = [1,0,1]
    输出：5
    解释：二进制数 (101) 转化为十进制数 (5)

示例 2：
    输入：head = [0]
    输出：0

示例 3：
    输入：head = [1]
    输出：1

示例 4：
    输入：head = [1,0,0,1,0,0,1,1,1,0,0,0,0,0,0]
    输出：18880

示例 5：
    输入：head = [0,0]
    输出：0

提示：
    链表不为空。
    链表的结点总数不超过 30。
    每个结点的值不是 0 就是 1。

"""

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

""" 解法1
    十进制转化为二进制的步骤是除二取余，逆序排列。这里要反推回去，只要把上述操作反过来就行。因为给出的列表已经是逆序的，所以我们要做的就是乘二加余。"""
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        cur = head
        ans = 0
        while cur:
            ans = ans * 2 + cur.val
            cur = cur.next
        return ans
        
if __name__ == "__main__":
    head = listToLinkedList([1,0,0,1,0,0,1,1,1,0,0,0,0,0,0])
    sol = Solution()
    result = sol.getDecimalValue(head)
    print(result)





    
