"""
https://leetcode.cn/problems/remove-digit-from-number-to-maximize-result/

给你一个表示某个正整数的字符串 number 和一个字符 digit 。

从 number 中 恰好 移除 一个 等于 digit 的字符后，找出并返回按 十进制 表示 最大 的结果字符串。生成的测试用例满足 digit 在 number 中出现至少一次。

示例 1：
    输入：number = "123", digit = "3"
    输出："12"
    解释："123" 中只有一个 '3' ，在移除 '3' 之后，结果为 "12" 。

示例 2：
    输入：number = "1231", digit = "1"
    输出："231"
    解释：可以移除第一个 '1' 得到 "231" 或者移除第二个 '1' 得到 "123" 。
    由于 231 > 123 ，返回 "231" 。

示例 3：
    输入：number = "551", digit = "5"
    输出："51"
    解释：可以从 "551" 中移除第一个或者第二个 '5' 。
    两种方案的结果都是 "51" 。

提示：
    2 <= number.length <= 100
    number 由数字 '1' 到 '9' 组成
    digit 是 '1' 到 '9' 中的一个数字
    digit 在 number 中出现至少一次

"""

"""方法一：枚举移除下标"""
class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        n = len(number)
        res = ""   # 可以得到的最大结果
        for i in range(n):              # 遍历字符串number
            if number[i] == digit:      # 如果某个字符等于digit
                tmp = number[:i] + number[i+1:] # 临时数组为去掉该字符的数组
                res = max(res, tmp)             # 如果比res大，则更新答案
        return res

"""方法二：贪心"""
class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        n = len(number)
        last = -1   # 最后一个可删除的下标
        for i in range(n):
            if number[i] == digit:
                last = i
                if i < n - 1 and number[i] < number[i+1]:
                    return number[:i] + number[i+1:]
        return number[:last] + number[last+1:]

if __name__ == "__main__":
    number = "1231"
    digit = "1"
    sol = Solution()
    result = sol.removeDigit(number, digit)
    print (result)