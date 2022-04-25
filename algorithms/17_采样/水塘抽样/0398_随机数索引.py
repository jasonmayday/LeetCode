"""
https://leetcode-cn.com/problems/random-pick-index/

给定一个可能含有重复元素的整数数组，要求随机输出给定的数字的索引。 您可以假设给定的数字一定存在于数组中。

注意：
    数组大小可能非常大。 使用太多额外空间的解决方案将不会通过测试。

示例:
    int[] nums = new int[] {1,2,3,3,3};
    Solution solution = new Solution(nums);

    // pick(3) 应该返回索引 2,3 或者 4。每个索引的返回概率应该相等。
    solution.pick(3);

    // pick(1) 应该返回 0。因为只有nums[0]等于1。
    solution.pick(1);

"""
import random
from typing import List

class Solution:
    def __init__(self, nums: List[int]):
        self.nums = nums

    def pick(self, target: int) -> int:
        i = 1
        res = None
        for idx, val in enumerate(self.nums):
            if val == target:
                if random.randint(1, i) == 1:   # 取1的概率为1/i
                    res = idx
                i += 1
        return res
    
    def pick(self, target: int) -> int:
        ans = cnt = 0
        for i, num in enumerate(self.nums):
            if num == target:
                cnt += 1  # 第 cnt 次遇到 target
                if random.randrange(cnt) == 0:
                    ans = i
        return ans

if __name__ == "__main__":
    nums = [1,2,3,3,3]
    sol = Solution(nums)
    print(sol.pick(3))  # pick(3) 应该返回索引 2,3 或者 4。每个索引的返回概率应该相等。
    print(sol.pick(1))  # pick(1) 应该返回 0。因为只有nums[0]等于1。