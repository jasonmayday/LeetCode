'''
https://leetcode-cn.com/problems/number-of-segments-in-a-string/

统计字符串中的单词个数，这里的单词指的是连续的不是空格的字符。

请注意，你可以假定字符串里不包括任何不可打印的字符。

示例:

输入: "Hello, my name is John"
输出: 5
解释: 这里的单词是指连续的不是空格的字符，所以 "Hello," 算作 1 个单词。

'''
s = "Hello, my name is John"

class Solution:
    def countSegments(self,s):
        ans, words = 0, s.split(' ')
        for word in words:
            if word != '':
                ans += 1
        return ans

if __name__ == "__main__":
    sol = Solution()
    result = sol.countSegments(s)
    print (result)  