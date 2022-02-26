"""
https://leetcode-cn.com/problems/max-stack/

设计一个最大栈数据结构，既支持栈操作，又支持查找栈中最大元素。

实现 MaxStack 类：
    MaxStack() 初始化栈对象
    void push(int x) 将元素 x 压入栈中。
    int pop() 移除栈顶元素并返回这个元素。
    int top() 返回栈顶元素，无需移除。
    int peekMax() 检索并返回栈中最大元素，无需移除。
    int popMax() 检索并返回栈中最大元素，并将其移除。如果有多个最大元素，只要移除 最靠近栈顶 的那个。

示例：
    输入
        ["MaxStack", "push", "push", "push", "top", "popMax", "top", "peekMax", "pop", "top"]
        [[], [5], [1], [5], [], [], [], [], [], []]

    输出
        [null, null, null, null, 5, 5, 1, 5, 1, 5]

    解释
        MaxStack stk = new MaxStack();
        stk.push(5);   // [5] - 5 既是栈顶元素，也是最大元素
        stk.push(1);   // [5, 1] - 栈顶元素是 1，最大元素是 5
        stk.push(5);   // [5, 1, 5] - 5 既是栈顶元素，也是最大元素
        stk.top();     // 返回 5，[5, 1, 5] - 栈没有改变
        stk.popMax();  // 返回 5，[5, 1] - 栈发生改变，栈顶元素不再是最大元素
        stk.top();     // 返回 1，[5, 1] - 栈没有改变
        stk.peekMax(); // 返回 5，[5, 1] - 栈没有改变
        stk.pop();     // 返回 1，[5] - 此操作后，5 既是栈顶元素，也是最大元素
        stk.top();     // 返回 5，[5] - 栈没有改变

提示：
    -10^7 <= x <= 10^7
    最多调用 10^4 次 push、pop、top、peekMax 和 popMax
    调用 pop、top、peekMax 或 popMax 时，栈中 至少存在一个元素

进阶： 
    试着设计解决方案：调用 top 方法的时间复杂度为 O(1) ，调用其他方法的时间复杂度为 O(logn) 。 

"""

""" 方法一：双栈 (一个数据栈，一个最大栈)
    一个普通的栈可以支持前三种操作 push(x)，pop() 和 top()，
    所以我们需要考虑的仅为后两种操作 peekMax() 和 popMax()。"""
class MaxStack(list):
    def push(self, x):  # 将元素 x 压入栈中。
        m = max(x, self[-1][1] if self else None)   # 另一个栈来存储每个位置到栈底的所有元素的最大值。
        # 例如，如果当前第一个栈中的元素为 [2, 1, 5, 3, 9]，那么第二个栈中的元素为 [2, 2, 5, 5, 9]。
        self.append((x, m)) # 将第二个栈的栈顶和 x 的最大值入栈

    def pop(self):      # 移除栈顶元素并返回这个元素。
        return list.pop(self)[0]    # 只需要将第二个栈进行出栈。

    def top(self):      # 返回栈顶元素，无需移除。
        return self[-1][0]

    def peekMax(self):  # 检索并返回栈中最大元素，无需移除。
        return self[-1][1]

    """ 对于 popMax()，由于我们知道当前栈中最大的元素值，因此可以直接将两个栈同时出栈，并存储第一个栈出栈的所有值。
        当某个时刻，第一个栈的出栈元素等于当前栈中最大的元素值时，就找到了最大的元素。
        此时我们将之前出第一个栈的所有元素重新入栈，并同步更新第二个栈，就完成了 popMax() 操作。
    """
    def popMax(self):   # 检索并返回栈中最大元素，并将其移除。如果有多个最大元素，只要移除 最靠近栈顶 的那个。
        m = self[-1][1]
        b = []
        while self[-1][0] != m:
            b.append(self.pop())

        self.pop()
        map(self.push, reversed(b))
        return m


class MaxStack:
    def __init__(self):
        self.num_stk = []
        self.max_stk = []

    def push(self, x: int) -> None:
        if self.max_stk == [] or x > self.max_stk[-1]:
            self.max_stk.append(x)
        else:
            self.max_stk.append(self.max_stk[-1])
        self.num_stk.append(x)

    def pop(self) -> int:
        self.max_stk.pop(-1)
        return self.num_stk.pop(-1)

    def top(self) -> int:
        return self.num_stk[-1]

    def peekMax(self) -> int:
        return self.max_stk[-1]

    def popMax(self) -> int:
        cur_max = self.max_stk[-1]
        tmp = []
        while self.num_stk[-1] != cur_max:
            tmp.append(self.pop())          #2个栈一起弹
        self.pop()
        while tmp:
            self.push(tmp.pop(-1))          #2个栈一起压
        return cur_max


"""方法二：双向链表 + 平衡树"""
if __name__ == "__main__":
    stk = MaxStack()
    stk.push(5)     # [5] - 5 既是栈顶元素，也是最大元素
    stk.push(1)     # [5, 1] - 栈顶元素是 1，最大元素是 5
    stk.push(5)     # [5, 1, 5] - 5 既是栈顶元素，也是最大元素
    stk.top()       # 返回 5，[5, 1, 5] - 栈没有改变
    stk.popMax()    # 返回 5，[5, 1] - 栈发生改变，栈顶元素不再是最大元素
    stk.top()       # 返回 1，[5, 1] - 栈没有改变
    stk.peekMax()   # 返回 5，[5, 1] - 栈没有改变
    stk.pop()       # 返回 1，[5] - 此操作后，5 既是栈顶元素，也是最大元素
    stk.top()       # 返回 5，[5] - 栈没有改变