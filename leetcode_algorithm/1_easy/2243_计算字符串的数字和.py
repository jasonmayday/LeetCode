"""
https://leetcode.cn/problems/calculate-digit-sum-of-a-string/

给你一个由若干数字（0 - 9）组成的字符串 s ，和一个整数。

如果 s 的长度大于 k ，则可以执行一轮操作。在一轮操作中，需要完成以下工作：

    1. 将 s 拆分 成长度为 k 的若干 连续数字组 ，使得前 k 个字符都分在第一组，接下来的 k 个字符都分在第二组，依此类推。注意，最后一个数字组的长度可以小于 k 。
    2. 用表示每个数字组中所有数字之和的字符串来 替换 对应的数字组。例如，"346" 会替换为 "13" ，因为 3 + 4 + 6 = 13 。
    3. 合并 所有组以形成一个新字符串。如果新字符串的长度大于 k 则重复第一步。

返回在完成所有轮操作后的 s 。

示例 1：
    输入：s = "11111222223", k = 3
    输出："135"
    解释：
        - 第一轮，将 s 分成："111"、"112"、"222" 和 "23" 。
        接着，计算每一组的数字和：1 + 1 + 1 = 3、1 + 1 + 2 = 4、2 + 2 + 2 = 6 和 2 + 3 = 5 。
          这样，s 在第一轮之后变成 "3" + "4" + "6" + "5" = "3465" 。
        - 第二轮，将 s 分成："346" 和 "5" 。
          接着，计算每一组的数字和：3 + 4 + 6 = 13 、5 = 5 。
          这样，s 在第二轮之后变成 "13" + "5" = "135" 。
        现在，s.length <= k ，所以返回 "135" 作为答案。

示例 2：
    输入：s = "00000000", k = 3
    输出："000"
    解释：
        将 "000", "000", and "00".
        接着，计算每一组的数字和：0 + 0 + 0 = 0 、0 + 0 + 0 = 0 和 0 + 0 = 0 。
        s 变为 "0" + "0" + "0" = "000" ，其长度等于 k ，所以返回 "000" 。

提示：
    1 <= s.length <= 100
    2 <= k <= 100
    s 仅由数字（0 - 9）组成。

"""

"""方法一：模拟"""
class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            tmp = []   # 每次操作结束的字符串对应数组
            n = len(s)
            for i in range(0, n, k):    # 遍历字符串 s，以每 k 个字符为一组
                val = 0                 # 一组内数字的和，初始val为0
                for j in range(i, min(i + k, n)):   # 从下标i开始，遍历i之后的k个数字（并且下标小于总长n的）
                    val += int(s[j])                # 计算该组的数字和 val，
                tmp.append(str(val))                # 并转化为字符串添加至 tmp 尾部。
            s = "".join(tmp)                        # 最终，将 s 更新为 tmp 所表示的字符串。
        return s

if __name__ == "__main__":
    s = "11111222223"
    k = 3
    sol = Solution()
    result = sol.digitSum(s, k)
    print (result)