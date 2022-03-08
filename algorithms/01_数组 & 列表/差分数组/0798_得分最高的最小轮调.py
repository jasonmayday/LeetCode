"""
https://leetcode-cn.com/problems/smallest-rotation-with-highest-score/

给定一个数组 A，我们可以将它按一个非负整数 K 进行轮调，这样可以使数组变为 A[K], A[K+1], A{K+2], ... A[A.length - 1], A[0], A[1], ..., A[K-1] 的形式。此后，任何值小于或等于其索引的项都可以记作一分。

例如，如果数组为 [2, 4, 1, 3, 0]，我们按 K = 2 进行轮调后，它将变成 [1, 3, 0, 2, 4]。这将记作 3 分，因为 1 > 0 [no points], 3 > 1 [no points], 0 <= 2 [one point], 2 <= 3 [one point], 4 <= 4 [one point]。

在所有可能的轮调中，返回我们所能得到的最高分数对应的轮调索引 K。如果有多个答案，返回满足条件的最小的索引 K。

示例 1：
    输入：[2, 3, 1, 4, 0]
    输出：3
    解释：
        下面列出了每个 K 的得分：
        K = 0,  A = [2,3,1,4,0],    score 2
        K = 1,  A = [3,1,4,0,2],    score 3
        K = 2,  A = [1,4,0,2,3],    score 3
        K = 3,  A = [4,0,2,3,1],    score 4
        K = 4,  A = [0,2,3,1,4],    score 3
        所以我们应当选择 K = 3，得分最高。

示例 2：
    输入：[1, 3, 0, 2, 4]
    输出：0
    解释：
        A 无论怎么变化总是有 3 分。
        所以我们将选择最小的 K，即 0。

提示：
    A 的长度最大为 20000。
    A[i] 的取值范围是 [0, A.length]。

"""
from typing import List

""" 方法一：差分数组 """
class Solution:
    def bestRotation(self, nums: List[int]) -> int:
        n = len(nums)
        diffs = [0] * n
        for i, num in enumerate(nums):  # [1,2,3,5]
            low = (i + 1) % n
            high = (i - num + n + 1) % n
            diffs[low] += 1
            diffs[high] -= 1
            if low >= high:
                diffs[0] += 1
        print('diffs: ', diffs)
        score, maxScore, idx = 0, 0, 0
        for i, diff in enumerate(diffs):
            score += diff
            if score > maxScore:
                maxScore, idx = score, i
        return idx

class Solution:
    def bestRotation(self, nums: List[int]) -> int:
        n = len(nums)
        step = [0] * n
        for i, a in enumerate(nums):
            if a <= 0 or a >= n:    # 不满足条件的跳过
                continue
            left = i - (a - 1)
            right = i - (n - 1)
            print(i, a, left, right)
            step[left % n] -= 1
            step[right % n] += 1
        print(step)
        val, max_val, max_index = 0, - n - 1, -1
        for i in range(n):
            s = step[i]
            val += s
            if val > max_val:
                max_val = val
                max_index = i
        return max_index

if __name__ == "__main__":
    nums = [1,2,3,5]
    sol = Solution()
    result = sol.bestRotation(nums)
    print(result)