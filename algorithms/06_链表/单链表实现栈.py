'''
链表栈是以单链表为基础实现的栈数据结构，主要有以下几个关键点：
    栈顶元素：栈顶元素即为链表的头结点
    压栈：向链表的头结点插进入栈元素，无表头链表则替换插入元素为头结点
    弹栈：弹出链表头结点，并将链表头结点替换为下一个元素
    维护头指针和链表长度；每次压入元素则在头结点前插入新结点，取出元素则删除头结点。
'''
class Empty(Exception):
    """尝试对空栈进行删除操作时抛出的异常"""
    pass


class _Node:
    """节点类"""

    def __init__(self, element, next=None):
        """
        :param element: 节点代表的对象元素
        :param next: 节点对象中用于指向下一个节点的实例属性
        """
        self.element = element
        self.next = next


class LinkedStack:
    """使用单链表实现的栈"""

    def __init__(self):
        """创建一个空的栈"""
        self._head = None  # 初始化头节点
        self._size = 0  # 保存栈的元素数量

    def __len__(self):
        """
        返回栈中当前元素数目
        :return: 栈的元素数量
        """
        return self._size

    def is_empty(self):
        """
        判断当前栈是否为空，如是则返回True
        :return: 栈是否为空
        """
        return self._size == 0

    def push(self, element):
        """
        :param element:
        :return: None
        """
        node = _Node(element)  # 将元素封装进节点
        node.next = self._head  # 先让新节点的next域指向原头节点
        self._head = node  # 让新节点成为头节点
        self._size += 1

    def top(self):
        """
        返回但不删除栈顶元素，当栈为空时抛出异常
        :return: 栈顶元素
        """
        if self.is_empty():
            raise Empty('栈为空！')
        return self._head.element  # 栈顶元素即为单链表头部元素

    def pop(self):
        """
        删除并返回栈顶元素，当栈为空时抛出异常
        :return: 栈顶元素
        """
        if self.is_empty():
            raise Empty('栈为空！')
        ans = self._head.element
        self._head = self._head.next  # 使当前头节点的下一个节点作为新的头节点
        self._size -= 1
        return ans


def main():
    stack = LinkedStack()
    stack.push(5)
    stack.push(3)
    print(len(stack))        # 输出为：2
    print(stack.pop())       # 输出为：3
    print(stack.is_empty())  # 输出为：False
    print(stack.pop())       # 输出为：5
    print(stack.is_empty())  # 输出为：True

if __name__ == '__main__':
    main()