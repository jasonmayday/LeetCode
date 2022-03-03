'''
这里介绍的堆结构就是一种完全二叉树。堆可分为最大堆和最小堆，区别就是父节点是否大于所有子节点。
最大堆的父节点大于它的子节点，而最小堆中子节点大于父节点。

'''

import heapq
"""
heapq.heappush(heap, item)          # 向堆中插入元素，heapq会维护列表heap中的元素保持堆的性质

heapq.heapify(x)                    # heapq把列表x转换成堆

heapq.nlargest(n, iterable[, key])  # 从可迭代的迭代器中返回最大的n个数，可以指定比较的key

heapq.nsmallest(n, iterable[, key]) # 从可迭代的迭代器中返回最小的n个数，可以指定比较的key

heapq.heappop(heap)                 # 从堆中删除元素，返回值是堆中最小或者最大的元素
"""

def heapq_int():
    heap = []
    #以堆的形式插入堆
    heapq.heappush(heap,10)
    heapq.heappush(heap,1)
    heapq.heappush(heap,10/2)
    [heapq.heappush(heap,i) for i in  range(10)]
    [heapq.heappush(heap,10 - i) for i in  range(10)]
    #最大的10个元素
    print (heapq.nlargest(10,heap))
    #输出所有元素
    print ([heapq.heappop(heap) for i in range(len(heap))])

def heapq_tuple():
    heap = []
    #向推中插入元组
    heapq.heappush(heap,(10,'ten'))
    heapq.heappush(heap,(1,'one'))
    heapq.heappush(heap,(10/2,'five'))
    while heap:
        print (heapq.heappop(heap),)
    print

class Skill(object):
    def __init__(self,priority,description):
        self.priority = priority
        self.description = description
    def __lt__(self,other):#operator < 
        return self.priority < other.priority
    def __ge__(self,other):#oprator >=
        return self.priority >= other.priority
    def __le__(self,other):#oprator <=
        return self.priority <= other.priority
    def __cmp__(self,other):
        #call global(builtin) function cmp for int
        return cmp(self.priority,other.priority)
    def __str__(self):
        return '(' + str(self.priority)+',\'' + self.description + '\')'

def heapq_class():
    heap  = []
    heapq.heappush(heap,Skill(5,'proficient'))
    heapq.heappush(heap,Skill(10,'expert'))
    heapq.heappush(heap,Skill(1,'novice'))
    while heap:
        print (heapq.heappop(heap),)
    print 
