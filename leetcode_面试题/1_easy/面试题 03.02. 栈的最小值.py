"""
https://leetcode-cn.com/problems/min-stack-lcci/

请设计一个栈，除了常规栈支持的pop与push函数以外，还支持min函数，该函数返回栈元素中的最小值。执行push、pop和min操作的时间复杂度必须为O(1)。

示例：
    MinStack minStack = new MinStack();
    minStack.push(-2);
    minStack.push(0);
    minStack.push(-3);
    minStack.getMin();   --> 返回 -3.
    minStack.pop();
    minStack.top();      --> 返回 0.
    minStack.getMin();   --> 返回 -2.

"""
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
        self.min_stack.append(min(x, self.min_stack[-1]))   # 如果self.min_stack是每个数字都维护了一个最小值，则在pop的时候，可以直接删除
    
    # 删除栈顶的元素
    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()    # 直接Pop,不会发生队空的情况

    # 获取栈顶元素
    def top(self) -> int:
        return self.stack[-1]

    # 检索栈中的最小元素
    def getMin(self) -> int:
        return self.min_stack[-1]
    
""" 解法2 只有当最小值需要更新时才入栈"""
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