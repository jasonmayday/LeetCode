"""
https://leetcode-cn.com/problems/beautiful-arrangement-ii/

给你两个整数 n 和 k ，请你构造一个答案列表 answer ，该列表应当包含从 1 到 n 的 n 个不同正整数，并同时满足下述条件：
    假设该列表是 answer = [a1, a2, a3, ... , an] ，那么列表 [|a1 - a2|, |a2 - a3|, |a3 - a4|, ... , |an-1 - an|] 中应该有且仅有 k 个不同整数。

返回列表 answer 。如果存在多种答案，只需返回其中 任意一种 。

示例 1：
    输入：n = 3, k = 1
    输出：[1, 2, 3]
    解释：[1, 2, 3] 包含 3 个范围在 1-3 的不同整数，并且 [1, 1] 中有且仅有 1 个不同整数：1

示例 2：
    输入：n = 3, k = 2
    输出：[1, 3, 2]
    解释：[1, 3, 2] 包含 3 个范围在 1-3 的不同整数，并且 [2, 1] 中有且仅有 2 个不同整数：1 和 2

提示：
    1 <= k < n <= 10^4

"""
from typing import List

""" 不断加减 """
class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        ans = list(range(1,n + 1))  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        i = 1
        while k:
            if i % 2 == 1:              # 奇数下标(从第二位开始)
                ans[i] = ans[i-1] + k   # 为前一个数 + k
            else:                       # 偶数下标
                ans[i] = ans[i-1] - k   # 为前一个数 - k
            i += 1  # 下标加 1
            k -= 1  # k 减 1
        return ans

""" 不停翻转 """
class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        res = list(range(1, n + 1)) # 刚开始有一个不同的差绝对值
        for i in range(1, k):       # 每翻转后面一次产生一个新的
            res[i:] = res[:i-1:-1]  # 翻转 第 i 个元素之后的数组
        return res

if __name__ == "__main__":
    n = 10
    k = 9
    sol = Solution()
    result = sol.constructArray(n, k)
    print (result) 