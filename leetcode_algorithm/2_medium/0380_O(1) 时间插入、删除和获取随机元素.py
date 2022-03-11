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
    randomizedSet.insert(1); // 向集合中插入 1 。返回 true 表示 1 被成功地插入。
    randomizedSet.remove(2); // 返回 false ，表示集合中不存在 2 。
    randomizedSet.insert(2); // 向集合中插入 2 。返回 true 。集合现在包含 [1,2] 。
    randomizedSet.getRandom(); // getRandom 应随机返回 1 或 2 。
    randomizedSet.remove(1); // 从集合中移除 1 ，返回 true 。集合现在包含 [2] 。
    randomizedSet.insert(2); // 2 已在集合中，所以返回 false 。
    randomizedSet.getRandom(); // 由于 2 是集合中唯一的数字，getRandom 总是返回 2 。

提示：
    -2^31 <= val <= 2^31 - 1
    最多调用 insert、remove 和 getRandom 函数 2 * 10^5 次
    在调用 getRandom 方法时，数据结构中 至少存在一个 元素。

"""

import random
class RandomizedSet():
    def __init__(self):
        self.dict = {}
        self.list = []

    def insert(self, val: int) -> bool: # 当元素 val 不存在时，向集合中插入该项，并返回 true ；否则，当元素 val 存在时返回 false
        if val in self.dict:
            return False
        self.dict[val] = len(self.list)
        self.list.append(val)
        return True
        
    def remove(self, val: int) -> bool: # 当元素 val 存在时，从集合中移除该项，并返回 true ；否则，当元素 val 不存在时返回 false
        if val in self.dict:
            # move the last element to the place idx of the element to delete
            last_element = self.list[-1]
            idx = self.dict[val]
            self.list[idx], self.dict[last_element] = last_element, idx

            self.list.pop()     # List 删除last_element
            del self.dict[val]  # dict 删除val
            return True
        return False

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