"""
https://leetcode-cn.com/problems/reverse-vowels-of-a-string/

给你一个字符串 s ，仅反转字符串中的所有元音字母，并返回结果字符串。

元音字母包括 'a'、'e'、'i'、'o'、'u'，且可能以大小写两种形式出现。

示例 1：
    输入：s = "hello"
    输出："holle"

示例 2：
    输入：s = "leetcode"
    输出："leotcede"

提示：
    1 <= s.length <= 3 * 10^5
    s 由 可打印的 ASCII 字符组成

"""

"""
方法一：双指针
使用两个指针 i 和 j 对字符串相向地进行遍历。
指针 i 初始时指向字符串 s 的首位，指针 j 初始时指向字符串 s 的末位。
在遍历的过程中，我们不停地将 i 向右移动，直到 i 指向一个元音字母（或者超出字符串的边界范围）；
同时，我们不停地将 j 向左移动，直到 j 指向一个元音字母。
此时，如果 i<j，那么我们交换 i 和 j 指向的元音字母，否则说明所有的元音字母均已遍历过，就可以退出遍历的过程。
"""

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {'a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U'}
        lt = list(s)            # str类型数据无法直接查询 in 和 not in，转换为list, lt = ['h', 'e', 'l', 'l', 'o']
        left  = 0               # 左指针
        right = len(s) - 1      # 右指针
        while left < right:     # 左右指针交错循环停止
            if lt[left] in vowels and lt[right] in vowels:    # 左右指针所指元素均在集合中
                lt[left], lt[right] = lt[right], lt[left]       # 交换左右指针所指元素
                left += 1   # 左指针右移
                right -= 1  # 右指针左移
            if lt[left] not in vowels:      # 左指针所指元素不在集合中
                left += 1       # 左指针右移
            if lt[right] not in vowels:     # 右指针所指元素不在集合中
                right -= 1      # 右指针左移
        return ''.join(lt)

if __name__ == "__main__":
    s = "hello"
    sol = Solution()
    result = sol.reverseVowels(s)
    print (result)