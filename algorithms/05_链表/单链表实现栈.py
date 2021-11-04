'''
链表栈是以单链表为基础实现的栈数据结构，主要有以下几个关键点：
    栈顶元素：栈顶元素即为链表的头结点
    压栈：向链表的头结点插进入栈元素，无表头链表则替换插入元素为头结点
    弹栈：弹出链表头结点，并将链表头结点替换为下一个元素
'''
class LNode(object):
    def __init__(self,x):
        self.data = x
        self.next = None

class MyStack(object):
    def __init__(self):
        #pHead = LNode
        self.data = None
        self.next = None

    def is_empty(self):
        """判断是否为空"""
        if self.next == None:
            return True
        return False

    def size(self):
        """返回栈的大小"""
        size=0
        p = self.next
        while p != None:
        # while p is not None:
            p = p.next
            size += 1
        return size

    def push(self, element):
        """压栈(加入元素)"""
        p = LNode(element)
        p.data = element
        p.next = self.next
        self.next = p

    def pop(self):
        """弹栈(弹出元素)"""
        tmp = self.next
        if tmp != None:
            self.next = tmp.next
        print("栈已经为空")
        return None

    def top(self):
        """返回栈顶元素"""
        if self.next != None:
            return self.next.data
        print("栈已经为空")
        return None

s = MyStack()
s.push(1)
print("栈顶元素为："+str(s.top()))
print("栈大小为："+str(s.size()))
s.pop()
print("弹栈成功")
s.pop()
"""
栈顶元素为：1
栈大小为：1
弹栈成功
栈已经为空
"""
