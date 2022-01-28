"""
https://leetcode-cn.com/problems/restore-ip-addresses/

有效 IP 地址 正好由四个整数（每个整数位于 0 到 255 之间组成，且不能含有前导 0），整数之间用 '.' 分隔。

    例如："0.1.2.201" 和 "192.168.1.1" 是 有效 IP 地址，但是 "0.011.255.245"、"192.168.1.312" 和 "192.168@1.1" 是 无效 IP 地址。

给定一个只包含数字的字符串 s ，用以表示一个 IP 地址，返回所有可能的有效 IP 地址，这些地址可以通过在 s 中插入 '.' 来形成。你不能重新排序或删除 s 中的任何数字。你可以按 任何 顺序返回答案。

示例 1：
    输入：s = "25525511135"
    输出：["255.255.11.135","255.255.111.35"]

示例 2：
    输入：s = "0000"
    输出：["0.0.0.0"]

示例 3：
    输入：s = "1111"
    输出：["1.1.1.1"]

示例 4：
    输入：s = "010010"
    输出：["0.10.0.10","0.100.1.0"]

示例 5：
    输入：s = "101023"
    输出：["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]

提示：
    0 <= s.length <= 20
    s 仅由数字组成

"""
from typing import List
""" 暴力枚举 """
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        n = len(s)
        res = []
		
        # 判读数字是否可做为 IP 中的某段数字
        def isValid(tmp):
            if not tmp or (tmp[0] == "0" and len(tmp) > 1) or int(tmp) > 255:
                return False
            return True
        
		# 三个循环,把数字分成四份
        for i in range(3):  # 每段最多三位数字
            for j in range(i + 1, i + 4):
                for k in range(j + 1, j + 4):
                    if i < n and j < n and k < n:
                        tmp1 = s[:i + 1]
                        tmp2 = s[i + 1:j + 1]
                        tmp3 = s[j + 1:k + 1]
                        tmp4 = s[k + 1:]
                        print(tmp1, tmp2, tmp3, tmp4)   # 列出所有可能的分割组合

                        if all(map(isValid, [tmp1, tmp2, tmp3, tmp4])):
                            res.append(tmp1 + "." + tmp2 + "." + tmp3 + "." + tmp4)
        return res

""" 回溯 """
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        path = [] # 存放分割后的字符
        
        # 判读数字是否可做为 IP 中的某段数字
        def isValid(p):
            if p == '0': return True # 解决"0000"
            if p[0] == '0': return False
            if int(p) > 0 and int(p) <256: return True
            return False

        def backtrack(s, startIndex):
            if len(s) > 12: return  # 字符串长度最大为12
            if len(path) == 4 and startIndex == len(s): # 确保切割完，且切割后的长度为4
                res.append(".".join(path[:])) # 字符拼接
                return

            for i in range(startIndex, len(s)):
                if len(s) - startIndex > 3*(4 - len(path)): continue # 剪枝，剩下的字符串大于允许的最大长度则跳过
                p = s[startIndex:i+1] # 分割字符
                if isValid(p): # 判断字符是否有效
                    path.append(p)
                else: continue
                backtrack(s, i + 1) # 寻找i+1为起始位置的子串
                path.pop()
        backtrack(s, 0)
        return res


if __name__ == "__main__":
    s = "101023"
    sol = Solution()
    result = sol.restoreIpAddresses(s)
    print(result)