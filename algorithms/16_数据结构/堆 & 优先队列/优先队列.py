'''
一个包含优先级元素的集合，这个集合允许插入任意的元素，并允许删除拥有最高优先级的元素。

“先进先出”（FIFO）的数据结构：队列（Queue）。

队列有一种变体叫做“优先队列”（Priority Queue）。优先队列的出队（Dequeue）操作和队列一样，都是从队首出队。

但在优先队列的内部，元素的次序却是由“优先级”来决定：高优先级的元素排在队首，而低优先级的元素则排在后面。

'''

import heapq
 
class PriorityQueue(object):
    def __init__ (self) :
        self._queue = []         # 创建一个空列表用于存放队列
        self._index = 0          # 指针用于记录push的次序
    
    def push(self, item, priority):     
        """
        队列由 (priority, index, item) 形式组成
        priority 增加 "-" 号是因为 heappush 默认是最小堆
        index 是为了当两个对象的优先级一致时，按照插入顺序排列
        """
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1
        
    def pop(self):     # 弹出优先级最高的对象
        return heapq.heappop(self._queue)[-1]      # 返回拥有最高优先级的项
    
    def qsize(self):
        return len(self._queue)

    def empty(self):
        return True if not self._queue else False 

class Car(object):
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __repr__(self):
        return "{0} -- {1}".format(self.name, self.value)

if __name__ == "__main__":
    car1 = Car("BMW", 45)
    car2 = Car("Maybach", 145)
    car3 = Car("Bugatti", 85)
    car4 = Car("Cadillac", 78)
    car5 = Car("Maserati", 85)
    pq = PriorityQueue()
    pq.push(car1, car1.value)
    pq.push(car2, car2.value)
    pq.push(car3, car3.value)
    pq.push(car4, car4.value)
    pq.push(car5, car5.value)
    print("队列大小：{0}".format(pq.qsize()))
    # 弹出元素
    while not pq.empty():
        print(pq.pop())
