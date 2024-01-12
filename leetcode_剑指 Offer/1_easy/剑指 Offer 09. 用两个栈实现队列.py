"""
用两个栈实现一个队列。队列的声明如下，请实现它的两个函数 appendTail 和 deleteHead ，分别完成在队列尾部插入整数和在队列头部删除整数的功能。(若队列中没有元素，deleteHead 操作返回 -1 )

示例 1：
    输入：
        ["CQueue","appendTail","deleteHead","deleteHead"]
        [[],[3],[],[]]
    输出：[null,null,3,-1]

示例 2：
    输入：
        ["CQueue","deleteHead","appendTail","appendTail","deleteHead","deleteHead"]
        [[],[],[5],[2],[],[]]
    输出：[null,-1,null,null,5,2]

提示：
    1 <= values <= 10000
    最多会对 appendTail、deleteHead 进行 10000 次调用

"""

class CQueue:
    def __init__(self):
        self.A = []
        self.B = []

    def appendTail(self, value: int) -> None:
        self.A.append(value)    # 直接将数字压入栈 A

    def deleteHead(self) -> int:
        if self.B:              # 如果栈 B 有元素
            return self.B.pop() # 弹出栈顶元素
        if not self.A:          # 如果栈 A 有元素
            return -1           # 说明队列中没有元素，返回 -1 
        while self.A:                   # 如果栈 A 有元素
            self.B.append(self.A.pop()) # 执行倒序，把 A 的元素弹出，加入B
        return self.B.pop()
    
if __name__ == "__main__":
    cQueue = CQueue()
    print (cQueue.deleteHead())
    print (cQueue.appendTail(5))
    print (cQueue.appendTail(2))
    print (cQueue.deleteHead())
    print (cQueue.deleteHead())