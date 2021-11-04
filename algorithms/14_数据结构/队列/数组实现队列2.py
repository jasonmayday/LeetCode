class MyQueue(object):
    """队列"""
    def __init__(self):
        self.items = []
        self.front = 0  # 队列头
        self.rear = 0   # 队列尾

    def is_empty(self):
        """判断队列是否为空"""
        return self.items == self.rear

    def enQueue(self, item):
        """进队列，从队尾加入"""
        self.items.append(item)
        self.rear += 1
        # self.items.insert(0,item)     # 从对头进

    def deQueue(self):
        """出队列，从队头出"""
        if self.rear > self.front:
            self.front += 1
        else:
            print("队列已经为空")
        # return self.items.pop()   # 从对尾出

    def getFront(self):
        if self.is_empty():
            return None
        return self.items[self.front]

    def getBack(self):
        if self.is_empty():
            return None
        return self.items[self.rear-1]

    def size(self):
        """返回大小"""
        return self.rear - self.front
        # return len(self.items)	# 看大小


queue = MyQueue()
queue.enQueue(1)
queue.enQueue(2)

print("队列头元素为："+str(queue.getFront()))
print("队列尾元素为："+str(queue.getBack()))
print("队列的大小为："+str(queue.size()))

queue.deQueue()
# queue.deQueue()
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
