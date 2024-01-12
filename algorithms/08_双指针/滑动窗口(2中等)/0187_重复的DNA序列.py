'''

所有 DNA 都由一系列缩写为 'A'，'C'，'G' 和 'T' 的核苷酸组成，例如："ACGAATTCCG"。在研究 DNA 时，识别 DNA 中的重复序列有时会对研究非常有帮助。

编写一个函数来找出所有目标子串，目标子串的长度为 10，且在 DNA 字符串 s 中出现次数超过一次。

示例 1：
    输入：s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
    输出：["AAAAACCCCC","CCCCCAAAAA"]

示例 2：
    输入：s = "AAAAAAAAAAAAA"
    输出：["AAAAAAAAAA"]

'''
from typing import List
from collections import Counter, defaultdict

""" 方法一：哈希表 """
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        L = 10
        ans = []
        cnt = defaultdict(int)
        for i in range(len(s) - L + 1):
            sub = s[i: i + L]
            cnt[sub] += 1
            if cnt[sub] == 2:
                ans.append(sub)
        return ans

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        return [t for t, v in Counter(s[i: i + 10] for i in range(len(s) - 9)).items() if v > 1]

if __name__ == "__main__":
    nums = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
    sol = Solution()
    result = sol.findRepeatedDnaSequences(nums)
    print (result)