"""
https://leetcode-cn.com/problems/number-of-days-in-a-month/

指定年份 year 和月份 month，返回 该月天数 。

示例 1：
    输入：year = 1992, month = 7
    输出：31

示例 2：
    输入：year = 2000, month = 2
    输出：29

示例 3：
    输入：year = 1900, month = 2
    输出：28

提示：
    1583 <= year <= 2100
    1 <= month <= 12

"""

class Solution(object):
    def numberOfDays(self, year: int, month: int) -> int:
        if (year % 100 != 0 and year % 4 == 0) or year % 400 == 0:
            return [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][month - 1] # 闰年
        else:
            return [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][month - 1] # 非闰年

if __name__ == "__main__":
    year = 2000
    month = 2
    sol = Solution()
    result = sol.numberOfDays(year, month)
    print(result)