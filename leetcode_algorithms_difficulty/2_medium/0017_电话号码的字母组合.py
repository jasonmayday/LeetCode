"""
https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number

给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。

给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。

示例 1：
    输入：digits = "23"
    输出：["ad","ae","af","bd","be","bf","cd","ce","cf"]

示例 2：
    输入：digits = ""
    输出：[]

示例 3：
    输入：digits = "2"
    输出：["a","b","c"]

提示：
    0 <= digits.length <= 4
    digits[i] 是范围 ['2', '9'] 的一个数字。

"""
from typing import List

"""方法1：回溯"""
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return list()
        
        phoneMap = {        # 首先使用哈希表存储每个数字对应的所有可能的字母，然后进行回溯操作。
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtrack(index: int):
            if index == len(digits):
                combinations.append("".join(combination))
            else:
                digit = digits[index]
                for letter in phoneMap[digit]:  # 每次取电话号码的一位数字，从哈希表中获得该数字对应的所有可能的字母
                    combination.append(letter)  # 并将其中的一个字母插入到已有的字母排列后面
                    backtrack(index + 1)        # 然后继续处理电话号码的后一位数字
                    combination.pop()

        combination = list()
        combinations = list()
        backtrack(0)
        return combinations


"""方法2：回溯（另一种格式）"""
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        phone = {'2':['a','b','c'],
                 '3':['d','e','f'],
                 '4':['g','h','i'],
                 '5':['j','k','l'],
                 '6':['m','n','o'],
                 '7':['p','q','r','s'],
                 '8':['t','u','v'],
                 '9':['w','x','y','z']}
                
        def backtrack(conbination, nextdigit):  # conbination为已经获得的字母组合，nextdigit 为后面还没有统计的数字
            if len(nextdigit) == 0:             # 所有数字都统计完时
                res.append(conbination)         # 将 combination 加入到结果中。
            else:       # 当 nextdigit 非空时，
                for letter in phone[nextdigit[0]]:  # 对于 nextdigit[0] 中的每一个字母 letter，执行回溯
                    backtrack(conbination + letter, nextdigit[1:])  # 直至 nextdigit 为空

        res = []
        backtrack('',digits)
        return res

"""方法3：队列"""
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        phone = ['abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
        queue = ['']  # 初始化队列
        for digit in digits:
            for _ in range(len(queue)):
                tmp = queue.pop(0)
                for letter in phone[ord(digit)-50]:# 这里我们不使用 int() 转换字符串，使用ASCII码
                    queue.append(tmp + letter)
        return queue

if __name__ == "__main__":
    digits = "23"
    sol = Solution()
    result = sol.letterCombinations(digits)
    print (result)