"""
https://leetcode-cn.com/problems/design-compressed-string-iterator/

设计并实现一个迭代压缩字符串的数据结构。给定的压缩字符串的形式是，每个字母后面紧跟一个正整数，表示该字母在原始未压缩字符串中出现的次数。

设计一个数据结构，它支持如下两种操作： next 和 hasNext。
    next() - 如果原始字符串中仍有未压缩字符，则返回下一个字符，否则返回空格。
    hasNext() - 如果原始字符串中存在未压缩的的字母，则返回true，否则返回false。

示例 1：
    输入：
        ["StringIterator", "next", "next", "next", "next", "next", "next", "hasNext", "next", "hasNext"]
        [["L1e2t1C1o1d1e1"], [], [], [], [], [], [], [], [], []]
    输出：
        [null, "L", "e", "e", "t", "C", "o", true, "d", true]

    解释：
        StringIterator stringIterator = new StringIterator("L1e2t1C1o1d1e1");
        stringIterator.next(); // 返回 "L"
        stringIterator.next(); // 返回 "e"
        stringIterator.next(); // 返回 "e"
        stringIterator.next(); // 返回 "t"
        stringIterator.next(); // 返回 "C"
        stringIterator.next(); // 返回 "o"
        stringIterator.hasNext(); // 返回 True
        stringIterator.next(); // 返回 "d"
        stringIterator.hasNext(); // 返回 True

提示：
    1 <= compressedString.length <= 1000
    compressedString 由小写字母、大写字母和数字组成。
    在 compressedString 中，单个字符的重复次数在 [1,10 ^9] 范围内。
    next 和 hasNext 的操作数最多为 100 。

"""

""" 模拟 栈 """
class StringIterator:

    def __init__(self, compressedString: str):
        self.string = list(compressedString)    # 把列表转化为字符串

    def next(self) -> str:
        if self.hasNext():
            temp = self.string.pop(0)
            n = ""
            while self.string and self.string[0].isdigit():
                n += self.string.pop(0)
            if int(n) >1:
                n = int(n) - 1
                self.string = [temp, str(n)]+self.string
            return temp
        else:
            return " "

    def hasNext(self) -> bool:
        return len(self.string) >= 2    # 剩下的字符串长度大于等于2

if __name__ == "__main__":
    stringIterator = StringIterator("L1e2t1C1o1d1e1")
    print (stringIterator.next())       # 返回 "L"
    print (stringIterator.next())       # 返回 "e"
    print (stringIterator.next())       # 返回 "e"
    print (stringIterator.next())       # 返回 "t"
    print (stringIterator.next())       # 返回 "C"
    print (stringIterator.next())       # 返回 "o"
    print (stringIterator.hasNext())    # 返回 True
    print (stringIterator.next())       # 返回 "d"
    print (stringIterator.hasNext())    # 返回 True