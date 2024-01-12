"""
https://leetcode-cn.com/problems/construct-string-with-repeat-limit/

给你一个字符串 s 和一个整数 repeatLimit ，用 s 中的字符构造一个新字符串 repeatLimitedString ，使任何字母 连续 出现的次数都不超过 repeatLimit 次。你不必使用 s 中的全部字符。

返回 字典序最大的 repeatLimitedString 。

如果在字符串 a 和 b 不同的第一个位置，字符串 a 中的字母在字母表中出现时间比字符串 b 对应的字母晚，则认为字符串 a 比字符串 b 字典序更大 。如果字符串中前 min(a.length, b.length) 个字符都相同，那么较长的字符串字典序更大。

示例 1：
    输入：s = "cczazcc", repeatLimit = 3
    输出："zzcccac"
    解释：使用 s 中的所有字符来构造 repeatLimitedString "zzcccac"。
    字母 'a' 连续出现至多 1 次。
    字母 'c' 连续出现至多 3 次。
    字母 'z' 连续出现至多 2 次。
    因此，没有字母连续出现超过 repeatLimit 次，字符串是一个有效的 repeatLimitedString 。
    该字符串是字典序最大的 repeatLimitedString ，所以返回 "zzcccac" 。
    注意，尽管 "zzcccca" 字典序更大，但字母 'c' 连续出现超过 3 次，所以它不是一个有效的 repeatLimitedString 。

示例 2：
    输入：s = "aababab", repeatLimit = 2
    输出："bbabaa"
    解释：
    使用 s 中的一些字符来构造 repeatLimitedString "bbabaa"。 
    字母 'a' 连续出现至多 2 次。 
    字母 'b' 连续出现至多 2 次。 
    因此，没有字母连续出现超过 repeatLimit 次，字符串是一个有效的 repeatLimitedString 。 
    该字符串是字典序最大的 repeatLimitedString ，所以返回 "bbabaa" 。 
    注意，尽管 "bbabaaa" 字典序更大，但字母 'a' 连续出现超过 2 次，所以它不是一个有效的 repeatLimitedString 。

提示：
    1 <= repeatLimit <= s.length <= 10^5
    s 由小写英文字母组成

"""


""" 方法一：双指针 """
class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        ans = sorted (list(s), reverse = True)  # 字符串转为列表，然后根据字母表倒序排列    ['z', 'z', 'c', 'c', 'c', 'c', 'a']
        cnt = 1
        right = 2
        for left in range(1, len(ans)):
            if ans[left - 1] != ans[left]:  # 左指针与左指针左边的不一样
                cnt = 1                     # cnt 重置为 1
            else:                           # 左指针与左指针左边的一样
                cnt += 1                    # 统计有多少个连续相同的
                if cnt > repeatLimit:       # 如果连续出现的字符超过限制：
                    right = max(right, left + 1)                        # 生成右指针
                    while right < len(ans) and ans[left] == ans[right]: # 在数组范围内，如果连续相同的字符继续重复：
                        right += 1                                      # 右指针继续向右移，直到右指针遇到和左指针不同的字符
                    if right < len(ans):                                # 在数组范围内
                        ans[left], ans[right] = ans[right], ans[left]   # 左右指针的数字交换，（第 "repeatLimit+1 个重复字符" 和 "后面第一个与之前不重复的字符" 交换）
                        cnt = 1
                    else:
                        ans = ans[:left]
                        break
        
        return "".join(ans)

if __name__ == "__main__":
    s = "cczazcc"
    repeatLimit = 3
    sol = Solution()
    result = sol.repeatLimitedString(s, repeatLimit)
    print (result)