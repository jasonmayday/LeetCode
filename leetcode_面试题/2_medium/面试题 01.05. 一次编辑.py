"""
https://leetcode-cn.com/problems/one-away-lcci/

字符串有三种编辑操作:插入一个字符、删除一个字符或者替换一个字符。 给定两个字符串，编写一个函数判定它们是否只需要一次(或者零次)编辑。

示例 1:
    输入:
    first = "pale"
    second = "ple"
    输出: True

示例 2:
    输入:
    first = "pales"
    second = "pal"
    输出: False

"""

"""方法一：分情况讨论"""
class Solution:
    def oneEditAway(self, first: str, second: str) -> bool:
        m, n = len(first), len(second)
        if m < n:
            return self.oneEditAway(second, first)
        if m - n > 1:
            return False
        for i, (x, y) in enumerate(zip(first, second)):
            if x != y:
                if m == n:
                    return first[i + 1:] == second[i + 1:]
                else:
                    return first[i + 1:] == second[i:]  # 注：改用下标枚举可达到 O(1) 空间复杂度
        return True

class Solution:
    def oneEditAway(self, first: str, second: str) -> bool:
        lf, ls = len(first), len(second)
        if lf > ls:
            return self.oneEditAway(second, first)
        if ls - lf > 1:
            return False
        if lf == ls:
            count = 0
            for i in range(lf):
                if first[i] != second[i]:
                    count += 1
            return count <= 1
        i, ofs = 0, 0
        while i < lf:
            if first[i] != second[i + ofs]:
                ofs += 1
                if ofs > 1:
                    return False
            else:
                i += 1
        return True

if __name__ == "__main__":
    first = "pale"
    second = "ple"
    sol = Solution()
    result = sol.oneEditAway(first, second)
    print(result)