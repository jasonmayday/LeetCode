'''
https://leetcode-cn.com/problems/sum-of-all-subset-xor-totals/

一个数组的 异或总和 定义为数组中所有元素按位 XOR 的结果；如果数组为 空 ，则异或总和为 0 。

例如，数组 [2,5,6] 的 异或总和 为 2 XOR 5 XOR 6 = 1 。
给你一个数组 nums ，请你求出 nums 中每个 子集 的 异或总和 ，计算并返回这些值相加之 和 。

注意：在本题中，元素 相同 的不同子集应 多次 计数。

数组 a 是数组 b 的一个 子集 的前提条件是：从 b 删除几个（也可能不删除）元素能够得到 a 。

示例 1：
    输入：nums = [1,3]
    输出：6
    解释：[1,3] 共有 4 个子集：
    - 空子集的异或总和是 0 。
    - [1] 的异或总和为 1 。
    - [3] 的异或总和为 3 。
    - [1,3] 的异或总和为 1 XOR 3 = 2 。
    0 + 1 + 3 + 2 = 6

示例 2：
    输入：nums = [5,1,6]
    输出：28
    解释：[5,1,6] 共有 8 个子集：
    - 空子集的异或总和是 0 。
    - [5] 的异或总和为 5 。
    - [1] 的异或总和为 1 。
    - [6] 的异或总和为 6 。
    - [5,1] 的异或总和为 5 XOR 1 = 4 。
    - [5,6] 的异或总和为 5 XOR 6 = 3 。
    - [1,6] 的异或总和为 1 XOR 6 = 7 。
    - [5,1,6] 的异或总和为 5 XOR 1 XOR 6 = 2 。
    0 + 5 + 1 + 6 + 4 + 3 + 7 + 2 = 28

示例 3：
    输入：nums = [3,4,5,6,7,8]
    输出：480
    解释：每个子集的全部异或总和值之和为 480 。

提示：
    1 <= nums.length <= 12
    1 <= nums[i] <= 20

'''


from typing import List

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)           # 用 n 表示 nums 的长度
        def dfs(value, idx):    # 用函数 dfs(value, idx) 来递归枚举数组 nums 的子集，dfs = Depth-First-Search = 深度优先搜索算法
            nonlocal res        # value代表当前选取部分的异或值，idx代表递归的当前位置
            if idx == n:        # idx == n，终止递归
                res += value
                return
            # 考虑选择当前数字
            dfs(value ^ nums[idx], idx + 1)
            # 考虑不选择当前数字
            dfs(value, idx + 1)
        
        dfs(0, 0)
        return res

if __name__ == "__main__":
    nums = [3,4,5,6,7,8]
    sol = Solution()
    result = sol.subsetXORSum(nums)
    print(result)