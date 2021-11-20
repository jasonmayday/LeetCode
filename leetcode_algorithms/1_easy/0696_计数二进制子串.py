"""
https://leetcode-cn.com/problems/count-binary-substrings/

给定一个字符串 s，计算具有相同数量 0 和 1 的非空（连续）子字符串的数量，并且这些子字符串中的所有 0 和所有 1 都是连续的。

重复出现的子串要计算它们出现的次数。

示例 1 :
    输入: "00110011"
    输出: 6
    解释: 有6个子串具有相同数量的连续1和0：“0011”，“01”，“1100”，“10”，“0011” 和 “01”。

    请注意，一些重复出现的子串要计算它们出现的次数。

    另外，“00110011”不是有效的子串，因为所有的0（和1）没有组合在一起。

示例 2 :
    输入: "10101"
    输出: 4
    解释: 有4个子串：“10”，“01”，“10”，“01”，它们具有相同数量的连续1和0。

提示：
    s.length 在1到50,000之间。
    s 只包含“0”或“1”字符。

"""
    
"""按字符分组"""
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        count = [1] # 将字符串 s 按照 0 和 1 的连续段分组，存在 counts 数组中
        j = 0                       # counts中的指针 j
        for i in range(1, len(s)):  # 统计连续的频数  例如 s = 00111011，可以得到 counts = {2,3,1,2}
            if s[i] == s[i-1]:      # 当前字符与前一字符相同：
                count[j] += 1       # count中的数字 +1
            else:                   # 当前字符与前一字符不同：
                count.append(1)     # counts数组加一位 1
                j += 1              # counts中的指针 j 向后移一位，处理后一位的数字
        res = 0
        for k in range(1, len(count)):
            res += min(count[k], count[k-1]) # 取相邻频数的最小值
        return res
    

if __name__ == "__main__":      
    s = "00110011"
    sol = Solution()
    result = sol.countBinarySubstrings(s)
    print(result)