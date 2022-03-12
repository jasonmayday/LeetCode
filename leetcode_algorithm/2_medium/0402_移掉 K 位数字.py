"""
https://leetcode-cn.com/problems/remove-k-digits/

给你一个以字符串表示的非负整数 num 和一个整数 k ，移除这个数中的 k 位数字，使得剩下的数字最小。请你以字符串形式返回这个最小的数字。

示例 1 ：
    输入：num = "1432219", k = 3
    输出："1219"
    解释：移除掉三个数字 4, 3, 和 2 形成一个新的最小的数字 1219 。

示例 2 ：
    输入：num = "10200", k = 1
    输出："200"
    解释：移掉首位的 1 剩下的数字为 200. 注意输出不能有任何前导零。

示例 3 ：
    输入：num = "10", k = 2
    输出："0"
    解释：从原数字移除所有的数字，剩余为空就是 0 。

提示：
    1 <= k <= num.length <= 10^5
    num 仅由若干位数字（0 - 9）组成
    除了 0 本身之外，num 不含任何前导零

"""

""" 方法一：贪心 + 单调栈
    给定一个长度为 nn 的数字序列 [D0 D1 D2 D3 … Dn−1]，从左往右找到第一个位置 i（i>0）使得 Di < Di−1，并删去 Di−1
    如果不存在，说明整个数字序列单调不降，删去最后一个数字即可。
"""
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        numStack = []   # 栈中的元素代表截止到当前位置，删除不超过 k 次个数字后，所能得到的最小整数。
        # 构建单调递增的数字串，保持栈内元素单调非严格递增
        for digit in num:
            while k and numStack and digit < numStack[-1]:  # 对于每个数字，如果该数字小于栈顶元素
                numStack.pop()                              # 我们就不断地弹出栈顶元素
                k -= 1
            numStack.append(digit)  # ['0', '2', '0', '0']

        # 如果 K > 0，删除末尾的 K 个字符
        finalStack = numStack[:-k] if k else numStack
        
        # 抹去前导零
        return "".join(finalStack).lstrip('0') or "0"

if __name__ == "__main__":
    num = "10200"
    k = 1
    sol = Solution()
    result = sol.removeKdigits(num, k)
    print (result)