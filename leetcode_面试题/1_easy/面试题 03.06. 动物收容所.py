"""
https://leetcode-cn.com/problems/animal-shelter-lcci/

动物收容所。有家动物收容所只收容狗与猫，且严格遵守“先进先出”的原则。在收养该收容所的动物时，收养人只能收养所有动物中“最老”（由其进入收容所的时间长短而定）的动物，或者可以挑选猫或狗（同时必须收养此类动物中“最老”的）。换言之，收养人不能自由挑选想收养的对象。请创建适用于这个系统的数据结构，实现各种操作方法，比如enqueue、dequeueAny、dequeueDog和dequeueCat。允许使用Java内置的LinkedList数据结构。

enqueue方法有一个animal参数，animal[0]代表动物编号，animal[1]代表动物种类，其中 0 代表猫，1 代表狗。

dequeue*方法返回一个列表[动物编号, 动物种类]，若没有可以收养的动物，则返回[-1,-1]。

示例1:

输入：
        ["AnimalShelf", "enqueue", "enqueue", "dequeueCat", "dequeueDog", "dequeueAny"]
        [[], [[0, 0]], [[1, 0]], [], [], []]
    输出：
        [null,null,null,[0,0],[-1,-1],[1,0]]

示例2:
    输入：
        ["AnimalShelf", "enqueue", "enqueue", "enqueue", "dequeueDog", "dequeueCat", "dequeueAny"]
        [[], [[0, 0]], [[1, 0]], [[2, 1]], [], [], []]
    输出：
        [null,null,null,null,[2,1],[0,0],[1,0]]

说明:
    收纳所的最大容量为20000

"""
from typing import List
from collections import deque

"""用两个队列放到一个列表中，列表0存放猫，列表1存放狗"""
class AnimalShelf:

    def __init__(self):
        self.a = [deque(),deque()]

    def __str__(self):
        return str(self.a)
    
    def enqueue(self, animal: List[int]) -> None:
        self.a[animal[1]].append(animal)

    def dequeueAny(self) -> List[int]:
        if self.a[0] and self.a[1]:
            return self.a[0][0][0] <self.a[1][0][0]  and self.a[0].popleft() or self.a[1].popleft()
        return self.a[0] and self.dequeueCat() or self.dequeueDog()

    def dequeueDog(self) -> List[int]:
        return self.a[1] and self.a[1].popleft() or [-1,-1]

    def dequeueCat(self) -> List[int]:
        return self.a[0] and self.a[0].popleft() or [-1,-1]

""" 三队列 
class AnimalShelf:

    def __init__(self):
        self.dog_deque = deque()
        self.cat_deque = deque()
        self.all_deque = deque()

    def __str__(self):
        return "Player"
    
    def enqueue(self, animal: List[int]) -> None:
        self.all_deque.append(animal)

    def dequeueAny(self) -> List[int]:
        if self.dog_deque:
            return self.dog_deque.popleft()
        if self.cat_deque:
            return self.cat_deque.popleft()
        if self.all_deque:
            return self.all_deque.popleft()
        return [-1, -1]
        
    def dequeueDog(self) -> List[int]:
        if self.dog_deque:
            return self.dog_deque.popleft()
        while self.all_deque:
            if self.all_deque[0][1] == 1:
                return self.all_deque.popleft()
            self.cat_deque.append(self.all_deque.popleft())
        return [-1, -1]

    def dequeueCat(self) -> List[int]:
        if self.cat_deque:
            return self.cat_deque.popleft()
        while self.all_deque:
            if self.all_deque[0][1] == 0:
                return self.all_deque.popleft()
            self.dog_deque.append(self.all_deque.popleft())
        return [-1, -1]"""

if __name__ == "__main__":
    shelf = AnimalShelf()
    shelf.enqueue([0, 0]) # 编号0，放入猫
    shelf.enqueue([1, 0]) # 编号1，放入猫
    shelf.enqueue([2, 1]) # 编号2，放入狗
    print(shelf.dequeueDog)
    print(shelf.dequeueCat)
    print(shelf.dequeueAny)
    print(shelf.dequeueDog)