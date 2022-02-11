"""
https://leetcode-cn.com/problems/longest-harmonious-subsequence/

和谐数组是指一个数组里元素的最大值和最小值之间的差别 正好是 1 。

现在，给你一个整数数组 nums ，请你在所有可能的子序列中找到最长的和谐子序列的长度。

数组的子序列是一个由数组派生出来的序列，它可以通过删除一些元素或不删除元素、且不改变其余元素的顺序而得到。

示例 1：
    输入：nums = [1,3,2,2,5,2,3,7]
    输出：5
    解释：最长的和谐子序列是 [3,2,2,2,3]

示例 2：
    输入：nums = [1,2,3,4]
    输出：2

示例 3：
    输入：nums = [1,1,1,1]
    输出：0

提示：
    1 <= nums.length <= 2 * 10^4
    -10^9 <= nums[i] <= 10^9

"""
from typing import List
from collections import Counter

"""解法1：枚举"""
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        nums.sort()                                 # 将数组按照从小到大进行排序
        res, begin = 0, 0                           # begin 指向第一个连续相同元素的子序列的第一个元素
        for end in range(len(nums)):                # end 指向相邻的第二个连续相同元素的子序列的末尾元素
            while nums[end] - nums[begin] > 1:      # 如果满足二者的元素之差大于 1
                begin += 1                          # 左指针右移
            if nums[end] - nums[begin] == 1:        # 如果满足二者的元素之差为 1
                res = max(res, end - begin + 1)     # 则当前的和谐子序列的长度即为两个子序列的长度之和，等于 end - begin + 1
        return res
    
"""解法2：哈希表"""
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        return max((val + cnt[key + 1] for key, val in cnt.items() if key + 1 in cnt), default=0)

if __name__ == "__main__":
    nums = [1,3,2,2,5,2,3,7]
    sol = Solution()
    result = sol.findLHS(nums)
    print(result)