"""
https://leetcode.cn/problems/my-calendar-ii/

实现一个 MyCalendar 类来存放你的日程安排。如果要添加的时间内不会导致三重预订时，则可以存储这个新的日程安排。

MyCalendar 有一个 book(int start, int end)方法。它意味着在 start 到 end 时间内增加一个日程安排，注意，这里的时间是半开区间，即 [start, end), 实数 x 的范围为，  start <= x < end。

当三个日程安排有一些时间上的交叉时（例如三个日程安排都在同一时间内），就会产生三重预订。

每次调用 MyCalendar.book方法时，如果可以将日程安排成功添加到日历中而不会导致三重预订，返回 true。否则，返回 false 并且不要将该日程安排添加到日历中。

请按照以下步骤调用MyCalendar 类: MyCalendar cal = new MyCalendar(); MyCalendar.book(start, end)

示例：
    MyCalendar();
    MyCalendar.book(10, 20); // returns true
    MyCalendar.book(50, 60); // returns true
    MyCalendar.book(10, 40); // returns true
    MyCalendar.book(5, 15);  // returns false
    MyCalendar.book(5, 10);  // returns true
    MyCalendar.book(25, 55); // returns true
    
    解释：
        前两个日程安排可以添加至日历中。 第三个日程安排会导致双重预订，但可以添加至日历中。
        第四个日程安排活动（5,15）不能添加至日历中，因为它会导致三重预订。
        第五个日程安排（5,10）可以添加至日历中，因为它未使用已经双重预订的时间10。
        第六个日程安排（25,55）可以添加至日历中，因为时间 [25,40] 将和第三个日程安排双重预订；
        时间 [40,50] 将单独预订，时间 [50,55）将和第二个日程安排双重预订。
 
提示：
    每个测试用例，调用 MyCalendar.book 函数最多不超过 1000次。
    调用函数 MyCalendar.book(start, end)时， start 和 end 的取值范围为 [0, 10^9]。

"""

"""方法一：直接遍历"""
class MyCalendarTwo:
    def __init__(self):
        self.booked = []        # 记录下所有已经预定的课程安排区间
        self.overlaps = []      # 记录下所有已经预定过两次的课程安排区间

    def book(self, start: int, end: int) -> bool:
        if any(s < end and start < e for s, e in self.overlaps):    # 首先检测新加入的区间 [start, end) 是否与已经预定过两次的区间有交集
            return False                                            # 如果与已经两次的有冲突，直接判断false
        for s, e in self.booked:                                    # 如果没有冲突，将新加入的区间与已经预定的区间进行检查
            if s < end and start < e:                               # 如果有冲突，加入新增的已预定两次的区间
                self.overlaps.append((max(s, start), min(e, end)))  # 新增的已经预定两次的区间
        self.booked.append((start, end))                            # 新增的已经预定的区间
        return True

"""方法二：差分数组"""
from sortedcontainers import SortedDict

class MyCalendarTwo:
    def __init__(self):
        self.cnt = SortedDict()

    def book(self, start: int, end: int) -> bool:
        self.cnt[start] = self.cnt.get(start, 0) + 1
        self.cnt[end] = self.cnt.get(end, 0) - 1
        maxBook = 0
        for c in self.cnt.values():
            maxBook += c
            if maxBook > 2:
                self.cnt[start] = self.cnt.get(start, 0) - 1
                self.cnt[end] = self.cnt.get(end, 0) + 1
                return False
        return True

"""方法三：线段树"""
class MyCalendarTwo:
    def __init__(self):
        self.tree = {}

    def update(self, start: int, end: int, val: int, l: int, r: int, idx: int) -> None:
        if r < start or end < l:
            return
        if start <= l and r <= end:
            p = self.tree.get(idx, [0, 0])
            p[0] += val
            p[1] += val
            self.tree[idx] = p
            return
        mid = (l + r) // 2
        self.update(start, end, val, l, mid, 2 * idx)
        self.update(start, end, val, mid + 1, r, 2 * idx + 1)
        p = self.tree.get(idx, [0, 0])
        p[0] = p[1] + max(self.tree.get(2 * idx, (0,))[0], self.tree.get(2 * idx + 1, (0,))[0])
        self.tree[idx] = p

    def book(self, start: int, end: int) -> bool:
        self.update(start, end - 1, 1, 0, 10 ** 9, 1)
        if self.tree[1][0] > 2:
            self.update(start, end - 1, -1, 0, 10 ** 9, 1)
            return False
        return True

if __name__ == "__main__":
    MyCalendar = MyCalendarTwo()
    print(MyCalendar.book(10, 20))     # returns true
    print(MyCalendar.book(50, 60))     # returns true
    print(MyCalendar.book(10, 40))     # returns true
    print(MyCalendar.book(5, 15))      # returns false
    print(MyCalendar.book(5, 10))      # returns true
    print(MyCalendar.book(25, 55))     # returns true