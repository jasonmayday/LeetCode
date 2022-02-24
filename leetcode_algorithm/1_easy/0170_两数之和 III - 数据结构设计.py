"""
https://leetcode-cn.com/problems/two-sum-iii-data-structure-design/

设计一个接收整数流的数据结构，该数据结构支持检查是否存在两数之和等于特定值。

实现 TwoSum 类：
    TwoSum() 使用空数组初始化 TwoSum 对象
    void add(int number) 向数据结构添加一个数 number
    boolean find(int value) 寻找数据结构中是否存在一对整数，使得两数之和与给定的值相等。如果存在，返回 true ；否则，返回 false 。

示例：
    输入：
    ["TwoSum", "add", "add", "add", "find", "find"]
    [[], [1], [3], [5], [4], [7]]
    输出：
    [null, null, null, null, true, false]

    解释：
    TwoSum twoSum = new TwoSum();
    twoSum.add(1);   // [] --> [1]
    twoSum.add(3);   // [1] --> [1,3]
    twoSum.add(5);   // [1,3] --> [1,3,5]
    twoSum.find(4);  // 1 + 3 = 4，返回 true
    twoSum.find(7);  // 没有两个整数加起来等于 7 ，返回 false
 
提示：
    -10^5 <= number <= 10^5
    -2^31 <= value <= 2^31 - 1
    最多调用 10^4 次 add 和 find

"""

""" 解法1:双指针 """
class TwoSum(object):
    def __init__(self):
        self.nums = []
        self.is_sorted = False

    def add(self, number):
        self.nums.append(number)
        self.is_sorted = False

    def find(self, value):
        if not self.is_sorted:
            self.nums.sort()
            self.is_sorted = True

        low  = 0
        high = len(self.nums)-1     # 初始化两个指针 low 和 high 分别指向列表的头尾。
        while low < high:           # 从两个方向同时进行迭代，要么找到两数之和的解，要么两个指针相遇。
            currSum = self.nums[low] + self.nums[high]
            if currSum < value:     # 如果当前指针指向元素的和小于目标值，
                low += 1            # 则应该增加总和来满足目标值，即将 low 指针向前移动获得更大的值。
            elif currSum > value:   # 如果当前指针指向元素的和大于目标值，
                high -= 1           # 则应该减少总和来满足目标值，即将 high 向 low 靠近来减少总和。
            elif currSum == value:  # 如果当前指针指向元素的和等于目标值，则直接返回结果。
                return True
        return False            # 如果两个指针相交，说明当前列表不存在组合成目标值的两个数。


""" 解法2:哈希表 """
class TwoSum(object):

    def __init__(self):
        self.num_counts = {}

    def add(self, number):
        """
        Add the number to an internal data structure..
        :type number: int
        :rtype: None
        """
        if number in self.num_counts:
            self.num_counts[number] += 1
        else:
            self.num_counts[number] = 1

    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        for num in self.num_counts.keys():
            comple = value - num
            if num != comple:
                if comple in self.num_counts:
                    return True
            elif self.num_counts[num] > 1:
                return True

        return False

if __name__ == "__main__":
    twoSum = TwoSum()
    twoSum.add(1)   # [] --> [1]
    twoSum.add(3)   # [1] --> [1,3]
    twoSum.add(5)   # [1,3] --> [1,3,5]
    twoSum.find(4)  # 1 + 3 = 4，返回 true
    twoSum.find(7)  # 没有两个整数加起来等于 7 ，返回 false
