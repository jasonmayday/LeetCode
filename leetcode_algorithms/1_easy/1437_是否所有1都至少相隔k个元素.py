"""
https://leetcode-cn.com/problems/check-if-all-1s-are-at-least-length-k-places-away/

给你一个由若干 0 和 1 组成的数组 nums 以及整数 k。如果所有 1 都至少相隔 k 个元素，则返回 True ；否则，返回 False 。

示例 1：
    输入：nums = [1,0,0,0,1,0,0,1], k = 2
    输出：true
    解释：每个 1 都至少相隔 2 个元素。

示例 2：
    输入：nums = [1,0,0,1,0,1], k = 2
    输出：false
    解释：第二个 1 和第三个 1 之间只隔了 1 个元素。

示例 3：
    输入：nums = [1,1,1,1,1], k = 0
    输出：true

示例 4：
    输入：nums = [0,1,0,1], k = 1
    输出：true

提示：
    1 <= nums.length <= 10^5
    0 <= k <= nums.length
    nums[i] 的值为 0 或 1

"""
class Solution:
    def kLengthApart(self, nums, k: int) -> bool:
        if len(nums) == 1: return True
        one_idx = []  # 记录 nums 中 1 出现的位置
        for idx, num in enumerate(nums):
            if num == 1:
                one_idx.append(idx)
        if len(one_idx) == 0 or len(one_idx) == 1:  # nums 中没有 0 或 nums中只有一个 0 的情况
            return True
        return True if all(one_idx[i] - one_idx[i - 1] - 1 >= k for i in range(1, len(one_idx))) else False  # 暴力

if __name__ == "__main__":
    s = "abbcccddddeeeeedcba"
    sol = Solution()
    result = sol.maxPower(s)
    print (result)