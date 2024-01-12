"""
https://leetcode.cn/problems/find-the-k-beauty-of-a-number/

一个整数 num 的 k 美丽值定义为 num 中符合以下条件的 子字符串 数目：
    子字符串长度为 k 。
    子字符串能整除 num 。

给你整数 num 和 k ，请你返回 num 的 k 美丽值。

注意：
    允许有 前缀 0 。
    0 不能整除任何值。
    一个 子字符串 是一个字符串里的连续一段字符序列。

示例 1：
    输入：num = 240, k = 2
    输出：2
    解释：以下是 num 里长度为 k 的子字符串：
    - "240" 中的 "24" ：24 能整除 240 。
    - "240" 中的 "40" ：40 能整除 240 。
    所以，k 美丽值为 2 。

示例 2：
    输入：num = 430043, k = 2
    输出：2
    解释：以下是 num 里长度为 k 的子字符串：
    - "430043" 中的 "43" ：43 能整除 430043 。
    - "430043" 中的 "30" ：30 不能整除 430043 。
    - "430043" 中的 "00" ：0 不能整除 430043 。
    - "430043" 中的 "04" ：4 不能整除 430043 。
    - "430043" 中的 "43" ：43 能整除 430043 。
    所以，k 美丽值为 2 。

提示：
    1 <= num <= 10^9
    1 <= k <= num.length （将 num 视为字符串）

"""

"""方法一：枚举"""
class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        s = str(num)   # num 十进制表示字符串
        n = len(s)
        res = 0
        for i in range(n - k + 1):
            tmp = int(s[i: i+k])    # 枚举所有长度为 k 的子串
            if tmp != 0 and num % tmp == 0: # 不为0，且能整除num
                res += 1
        return res

if __name__ == "__main__":
    num = 430043
    k = 2
    sol = Solution()
    result = sol.divisorSubstrings(num, k)
    print (result)