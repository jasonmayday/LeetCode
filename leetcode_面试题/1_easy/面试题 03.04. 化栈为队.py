"""
https://leetcode-cn.com/problems/implement-queue-using-stacks-lcci/

实现一个MyQueue类，该类用两个栈来实现一个队列。

示例：
    MyQueue queue = new MyQueue();

    queue.push(1);
    queue.push(2);
    queue.peek();  // 返回 1
    queue.pop();   // 返回 1
    queue.empty(); // 返回 false

说明：
    你只能使用标准的栈操作 -- 也就是只有 push to top, peek/pop from top, size 和 is empty 操作是合法的。
    你所使用的语言也许不支持栈。你可以使用 list 或者 deque（双端队列）来模拟一个栈，只要是标准的栈操作即可。
    假设所有操作都是有效的 （例如，一个空的队列不会调用 pop 或者 peek 操作）。

本题与主站 232 题相同：：https://leetcode-cn.com/problems/implement-queue-using-stacks/

"""

class MyQueue:
    def __init__(self):
        self.s1 = []
        self.s2 = []
        self.front = None

    def push(self, x: int) -> None:
        """Push element x to the back of queue."""
        if not self.s1: self.front = x
        self.s1.append(x)
        
    def pop(self) -> int:
        """Removes the element from in front of queue and returns that element."""
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
            self.front = None
        return self.s2.pop()

    def peek(self) -> int:
        """Get the front element."""
        if self.s2:
            return self.s2[-1]
        return self.front

    def empty(self) -> bool:
        """Returns whether the queue is empty."""
        if not self.s1 and not self.s2:
            return True
        return False

if __name__ == "__main__":
    obj = MyQueue()
    obj.push(1)
    param_2 = obj.pop()
    param_3 = obj.peek()
    param_4 = obj.empty()