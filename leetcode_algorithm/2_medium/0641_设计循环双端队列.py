"""
https://leetcode.cn/problems/design-circular-deque/

设计实现双端队列。

实现 MyCircularDeque 类:

    MyCircularDeque(int k) ：构造函数,双端队列最大为 k 。
    boolean insertFront()：将一个元素添加到双端队列头部。 如果操作成功返回 true ，否则返回 false 。
    boolean insertLast() ：将一个元素添加到双端队列尾部。如果操作成功返回 true ，否则返回 false 。
    boolean deleteFront() ：从双端队列头部删除一个元素。 如果操作成功返回 true ，否则返回 false 。
    boolean deleteLast() ：从双端队列尾部删除一个元素。如果操作成功返回 true ，否则返回 false 。
    int getFront() ：从双端队列头部获得一个元素。如果双端队列为空，返回 -1 。
    int getRear() ：获得双端队列的最后一个元素。 如果双端队列为空，返回 -1 。
    boolean isEmpty() ：若双端队列为空，则返回 true ，否则返回 false  。
    boolean isFull() ：若双端队列满了，则返回 true ，否则返回 false 。

示例 1：
    输入
        ["MyCircularDeque", "insertLast", "insertLast", "insertFront", "insertFront", "getRear", "isFull", "deleteLast", "insertFront", "getFront"]
        [[3], [1], [2], [3], [4], [], [], [], [4], []]
    输出
        [null, true, true, true, false, 2, true, true, true, 4]

    解释
        MyCircularDeque circularDeque = new MycircularDeque(3); // 设置容量大小为3
        circularDeque.insertLast(1);			                // 返回 true
        circularDeque.insertLast(2);			                // 返回 true
        circularDeque.insertFront(3);			                // 返回 true
        circularDeque.insertFront(4);			                // 已经满了，返回 false
        circularDeque.getRear();  				                // 返回 2
        circularDeque.isFull();				                    // 返回 true
        circularDeque.deleteLast();			                    // 返回 true
        circularDeque.insertFront(4);			                // 返回 true
        circularDeque.getFront();				                // 返回 4

提示：
    1 <= k <= 1000
    0 <= value <= 1000
    insertFront, insertLast, deleteFront, deleteLast, getFront, getRear, isEmpty, isFull  调用次数不大于 2000 次

"""


"""方法一：数组"""
class MyCircularDeque:
    def __init__(self, k: int):         # k：循环队列的容量
        self.front = self.rear = 0      # front：队列首元素对应的数组的索引。rear：队列尾元素对应的索引的下一个索引。
        self.elements = [0] * (k + 1)   # elements是一个固定大小的数组，用于保存循环队列的元素。

    def insertFront(self, value: int) -> bool:  # 队列未满时，在队首插入一个元素。
        if self.isFull():
            return False
        self.front = (self.front - 1) % len(self.elements)  # 首先将队首 front 移动一个位置，
        self.elements[self.front] = value                   # 更新队首索引为 front 更新为 (front − 1 + capacity) mod capacity。
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        self.elements[self.rear] = value                    # 队列未满时，在队列的尾部插入一个元素，
        self.rear = (self.rear + 1) % len(self.elements)    # 并同时将队尾的索引 rear 更新为 (rear+1) mod capacity
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.front = (self.front + 1) % len(self.elements)  # 队列不为空时，从队首删除一个元素，
        return True                                         # 并同时将队首的索引 front 更新为 (front+1) mod capacity。

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.rear = (self.rear - 1) % len(self.elements)    # 队列不为空时，从队尾删除一个元素。
        return True                                         # 并同时将队尾的索引 rear 更新为 (rear − 1 + capacity) mod capacity。

    def getFront(self) -> int:          # 返回队首的元素，需要检测队列是否为空。
        return -1 if self.isEmpty() else self.elements[self.front]

    def getRear(self) -> int:           # 返回队尾的元素，需要检测队列是否为空。
        return -1 if self.isEmpty() else self.elements[(self.rear - 1) % len(self.elements)]

    def isEmpty(self) -> bool:  # 根据循环队列的定义，队列判空的条件是 front = rear
        return self.rear == self.front

    def isFull(self) -> bool:   # 队列判满的条件是 front = (rear+1) mod capacity
        return (self.rear + 1) % len(self.elements) == self.front


"""方法二：链表"""
class Node:
    __slots__ = 'prev', 'next', 'val'   # 初始化链表节点

    def __init__(self, val):
        self.prev = self.next = None
        self.val = val

class MyCircularDeque:
    def __init__(self, k: int):
        self.head = self.tail = None    # 初始化队列，head, tail 初始化为空。
        self.capacity = k
        self.size = 0                   # 初始化队列元素数量 size 为 0。

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        node = Node(value)
        if self.isEmpty():
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
        self.size += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        node = Node(value)
        if self.isEmpty():
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        self.size += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        self.size -= 1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.tail = self.tail.prev
        if self.tail:
            self.tail.next = None
        self.size -= 1
        return True

    def getFront(self) -> int:
        return -1 if self.isEmpty() else self.head.val

    def getRear(self) -> int:
        return -1 if self.isEmpty() else self.tail.val

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.capacity


if __name__ == "__main__":
    circularDeque = MyCircularDeque(3)      # 设置容量大小为3
    print(circularDeque.insertLast(1))      # 返回 True
    print(circularDeque.insertLast(2))      # 返回 True
    print(circularDeque.insertFront(3))     # 返回 True
    print(circularDeque.insertFront(4))     # 已经满了，返回 False
    print(circularDeque.getRear())          # 返回 2
    print(circularDeque.isFull())           # 返回 True
    print(circularDeque.deleteLast())       # 返回 True
    print(circularDeque.insertFront(4))     # 返回 True
    print(circularDeque.getFront())         # 返回 4
