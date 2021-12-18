'''
https://leetcode-cn.com/problems/replace-all-s-to-avoid-consecutive-repeating-characters/

给你一个仅包含小写英文字母和 '?' 字符的字符串 s，请你将所有的 '?' 转换为若干小写字母，使最终的字符串不包含任何 连续重复 的字符。
注意：你 不能 修改非 '?' 字符。
题目测试用例保证 除 '?' 字符 之外，不存在连续重复的字符。
在完成所有转换（可能无需转换）后返回最终的字符串。如果有多个解决方案，请返回其中任何一个。可以证明，在给定的约束条件下，答案总是存在的。

示例 1：
输入：s = "?zs"
输出："azs"
解释：该示例共有 25 种解决方案，从 "azs" 到 "yzs" 都是符合题目要求的。只有 "z" 是无效的修改，因为字符串 "zzs" 中有连续重复的两个 'z' 。

示例 2：
输入：s = "ubv?w"
输出："ubvaw"
解释：该示例共有 24 种解决方案，只有替换成 "v" 和 "w" 不符合题目要求。因为 "ubvvw" 和 "ubvww" 都包含连续重复的字符。

示例 3：
输入：s = "j?qg??b"
输出："jaqgacb"

示例 4：
输入：s = "??yw?ipkj?"
输出："acywaipkja"

提示：
1 <= s.length <= 100
s 仅包含小写英文字母和 '?' 字符
'''


# 两层循环+两个哨兵，解决边界问号，每趟判断当前位置的左右两侧是否满足条件，不满足，顺序查找字母替换即可
import string

class Solution:
    def modifyString(self, s: str) -> str:
        alphabet = string.ascii_lowercase   #  alphabet = 'abcdefghijklmnopqrstuvwxyz'
        res = list('?' + s + '?')           #  把s字符串分解，res = ['?', 'u', 'b', 'v', '?', 'w', '?']，加头加尾就不用考虑麻烦的边界了
        
        for i in range (1, len(res)-1):               #  在这里 len(res) - 1 = 6
            if res[i] == '?':                         #  如果列表中某个字母为"?"
                for j in range (1, len(alphabet)-1):  #  在26个字母表中查找字母替换
                    if alphabet[j] != res[i-1] and alphabet[j] != res[i+1]:   #  如果新字母不等于"?"前后的字母：
                        res[i] = alphabet[j]                                  #  用新字母替换"?"
                        break
        return ''.join(res[1:-1])  #  生成新的字符串，去掉列表中第一个和最后一个字符。

if __name__ == "__main__":
    s = "ubv?w"
    sol = Solution()
    result = sol.modifyString(s)
    print (result)