"""
https://leetcode-cn.com/problems/array-transformation/

首先，给你一个初始数组 arr。然后，每天你都要根据前一天的数组生成一个新的数组。

第 i 天所生成的数组，是由你对第 i-1 天的数组进行如下操作所得的：
    1. 假如一个元素小于它的左右邻居，那么该元素自增 1。
    2. 假如一个元素大于它的左右邻居，那么该元素自减 1。
    3. 首、尾元素 永不 改变。

过些时日，你会发现数组将会不再发生变化，请返回最终所得到的数组。

示例 1：
    输入：[6,2,3,4]
    输出：[6,3,3,4]
    解释：
    第一天，数组从 [6,2,3,4] 变为 [6,3,3,4]。
    无法再对该数组进行更多操作。

示例 2：
    输入：[1,6,3,4,3,5]
    输出：[1,4,4,4,4,5]
    解释：
    第一天，数组从 [1,6,3,4,3,5] 变为 [1,5,4,3,4,5]。
    第二天，数组从 [1,5,4,3,4,5] 变为 [1,4,4,4,4,5]。
    无法再对该数组进行更多操作。

提示：
    1 <= arr.length <= 100
    1 <= arr[i] <= 100

"""
from typing import List
import copy

class Solution:
    def transformArray(self, arr: List[int]) -> List[int]:
        flag = 0
        arrtemp = arr.copy()
        while flag == 0:
            arrtemp = arr.copy()
            flag = 1
            for i in range(1, len(arr) - 1):
                if arr[i] < min(arr[i - 1], arr[i + 1]):
                    arrtemp[i] = arr[i] + 1
                    flag = 0
                elif arr[i - 1] < arr[i] and arr[i + 1] < arr[i]:
                    arrtemp[i] = arr[i] - 1
                    flag = 0
            arr = arrtemp.copy()
        return arrtemp

class Solution:
    def transformArray(self, arr: List[int]) -> List[int]:
        cpy = copy.copy(arr)
        for i in range(1, len(arr) - 1):
            if arr[i] < min(arr[i - 1], arr[i + 1]):
                cpy[i] += 1
            elif arr[i] > max(arr[i - 1], arr[i + 1]):
                cpy[i] -= 1
        if cpy == arr:
            return cpy
        else:
            return self.transformArray(cpy)

class Solution:
    def transformArray(self, arr: List[int]) -> List[int]:
        n = len(arr)
        stack = []
        for i in range(1,n-1):
            if arr[i-1] < arr[i] and arr[i] > arr[i+1]:
                stack.append((i,-1))
            elif arr[i-1] > arr[i] and arr[i] < arr[i+1]:
                stack.append((i,1))
        if not stack: return arr
        for i,j in stack:
            arr[i] += j
        return self.transformArray(arr)

if __name__ == "__main__":
    arr = [1,6,3,4,3,5]
    sol = Solution()
    result = sol.transformArray(arr)
    print(result)