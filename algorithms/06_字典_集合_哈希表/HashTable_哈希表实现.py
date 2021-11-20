class Array(object):
 
    def __init__(self, size=32, init=None):
        self._size = size
        self._items = [init] * size
 
    def __getitem__(self, index):
        return self._items[index]
 
    def __setitem__(self, index, value):
        self._items[index] = value
 
    def __len__(self):
        return self._size
 
    def clear(self, value=None):
        for i in range(len(self._items)):
            self._items[i] = value
 
    def __iter__(self):
        for item in self._items:
            yield item
 
class Slot(object):
    """
    定义一个 hash 表数组的槽(slot 这里指的就是数组的一个位置)
    hash table 就是一个数组，每个数组的元素（也叫slot槽）是一个对象，对象包含两个属性 key 和 value。
 
    注意，一个槽有三种状态，看你能否想明白。相比链接法解决冲突，探查法删除一个 key 的操作稍微复杂。
    1.从未使用 HashMap.UNUSED。此槽没有被使用和冲突过，查找时只要找到 UNUSED 就不用再继续探查了
    2.使用过但是 remove 了，此时是 HashMap.EMPTY，该探查点后边的元素仍然可能是有key的，需要继续查找
    3.槽正在使用 Slot 节点
    """
 
    def __init__(self, key, value):
        self.key, self.value = key, value
 
class HashTable(object):
    UNUSED = None  # 没被使用过
    EMPTY = Slot(None, None)  # 使用却被删除过
 
    def __init__(self):
        self._table = Array(8, init=HashTable.UNUSED)  # 保持 2*i 次方
        self.length = 0
 
    @property
    def _load_factor(self):
        # load_factor 超过 0.8 重新分配
        return self.length / float(len(self._table))
 
    def __len__(self):
        return self.length
 
    # 进行哈希
    def _hash(self, key):
        return abs(hash(key)) % len(self._table)
 
    # 查找key
    def _find_key(self, key):
        """
        解释一个 slot 为 UNUSED 和 EMPTY 的区别
        因为使用的是二次探查的方式，假如有两个元素 A，B 冲突了，
        首先A hash 得到是 slot 下标5，A 放到了第5个槽，之后插入 B 因为冲突了，所以继续根据二次探查方式放到了 slot下标8。
        然后删除 A，槽 5 被置为 EMPTY。然后我去查找 B，
        第一次 hash 得到的是 槽5，但是这个时候我还是需要第二次计算 hash 才能找到 B。
        但是如果槽是 UNUSED 我就不用继续找了，我认为 B 就是不存在的元素。这个就是 UNUSED 和 EMPTY 的区别。
        """
        origin_index = index = self._hash(key)  # origin_index 判断是否又走到了起点，如果查找一圈了都找不到则无此元素
        _len = len(self._table)
        while self._table[index] is not HashTable.UNUSED:
            if self._table[index] is HashTable.EMPTY:  # 注意如果是 EMPTY，继续寻找下一个槽
                index = (index * 5 + 1) % _len
                if index == origin_index:
                    break
                continue
            if self._table[index].key == key:  # 找到了key
                return index
            else:
                index = (index * 5 + 1) % _len  # 没有找到继续找下一个位置
                if index == origin_index:
                    break
 
        return None
 
    # 找能插入的槽
    def _find_slot_for_insert(self, key):
        index = self._hash(key)
        _len = len(self._table)
        while not self._slot_can_insert(index):  # 直到找到一个可以用的槽
            index = (index * 5 + 1) % _len
        return index
 
    # 槽是否能插入
    def _slot_can_insert(self, index):
        return self._table[index] is HashTable.EMPTY or self._table[index] is HashTable.UNUSED
 
    # in operator，实现之后可以使用 in 操作符判断
    def __contains__(self, key):
        index = self._find_key(key)
        return index is not None
 
    # 添加元素
    def add(self, key, value):
        if key in self:  # update
            index = self._find_key(key)
            self._table[index].value = value
            return False
        else:
            index = self._find_slot_for_insert(key)
            self._table[index] = Slot(key, value)
            self.length += 1
            if self._load_factor >= 0.8:
                self._rehash()
            return True
 
    # 槽不够时，重哈希
    def _rehash(self):
        old_table = self._table
        newsize = len(self._table) * 2
        self._table = Array(newsize, HashTable.UNUSED)
 
        self.length = 0
 
        for slot in old_table:
            if slot is not HashTable.UNUSED and slot is not HashTable.EMPTY:
                index = self._find_slot_for_insert(slot.key)
                self._table[index] = slot
                self.length += 1
 
    # 获取值
    def get(self, key, default=None):
        index = self._find_key(key)
        if index is None:
            return default
        else:
            return self._table[index].value
 
    # 移除
    def remove(self, key):
        index = self._find_key(key)
        if index is None:
            raise KeyError()
        value = self._table[index].value
        self.length -= 1
        self._table[index] = HashTable.EMPTY
        return value
 
    # 遍历
    def __iter__(self):
        for slot in self._table:
            if slot not in (HashTable.EMPTY, HashTable.UNUSED):
                yield slot.key

if __name__ == '__main__':
    h = HashTable()
    h.add('a', 0)
    h.add('b', 1)
    h.add('c', 2)
    print(len(h)) #
    print(h.get('a')) #
    print(h.get('b')) #
    print(h.get('hehe')) # None
    h.remove('a')
    print(h.get('a')) # None
    print(sorted(list(h))) # ['b', 'c']