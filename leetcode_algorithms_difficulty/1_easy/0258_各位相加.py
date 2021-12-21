"""
https://leetcode-cn.com/problems/add-digits/

给定一个非负整数 num，反复将各个位上的数字相加，直到结果为一位数。

示例:
    输入: 38
    输出: 2 
    解释: 各位相加的过程为：3 + 8 = 11, 1 + 1 = 2。 由于 2 是一位数，所以返回 2。

进阶:
    你可以不使用循环或者递归，且在 O(1) 时间复杂度内解决这个问题吗？

"""

"""递归"""
class Solution:
    def addDigits(self, num: int) -> int:
        if (len(str(num))==1):
            return num
        else:
            num = sum([int(i) for i in list(str(num))])
            return self.addDigits(num)

"""任意num为9的倍数时，其位数最终和必为0"""
class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        if num % 9 == 0:
            return 9
        return num % 9


if __name__ == "__main__":
    num = 38
    sol = Solution()
    result = sol.addDigits(num)
    print(result)