"""
https://leetcode-cn.com/problems/intersection-of-three-sorted-arrays/

给出三个均为 严格递增排列 的整数数组 arr1，arr2 和 arr3。返回一个由 仅 在这三个数组中 同时出现 的整数所构成的有序数组。

示例 1：
    输入: arr1 = [1,2,3,4,5], arr2 = [1,2,5,7,9], arr3 = [1,3,4,5,8]
    输出: [1,5]
    解释: 只有 1 和 5 同时在这三个数组中出现.

示例 2:
    输入: arr1 = [197,418,523,876,1356], arr2 = [501,880,1593,1710,1870], arr3 = [521,682,1337,1395,1764]
    输出: []

提示：
    1 <= arr1.length, arr2.length, arr3.length <= 1000
    1 <= arr1[i], arr2[i], arr3[i] <= 2000

"""
from typing import List

class Solution():
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        res = []
        count = [0 for _ in range(2005)]
        for num in arr1 + arr2 + arr3:
            count[num] += 1
        for i in range(len(count)):
            if count[i] == 3:
                res.append(i)
        return res


class Solution():
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        return sorted(list(set(arr1) & set(arr2) & set(arr3)))


""" 三指针 """
class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        i,j,k = 0,0,0       # 初始化三指针
        minlength = min([len(arr1),len(arr2),len(arr3)])    # 获取最小长度
        ans = []
        while i < minlength and j < minlength and k < minlength:  # 只要有一个数组遍历结束，整体查找即告结束
            if arr1[i] == arr2[j] == arr3[k]:   # 此轮遍历三个数组的值相同，即找到了同时出现在三个数组中的值
                ans.append(arr1[i])
                i += 1  # i、j、k都向右移动一位
                j += 1
                k += 1
            else:
                # 此轮遍历三个数组的值至少有1个不同
                cur_max = max(arr1[i], arr2[j], arr3[k])
                # 最大的值所在的指针“等待”小的值指针，除了最大值，其余值的指针向右移动1位
                if arr1[i] < cur_max:
                    i += 1
                if arr2[j] < cur_max:
                    j += 1
                if arr3[k] < cur_max:
                    k += 1
        return ans


if __name__ == "__main__":
    arr1 = [1,2,3,4,5]
    arr2 = [1,2,5,7,9]
    arr3 = [1,3,4,5,8]
    sol = Solution()
    result = sol.arraysIntersection(arr1, arr2, arr3)
    print(result)