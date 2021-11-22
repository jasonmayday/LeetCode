"""
https://leetcode-cn.com/problems/sort-array-by-parity/

给定一个非负整数数组 A，返回一个数组，在该数组中， A 的所有偶数元素之后跟着所有奇数元素。

你可以返回满足此条件的任何数组作为答案。

示例：
    输入：[3,1,2,4]
    输出：[2,4,3,1]
    输出 [4,2,3,1]，[2,4,1,3] 和 [4,2,1,3] 也会被接受。

提示：
    1 <= A.length <= 5000
    0 <= A[i] <= 5000

"""

"""使用排序算法，按照模 2 的结果排序。"""
class Solution(object):
    def sortArrayByParity(self, A):
        A.sort(key = lambda x: x % 2)
        return A
    
"""第一遍输出偶数，第二遍输出奇数。"""
class Solution(object):
    def sortArrayByParity(self, A):
        return ([x for x in A if x % 2 == 0] +
                [x for x in A if x % 2 == 1])

""" 原地算法
    维护两个指针 i 和 j，循环保证每刻小于 i 的变量都是偶数（也就是 A[k] % 2 == 0 当 k < i），所有大于 j 的都是奇数"""
class Solution(object):
    def sortArrayByParity(self, A):
        i, j = 0, len(A) - 1
        while i < j:                        # 查看所有数字除以2的余数
            if A[i] % 2 > A[j] % 2:         # 如果是 (1, 0)，
                A[i], A[j] = A[j], A[i]     # 那么交换两个元素，然后继续
            if A[i] % 2 == 0:               # 如梭左边指针是偶数
                i += 1                      # 右移左边指针
            if A[j] % 2 == 1:               # 如果右边指针是奇数
                j -= 1                      # 左移右边指针
        return A

if __name__ == "__main__":
    A = [3,1,2,4]
    sol = Solution()
    result = sol.sortArrayByParity(A)
    print (result)