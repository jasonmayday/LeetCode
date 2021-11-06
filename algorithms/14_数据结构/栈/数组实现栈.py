'''

'''

class ArrayStack(object):
    """模拟栈"""

    def __init__(self):
        self.items = []
    
    def __len__(self):
        return len(self.items)

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

if __name__ == '__main__':
  S = ArrayStack()                 # contents: [ ]
  S.push(5)                        # contents: [5]
  S.push(3)                        # contents: [5, 3]
  print(len(S))                    # contents: [5, 3];      outputs 2
  print(S.pop())                   # contents: [5];         outputs 3
  print(S.is_empty())              # contents: [5];         outputs False
  print(S.pop())                   # contents: [ ];         outputs 5
  print(S.is_empty())              # contents: [ ];         outputs True
  S.push(7)                        # contents: [7]
  S.push(9)                        # contents: [7, 9]
  print(S.top())                   # contents: [7, 9];      outputs 9
  S.push(4)                        # contents: [7, 9, 4]
  print(len(S))                    # contents: [7, 9, 4];   outputs 3
  print(S.pop())                   # contents: [7, 9];      outputs 4
  S.push(6)                        # contents: [7, 9, 6]
  S.push(8)                        # contents: [7, 9, 6, 8]
  print(S.pop())                   # contents: [7, 9, 6];   outputs 8