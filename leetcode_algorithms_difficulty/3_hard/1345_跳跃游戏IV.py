"""
https://leetcode-cn.com/problems/jump-game-iv/

给你一个整数数组 arr ，你一开始在数组的第一个元素处（下标为 0）。

每一步，你可以从下标 i 跳到下标：
    i + 1 满足：i + 1 < arr.length
    i - 1 满足：i - 1 >= 0
    j 满足：arr[i] == arr[j] 且 i != j

请你返回到达数组最后一个元素的下标处所需的 最少操作次数 。

注意：任何时候你都不能跳到数组外面。

示例 1：
    输入：arr = [100,-23,-23,404,100,23,23,23,3,404]
    输出：3
    解释：那你需要跳跃 3 次，下标依次为 0 --> 4 --> 3 --> 9 。下标 9 为数组的最后一个元素的下标。

示例 2：
    输入：arr = [7]
    输出：0
    解释：一开始就在最后一个元素处，所以你不需要跳跃。

示例 3：
    输入：arr = [7,6,9,6,9,6,9,7]
    输出：1
    解释：你可以直接从下标 0 处跳到下标 7 处，也就是数组的最后一个元素处。

示例 4：
    输入：arr = [6,1,9]
    输出：2

示例 5：
    输入：arr = [11,22,7,7,7,7,7,7,7,22,13]
    输出：3

提示：
    1 <= arr.length <= 5 * 10^4
    -10^8 <= arr[i] <= 10^8

"""
from typing import List
from collections import deque
from collections import defaultdict

'''方法一：广度优先搜索'''
class Solution:
    def minJumps(self, arr: List[int]) -> int:
        idxSameValue = defaultdict(list)
        for i, a in enumerate(arr):
            idxSameValue[a].append(i)
        visitedIndex = set()
        q = deque()
        q.append([0, 0])
        visitedIndex.add(0)
        while q:
            idx, step = q.popleft()
            if idx == len(arr) - 1:
                return step
            v = arr[idx]
            step += 1
            for i in idxSameValue[v]:
                if i not in visitedIndex:
                    visitedIndex.add(i)
                    q.append([i, step])
            del idxSameValue[v]
            if idx + 1 < len(arr) and (idx + 1) not in visitedIndex:
                visitedIndex.add(idx + 1)
                q.append([idx+1, step])
            if idx - 1 >= 0 and (idx - 1) not in visitedIndex:
                visitedIndex.add(idx - 1)
                q.append([idx-1, step])

if __name__ == "__main__":
    arr = [100,-23,-23,404,100,23,23,23,3,404]
    sol = Solution()
    result = sol.minJumps(arr)
    print(result)