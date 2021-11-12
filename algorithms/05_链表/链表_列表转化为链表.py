"""
单链表的结点是一个二元组，元素域value保存着作为表元素的数据项，链接域next里保存同一个表里的下一个节点的标识
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

'''根据输入的列表创建链表'''
def create_linked_list(list):
    head = ListNode(list[0])
    cur = head
    for i in range(1, len(list)):
        cur.next = ListNode(list[i])
        cur = cur.next
    return head

# 传入链表头节点，以数组形式返回
def print_linked_list(head):
    cur = head
    list = []
    while cur:
        list.append(cur.val)
        cur = cur.next
    return list

# 计算链表长度
def length(node):
    cur = node              
    len = 0                 # 计数
    while cur != None:      # 遍历所有节点
        len += 1            # 计数
        cur = cur.next      # cur指向下一个节点
    return len   


if __name__ == "__main__":
    node = create_linked_list([99,1,34,2,6,1,35,657,5,3,8,7])
    print (print_linked_list(node))
    print (length(node))