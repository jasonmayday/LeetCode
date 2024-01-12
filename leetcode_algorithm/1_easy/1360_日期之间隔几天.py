"""
https://leetcode-cn.com/problems/number-of-days-between-two-dates/

请你编写一个程序来计算两个日期之间隔了多少天。

日期以字符串形式给出，格式为 YYYY-MM-DD，如示例所示。

示例 1：
    输入：date1 = "2019-06-29", date2 = "2019-06-30"
    输出：1

示例 2：
    输入：date1 = "2020-01-15", date2 = "2019-12-31"
    输出：15

提示：
    给定的日期是 1971 年到 2100 年之间的有效日期。

"""

"""解法1：datetime库"""
class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        from datetime import datetime
        date1 = datetime.strptime(date1,'%Y-%m-%d')
        date2 = datetime.strptime(date2,'%Y-%m-%d')
        res = abs((date1 - date2).days)
        return res
    
"""解法2：计算俩日期与1970年1月1日相差的天数，再计算俩天数之差"""
class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        
        return abs(self.gap(*self.format_date(date1)) - self.gap(*self.format_date(date2)))
    
    def gap(self, y, m, d):
        res, y_leap_year = 0, self.is_leap(y)
        month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        while y > 1971:
            if self.is_leap(y):
                res += 366
            else:
                res += 365
            y -= 1
        res += sum(month[:m]) + d
        if y_leap_year and m < 3:
            res -= 1
        return res

    def format_date(self, date_str):
        return map(int, date_str.split('-'))

    def is_leap(self, year):
        return year % 400 == 0 or (year % 100 != 0 and year % 4 == 0)

"""解法3：zeller公式"""
class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        return abs(self.to_day(date1) - self.to_day(date2))
    
    def to_day(self, date_str):
        year, month, day = map(int, date_str.split('-'))
        if month < 3:
            year, month = year-1, month+10
        else:
            month -= 2
        return 365 * year + year // 4 - year // 100 + year // 400 + 30 * month + (3 * month - 1) // 5 + day #- 584418

"""解法4：判断俩日期大小再计算"""
class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        year1, month1, day1 = self.format_date(max(date1, date2))
        year2, month2, day2 = self.format_date(min(date1, date2))
        return self.days_from_start(year1, month1, day1) - self.days_from_start(year2, month2, day2) + self.gap(year2, year1)

    def format_date(self, date_str):
        return map(int, date_str.split('-'))

    def is_leap(self, year):
        return year % 400 == 0 or (year % 100 != 0 and year % 4 == 0)

    def gap(self, y1, y2):
        return sum(366 if self.is_leap(y) else 365 for y in range(y1, y2))

    def days_from_start(self, y, m, d):
        month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        return sum(month_days[:m-1]) + d + (1 if self.is_leap(y) and m > 2 else 0)

if __name__ == "__main__":
    date1 = "1990-01-15"
    date2 = "2019-12-31"
    sol = Solution()
    result = sol.daysBetweenDates(date1, date2)
    print(result)