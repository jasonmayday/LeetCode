"""
https://leetcode-cn.com/problems/nth-digit/

给你一个整数 n ，请你在无限的整数序列 [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...] 中找出并返回第 n 位数字。

示例 1：
    输入：n = 3
    输出：3

示例 2：
    输入：n = 11
    输出：0
    解释：第 11 位数字在序列 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... 里是 0 ，它是 10 的一部分。

提示：
1 <= n <= 2^31 - 1

"""
class Solution:
    def findNthDigit(self, n: int) -> int:
        section_cnt = 9     #当前的数字长度，区间的数字个数
        num_len = 1         #数字的长度
        while section_cnt * num_len < n:
            n -= section_cnt * num_len  #减去当前这个长度所占的位数
            num_len += 1
            section_cnt *= 10

        section_cnt //= 9       #比如是10000
        target_num = section_cnt + (n - 1) // num_len   #第n位所在的那个数字
        idx = (n - 1) % num_len                         #第n为是在那个数字的第idx位
        return int(str(target_num)[idx])


if __name__ == "__main__":
    n = 2**30
    sol = Solution()
    result = sol.findNthDigit(n)
    print (result) 