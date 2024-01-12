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
        self.stack1 = []    # stack1 存放新进入的元素
        self.stack2 = []    # stack2 存放已经完成倒序的元素, 这样B出栈就相当于队列出队

    def push(self, x: int) -> None: # 加在 stack1 里面
        self.stack1.append(x)

    def pop(self) -> int:           # 移除并返回队列最前端的元素
        if len(self.stack2) == 0:   # 如果 stack2 为空
            while self.stack1:      # 那么就从 stack1 里面所有元素出栈并放入 stack2 中
                self.stack2.append(self.stack1.pop())   # 这样所有A的元素都完成倒序了。之后从B中出栈即可
        return self.stack2.pop()    # 如果 stack2 中有元素，说明还有完成倒序的元素存在，直接 stack2 出栈

    def peek(self) -> int:          # 返回队列最前端的元素（不移除）
        if len(self.stack2) == 0:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2[-1]

    def empty(self) -> bool:        # 返回队列是否为空
        return len(self.stack2) == 0 and len(self.stack1) == 0

if __name__ == "__main__":
    obj = MyQueue()
    obj.push(1)
    param_2 = obj.pop()
    param_3 = obj.peek()
    param_4 = obj.empty()