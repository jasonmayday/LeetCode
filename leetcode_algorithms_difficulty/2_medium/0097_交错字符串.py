"""
https://leetcode-cn.com/problems/interleaving-string/

给定三个字符串 s1、s2、s3，请你帮忙验证 s3 是否是由 s1 和 s2 交错 组成的。

两个字符串 s 和 t 交错 的定义与过程如下，其中每个字符串都会被分割成若干 非空 子字符串：
    s = s1 + s2 + ... + sn
    t = t1 + t2 + ... + tm
    |n - m| <= 1
    交错 是 s1 + t1 + s2 + t2 + s3 + t3 + ... 或者 t1 + s1 + t2 + s2 + t3 + s3 + ...

提示：a + b 意味着字符串 a 和 b 连接。

示例 1：
    输入：s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
    输出：true

示例 2：
    输入：s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
    输出：false

示例 3：
    输入：s1 = "", s2 = "", s3 = ""
    输出：true

提示：
    0 <= s1.length, s2.length <= 100
    0 <= s3.length <= 200
    s1、s2、和 s3 都由小写英文字母组成

"""

""" 使用 dp[i][j] 表示 s1 的前 i 个字符和 s2 的前 j 个字符是否能构成 s3 的前 i+j 个字符。"""
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        len1 = len(s1)  # aabcc
        len2 = len(s2)  # dbbca
        len3 = len(s3)  # aadbbcbcac
        if(len1 + len2 != len3):
            return False
        dp = [[False]*(len2+1) for i in range(len1+1)]  # 初始化 dp 为 (len1+1) ∗ (len2+1) 的 False 数组
        '''
            "   d   b   b   c   a
        "   F   F   F   F   F   F
        a   F   F   F   F   F   F
        a   F   F   F   F   F   F
        b   F   F   F   F   F   F
        c   F   F   F   F   F   F
        c   F   F   F   F   F   F
        '''
        dp[0][0]=True
        for i in range(1,len1+1):
            dp[i][0]=(dp[i-1][0] and s1[i-1]==s3[i-1])
        for i in range(1,len2+1):
            dp[0][i]=(dp[0][i-1] and s2[i-1]==s3[i-1])
        for i in range(1,len1+1):
            for j in range(1,len2+1):
                dp[i][j]=(dp[i][j-1] and s2[j-1]==s3[i+j-1]) or (dp[i-1][j] and s1[i-1]==s3[i+j-1])
        return dp[-1][-1]

if __name__ == "__main__":
    s1 = "aabcc"
    s2 = "dbbca"
    s3 = "aadbbcbcac"
    sol = Solution()
    result = sol.isInterleave(s1,s2,s3)
    print(result)