"""
https://leetcode-cn.com/problems/insert-delete-getrandom-o1/

实现RandomizedSet 类：
    RandomizedSet() 初始化 RandomizedSet 对象
    bool insert(int val) 当元素 val 不存在时，向集合中插入该项，并返回 true ；否则，返回 false 。
    bool remove(int val) 当元素 val 存在时，从集合中移除该项，并返回 true ；否则，返回 false 。
    int getRandom() 随机返回现有集合中的一项（测试用例保证调用此方法时集合中至少存在一个元素）。每个元素应该有 相同的概率 被返回。

你必须实现类的所有函数，并满足每个函数的 平均 时间复杂度为 O(1) 。

示例：
    输入
    ["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
    [[], [1], [2], [2], [], [1], [2], []]
    输出
    [null, true, false, true, 2, true, false, 2]

    解释
    RandomizedSet randomizedSet = new RandomizedSet();
    randomizedSet.insert(1);    // 向集合中插入 1 。返回 true 表示 1 被成功地插入。
    randomizedSet.remove(2);    // 返回 false ，表示集合中不存在 2 。
    randomizedSet.insert(2);    // 向集合中插入 2 。返回 true 。集合现在包含 [1,2] 。
    randomizedSet.getRandom();  // getRandom 应随机返回 1 或 2 。
    randomizedSet.remove(1);    // 从集合中移除 1 ，返回 true 。集合现在包含 [2] 。
    randomizedSet.insert(2);    // 2 已在集合中，所以返回 false 。
    randomizedSet.getRandom();  // 由于 2 是集合中唯一的数字，getRandom 总是返回 2 。

提示：
    -2^31 <= val <= 2^31 - 1
    最多调用 insert、remove 和 getRandom 函数 2 * 10^5 次
    在调用 getRandom 方法时，数据结构中 至少存在一个 元素。

"""

import random
""" 数组 + 哈希表
    数组中存储元素，哈希表中存储每个元素在数组中的下标。
    插入：val:len(nums) 该元素作为key，末尾作为其索引
    删除：找到队尾元素，将其索引改为val的索引，然后将val与队尾元素互换，pop出val，删掉字典中val的项
"""
class RandomizedSet():
    def __init__(self):
        self.dict = {}  # 哈希表的 key 为元素，值为位置
        self.list = []

    def insert(self, val: int) -> bool:     # 当元素 val 不存在时，向集合中插入该项，并返回 true ；否则，当元素 val 存在时返回 false
        if val in self.dict:
            return False
        self.dict[val] = len(self.list)     # 插入一个数时，先放到最后，val的索引存入哈希表中【idx = 队尾】
        self.list.append(val)               # 在数组的末尾添加 val
        return True
        
    def remove(self, val: int) -> bool: # 当元素 val 存在时，从集合中移除该项，并返回 true ；否则，当元素 val 不存在时返回 false
        if val not in self.dict:        # val 不在哈希表中，则返回 false
            return False
        last_element = self.list[-1]    # 删除一个数时，让最后一个数字去替换: 先找到最后一个元素
        idx = self.dict[val]            # 找到需要删除的元素的位置
        self.list[idx] = last_element   # 将数组最后一个元素移到要删除的元素的位置 idx
        self.dict[last_element] = idx   # 在哈希表中将 last_element 的下标更新为 idx
        self.list.pop()     # List 删除 last_element (已交换位置，相当于删除输入的元素)
        del self.dict[val]  # dict 删除 val
        return True

    def getRandom(self) -> int:     # 随机返回现有集合中的一项
        return random.choice(self.list)

if __name__ == "__main__":
    randomizedSet = RandomizedSet()
    print(randomizedSet.insert(1))     # 向集合中插入 1 。返回 true 表示 1 被成功地插入。
    print(randomizedSet.remove(2))     # 返回 false ，表示集合中不存在 2 。
    print(randomizedSet.insert(2))     # 向集合中插入 2 。返回 true 。集合现在包含 [1,2] 。
    print(randomizedSet.getRandom())   # getRandom 应随机返回 1 或 2 。
    print(randomizedSet.remove(1))     # 从集合中移除 1 ，返回 true 。集合现在包含 [2] 。
    print(randomizedSet.insert(2))     # 已在集合中，所以返回 false 。
    print(randomizedSet.getRandom())   # 由于 2 是集合中唯一的数字，getRandom 总是返回 2 。