class MyStack(object):
    """模拟栈"""

    def __init__(self):
        self.items = []

    def is_empty(self):
        """判断是否为空"""
        return self.items == []

    def size(self):
        """返回栈的大小"""
        return len(self.items)

    def push(self, item):
        """压栈(加入元素)"""
        self.items.append(item)


    def pop(self):
        """弹栈(弹出元素)"""
        if len(self.items)>0:
            return self.items.pop()
        else:
            print("栈已经为空")
            return None

    def top(self):
        """返回栈顶元素"""
        if not self.is_empty():
            return self.items[len(self.items) - 1]
        else:
            return None

s = MyStack()
s.push(4)
print("栈顶元素为："+str(s.top()))
print("栈大小为："+str(s.size()))
s.pop()
print("弹栈成功")
s.pop()
"""
栈顶元素为：4
栈大小为：1
弹栈成功
栈已经为空
"""
