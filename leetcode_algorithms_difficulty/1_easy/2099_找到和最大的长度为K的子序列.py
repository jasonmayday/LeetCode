"""
https://leetcode-cn.com/problems/find-subsequence-of-length-k-with-the-largest-sum/

给你一个整数数组 nums 和一个整数 k 。你需要找到 nums 中长度为 k 的 子序列 ，且这个子序列的 和最大 。

请你返回 任意 一个长度为 k 的整数子序列。

子序列 定义为从一个数组里删除一些元素后，不改变剩下元素的顺序得到的数组。

示例 1：
    输入：nums = [2,1,3,3], k = 2
    输出：[3,3]
    解释：
        子序列有最大和：3 + 3 = 6 。

示例 2：
    输入：nums = [-1,-2,3,4], k = 3
    输出：[-1,3,4]
    解释：
        子序列有最大和：-1 + 3 + 4 = 6 。

示例 3：
    输入：nums = [3,4,3,3], k = 2
    输出：[3,4]
    解释：
    子序列有最大和：3 + 4 = 7 。
        另一个可行的子序列为 [4, 3] 。

提示：
    1 <= nums.length <= 1000
    -10^5 <= nums[i] <= 10^5
    1 <= k <= nums.length

"""
from typing import List
from collections import Counter

""" 此题关键点在于返回的子序列中元素的顺序与之前的相同。
    如果仅仅排序后提取元素，顺序会不符"""
class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        vals = [[i, nums[i]] for i in range(n)] # 辅助数组，[下标,值]： [[0, -1], [1, -2], [2, 3], [3, 4]]
        vals.sort(key = lambda x: -x[1])        # 按照数值降序排序,     [[3, 4], [2, 3], [0, -1], [1, -2]]
        vals = sorted(vals[:k])                 # 前 k 个并按照下标升序排序, [[0, -1], [2, 3], [3, 4]]
        res = [item[1] for item in vals]        # 目标子序列, [-1, 3, 4]
        return res


class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        num_freq = Counter(sorted(nums, reverse = True)[ :k]) # ({4: 1, 3: 1, -1: 1})
        res = []
        for x in nums:
            if num_freq[x] > 0:
                res.append(x)
                num_freq[x] -= 1
        return res


if __name__ == "__main__":
    nums = [-1,-2,3,4]
    k = 3
    sol = Solution()
    result = sol.maxSubsequence(nums, k)
    print (result)