'''
使链表尾部节点的 "next" 指针指向链表的头部，这种结构为循环链表

'''

"""节点类"""
class Node():
    def __init__(self, item, per=None, next=None):
        self.per = per
        self.item = item
        self.next = next

"""循环链表"""
class LinkList():

    def __init__(self, node=None):
        self.head = node

    """判断链表是否为空"""
    def is_empty(self):
        return True if self.head else False

    """返回链表长度"""
    def length(self):
        num = 0
        node = self.head
        if node == None:
            return num
        num += 1
        while node.next!=self.head:
            node = node.next
            num += 1
        return num

    """链表头部添加"""
    def add(self, item):
        self.head = Node(item, per=self.head.per, next=self.head)

    """链表尾部添加元素"""
    def addend(self, item):
        node = self.head
        if node == None:
            node = Node(item)
            node.per=node
            node.next=node
            self.head = node
            return
        while node.next:
            node = node.next
        node.next = Node(item, node, node.next)

    """指定位置添加"""
    def insert(self, index, item):
        if index == 0:
            self.add(item)
            return
        node = self.head
        try:
            for i in range(index):
                node = node.next
            node.next = None(item, node, node.next)
        except:
            assert "索引超出范围"

    """删除指定节点"""
    def remove(self, index):
        if index == 0:
            self.head = self.head.next
            return
        node = self.head
        try:
            for i in range(index-1):
                node = node.next
            node.next = node.next.next
            node.next.per=node
        except:
            assert "索引超出范围"

    """查找节点是否存在"""
    def search(self, item):
        index = 0
        node = self.head
        while node.next:
            if node.item==item:
                return index
            index += 1
            node = node.next
        return "该元素不存在"

    """遍历整个链表"""    
    def travel(self):
        node = self.head
        if node == None:
            return
        print(node.item)
        while node.next!=self.head:
            node = node.next
            print(node.item)