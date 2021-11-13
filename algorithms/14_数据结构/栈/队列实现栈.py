
import collections

"""
使用2个队列

为了满足栈的特性，即最后入栈的元素最先出栈，在使用队列实现栈时，应满足队列前端的元素是最后入栈的元素。
可以使用两个队列实现栈的操作，其中 queue1用于存储栈内的元素，queue2 作为入栈操作的辅助队列。

入栈操作时，首先将元素入队到 queue2，然后将queue1的全部元素依次出队并入队到queue2，此时queue2的前端的元素即为新入栈的元素，
再将queue1和queue2互换，则queue1的元素即为栈内的元素，queue1的前端和后端分别对应栈顶和栈底。

由于每次入栈操作都确保queue1的前端元素为栈顶元素，因此出栈操作和获得栈顶元素操作都可以简单实现。
出栈操作只需要移除queue1的前端元素并返回即可，获得栈顶元素操作只需要获得queue1的前端元素并返回即可（不移除元素）。

由于queue1用于存储栈内的元素，判断栈是否为空时，只需要判断queue1是否为空即可。
"""
class MyStack:
    def __init__(self):
        self.queue1 = collections.deque()
        self.queue2 = collections.deque()

    def push(self, x: int) -> None:
        """Push element x onto stack."""
        self.queue2.append(x)
        while self.queue1:
            self.queue2.append(self.queue1.popleft())
        self.queue1, self.queue2 = self.queue2, self.queue1

    def pop(self) -> int:
        """Removes the element on top of the stack and returns that element."""
        return self.queue1.popleft()

    def top(self) -> int:
        """Get the top element."""
        return self.queue1[0]

    def empty(self) -> bool:
        """Returns whether the stack is empty."""
        return not self.queue1


"""使用1个队列

使用一个队列时，为了满足栈的特性，即最后入栈的元素最先出栈，同样需要满足队列前端的元素是最后入栈的元素。

入栈操作时，首先获得入栈前的元素个数 nn，然后将元素入队到队列，再将队列中的前 nn 个元素（即除了新入栈的元素之外的全部元素）依次出队并入队到队列，此时队列的前端的元素即为新入栈的元素，且队列的前端和后端分别对应栈顶和栈底。

由于每次入栈操作都确保队列的前端元素为栈顶元素，因此出栈操作和获得栈顶元素操作都可以简单实现。出栈操作只需要移除队列的前端元素并返回即可，获得栈顶元素操作只需要获得队列的前端元素并返回即可（不移除元素）。

由于队列用于存储栈内的元素，判断栈是否为空时，只需要判断队列是否为空即可。

"""
class MyStack:
    def __init__(self):
        self.queue = collections.deque()

    def push(self, x: int) -> None:
        """Push element x onto stack."""
        n = len(self.queue)
        self.queue.append(x)
        for _ in range(n):
            self.queue.append(self.queue.popleft())

    def pop(self) -> int:
        """Removes the element on top of the stack and returns that element."""
        return self.queue.popleft()

    def top(self) -> int:
        """Get the top element."""
        return self.queue[0]

    def empty(self) -> bool:
        """Returns whether the stack is empty."""
        return not self.queue

