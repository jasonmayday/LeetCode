'''
链表栈是以单链表为基础实现的栈数据结构，主要有以下几个关键点：
    栈顶元素：栈顶元素即为链表的头结点
    压栈：向链表的头结点插进入栈元素，无表头链表则替换插入元素为头结点
    弹栈：弹出链表头结点，并将链表头结点替换为下一个元素
'''
class Node:
    def __init__(self, val=None, nxt=None):
        self.value = val
        self.next = nxt
    
    def __str__(self):
        return str(self.value)