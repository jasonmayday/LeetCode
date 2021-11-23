'''
给你长度相等的两个字符串 s1 和 s2 。一次 字符串交换 操作的步骤如下：选出某个字符串中的两个下标（不必不同），并交换这两个下标所对应的字符。

如果对 其中一个字符串 执行 最多一次字符串交换 就可以使两个字符串相等，返回 true ；否则，返回 false 。

示例 1：
输入：s1 = "bank", s2 = "kanb"
输出：true
解释：例如，交换 s2 中的第一个和最后一个字符可以得到 "bank"

示例 2：
输入：s1 = "attack", s2 = "defend"
输出：false
解释：一次字符串交换无法使两个字符串相等

示例 3：
输入：s1 = "kelb", s2 = "kelb"
输出：true
解释：两个字符串已经相等，所以不需要进行字符串交换

示例 4：
输入：s1 = "abcd", s2 = "dcba"
输出：false

'''

# 结束的时候，判断二者的长度是否等于 2 并且相等就行了

s1 = "bank"
s2 = "kanb"

class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        s1_str = ""
        s2_str = ""   # 提前申请两个字符串变量用于记录不同的字符
        for i in range(len(s1)):
            if s1[i] == s2[i]:
                continue
            else:     # 对于 s1 与 s2 不同的字符:
                s1_str += s1[i]           # 加到 s1 对应字符串变量的后面
                s2_str = s2[i] + s2_str   # 加到 s2 对应字符串变量的前面
                if len(s1_str) > 2:       # 结束的时候，判断二者的长度是否等于 2 并且相等：
                    return False          # 如果不同字母组成的新字符串大于2，返回 False
        return len(s1_str) == 2 and s1_str == s2_str  # 如果不同字母组成的新字符串等于2且相同，返回 True

if __name__ == "__main__":
    sol = Solution()
    result = sol.areAlmostEqual(s1, s2)
    print(result)


