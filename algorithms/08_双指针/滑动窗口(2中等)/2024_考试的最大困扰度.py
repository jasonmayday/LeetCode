"""
https://leetcode-cn.com/problems/maximize-the-confusion-of-an-exam/

一位老师正在出一场由 n 道判断题构成的考试，每道题的答案为 true （用 'T' 表示）或者 false （用 'F' 表示）。
老师想增加学生对自己做出答案的不确定性，方法是 最大化 有 连续相同 结果的题数。（也就是连续出现 true 或者连续出现 false）。

给你一个字符串 answerKey ，其中 answerKey[i] 是第 i 个问题的正确结果。除此以外，还给你一个整数 k ，表示你能进行以下操作的最多次数：

    每次操作中，将问题的正确答案改为 'T' 或者 'F' （也就是将 answerKey[i] 改为 'T' 或者 'F' ）。

请你返回在不超过 k 次操作的情况下，最大 连续 'T' 或者 'F' 的数目。

示例 1：
    输入：answerKey = "TTFF", k = 2
    输出：4
    解释：我们可以将两个 'F' 都变为 'T' ，得到 answerKey = "TTTT" 。
    总共有四个连续的 'T' 。

示例 2：
    输入：answerKey = "TFFT", k = 1
    输出：3
    解释：我们可以将最前面的 'T' 换成 'F' ，得到 answerKey = "FFFT" 。
    或者，我们可以将第二个 'T' 换成 'F' ，得到 answerKey = "TFFF" 。
    两种情况下，都有三个连续的 'F' 。

示例 3：
    输入：answerKey = "TTFTTFTT", k = 1
    输出：5
    解释：我们可以将第一个 'F' 换成 'T' ，得到 answerKey = "TTTTTFTT" 。
    或者我们可以将第二个 'F' 换成 'T' ，得到 answerKey = "TTFTTTTT" 。
    两种情况下，都有五个连续的 'T' 。

提示：
    n == answerKey.length
    1 <= n <= 5 * 10^4
    answerKey[i] 要么是 'T' ，要么是 'F'
    1 <= k <= n

"""
from collections import Counter

""" 滑动窗口 """
class Solution:
    def maxConsecutiveAnswers(self, s: str, k: int) -> int:
        count = Counter()   # 记录遇到的 'T' 和 'F' 数量
        n, res = len(s), 0
        left, right = 0, 0

        while right < n:
            count[s[right]] += 1    # 右边一直扩展，最右的计数加一
            if min(count['T'], count['F']) > k: # T 和 F 数量小的会被改变，当范围内的计数小的答案超过了可调整次数时，表示当前无法再允许调整
                count[s[left]] -= 1         # 滑窗平移，最左的计数减一
                left += 1                   # 最左的指针向右一位
            right += 1
            res = max(res, right - left)    # 滑窗平移时不会影响最佳答案的更新
        return res

""" 滑动窗口 """
class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        def maxConsecutiveChar(ch: str) -> int:
            ans, left, sum = 0, 0, 0
            for right in range(len(answerKey)):
                sum += answerKey[right] != ch
                while sum > k:
                    sum -= answerKey[left] != ch
                    left += 1
                ans = max(ans, right - left + 1)
            return ans
        return max(maxConsecutiveChar('T'), maxConsecutiveChar('F'))

if __name__ == "__main__":
    answerKey = "TTFTTFTT"
    k = 1
    sol = Solution()
    result = sol.maxConsecutiveAnswers(answerKey, k)
    print(result)