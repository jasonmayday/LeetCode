"""
https://leetcode-cn.com/problems/duplicate-zeros/

给你一个长度固定的整数数组 arr，请你将该数组中出现的每个零都复写一遍，并将其余的元素向右平移。

注意：请不要在超过该数组长度的位置写入元素。

要求：请对输入的数组 就地 进行上述修改，不要从函数返回任何东西。

示例 1：
    输入：[1,0,2,3,0,4,5,0]
    输出：null
    解释：调用函数后，输入的数组将被修改为：[1,0,0,2,3,0,0,4]

示例 2：
    输入：[1,2,3]
    输出：null
    解释：调用函数后，输入的数组将被修改为：[1,2,3]

提示：
    1 <= arr.length <= 10000
    0 <= arr[i] <= 9

"""

class Solution(object):
    def duplicateZeros(self, arr):
        n = len(arr)
        i = 0
        while i < n:
            if arr[i] == 0:         # i 位置的数字为0
                arr.insert(i, 0)    # 插入一个0
                arr.pop()           # 因为总长度不变，所以弹出最后一个数字
                i += 2              # 指针后移两位
            else:
                i += 1
        return arr

if __name__ == "__main__":
    arr = [1,0,2,3,0,4,5,0]
    sol = Solution()
    result = sol.duplicateZeros(arr)
    print(result)