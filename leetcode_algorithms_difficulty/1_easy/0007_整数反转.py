'''
https://leetcode-cn.com/problems/reverse-integer/

给你一个 32 位的有符号整数 x ，返回将 x 中的数字部分反转后的结果。

如果反转后整数超过 32 位的有符号整数的范围 [−231,  231 − 1] ，就返回 0。

假设环境不允许存储 64 位整数（有符号或无符号）。

示例 1：
    输入：x = 123
    输出：321

示例 2：
    输入：x = -123
    输出：-321

示例 3：
    输入：x = 120
    输出：21

示例 4：
    输入：x = 0
    输出：0

提示：
    -2^31 <= x <= 2^31-1

'''

class Solution:
    def reverse(self, x: int) -> int:
        if -10 < x < 10:
            return x
        str_x = str(x)
        if str_x[0] != "-":        # 如果是正数
            str_x = str_x[::-1]    # a[::-1] end to beginning, counting down by 1，e.g. 210 → 012
            x = int(str_x)         # 转化为整数，解决末尾是0的问题，e.g. 012 → 12
        else:                      # 如果是负数
            str_x = str_x[:0:-1]   # a[:0:-1]: 去除首位字符、并反转第 1-n 位字符, e.g. -210 → 012
            x = int(str_x)         # 转化为整数，e.g. 012 → 12
            x = -x                 # e.g. 12 → -12
        return x if -2147483648 < x < 2147483647 else 0

if __name__ == "__main__":
    x = -210
    sol = Solution()
    result = sol.reverse(x)
    print(result)

