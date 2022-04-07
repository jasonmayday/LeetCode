'''
https://leetcode-cn.com/problems/bao-han-minhan-shu-de-zhan-lcof/

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
    
注意：本题与主站 155 题相同：https://leetcode-cn.com/problems/min-stack/

'''
import math

""" 本题难点：获取栈最小值 min() 函数需要遍历整个栈，复杂度为 O(N) 。
    借助辅助栈实现："""
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
    
""" 解法2 """
class MinStack:
    def __init__(self):
        self.A, self.B = [], []

    def push(self, x: int) -> None:
        self.A.append(x)                    # 执行「元素 x 压入栈 A」 ；
        if not self.B or self.B[-1] >= x:   # 保持栈 B 的元素是 非严格降序 的；
            self.B.append(x)                # 若「栈 B 为空」或「x ≤ 栈 B 的栈顶元素」，则执行「元素 x 压入栈 B」 ；

    def pop(self) -> None:
        if self.A.pop() == self.B[-1]:  # 执行「栈 A 元素出栈」，将出栈元素记为 y ；
            self.B.pop()                # 若 「y 等于栈 B 的栈顶元素」，则执行「栈 B 元素出栈」；

    def top(self) -> int:
        return self.A[-1]

    def getMin(self) -> int:
        return self.B[-1]


if __name__ == "__main__":
    minStack = MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    print(minStack.getMin())   # 返回 -3
    minStack.pop()
    print(minStack.top())      # 返回  0
    print(minStack.getMin())   # 返回 -2