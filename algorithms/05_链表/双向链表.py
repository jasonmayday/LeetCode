class Node():
    """节点类"""
    def __init__(self, item, per=None, next=None):
        self.per = per
        self.item = item
        self.next = next

class LinkList():
    """双向链表"""
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
        while node.next:
            node = node.next
            num += 1
        return num

    def add(self, item):
        """链表头部添加"""
        self.head = Node(item, next=self.head)

    def travel(self):
        """遍历整个链表"""
        node = self.head
        if node == None:
            return
        print(node.item)
        while node.next:
            node = node.next
            print(node.item)

    def addend(self, item):
        """链表尾部添加元素"""
        node = self.head
        if node == None:
            self.head = Node(item)
            return
        while node.next:
            node = node.next
        node.next = Node(item, node)

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