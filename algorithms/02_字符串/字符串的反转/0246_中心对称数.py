"""
https://leetcode-cn.com/problems/strobogrammatic-number/

中心对称数是指一个数字在旋转了 180 度之后看起来依旧相同的数字（或者上下颠倒地看）。

请写一个函数来判断该数字是否是中心对称数，其输入将会以一个字符串的形式来表达数字。

示例 1:
    输入: num = "69"
    输出: true

示例 2:
    输入: num = "88"
    输出: true

示例 3:
    输入: num = "962"
    输出: false

示例 4：
    输入：num = "1"
    输出：true

"""

class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        strobogrammatic_numbers = { "6" : "9",
                                    "9" : "6",
                                    "8" : "8",
                                    "1" : "1",
                                    "0" : "0"   }
        rotated_num = ""
        for a in num:
            if a in strobogrammatic_numbers:
                rotated_num += strobogrammatic_numbers[a]
            else:
                return False
        return rotated_num[::-1] == num

if __name__ == "__main__":
    num = "69"
    sol = Solution()
    result = sol.isStrobogrammatic(num)
    print(result)