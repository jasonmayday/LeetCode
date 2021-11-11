'''
在链接表两端操作，从一端插入元素，从另一端删除
'''

class LNode(object):
    def __init__(self,x):
        self.data = x
        self.next = None

class LinkedQueue(object):
    def __init__(self):
        """分配头结点"""
        self.pHead = None
        self.pEnd = None

    def is_empty(self):
        """判断是否为空"""
        if self.pHead == None:
            return True
        return False

    def size(self):
        """获取队列的大小"""
        size=0
        p = self.pHead
        while p != None:
        # while p is not None:
            p = p.next
            size += 1
        return size

    def enQueue(self, element):
        """入队列，从队尾加"""
        p = LNode(element)
        p.data = element
        p.next = None
        if self.pHead == None:
            self.pHead = self.pEnd=p
        else:
            self.pEnd.next = p
            self.pEnd = p

    def deQueue(self):
        """出队列，删除首元素"""
        if self.pHead == None:
            print("出队列失败，队列已经为空")
        self.pHead = self.pHead.next
        if self.pHead == None:
            self.pEnd = None

    def getFront(self):
        """返回队列首元素"""
        if self.pHead == None:
            print("获取队列首元素失败，队列已经为空")
            return None
        return self.pHead.data

    def getBack(self):
    	"""返回队列尾元素"""
        if self.pEnd == None:
            print("获取队列尾元素失败，队列已经为空")
            return None
        return self.pEnd.data

queue = LinkedQueue()
queue.enQueue(1)
queue.enQueue(2)

print("队列头元素为："+str(queue.getFront()))
print("队列尾元素为："+str(queue.getBack()))
print("队列的大小为："+str(queue.size()))

queue.deQueue()
print("队列头元素为："+str(queue.getFront()))
print("队列尾元素为："+str(queue.getBack()))
print("队列的大小为："+str(queue.size()))
"""
队列头元素为：1
队列尾元素为：2
队列的大小为：2
队列头元素为：2
队列尾元素为：2
队列的大小为：1
"""
