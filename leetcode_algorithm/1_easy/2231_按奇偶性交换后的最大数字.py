"""
https://leetcode.cn/problems/largest-number-after-digit-swaps-by-parity/

给你一个正整数 num 。你可以交换 num 中 奇偶性 相同的任意两位数字（即，都是奇数或者偶数）。

返回交换 任意 次之后 num 的 最大 可能值。

示例 1：
    输入：num = 1234
    输出：3412
    解释：交换数字 3 和数字 1 ，结果得到 3214 。
    交换数字 2 和数字 4 ，结果得到 3412 。
    注意，可能存在其他交换序列，但是可以证明 3412 是最大可能值。
    注意，不能交换数字 4 和数字 1 ，因为它们奇偶性不同。

示例 2：
    输入：num = 65875
    输出：87655
    解释：交换数字 8 和数字 6 ，结果得到 85675 。
    交换数字 5 和数字 7 ，结果得到 87655 。
    注意，可能存在其他交换序列，但是可以证明 87655 是最大可能值。

提示：
    1 <= num <= 10^9

"""
class Solution:
    def largestInteger(self, num: int) -> int:
        l = [int(d) for d in list(str(num))]   # [1, 2, 3, 4]
        n = len(l)
        # 进行选择排序
        for i in range(n - 1):
            for j in range(i + 1, n):
                if (l[i] - l[j]) % 2 == 0 and l[i] < l[j]:  # 数值奇偶相同，且后面数字大于前面数字时
                    l[i], l[j] = l[j], l[i]                 # 交换两个数字位置
        # 转化为最终的整数
        return int("".join(str(d) for d in l))

if __name__ == "__main__":
    num = 1234
    sol = Solution()
    result = sol.largestInteger(num)
    print (result)