# Definition for singly-linked list.

'''单链表的结点'''
class Node:   # 节点类
    def __init__(self, val = 0, next = None):  # 初始化节点
        self.val = val     # val存放数据元素
        self.next = next   # 保存当前节点中下一个节点的引用
        # 每个节点包含两个部分，一部分存放数据变量的val，另一部分存放下一个节点的位置信息next。

'''单链表'''
class SingleLinkedList():
    def __init__(self):   # 初始化链表
        self.head = None  # 先初始化一个头节点为空

    '''展示功能'''
    # 判断链表是否为空
    def is_empty(self):
        return not self.head  # if self.head is None: return Ture.

    # 获取链表的长度
    def length(self):
        cur = self.head        # 初始指针，用来移动遍历节点，指向head
        count = 0              # count记录节点数量
        while cur is not None: # 指针指向 None 时表示到达尾部
            count += 1         # 指针后移
            cur = cur.next
        return count

    # 展示链表
    def display(self):
        cur = self.head.next          # 定位到第一个节点
        for i in range(self.length):  # 根据长度判断是否到末尾
            print(cur.val)            # 输出节点数据
            cur = cur.next            # 指向下一节点

    '''添加节点'''
    # 在链表的头部添加元素
    def add_first(self, val):
        node = Node(val)
        node.next = self.head   # 新节点指针指向原头部节点
        self.head = node        # 头部节点指针修改为新节点
    
    # 在链表的尾部添加元素
    def add_last(self, val):
        node = Node(val)       # 创建一个新节点
        if self.is_empty():    # 先判断是否为空链表
            self.head = node   # 空链表，head 指向新节点
        else:
            cur = self.head    # 不是空链表：则找到尾部，将尾部next节点指向新节点
            while cur.next is not None:
                cur = cur.next
            cur.next = node

    # 在指定位置添加元素 
    def insert_node(self, index, val):
        node = Node(val)
        if index < 0 or index > self.length():  # 位置超出链表范围，返回错误
            return False
        elif index == 0:               # 指定位置在为第一个元素之前：
            self.add_fist()            # 在头部插入
        elif index == self.length():   # 指定位置在尾部：
            self.add_last()            # 在链表的尾部添加元素
        else:                          # else: 插入位置在链表中间
            cur = self.head
            count = 0
            while count < index - 1:
                cur = cur.next
                count += 1
            node.next = cur.next
            cur.next = node

    '''删除节点'''
    # 删除指定结点
    def remove_node(self, val):
        cur = self.head  # 指针指向的结点
        pre = None       # 指针指向结点的前一个
        if self.head == val:              # 找到指定元素
            self.head.next = self.head    
        else:
            while cur.val is not val:
                pre = cur                 
                cur = cur.next            # 继续按链表后移节点
            pre.next = cur.next           # 将删除位置前一个节点的next指向删除位置的后一个节点

    '''查找功能'''
    # 查找指定结点是否存在
    def search_node_is_exist(self, val):
        cur = self.head
        while cur is not None:
            if cur.val == val:
                return True
            else:
                cur = cur.next
        return False

    # 遍历整个链表
    def traversal(self):
        cur = self.head         # 获取head指针
        while cur is not None:  # 循环遍历
            print(cur.val)      # 返回value
            cur = cur.next      # 指针后移
        # print("\n")

'''创建链表'''
if __name__ == '__main__':
    l1 = SingleLinkedList()
    l1.add_first(1)
    l1.add_last(2)
    l1.add_last(4)
    l1.insert_node(2, 3)
    l1.traversal()
    # 1 2 3 4

    print(l1.is_empty())
    # False

    print(l1.length())
    # 4

    l1.remove_node(4)
    print(l1.search_node_is_exist(3))
    # True

    l1.traversal()
    # 1 2 3
