'''
https://leetcode-cn.com/problems/word-pattern/

给定一种规律 pattern 和一个字符串 str ，判断 str 是否遵循相同的规律。

这里的 遵循 指完全匹配，例如， pattern 里的每个字母和字符串 str 中的每个非空单词之间存在着双向连接的对应规律。

示例1:
    输入: pattern = "abba", str = "dog cat cat dog"
    输出: true

示例 2:
    输入:pattern = "abba", str = "dog cat cat fish"
    输出: false

示例 3:
    输入: pattern = "aaaa", str = "dog cat cat dog"
    输出: false

示例 4:
    输入: pattern = "abba", str = "dog dog dog dog"
    输出: false

说明:
    你可以假设 pattern 只包含小写字母， str 包含了由单个空格分隔的小写字母。  

'''
pattern = "abba"
str = "dog cat cat dog"

class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        words = str.split(' ')            # words = ['dog', 'cat', 'cat', 'dog']
        m, n = len(pattern), len(words)
        if m != n:
            return False
        hash = {}          # 新建哈希表，用pattern中的字母做keys，用str中的单词做values
        for i in range(m):                         # 遍历pattern中的字母：
            if pattern[i] not in hash.keys():      # 哈希表中没有当前key时：
                if  words[i] not in hash.values(): # 同时哈希表中也没有当前的value时：
                    hash[pattern[i]] = words[i]    # 在哈希表中建立字母和对应位置单词的对应关系
                else:                              # 对应value已存在但key值不同：
                    hash[pattern[i]] = 0           # 
            if hash[pattern[i]] != words[i]:       # 遍历到哈希表中的value与word不对应时，返回False
                return False
        return True

if __name__ == "__main__":
    sol = Solution()
    result = sol.wordPattern(pattern, str)
    print (result)