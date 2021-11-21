"""
https://leetcode-cn.com/problems/self-dividing-numbers

自除数 是指可以被它包含的每一位数除尽的数。

例如，128 是一个自除数，因为 128 % 1 == 0，128 % 2 == 0，128 % 8 == 0。

还有，自除数不允许包含 0 。

给定上边界和下边界数字，输出一个列表，列表的元素是边界（含边界）内所有的自除数。

示例 1：
    输入： 
    上边界left = 1, 下边界right = 22
    输出： [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]

注意：
    每个输入参数的边界满足 1 <= left <= right <= 10000。

"""

class Solution(object):
    def selfDividingNumbers(self, left, right):
        def self_dividing(n):       # 定义函数判断是不是自除数
            for d in str(n):        # 把数字转换为字符串，然后遍历
                if d == '0' or n % int(d) > 0:  # 当出现某位是0或者某位不能被数字整除时，不是自除数
                    return False
            return True

        ans = []
        for n in range(left, right + 1):
            if self_dividing(n):
                ans.append(n)
        return ans


if __name__ == "__main__":
    left = 1
    right = 10000
    sol = Solution()
    result = sol.selfDividingNumbers(left,right)
    print(result)