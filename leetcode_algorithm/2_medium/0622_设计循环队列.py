"""
https://leetcode.cn/problems/design-circular-queue/

设计你的循环队列实现。 循环队列是一种线性数据结构，其操作表现基于 FIFO（先进先出）原则并且队尾被连接在队首之后以形成一个循环。它也被称为“环形缓冲器”。

循环队列的一个好处是我们可以利用这个队列之前用过的空间。在一个普通队列里，一旦一个队列满了，我们就不能插入下一个元素，即使在队列前面仍有空间。但是使用循环队列，我们能使用这些空间去存储新的值。

你的实现应该支持如下操作：

    MyCircularQueue(k): 构造器，设置队列长度为 k 。
    Front: 从队首获取元素。如果队列为空，返回 -1 。
    Rear: 获取队尾元素。如果队列为空，返回 -1 。
    enQueue(value): 向循环队列插入一个元素。如果成功插入则返回真。
    deQueue(): 从循环队列中删除一个元素。如果成功删除则返回真。
    isEmpty(): 检查循环队列是否为空。
    isFull(): 检查循环队列是否已满。

示例：

    MyCircularQueue circularQueue = new MyCircularQueue(3); // 设置长度为 3
    circularQueue.enQueue(1);  // 返回 true
    circularQueue.enQueue(2);  // 返回 true
    circularQueue.enQueue(3);  // 返回 true
    circularQueue.enQueue(4);  // 返回 false，队列已满
    circularQueue.Rear();  // 返回 3
    circularQueue.isFull();  // 返回 true
    circularQueue.deQueue();  // 返回 true
    circularQueue.enQueue(4);  // 返回 true
    circularQueue.Rear();  // 返回 4

提示：

    所有的值都在 0 至 1000 的范围内；
    操作数将在 1 至 1000 的范围内；
    请不要使用内置的队列库。

"""

"""方法一：数组"""
class MyCircularQueue:
    def __init__(self, k: int):
        self.front = self.rear = 0
        self.elements = [0] * (k + 1)

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.elements[self.rear] = value
        self.rear = (self.rear + 1) % len(self.elements)
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.front = (self.front + 1) % len(self.elements)
        return True

    def Front(self) -> int:
        return -1 if self.isEmpty() else self.elements[self.front]

    def Rear(self) -> int:
        return -1 if self.isEmpty() else self.elements[(self.rear - 1) % len(self.elements)]

    def isEmpty(self) -> bool:
        return self.rear == self.front

    def isFull(self) -> bool:
        return (self.rear + 1) % len(self.elements) == self.front

"""方法二：链表"""
class MyCircularQueue:
    def __init__(self, k: int):
        self.head = self.tail = None
        self.capacity = k
        self.size = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        node = ListNode(value)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.head = self.head.next
        self.size -= 1
        return True

    def Front(self) -> int:
        return -1 if self.isEmpty() else self.head.val

    def Rear(self) -> int:
        return -1 if self.isEmpty() else self.tail.val

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.capacity

if __name__ == "__main__":
    circularQueue = MyCircularQueue(3)  # 设置长度为 3
    circularQueue.enQueue(1)            # 返回 true
    circularQueue.enQueue(2)            # 返回 true
    circularQueue.enQueue(3)            # 返回 true
    circularQueue.enQueue(4)            # 返回 false，队列已满
    circularQueue.Rear()                # 返回 3
    circularQueue.isFull()              # 返回 true
    circularQueue.deQueue()             # 返回 true
    circularQueue.enQueue(4)            # 返回 true
    circularQueue.Rear()                # 返回 4