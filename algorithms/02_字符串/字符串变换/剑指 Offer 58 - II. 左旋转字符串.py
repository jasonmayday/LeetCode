"""
字符串的左旋转操作是把字符串前面的若干个字符转移到字符串的尾部。

请定义一个函数实现字符串左旋转操作的功能。比如，输入字符串"abcdefg"和数字2，该函数将返回左旋转两位得到的结果"cdefgab"。

示例 1：
    输入: s = "abcdefg", k = 2
    输出: "cdefgab"

示例 2：
    输入: s = "lrloseumgh", k = 6
    输出: "umghlrlose"

限制：
    1 <= k < s.length <= 10000

"""


""" 方法一：字符串切片"""
class Solution:
    def reverseLeftWords(self, s: str, k: int) -> str:
        return s[k:] + s[:k]


""" 方法二：列表遍历拼接"""
class Solution:
    def reverseLeftWords(self, s: str, k: int) -> str:
        res = []
        for i in range(k, len(s)):
            res.append(s[i])    # 添加 k+1 位至末位的字符
        for i in range(k):
            res.append(s[i])
        return ''.join(res)     # 添加首位至第 k 位的字符


""" 方法三：字符串遍历拼接"""
class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        res = ""
        for i in range(n, len(s)):
            res += s[i]
        for i in range(n):
            res += s[i]
        return res


if __name__ == "__main__":
    s = "abcdefg"
    k = 2
    sol = Solution()
    result = sol.reverseLeftWords(s,k)
    print (result)