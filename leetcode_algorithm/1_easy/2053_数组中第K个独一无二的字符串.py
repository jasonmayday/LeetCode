"""
https://leetcode-cn.com/problems/kth-distinct-string-in-an-array/

独一无二的字符串 指的是在一个数组中只出现过 一次 的字符串。

给你一个字符串数组 arr 和一个整数 k ，请你返回 arr 中第 k 个 独一无二的字符串 。如果 少于 k 个独一无二的字符串，那么返回 空字符串 "" 。

注意，按照字符串在原数组中的 顺序 找到第 k 个独一无二字符串。

示例 1:
    输入：arr = ["d","b","c","b","c","a"], k = 2
    输出："a"
    解释：
    arr 中独一无二字符串包括 "d" 和 "a" 。
    "d" 首先出现，所以它是第 1 个独一无二字符串。
    "a" 第二个出现，所以它是 2 个独一无二字符串。
    由于 k == 2 ，返回 "a" 。

示例 2:
    输入：arr = ["aaa","aa","a"], k = 1
    输出："aaa"
    解释：
    arr 中所有字符串都是独一无二的，所以返回第 1 个字符串 "aaa" 。

示例 3：
    输入：arr = ["a","b","a"], k = 3
    输出：""
    解释：
    唯一一个独一无二字符串是 "b" 。由于少于 3 个独一无二字符串，我们返回空字符串 "" 。

提示：
    1 <= k <= arr.length <= 1000
    1 <= arr[i].length <= 5
    arr[i] 只包含小写英文字母。

"""
from typing import List
from collections import Counter

class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        for i in arr:               # 顺序遍历数组
            if arr.count(i) == 1:   # 如果遍历到的字符串在数组中出现频数为 1
                k -= 1              # 将计数 kk 减去 1
            if k == 0:              # 当上述操作后 k 到达 0 时
                return i            # 对应的字符串即为第 k 个独一无二的字符串
        return ''                   # 若遍历完成数组，k 仍未到达 0，则该数组中不存在第 k 个独一无二的字符串

class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        freq = Counter(arr)     # 维护 arr 中每个字符串的频数
        for s in arr:           # 遍历 arr 寻找第 k 个独一无二的字符串
            if freq[s] == 1:
                k -= 1
                if k == 0:
                    return s
        return ""

if __name__ == "__main__":
    arr = ["d","b","c","b","c","a"]
    k = 2
    sol = Solution()
    result = sol.kthDistinct(arr, k)
    print(result)