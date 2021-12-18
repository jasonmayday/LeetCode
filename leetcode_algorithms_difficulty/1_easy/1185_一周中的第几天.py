"""
https://leetcode-cn.com/problems/day-of-the-week/

给你一个日期，请你设计一个算法来判断它是对应一周中的哪一天。

输入为三个整数：day、month 和 year，分别表示日、月、年。

您返回的结果必须是这几个值中的一个 {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"}。

示例 1：
    输入：day = 31, month = 8, year = 2019
    输出："Saturday"

示例 2：
    输入：day = 18, month = 7, year = 1999
    输出："Sunday"

示例 3：
    输入：day = 15, month = 8, year = 1993
    输出："Sunday"

提示：
    给出的日期一定是在 1971 到 2100 年之间的有效日期。

"""

class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        # 1971年1月1日为星期五
        res = ["Friday", "Saturday","Sunday", "Monday", "Tuesday", "Wednesday", "Thursday"]
        # 后续算时间需要减掉1天，故置为-1
        days = -1
        for y in range(1971, year):
            if self.isLeapYear(y):
                days += 366
            else:
                days += 365
        for m in range(1, month):
            if m == 2:
                if self.isLeapYear(year):
                    days += 29
                else:
                    days += 28
            elif m in [1,3,5,7,8,10,12]:
                days += 31
            else:
                days += 30
        days += day
        return res[days % 7]
    
    def isLeapYear(self,year):
        if year % 400 == 0: return True
        if year % 4 == 0 and year % 100 != 0: return True
        return False

if __name__ == "__main__":
    text = "loonbalxballpoon"
    sol = Solution()
    result = sol.maxNumberOfBalloons(text)
    print(result)