'''
https://leetcode-cn.com/problems/reformat-date/

给你一个字符串 date ，它的格式为 Day Month Year ，其中：

Day 是集合 {"1st", "2nd", "3rd", "4th", ..., "30th", "31st"} 中的一个元素。
Month 是集合 {"Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"} 中的一个元素。
Year 的范围在 ​[1900, 2100] 之间。
请你将字符串转变为 YYYY-MM-DD 的格式，其中：

YYYY 表示 4 位的年份。
MM 表示 2 位的月份。
DD 表示 2 位的天数。

示例 1：
输入：date = "20th Oct 2052"
输出："2052-10-20"

示例 2：
输入：date = "6th Jun 1933"
输出："1933-06-06"

示例 3：
输入：date = "26th May 1960"
输出："1960-05-26"

'''
date = "20th Oct 1991"

class Solution:
    def reformatDate(self, date: str) -> str:
        day, month, year = date.split(' ')
        MonthDict = {"Jan":"01", "Feb":"02", "Mar":"03", "Apr":"04", "May":"05", "Jun":"06", "Jul":"07", "Aug":"08", "Sep":"09", "Oct":"10", "Nov":"11", "Dec":"12"}
        month = MonthDict[month]
        day = day[:2] if day[1].isdigit() else '0' + str(day[0])
        return '-'.join([year,month,day])

sol = Solution()
result = sol.reformatDate(date)
print(result)
