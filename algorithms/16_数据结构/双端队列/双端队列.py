'''

双端队列是与队列类似的有序集合。它有一前、一后两端，元素在其中保持自己的位置。
与队列不同的是，双端队列对在哪一端添加和移除元素没有任何限制。
新元素既可以被添加到前端，也可以被添加到后端。同理，已有的元素也能从任意一端移除。
某种意义上，双端队列是栈和队列的结合。

'''

class Deque:
    def __init__(self):
        self.items = []
    
    '''判断队列是否为空'''
    def isEmpty(self):
        return self.items == []
    
    '''在队头添加元素'''
    def addFront(self, item):
        self.items.append(item)     # 用append方法添加元素
    
    '''在队尾添加元素'''
    def addRear(self, item):        # 用insert方法添加元素，因为append方法只能在列表的最后添加元素
        self.items.insert(0, item)
    
    '''从队头删除元素'''
    def removeFront(self):
        return self.items.pop()     # 使用 pop 方法移除列表中的最后一个元素
    
    '''从队尾删除元素'''
    def removeRear(self):
        return self.items.pop(0)    # 使用 pop(0) 方法移除列表中的第一个元素
    
    '''返回队列大小'''
    def size(self):
        return len(self.items)

if __name__ == '__main__':
    deque = Deque()
    deque.isEmpty()
    deque.addRear(4)
    deque.addRear('dog')
    deque.addFront('cat')
    deque.addFront(True)
    deque.size()
    deque.isEmpty()
    deque.addRear(8.4)
    deque.removeRear()
    deque.removeFront()