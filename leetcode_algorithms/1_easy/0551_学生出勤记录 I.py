"""
https://leetcode-cn.com/problems/student-attendance-record-i/

给你一个字符串 s 表示一个学生的出勤记录，其中的每个字符用来标记当天的出勤情况（缺勤、迟到、到场）。记录中只含下面三种字符：
    'A'：Absent，缺勤
    'L'：Late，迟到
    'P'：Present，到场

如果学生能够 同时 满足下面两个条件，则可以获得出勤奖励：
    按 总出勤 计，学生缺勤（'A'）严格 少于两天。
    学生 不会 存在 连续 3 天或 连续 3 天以上的迟到（'L'）记录。

如果学生可以获得出勤奖励，返回 true ；否则，返回 false 。

示例 1：
    输入：s = "PPALLP"
    输出：true
    解释：学生缺勤次数少于 2 次，且不存在 3 天或以上的连续迟到记录。

示例 2：
    输入：s = "PPALLL"
    输出：false
    解释：学生最后三天连续迟到，所以不满足出勤奖励的条件。

提示：
    1 <= s.length <= 1000
    s[i] 为 'A'、'L' 或 'P'

"""

class Solution:
    def checkRecord(self, s: str) -> bool:
        absents = lates = 0
        for i in enumerate(s):
            if i == "A":
                absents += 1
                if absents >= 2:
                    return False
            if i == "L":
                lates += 1
                if lates >= 3:
                    return False
            else:
                lates = 0       # 如果lates没有连续三天出现，则lates清零
        return True

class Solution:
    def checkRecord(self, s: str) -> bool:
        if "LLL" in s or s.count('A') > 1:
            return False
        return True

if __name__ == "__main__":
    s = "LLALLPLLPLL"
    sol = Solution()
    result = sol.checkRecord(s)
    print(result)