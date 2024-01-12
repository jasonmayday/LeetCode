"""
https://leetcode-cn.com/problems/array-of-doubled-pairs/

给定一个长度为偶数的整数数组 arr，只有对 arr 进行重组后可以满足 “对于每个 0 <= i < len(arr) / 2，都有 arr[2 * i + 1] = 2 * arr[2 * i]” 时，返回 true；否则，返回 false。

设 arr 的长度为 n，题目本质上是问 arr 能否分成 n/2 对元素，每对元素中一个数是另一个数的两倍。

示例 1：
    输入：arr = [3,1,3,6]
    输出：false

示例 2：
    输入：arr = [2,1,2,6]
    输出：false

示例 3：
    输入：arr = [4,-2,2,-4]
    输出：true
    解释：可以用 [-2,-4] 和 [2,4] 这两组组成 [-2,-4,2,4] 或是 [2,4,-2,-4]

提示：
    0 <= arr.length <= 3 * 10^4
    arr.length 是偶数
    -10^5 <= arr[i] <= 10^5

"""
from typing import List
from collections import Counter

""" 方法一：哈希表 + 排序"""
class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        cnt = Counter(arr)  # {4: 1, -2: 1, 2: 1, -4: 1}
        if cnt[0] % 2:      # 对于 arr 中的 0，它只能与 0 匹配。
            return False    # 如果 cnt[0] 是奇数，那么必然无法满足题目要求。
        for x in sorted(cnt, key = abs):    # [-2, 2, 4, -4]
            if cnt[2 * x] < cnt[x]:  # 无法找到足够的 2x 与 x 配对
                return False
            cnt[2 * x] -= cnt[x]
        return True

class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        arr.sort(key = lambda x: abs(x))
        cnt = Counter()
        for i in arr:
            if cnt[i]:
                cnt[i] -= 1
                continue
            cnt[2 * i] += 1
        return not any(cnt.values())

if __name__ == "__main__":
    arr = [4,-2,2,-4]
    sol = Solution()
    result = sol.canReorderDoubled(arr)
    print(result)