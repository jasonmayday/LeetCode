"""
https://leetcode-cn.com/problems/design-hashset/

不使用任何内建的哈希表库设计一个哈希集合（HashSet）。

实现 MyHashSet 类：
    void add(key) 向哈希集合中插入值 key 。
    bool contains(key) 返回哈希集合中是否存在这个值 key 。
    void remove(key) 将给定值 key 从哈希集合中删除。如果哈希集合中没有这个值，什么也不做。
 
示例：
    输入：
        ["MyHashSet", "add", "add", "contains", "contains", "add", "contains", "remove", "contains"]
        [[], [1], [2], [1], [3], [2], [2], [2], [2]]
    
    输出：
    [n  ull, true, false, null, true, null, false]

    解释：
        MyHashSet myHashSet = new MyHashSet();
        myHashSet.add(1);      // set = [1]
        myHashSet.add(2);      // set = [1, 2]
        myHashSet.contains(1); // 返回 True
        myHashSet.contains(3); // 返回 False ，（未找到）
        myHashSet.add(2);      // set = [1, 2]
        myHashSet.contains(2); // 返回 True
        myHashSet.remove(2);   // set = [1]
        myHashSet.contains(2); // 返回 False ，（已移除）

提示：
    0 <= key <= 10^6
    最多调用 10^4 次 add、remove 和 contains 。

进阶：你可以不使用内建的哈希集合库解决此问题吗？

"""


''' 解法1：超大数组
    能使用超大数组来解决本题是因为输入数据的范围在 0 <= key <= 10^6 
    因此我们只需要 10 ^ 6 + 1 大小的数组，就能让每个数据都有一个单独的索引，不会有 key 的碰撞问题。'''
class MyHashSet:

    def __init__(self):
        self.set = [False] * 1000001

    def add(self, key):
        self.set[key] = True

    def remove(self, key):
        self.set[key] = False

    def contains(self, key):
        return self.set[key]


''' 解法2：拉链法
    我们定义了一个比较小的数组，然后使用 hash 方法来把求出 key 应该出现在数组中的位置；
    但是由于不同的 key 在求完 hash 之后，可能会存在碰撞冲突，所以数组并不直接保存元素，而是每个位置都指向了一条链表（或数组）用于存储元素。
    我们可以看出在查找一个 key 的时候需要两个步骤：
    1. 求hash到数组中的位置；
    2. 在链表中遍历找key。'''
class MyHashSet:

    def __init__(self):
        self.buckets = 1000
        self.itemsPerBucket = 1001
        self.table = [[] for _ in range(self.buckets)]

    def hash(self, key):
        return key % self.buckets
    
    def pos(self, key):
        return key // self.buckets
    
    def add(self, key):
        hashkey = self.hash(key)
        if not self.table[hashkey]:
            self.table[hashkey] = [0] * self.itemsPerBucket
        self.table[hashkey][self.pos(key)] = 1
        
    def remove(self, key):
        hashkey = self.hash(key)
        if self.table[hashkey]:
            self.table[hashkey][self.pos(key)] = 0

    def contains(self, key):
        hashkey = self.hash(key)
        return (self.table[hashkey] != []) and (self.table[hashkey][self.pos(key)] == 1)


''' 解法3：不定长拉链数组
    不定长的拉链数组是说拉链会根据分桶中的 key 动态增长，更类似于真正的链表。
    分桶数一般取质数，这是因为经验上来说，质数个的分桶能让数据更加分散到各个桶中。
    下面的代码中把分桶数去了 1009，是因为 1009 是大于 1000 的第一个质数。'''
class MyHashSet:

    def __init__(self):
        self.buckets = 1009
        self.table = [[] for _ in range(self.buckets)]

    def hash(self, key):
        return key % self.buckets
    
    def add(self, key):
        hashkey = self.hash(key)
        if key in self.table[hashkey]:
            return
        self.table[hashkey].append(key)
        
    def remove(self, key):
        hashkey = self.hash(key)
        if key not in self.table[hashkey]:
            return
        self.table[hashkey].remove(key)

    def contains(self, key):
        hashkey = self.hash(key)
        return key in self.table[hashkey]

if __name__ == '__main__':
    myHashSet = MyHashSet()
    myHashSet.add(1)                # set = [1]
    myHashSet.add(2)                # set = [1, 2]
    print (myHashSet.contains(1))   # 返回 True
    print (myHashSet.contains(3))   # 返回 False ，（未找到）
    myHashSet.add(2)                # set = [1, 2]
    print (myHashSet.contains(2))   # 返回 True
    myHashSet.remove(2)             # set = [1]
    print (myHashSet.contains(2))   # 返回 False ，（已移除）
