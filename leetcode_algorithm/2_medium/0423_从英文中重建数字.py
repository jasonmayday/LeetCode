"""
https://leetcode-cn.com/problems/reconstruct-original-digits-from-english/

给你一个字符串 s ，其中包含字母顺序打乱的用英文单词表示的若干数字（0-9）。按 升序 返回原始的数字。

示例 1：
    输入：s = "owoztneoer"
    输出："012"

示例 2：
    输入：s = "fviefuro"
    输出："45"

提示：
    1 <= s.length <= 10^5
    s[i] 为 ["e","g","f","i","h","o","n","s","r","u","t","w","v","x","z"] 这些字符之一
    s 保证是一个符合题目要求的字符串

"""
from collections import Counter

"""
统计每个字母分别在哪些数字中出现：

字母	数字
z	    0
w	    2
u	    4
x	    6
g	    8

h	    3 8
f	    4 5
s	    6 7

o	    0 1 2 4
i	    5 6 8 9

e	    0 1 3 5 7 8 9
n	    1 7 9
r	    0 3 4
t	    2 3 8
v	    5 7

"""
class Solution:
    def originalDigits(self, s: str) -> str:
        c = Counter(s)

        cnt = [0] * 10
        cnt[0] = c["z"]     # z, w, u, x, g 都只在一个数字中
        cnt[2] = c["w"]     # 即 0, 2, 4, 6, 8 中出现
        cnt[4] = c["u"]     # 因此我们可以使用一个哈希表统计每个字母出现的次数
        cnt[6] = c["x"]     # 那么 z, w, u, x, g 出现的次数
        cnt[8] = c["g"]     # 即分别为 0, 2, 4, 6, 8 出现的次数

        cnt[3] = c["h"] - cnt[8]    # h 只在 3, 8 中出现。由于我们已经知道了 8 出现的次数，因此可以计算出 3 出现的次数。
        cnt[5] = c["f"] - cnt[4]    # f 只在 4, 5 中出现。由于我们已经知道了 4 出现的次数，因此可以计算出 5 出现的次数。
        cnt[7] = c["s"] - cnt[6]    # s 只在 6, 7 中出现。由于我们已经知道了 6 出现的次数，因此可以计算出 7 出现的次数。
        
        cnt[1] = c["o"] - cnt[0] - cnt[2] - cnt[4]  # o 只在 0,1,2,4 中出现，由于我们已经知道了 0,2,4 出现的次数，因此可以计算出 1 出现的次数。

        cnt[9] = c["i"] - cnt[5] - cnt[6] - cnt[8]  # 最后的 9 就可以通过 n, i, e 中的任一字符计算得到了

        return "".join(str(x) * cnt[x] for x in range(10))  # 按照升序将它们进行拼接
    
if __name__ == "__main__":
    s = "owoztneoer"
    sol = Solution()
    result = sol.originalDigits(s)
    print (result) 