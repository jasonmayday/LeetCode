"""
请定义一个队列并实现函数 max_value 得到队列里的最大值，要求函数max_value、push_back 和 pop_front 的均摊时间复杂度都是O(1)。

若队列为空，pop_front 和 max_value 需要返回 -1

示例 1：
    输入: 
    ["MaxQueue","push_back","push_back","max_value","pop_front","max_value"]
    [[],[1],[2],[],[],[]]
    输出: [null,null,null,2,1,2]

示例 2：
    输入: 
    ["MaxQueue","pop_front","max_value"]
    [[],[],[]]
    输出: [null,-1,-1]

限制：
    1 <= push_back,pop_front,max_value的总操作数 <= 10000
    1 <= value <= 10^5

"""
import queue

""" 使用辅助双向队列"""
class MaxQueue:
    def __init__(self):
        self.queue = queue.Queue()
        self.deque = queue.deque()

    def max_value(self) -> int:
        return self.deque[0] if self.deque else -1

    def push_back(self, value: int) -> None:
        self.queue.put(value)
        while self.deque and self.deque[-1] < value:    # 若入队一个比队列某些元素更大的数字 x
            self.deque.pop()                            # 则为了保持此列表递减，需要将双向队列 尾部所有小于 x 的元素 弹出。
        self.deque.append(value)

    def pop_front(self) -> int:
        if self.queue.empty():
            return -1
        val = self.queue.get()
        if val == self.deque[0]:
            self.deque.popleft()
        return val
    
if __name__ == "__main__":
    q = MaxQueue()
    q.push_back(1)          # [1]
    q.push_back(2)          # [1, 2]
    print (q.max_value())   # 2
    print (q.pop_front())   # 1
    print (q.max_value())   # 1
