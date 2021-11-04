'''
使链表尾部节点的 "next" 指针指向链表的头部，这种结构为循环链表

'''

class Node():
    """节点类"""
    def __init__(self, item, per=None, next=None):
        self.per = per
        self.item = item
        self.next = next

class LinkList():
    """循环链表"""
    def __init__(self, node=None):
        self.head = node

    def is_empty(self):
        """判断链表是否为空"""
        return True if self.head else False
    
    def length(self):
        """返回链表长度"""
        num = 0
        node = self.head
        if node == None:
            return num
        num += 1
        while node.next!=self.head:
            node = node.next
            num += 1
        return num
    
    def add(self, item):
        """链表头部添加"""
        self.head = Node(item, per=self.head.per, next=self.head)
    
    def travel(self):
        """遍历整个链表"""
        node = self.head
        if node == None:
            return
        print(node.item)
        while node.next!=self.head:
            node = node.next
            print(node.item)
    
    def addend(self, item):
        """链表尾部添加元素"""
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
    
    def insert(self, index, item):
        """指定位置添加"""
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
    
    def remove(self, index):
        """删除指定节点"""
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
    
    def search(self, item):
        """查找节点是否存在"""
        index = 0
        node = self.head
        while node.next:
            if node.item==item:
                return index
            index += 1
            node = node.next
        return "该元素不存在"