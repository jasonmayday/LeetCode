"""
https://leetcode-cn.com/problems/buddy-strings/

给你两个字符串 s 和 goal ，只要我们可以通过交换 s 中的两个字母得到与 goal 相等的结果，就返回 true ；否则返回 false 。

交换字母的定义是：取两个下标 i 和 j （下标从 0 开始）且满足 i != j ，接着交换 s[i] 和 s[j] 处的字符。

例如，在 "abcd" 中交换下标 0 和下标 2 的元素可以生成 "cbad" 。

示例 1：
    输入：s = "ab", goal = "ba"
    输出：true
    解释：你可以交换 s[0] = 'a' 和 s[1] = 'b' 生成 "ba"，此时 s 和 goal 相等。

示例 2：
    输入：s = "ab", goal = "ab"
    输出：false
    解释：你只能交换 s[0] = 'a' 和 s[1] = 'b' 生成 "ba"，此时 s 和 goal 不相等。

示例 3：
    输入：s = "aa", goal = "aa"
    输出：true
    解释：你可以交换 s[0] = 'a' 和 s[1] = 'a' 生成 "aa"，此时 s 和 goal 相等。

示例 4：
    输入：s = "aaaaaaabc", goal = "aaaaaaacb"
    输出：true
 

提示：
    1 <= s.length, goal.length <= 2 * 10^4
    s 和 goal 由小写英文字母组成

"""

class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        diff = []
        if len(A) == len(B):        # 字符串长度不相等, 直接返回false
            for i in range(len(A)):
                if A[i] != B[i]:    # diff 为两个字符串中下标相同但字母不同的元素
                    diff.append(i)
            if len(diff) == 2 and A[diff[0]] == B[diff[1]] and A[diff[1]] == B[diff[0]]:
                return True         # 有两个不同元素时，交换后相同为True
            if len(diff) == 0 and len(A) - len(set(A)) > 0:
                return True         # 元素完全相同时，A 中有重复字符时才为 True
        return False                # 比如'abcd'与'abcd'返回的是false，但是'abca'与'abca'返回的是true。

if __name__ == "__main__":
    s = "abc"
    goal = "cba"
    sol = Solution()
    result = sol.buddyStrings(s, goal)
    print(result)