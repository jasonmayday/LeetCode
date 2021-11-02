# Definition for singly-linked list.

class Node:   # 节点类
    def __init__(self, val = 0, next = None):  # 初始化节点
        self.val = val     # 保存当前节点的值
        self.next = next   # 保存当前节点中下一个节点的引用
        # 每个节点包含两个部分，一部分存放数据变量的val，另一部分存放下一个节点的位置信息next。

class SingleLinkedList(): # 链表类
    def __init__(self): # 初始化链表
        self.head = None  # 头节点

    '''展示功能'''
    # 判断链表是否为空
    def is_empty(self):
        return not self.head  # if self.head is None: return Ture.

    # 获取链表的长度
    def length(self):
        cur = self.head
        count = 0
        while cur is not None:
            count += 1
            cur = cur.next
        return count

    '''添加节点'''
    # 在链表的头部添加元素
    def add_first(self, val):
        node = Node(val)
        node.next = self.head
        self.head = node
    
    # 在链表的尾部添加元素
    def add_last(self, val):
        node = Node(val)
        if self.is_empty():
            self.head = node
        else:
            cur = self.head
            while cur.next is not None:
                cur = cur.next
            cur.next = node

    # 在指定位置添加元素 
    def insert_node(self, index, val):
        node = Node(val)
        if index < 0 or index > self.length():
            return False
        elif index == 0:
            self.add_fist()
        elif index == self.length():
            self.add_last()
        else:
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
        if self.head == val:
            self.head.next = self.head
        else:
            while cur.val is not val:
                pre = cur
                cur = cur.next
            pre.next = cur.next

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
        cur = self.head
        while cur is not None:
            print(cur.val)
            cur = cur.next

if __name__ == '__main__':
    l1 = SingleLinkedList()
    l1.add_first(1)
    l1.add_last(2)
    l1.add_last(4)
    l1.insert_node(2, 3)
    l1.traversal()
    print(l1.is_empty())
    print(l1.length())
    l1.remove_node(4)
    print(l1.search_node_is_exist(3))
    l1.traversal()
