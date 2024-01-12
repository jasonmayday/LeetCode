"""
https://leetcode-cn.com/problems/valid-word-abbreviation/

字符串可以用 缩写 进行表示，缩写 的方法是将任意数量的 不相邻 的子字符串替换为相应子串的长度。例如，字符串 "substitution" 可以缩写为（不止这几种方法）：
    "s10n" ("s ubstitutio n")
    "sub4u4" ("sub stit u tion")
    "12" ("substitution")
    "su3i1u2on" ("su bst i t u ti on")
    "substitution" (没有替换子字符串)

下列是不合法的缩写：
    "s55n" ("s ubsti tutio n"，两处缩写相邻)
    "s010n" (缩写存在前导零)
    "s0ubstitution" (缩写是一个空字符串)

给你一个字符串单词 word 和一个缩写 abbr ，判断这个缩写是否可以是给定单词的缩写。

子字符串是字符串中连续的非空字符序列。

示例 1：
    输入：word = "internationalization", abbr = "i12iz4n"
    输出：true
    解释：单词 "internationalization" 可以缩写为 "i12iz4n" ("i nternational iz atio n") 。

示例 2：
    输入：word = "apple", abbr = "a2e"
    输出：false
    解释：单词 "apple" 无法缩写为 "a2e" 。

提示：
    1 <= word.length <= 20
    word 仅由小写英文字母组成
    1 <= abbr.length <= 10
    abbr 由小写英文字母和数字组成
    abbr 中的所有数字均符合 32-bit 整数范围

"""

class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        point = 0
        num = 0         # 对于数字，尤其多位数字我们需要维护一个临时的num用于记录。
        leng = len(word)
        for i in abbr:
            if i.isdigit():
                if num == 0 and i == '0':   # (缩写存在前导零)
                    return False
                num = num * 10 + int(i)     # 当出现多位数字时，追加记录连续的数字
                continue
            if num:
                point += num    # 指针追加num
                num = 0
            if point >= leng or word[point] != i:   # 判断指针是否以超过word总长
                return False
            point += 1
        if point + num == leng: # 对于数字出现在最后的问题，需要在末尾添加point+num的操作后再进行判断
            return True
        else: return False

if __name__ == "__main__":
    word = "internationalization"
    abbr = "i12iz4n"
    sol = Solution()
    result = sol.validWordAbbreviation(word, abbr)
    print(result)