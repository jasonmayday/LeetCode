"""
https://leetcode-cn.com/problems/logger-rate-limiter/

请你设计一个日志系统，可以流式接收消息以及它的时间戳。每条 不重复 的消息最多只能每 10 秒打印一次。也就是说，如果在时间戳 t 打印某条消息，那么相同内容的消息直到时间戳变为 t + 10 之前都不会被打印。

所有消息都按时间顺序发送。多条消息可能到达同一时间戳。

实现 Logger 类：
    Logger() 初始化 logger 对象
    bool shouldPrintMessage(int timestamp, string message) 如果这条消息 message 在给定的时间戳 timestamp 应该被打印出来，则返回 true ，否则请返回 false 。

示例：
    输入：
        ["Logger", "shouldPrintMessage", "shouldPrintMessage", "shouldPrintMessage", "shouldPrintMessage", "shouldPrintMessage", "shouldPrintMessage"]
        [[], [1, "foo"], [2, "bar"], [3, "foo"], [8, "bar"], [10, "foo"], [11, "foo"]]
    输出：
        [null, true, true, false, false, false, true]

    解释：
        Logger logger = new Logger();
        logger.shouldPrintMessage(1, "foo");  // 返回 true ，下一次 "foo" 可以打印的时间戳是 1 + 10 = 11
        logger.shouldPrintMessage(2, "bar");  // 返回 true ，下一次 "bar" 可以打印的时间戳是 2 + 10 = 12
        logger.shouldPrintMessage(3, "foo");  // 3 < 11 ，返回 false
        logger.shouldPrintMessage(8, "bar");  // 8 < 12 ，返回 false
        logger.shouldPrintMessage(10, "foo"); // 10 < 11 ，返回 false
        logger.shouldPrintMessage(11, "foo"); // 11 >= 11 ，返回 true ，下一次 "foo" 可以打印的时间戳是 11 + 10 = 21

提示：
    0 <= timestamp <= 10^9
    每个 timestamp 都将按非递减顺序（时间顺序）传递
    1 <= message.length <= 30
    最多调用 10^4 次 shouldPrintMessage 方法

"""

""" 方法一：队列 + 集合 """
from collections import deque

class Logger(object):
    def __init__(self):
        self.msg_set = set()
        self.msg_queue = deque()

    def shouldPrintMessage(self, timestamp, message):
        while self.msg_queue:
            msg, ts = self.msg_queue[0]
            if timestamp - ts >= 10:
                self.msg_queue.popleft()
                self.msg_set.remove(msg)
            else:
                break

        if message not in self.msg_set:
            self.msg_set.add(message)
            self.msg_queue.append((message, timestamp))
            return True
        else:
            return False

""" 方法二：哈希表 / 字典 """
class Logger(object):

    def __init__(self):
        self.dict = {}

    def shouldPrintMessage(self, timestamp, message):
        if message not in self.dict:                # case 1). add the message to print
            self.dict[message] = timestamp
            return True

        if timestamp - self.dict[message] >= 10:    # case 2). update the timestamp of the message
            self.dict[message] = timestamp
            return True

        else:
            return False

if __name__ == "__main__":
    logger = Logger()
    print(logger.shouldPrintMessage(1, "foo"))  # 返回 true ，下一次 "foo" 可以打印的时间戳是 1 + 10 = 11
    print(logger.shouldPrintMessage(2, "bar"))  # 返回 true ，下一次 "bar" 可以打印的时间戳是 2 + 10 = 12
    print(logger.shouldPrintMessage(3, "foo"))  # 3 < 11 ，返回 false
    print(logger.shouldPrintMessage(8, "bar"))  # 8 < 12 ，返回 false
    print(logger.shouldPrintMessage(10, "foo")) # 10 < 11 ，返回 false
    print(logger.shouldPrintMessage(11, "foo")) # 11 >= 11 ，返回 true ，下一次 "foo" 可以打印的时间戳是 11 + 10 = 21