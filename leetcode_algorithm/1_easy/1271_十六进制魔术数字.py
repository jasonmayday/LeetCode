"""
https://leetcode-cn.com/problems/hexspeak/

你有一个十进制数字，请按照此规则将它变成「十六进制魔术数字」：首先将它变成字母大写的十六进制字符串，然后将所有的数字 0 变成字母 O ，将数字 1  变成字母 I 。

如果一个数字在转换后只包含 {"A", "B", "C", "D", "E", "F", "I", "O"} ，那么我们就认为这个转换是有效的。

给你一个字符串 num ，它表示一个十进制数 N，如果它的十六进制魔术数字转换是有效的，请返回转换后的结果，否则返回 "ERROR" 。

示例 1：
    输入：num = "257"
    输出："IOI"
    解释：257 的十六进制表示是 101 。

示例 2：
    输入：num = "3"
    输出："ERROR"

提示：
    1 <= N <= 10^12
    给定字符串不会有前导 0 。
    结果中的所有字母都应该是大写字母。

"""

""" 方法一：模拟 """
class Solution:
    def toHexspeak(self, num: str) -> str:
        num_hex = hex(int(num))[2:]     # 101
        transform = {
            "0": "O",
            "1": "I",
            "a": "A",
            "b": "B",
            "c": "C",
            "d": "D",
            "e": "E",
            "f": "F",
        }
        ans = ""
        for ch in num_hex:
            if ch not in transform:
                return "ERROR"
            ans += transform[ch]
        return ans


""" 正则表达式
    https://docs.python.org/3/library/re.html"""
class Solution:
    def toHexspeak(self, num: str) -> str:
        import re
        hexStr = hex(int(num))[2:].replace("0", "O").replace("1", "I").upper()
        return hexStr if re.sub(r"A|B|C|D|E|F|I|O", "", hexStr) == "" else "ERROR"

class Solution:
    def toHexspeak(self, num: str) -> str:
        s = hex(int(num))[2:].upper().replace('0', 'O').replace('1', 'I')
        return s if set(s) < {"A", "B", "C", "D", "E", "F", "I", "O"} else "ERROR"

if __name__ == "__main__":
    num = "257"
    sol = Solution()
    result = sol.toHexspeak(num)
    print(result)