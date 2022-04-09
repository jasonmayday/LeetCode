"""
https://leetcode-cn.com/problems/three-in-one-lcci/

三合一。描述如何只用一个数组来实现三个栈。

你应该实现push(stackNum, value)、pop(stackNum)、isEmpty(stackNum)、peek(stackNum)方法。stackNum表示栈下标，value表示压入的值。

构造函数会传入一个stackSize参数，代表每个栈的大小。

示例1:
    输入：
        ["TripleInOne", "push", "push", "pop", "pop", "pop", "isEmpty"]
        [[1], [0, 1], [0, 2], [0], [0], [0], [0]]
    输出：
        [null, null, null, 1, -1, -1, true]
        说明：当栈为空时`pop, peek`返回-1，当栈满时`push`不压入元素。
示例2:
    输入：
        ["TripleInOne", "push", "push", "push", "pop", "pop", "pop", "peek"]
        [[2], [0, 1], [0, 2], [0, 3], [0], [0], [0], [0]]
    输出：
        [null, null, null, null, 2, 1, -1, -1]
 
提示：
    0 <= stackNum <= 2

"""

""" 使用一个二维列表实现三个栈"""
class TripleInOne:

    def __init__(self, stackSize: int):             # 每一个三合一栈有以下属性：
        self.TripleStack = [[] for _ in range(3)]   # 二维列表表示三个栈：[[], [], []]
        self.stackSize = stackSize                  # stackSize参数，代表每个栈的大小。

    def push(self, stackNum: int, value: int) -> None:
        if len(self.TripleStack[stackNum]) < self.stackSize:    # 需要插入数字那个栈的长度 小于 三合一栈的stackSize参数时
            self.TripleStack[stackNum].append(value)            # 才执行push命令

    def pop(self, stackNum: int) -> int:
        if self.TripleStack[stackNum] != []:        # 需要pop的栈不为空
            value = self.TripleStack[stackNum][-1]  # 需要弹出的元素
            self.TripleStack[stackNum] = self.TripleStack[stackNum][:-1]    # 弹出元素后的栈（数组）
            return value                            # 返回弹出的元素
        else:
            return -1

    def peek(self, stackNum: int) -> int:           # 与pop相似，只是不改变 TripleStack[stackNum] 的信息
        if self.TripleStack[stackNum] != []:
            value = self.TripleStack[stackNum][-1]
            return value
        else:
            return -1

    def isEmpty(self, stackNum: int) -> bool:
        return self.TripleStack[stackNum] == []
    
    
""" 使用一个二维列表实现三个栈"""
class TripleInOne:
    def __init__(self, stackSize: int):
        self.stack = [[] for _ in range(3)]
        self.stackSize = stackSize

    def push(self, stackNum: int, value: int) -> None:
        if len(self.stack[stackNum]) < self.stackSize:
            self.stack[stackNum].append(value)

    def pop(self, stackNum: int) -> int:
        return self.stack[stackNum].pop() if self.stack[stackNum] else -1

    def peek(self, stackNum: int) -> int:
        return self.stack[stackNum][-1] if self.stack[stackNum] else -1

    def isEmpty(self, stackNum: int) -> bool:
        return self.stack[stackNum] == []


if __name__ == "__main__":
    tripleInOne = TripleInOne(1)    # 每个栈大小为 1
    tripleInOne.push(0, 1)          # push(stackNum = 0, value = 1)
    tripleInOne.push(0, 2)          # push(stackNum = 0, value = 2)
    print(tripleInOne.pop(0))       # pop(stackNum = 0)
    print(tripleInOne.pop(0))       # pop(stackNum = 0)
    print(tripleInOne.pop(0))       # pop(stackNum = 0)
    print(tripleInOne.isEmpty(0))   # isEmpty(stackNum = 0)