"""
https://leetcode-cn.com/problems/range-sum-query-mutable/

给你一个数组 nums ，请你完成两类查询。
    其中一类查询要求 更新 数组 nums 下标对应的值
    另一类查询要求返回数组 nums 中索引 left 和索引 right 之间（ 包含 ）的nums元素的 和 ，其中 left <= right

实现 NumArray 类：
    NumArray(int[] nums) 用整数数组 nums 初始化对象
    void update(int index, int val) 将 nums[index] 的值 更新 为 val
    int sumRange(int left, int right) 返回数组 nums 中索引 left 和索引 right 之间（ 包含 ）的nums元素的 和 （即，nums[left] + nums[left + 1], ..., nums[right]）

示例 1：
    输入：
        ["NumArray", "sumRange", "update", "sumRange"]
        [[[1, 3, 5]], [0, 2], [1, 2], [0, 2]]
    输出：
        [null, 9, null, 8]

    解释：
        NumArray numArray = new NumArray([1, 3, 5]);
        numArray.sumRange(0, 2); // 返回 1 + 3 + 5 = 9
        numArray.update(1, 2);   // nums = [1,2,5]
        numArray.sumRange(0, 2); // 返回 1 + 2 + 5 = 8

提示：
    1 <= nums.length <= 3 * 10^4
    -100 <= nums[i] <= 100
    0 <= index < nums.length
    -100 <= val <= 100
    0 <= left <= right < nums.length
    调用 pdate 和 sumRange 方法次数不大于 3 * 10^4 

"""

from typing import List

""" 线段树数组实现
    树状数组        """
class SegmentTree:
    def __init__(self, data, merge):
        self.data = data    # data: 传入的数组
        self.n = len(data)
        self.tree = [None] * (4 * self.n)   # 申请4倍 data 长度的空间来存线段树节点    # 索引i的左孩子索引为2i+1，右孩子为2i+2
        self._merge = merge                 # merge: 处理的业务逻辑，例如求和/最大值/最小值，lambda表达式
        if self.n:
            self._build(0, 0, self.n-1)

    def query(self, ql, qr):    # 返回区间 [ql,..,qr] 的值
        return self._query(0, 0, self.n-1, ql, qr)

    def update(self, index, value):
        self.data[index] = value            # 将data数组index位置的值更新为value
        self._update(0, 0, self.n-1, index) # 然后递归更新线段树中被影响的各节点的值

    def _build(self, tree_index, l, r): # 递归创建线段树；l, r : 该节点表示的区间的左,右边界
        if l == r:
            self.tree[tree_index] = self.data[l]    # tree_index : 线段树节点在数组中位置
            return
        mid = (l+r) // 2        # mid为区间中点,对应左孩子区间结束,右孩子区间开头
        left, right = 2 * tree_index + 1, 2 * tree_index + 2 # tree_index的左右子树索引
        self._build(left, l, mid)
        self._build(right, mid+1, r)
        self.tree[tree_index] = self._merge(self.tree[left], self.tree[right])

    def _query(self, tree_index, l, r, ql, qr):
        ''' 递归查询区间[ql,..,qr]的值
            tree_index : 某个根节点的索引
            l, r : 该节点表示的区间的左右边界
            ql, qr: 待查询区间的左右边界'''
        if l == ql and r == qr:
            return self.tree[tree_index]

        mid = (l+r) // 2 # 区间中点,对应左孩子区间结束,右孩子区间开头
        left, right = tree_index * 2 + 1, tree_index * 2 + 2
        if qr <= mid:
            # 查询区间全在左子树
            return self._query(left, l, mid, ql, qr)
        elif ql > mid:
            # 查询区间全在右子树
            return self._query(right, mid+1, r, ql, qr)

        # 查询区间一部分在左子树一部分在右子树
        return self._merge(self._query(left, l, mid, ql, mid),
                          self._query(right, mid+1, r, mid+1, qr))

    def _update(self, tree_index, l, r, index):
        '''
        tree_index:某个根节点索引
        l, r : 此根节点代表区间的左右边界
        index : 更新的值的索引
        '''
        if l == r == index:
            self.tree[tree_index] = self.data[index]
            return
        mid = (l+r)//2
        left, right = 2 * tree_index + 1, 2 * tree_index + 2
        if index > mid:
            # 要更新的区间在右子树
            self._update(right, mid+1, r, index)
        else:
            # 要更新的区间在左子树index<=mid
            self._update(left, l, mid, index)
        # 里面的小区间变化了，包裹的大区间也要更新
        self.tree[tree_index] = self._merge(self.tree[left], self.tree[right])

class NumArray:
    def __init__(self, nums: List[int]):
        self.segment_tree = SegmentTree(nums, lambda x, y : x + y)

    def update(self, i: int, val: int) -> None:
        self.segment_tree.update(i, val)

    def sumRange(self, i: int, j: int) -> int:
        return self.segment_tree.query(i, j)

if __name__ == "__main__":
    numArray = NumArray([1, 3, 5])
    numArray.sumRange(0, 2)     # 返回 下标 0 ~ 2：1 + 3 + 5 = 9
    numArray.update(1, 2)       # 将 nums[1] 的值 更新 为 2, nums = [1,2,5]
    numArray.sumRange(0, 2)     # 返回 下标 0 ~ 2：1 + 2 + 5 = 8