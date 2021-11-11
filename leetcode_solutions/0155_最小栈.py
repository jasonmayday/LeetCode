'''
https://leetcode-cn.com/problems/min-stack/

设计一个支持 push ，pop ，top 操作，并能在常数时间内检索到最小元素的栈。
    push(x) —— 将元素 x 推入栈中。
    pop() —— 删除栈顶的元素。
    top() —— 获取栈顶元素。
    getMin() —— 检索栈中的最小元素。
 
示例:
    输入：
    ["MinStack","push","push","push","getMin","pop","top","getMin"]
    [[],[-2],[0],[-3],[],[],[],[]]

    输出：
    [null,null,null,null,-3,null,0,-2]

    解释：
    MinStack minStack = new MinStack();
    minStack.push(-2);
    minStack.push(0);
    minStack.push(-3);
    minStack.getMin();   --> 返回 -3.
    minStack.pop();
    minStack.top();      --> 返回 0.
    minStack.getMin();   --> 返回 -2.
 
提示：
    pop、top 和 getMin 操作总是在 非空栈 上调用。

'''
import math

class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = [math.inf]

    # 将元素 x 推入栈中
    def push(self, x: int) -> None:
        self.stack.append(x)
        self.min_stack.append(min(x, self.min_stack[-1]))
    
    # 删除栈顶的元素
    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    # 获取栈顶元素
    def top(self) -> int:
        return self.stack[-1]

    # 检索栈中的最小元素
    def getMin(self) -> int:
        return self.min_stack[-1]

