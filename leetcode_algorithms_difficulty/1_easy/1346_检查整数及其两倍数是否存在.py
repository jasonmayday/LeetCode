"""
https://leetcode-cn.com/problems/check-if-n-and-its-double-exist/

给你一个整数数组 arr，请你检查是否存在两个整数 N 和 M，满足 N 是 M 的两倍（即，N = 2 * M）。

更正式地，检查是否存在两个下标 i 和 j 满足：
    i != j
    0 <= i, j < arr.length
    arr[i] == 2 * arr[j]

示例 1：
    输入：arr = [10,2,5,3]
    输出：true
    解释：N = 10 是 M = 5 的两倍，即 10 = 2 * 5 。

示例 2：
    输入：arr = [7,1,14,11]
    输出：true
    解释：N = 14 是 M = 7 的两倍，即 14 = 2 * 7 。

示例 3：
    输入：arr = [3,1,7,11]
    输出：false
    解释：在该情况下不存在 N 和 M 满足 N = 2 * M 。

提示：
    2 <= arr.length <= 500
    -10^3 <= arr[i] <= 10^3

"""
from typing import List

"""解法1：使用Counter计数"""
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        from collections import Counter
        s = Counter(arr)
        for n in s:
            if n == 0:
                if s[n] > 1:        # 虽然 0 的 2 倍仍然是 0 本身，但是只有 1 个 0 仍是不行的。
                    return True     # 如果有两个以上 0，返回 True
            elif n << 1 in s:
                return True
        return False
    

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        res = []
        for i in arr:
            if i % 2 == 0:
                res.append(i) 
        if len(res) == 0: return False
        if res.count(0) >= 2: return True
        flag = 0
        for i in res:
            if i/2 in arr and i != 0:
                flag = 1
                break
        return flag == 1

if __name__ == "__main__":
    arr = [7,1,14,11]
    sol = Solution()
    result = sol.checkIfExist(arr)
    print(result)