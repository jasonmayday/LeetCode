'''
给你一个字符串数组 words ，只返回可以使用在 美式键盘 同一行的字母打印出来的单词。键盘如下图所示。

美式键盘 中：

第一行由字符 "qwertyuiop" 组成。
第二行由字符 "asdfghjkl" 组成。
第三行由字符 "zxcvbnm" 组成。

https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/10/12/keyboard.png

示例 1：
输入：words = ["Hello","Alaska","Dad","Peace"]
输出：["Alaska","Dad"]

示例 2：
输入：words = ["omk"]
输出：[]

示例 3：
输入：words = ["adsdf","sfd"]
输出：["adsdf","sfd"]

提示：
1 <= words.length <= 20
1 <= words[i].length <= 100
words[i] 由英文字母（小写和大写字母）组成

'''
words = ["Hello","Alaska","Dad","Peace"]

from typing import List
LINES = [set("qwertyuiop"), set("asdfghjkl"), set("zxcvbnm")]
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        ans = [word for word in words if any(set(word.lower()).issubset(LINE) for LINE in LINES)]
        return ans
        # 返回列表中的元素 - 列表生成式，返回iterable中所有满足condition（为True）的所有元素 [x for x in iterable if condition]
        #       判断条件：该元素的转换成小写形式，取集合，是三行中任意一行的子集
        #                word.lower()                    转小写：                                 返回：小写字符串
        #                set(word.lower())               取集合：                                 返回：集合
        #                set(word.lower()).issubset(x)   是子集：            传入：集合            返回：Ture/False
        #                any(iterable)                   是任意一行的子集：   传入：T/F的可迭代对象  返回：存在Ture就返回True，否则返回False

sol = Solution()
result = sol.findWords(words)
print(result)


'''
class Solution(object):
    def findWords(self, words):
        set1 = set('qwertyuiop')
        set2 = set('asdfghjkl')
        set3 = set('zxcvbnm')
        res = []
        for i in words:
            x = i.lower()
            setx = set(x)
            if setx<=set1 or setx<=set2 or setx<=set3:
                res.append(i)
        return res
'''