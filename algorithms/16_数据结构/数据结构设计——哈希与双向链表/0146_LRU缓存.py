"""
https://leetcode-cn.com/problems/lru-cache/

请你设计并实现一个满足  LRU (最近最少使用) 缓存 约束的数据结构。

实现 LRUCache 类：
    LRUCache(int capacity) 以 正整数 作为容量 capacity 初始化 LRU 缓存
    int get(int key) 如果关键字 key 存在于缓存中，则返回关键字的值，否则返回 -1 。
    void put(int key, int value) 
        如果关键字 key 已经存在，则变更其数据值 value ；
        如果不存在，则向缓存中插入该组 key-value 。
        如果插入操作导致关键字数量超过 capacity ，则应该 逐出 最久未使用的关键字。

函数 get 和 put 必须以 O(1) 的平均时间复杂度运行。

示例：
    输入
        ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
        [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
    
    输出
        [null, null, null, 1, null, -1, null, -1, 3, 4]

    解释
        LRUCache lRUCache = new LRUCache(2);
        lRUCache.put(1, 1); // 缓存是 {1=1}
        lRUCache.put(2, 2); // 缓存是 {1=1, 2=2}
        lRUCache.get(1);    // 返回 1
        lRUCache.put(3, 3); // 该操作会使得关键字 2 作废，缓存是 {1=1, 3=3}
        lRUCache.get(2);    // 返回 -1 (未找到)
        lRUCache.put(4, 4); // 该操作会使得关键字 1 作废，缓存是 {4=4, 3=3}
        lRUCache.get(1);    // 返回 -1 (未找到)
        lRUCache.get(3);    // 返回 3
        lRUCache.get(4);    // 返回 4

提示：
    1 <= capacity <= 3000
    0 <= key <= 10000
    0 <= value <= 10^5
    最多调用 2 * 10^5 次 get 和 put

"""
from collections import OrderedDict

""" 解法1：使用结合了哈希表与双向链表的数据结构 OrderedDict """
class LRUCache(OrderedDict):

    def __init__(self, capacity: int):
        super().__init__()
        self.capacity = capacity


    def get(self, key: int) -> int:
        if key not in self:
            return -1
        self.move_to_end(key)
        return self[key]

    def put(self, key: int, value: int) -> None:
        if key in self:
            self.move_to_end(key)
        self[key] = value
        if len(self) > self.capacity:
            self.popitem(last=False)


""" 解法2：使用 哈希表 + 双向链表 """
class DLinkedNode:
    def __init__(self, key = 0, value = 0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = dict()
        # 使用伪头部和伪尾部节点      # 双向链表按照被使用的顺序存储了这些键值对
        self.head = DLinkedNode()   # 靠近头部的键值对是最近使用的
        self.tail = DLinkedNode()   # 而靠近尾部的键值对是最久未使用的。
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity
        self.size = 0

    def get(self, key: int) -> int: # 对于 get 操作，首先判断 key 是否存在：
        if key not in self.cache:   # 如果 key 不存在，则返回 −1
            return -1
        node = self.cache[key]  # 如果 key 存在，则 key 对应的节点是最近被使用的节点，通过哈希表定位到该节点在双向链表中的位置
        self.moveToHead(node)   # 并将其移动到双向链表的头部
        return node.value       # 最后返回该节点的值

    def put(self, key: int, value: int) -> None:    # 对于 put 操作，首先判断 key 是否存在：
        if key not in self.cache:           # 如果 key 不存在
            node = DLinkedNode(key, value)  # 使用 key 和 value 创建一个新的节点，
            self.cache[key] = node  # 将 key 和该节点添加进哈希表中
            self.addToHead(node)    # 并在双向链表的头部添加该节点
            self.size += 1
            if self.size > self.capacity:   # 如果超出容量，
                removed = self.removeTail() # 删除双向链表的尾部节点
                self.cache.pop(removed.key) # 并且删除哈希表中对应的项
                self.size -= 1
        else:                       # 如果 key 存在
            node = self.cache[key]  # 先通过哈希表定位
            node.value = value      # 再将对应的节点的值更新为 value
            self.moveToHead(node)   # 并将该节点移到双向链表的头部。
    
    def addToHead(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
    
    def removeNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def moveToHead(self, node):
        self.removeNode(node)
        self.addToHead(node)

    def removeTail(self):
        node = self.tail.prev
        self.removeNode(node)
        return node
    
if __name__ == "__main__":
    cache = LRUCache(2)      # 容量为 2
    print(cache.put(1, 1))   # 缓存是 {1=1}
    print(cache.put(2, 2))   # 缓存是 {1=1, 2=2}
    print(cache.get(1))      # 返回  1
    print(cache.put(3, 3))   # 该操作会使得密钥 2 作废，缓存是 {1=1, 3=3} （逐出最久未使用的关键字）
    print(cache.get(2))      # 返回 -1 (未找到)
    print(cache.put(4, 4))   # 该操作会使得密钥 1 作废，缓存是 {4=4, 3=3}
    print(cache.get(1))      # 返回 -1 (未找到)
    print(cache.get(3))      # 返回  3
    print(cache.get(4))      # 返回  4
    
