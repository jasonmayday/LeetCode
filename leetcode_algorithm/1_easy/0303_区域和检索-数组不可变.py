"""
给定一个整数数组  nums，求出数组从索引 i 到 j（i ≤ j）范围内元素的总和，包含 i、j 两点。

实现 NumArray 类：
    NumArray(int[] nums) 使用数组 nums 初始化对象
    int sumRange(int i, int j) 返回数组 nums 从索引 i 到 j（i ≤ j）范围内元素的总和，包含 i、j 两点（也就是 sum(nums[i], nums[i + 1], ... , nums[j])）
 
示例：
    输入：
        ["NumArray", "sumRange", "sumRange", "sumRange"]
        [[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
    输出：
        [null, 1, -1, -3]

    解释：
        NumArray numArray = new NumArray([-2, 0, 3, -5, 2, -1]);
        numArray.sumRange(0, 2); // return 1 ((-2) + 0 + 3)
        numArray.sumRange(2, 5); // return -1 (3 + (-5) + 2 + (-1))
        numArray.sumRange(0, 5); // return -3 ((-2) + 0 + 3 + (-5) + 2 + (-1))

提示：
    0 <= nums.length <= 10^4
    -10^5 <= nums[i] <= 10^5
    0 <= i <= j < nums.length
    最多调用 10^4 次 sumRange 方法

"""
from typing import List

class NumArray:
    def __init__(self, nums: List[int]):
        self.sums = [0]
        rangeSum = self.sums

        for num in nums:
            rangeSum.append(rangeSum[-1] + num)

    def sumRange(self, i: int, j: int) -> int:
        rangeSum = self.sums
        return rangeSum[j+1] - rangeSum[i]

if __name__ == "__main__":
    numArray = NumArray([-2, 0, 3, -5, 2, -1])
    print (numArray.sumRange(0, 2))     # return 1 ((-2) + 0 + 3)
    print (numArray.sumRange(2, 5))     # return -1 (3 + (-5) + 2 + (-1))
    print (numArray.sumRange(0, 5))     # return -3 ((-2) + 0 + 3 + (-5) + 2 + (-1))

