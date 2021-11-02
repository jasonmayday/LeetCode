# Definition for singly-linked list.
class ListNode:   # 节点类
    def __init__(self, val = 0, next = None):  # 初始化节点
        self.val = val     # 保存当前节点的值
        self.next = next   # 保存当前节点中下一个节点的引用
        # 每个节点包含两个部分，一部分存放数据变量的data，另一部分存放下一个节点的位置信息next。

class Linkedlist(): # 链表类
    def __init__(self): # 初始化链表
        self.head = None  # 头节点
        self.length = 0   # 链表长度
