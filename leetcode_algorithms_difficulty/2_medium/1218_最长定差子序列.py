'''
https://leetcode-cn.com/problems/longest-arithmetic-subsequence-of-given-difference/

给你一个整数数组 arr 和一个整数 difference，请你找出并返回 arr 中最长等差子序列的长度，该子序列中相邻元素之间的差等于 difference 。

子序列 是指在不改变其余元素顺序的情况下，通过删除一些元素或不删除任何元素而从 arr 派生出来的序列。

示例 1：
    输入：arr = [1,2,3,4], difference = 1
    输出：4
    解释：最长的等差子序列是 [1,2,3,4]。

示例 2：
    输入：arr = [1,3,5,7], difference = 1
    输出：1
    解释：最长的等差子序列是任意单个元素。

示例 3：
    输入：arr = [1,5,7,8,5,3,4,2,1], difference = -2
    输出：4
    解释：最长的等差子序列是 [7,5,3,1]。
 
提示：
    1 <= arr.length <= 10^5
    -10^4 <= arr[i], difference <= 10^4

'''
from typing import List

# 方法1：动态规划
class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dict = {}
        for n in arr:                                   # dict[n] 存储以数字n结尾的子序列的最大长度
            dict[n] = dict.get(n - difference, 0) + 1   # 遍历数组，如果 n-difference 存在则代表n可以拼接在子序列后面，使长度加1
        return max(dict.values())                       # 所有长度的最大值，即为答案。

if __name__ == "__main__":
    arr = [1,2,4,3,5,8,7,5,1]
    difference = 2
    sol = Solution()
    result = sol.longestSubsequence(arr, difference)
    print(result)