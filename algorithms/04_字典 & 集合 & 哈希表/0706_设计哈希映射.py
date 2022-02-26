"""
https://leetcode-cn.com/problems/design-hashmap/

不使用任何内建的哈希表库设计一个哈希映射（HashMap）。

实现 MyHashMap 类：
    MyHashMap() 用空映射初始化对象
    void put(int key, int value) 向 HashMap 插入一个键值对 (key, value) 。如果 key 已经存在于映射中，则更新其对应的值 value 。
    int get(int key) 返回特定的 key 所映射的 value ；如果映射中不包含 key 的映射，返回 -1 。
    void remove(key) 如果映射中存在 key 的映射，则移除 key 和它所对应的 value 。

示例：
    输入：
        ["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"]
        [[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]
    输出：
        [nu 1, null, 1, null, -1]

    解释：
        MyHashMap myHashMap = new MyHashMap();
        myHashMap.put(1, 1); // myHashMap 现在为 [[1,1]]
        myHashMap.put(2, 2); // myHashMap 现在为 [[1,1], [2,2]]
        myHashMap.get(1);    // 返回 1 ，myHashMap 现在为 [[1,1], [2,2]]
        myHashMap.get(3);    // 返回 -1（未找到），myHashMap 现在为 [[1,1], [2,2]]
        myHashMap.put(2, 1); // myHashMap 现在为 [[1,1], [2,1]]（更新已有的值）
        myHashMap.get(2);    // 返回 1 ，myHashMap 现在为 [[1,1], [2,1]]
        myHashMap.remove(2); // 删除键为 2 的数据，myHashMap 现在为 [[1,1]]
        myHashMap.get(2);    // 返回 -1（未找到），myHashMap 现在为 [[1,1]]

提示：

    0 <= key, value <= 10^6
    最多调用 10^4 次 put、get 和 remove 方法
 
进阶：你能否不使用内置的 HashMap 库解决此问题？

"""


''' 解法1：超大数组
    能使用超大数组来解决本题是因为输入数据的范围在 0 <= key <= 10^6 
    因此我们只需要 10 ^ 6 + 1 大小的数组，就能让每个数据都有一个单独的索引，不会有 key 的碰撞问题。'''
class MyHashMap(object):

    def __init__(self):
        self.map = [-1] * 1000001

    def put(self, key, value):
        self.map[key] = value

    def get(self, key):
        return self.map[key]

    def remove(self, key):
        self.map[key] = -1


''' 解法2：拉链法
    我们定义了一个比较小的数组，然后使用 hash 方法来把求出 key 应该出现在数组中的位置；
    但是由于不同的 key 在求完 hash 之后，可能会存在碰撞冲突，所以数组并不直接保存元素，而是每个位置都指向了一条链表（或数组）用于存储元素。
    我们可以看出在查找一个 key 的时候需要两个步骤：
    1. 求hash到数组中的位置；
    2. 在链表中遍历找key。'''
class MyHashMap(object):

    def __init__(self):
        self.map = [[-1] * 1000 for _ in range(1001)]

    def put(self, key, value):
        row, col = key // 1000, key % 1000
        self.map[row][col] = value

    def get(self, key):
        row, col = key // 1000, key % 1000
        return self.map[row][col]

    def remove(self, key):
        row, col = key // 1000, key % 1000
        self.map[row][col] = -1

    
''' 解法3：不定长拉链数组
    不定长的拉链数组是说拉链会根据分桶中的 key 动态增长，更类似于真正的链表。
    分桶数一般取质数，这是因为经验上来说，质数个的分桶能让数据更加分散到各个桶中。
    下面的代码中把分桶数去了 1009，是因为 1009 是大于 1000 的第一个质数。'''
class MyHashMap:

    def __init__(self):
        self.buckets = 1009
        self.table = [[] for _ in range(self.buckets)]

    def hash(self, key):
        return key % self.buckets
    
    def put(self, key: int, value: int) -> None:
        hashkey = self.hash(key)
        for item in self.table[hashkey]:
            if item[0] == key:
                item[1] = value
                return
        self.table[hashkey].append([key, value])

    def get(self, key: int) -> int:
        hashkey = self.hash(key)
        for item in self.table[hashkey]:
            if item[0] == key:
                return item[1]
        return -1

    def remove(self, key: int) -> None:
        hashkey = self.hash(key)
        for i, item in enumerate(self.table[hashkey]):
            if item[0] == key:
                self.table[hashkey].pop(i)
                return


if __name__ == '__main__':
    myHashMap = MyHashMap()
    myHashMap.put(1, 1)         # myHashMap 现在为 [[1,1]]
    myHashMap.put(2, 2)         # myHashMap 现在为 [[1,1], [2,2]]
    print (myHashMap.get(1))    # 返回 1 ，myHashMap 现在为 [[1,1], [2,2]]
    print (myHashMap.get(3))    # 返回 -1（未找到），myHashMap 现在为 [[1,1], [2,2]]
    myHashMap.put(2, 1)         # myHashMap 现在为 [[1,1], [2,1]]（更新已有的值）
    print (myHashMap.get(2))    # 返回 1 ，myHashMap 现在为 [[1,1], [2,1]]
    myHashMap.remove(2)         # 删除键为 2 的数据，myHashMap 现在为 [[1,1]]
    print (myHashMap.get(2))    # 返回 -1（未找到），myHashMap 现在为 [[1,1]]