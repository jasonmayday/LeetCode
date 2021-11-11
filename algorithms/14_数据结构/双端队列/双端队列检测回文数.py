class Deque:
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items == []
    
    def addFront(self, item):
        self.items.append(item)     # 用append方法添加元素
    
    def addRear(self, item):        # 用insert方法添加元素，因为append方法只能在列表的最后添加元素
        self.items.insert(0, item)
    
    def removeFront(self):
        return self.items.pop()     # 使用 pop 方法移除列表中的最后一个元素
    
    def removeRear(self):
        return self.items.pop(0)    # 使用 pop(0) 方法移除列表中的第一个元素
    
    def size(self):
        return len(self.items)

def palchecker(aString):
    chardeque = Deque()
    for ch in aString:
        chardeque.addRear(ch)
    stillEqual = True
    while chardeque.size() > 1 and stillEqual:
        first = chardeque.removeFront()
        last = chardeque.removeRear()
        if first != last:
            stillEqual = False
    return stillEqual

if __name__ == '__main__':
    palchecker("lsdkjfskf")