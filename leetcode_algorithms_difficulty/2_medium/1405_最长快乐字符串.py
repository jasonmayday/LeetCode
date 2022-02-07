"""
https://leetcode-cn.com/problems/longest-happy-string/

如果字符串中不含有任何 'aaa'，'bbb' 或 'ccc' 这样的字符串作为子串，那么该字符串就是一个「快乐字符串」。

给你三个整数 a，b ，c，请你返回 任意一个 满足下列全部条件的字符串 s：
    s 是一个尽可能长的快乐字符串。
    s 中 最多 有a 个字母 'a'、b 个字母 'b'、c 个字母 'c' 。
    s 中只含有 'a'、'b' 、'c' 三种字母。

如果不存在这样的字符串 s ，请返回一个空字符串 ""。

示例 1：
    输入：a = 1, b = 1, c = 7
    输出："ccaccbcc"
    解释："ccbccacc" 也是一种正确答案。

示例 2：
    输入：a = 2, b = 2, c = 1
    输出："aabbc"

示例 3：
    输入：a = 7, b = 1, c = 0
    输出："aabaa"
    解释：这是该测试用例的唯一正确答案。

提示：
    0 <= a, b, c <= 100
    a + b + c > 0

"""

""" 方法一：贪心
    采用贪心策略，每次尽可能优先使用当前数量最多的字母，因为最后同一种字母剩余的越多，越容易出现字母连续相同的情况
    如果不满足条件，再使用剩余数量次多的字母，由于只有三种字母，实际上每次只会在数量最多和次多的字母中选择一个
    如果尝试所有的字母都无法使用，则直接结束，此时构成的字符串即为所求"""
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        dict = {'a': min(a, 2*(b+c+1)), # 根据插空规则修正单个字符最大可能的数量。含多少个a, 多少个b, 多少个c.
                'b': min(b, 2*(a+c+1)), # 任何单一字符最大数量必须小于（另外两个字符+1）* 2
                'c': min(c, 2*(b+a+1))} # 如'aabaabaacaa', b与c插入到a序列中，a 的数量最多为 8
        print (dict)            # {'a': 1, 'b': 1, 'c': 6}
        n = sum(dict.values())  # 最终结果字串的总长度
        print (n)               # 8
        
        res = []
        for i in range(n):  # 依次把字母填到结果里, 每次只填一个字母.
            cand = set(['a','b','c'])   # 候选的字母
            if len(res) > 1 and res[-1] == res[-2]:     # 看当前拼好的字串中最后2个字母是否一样
                cand.remove(res[-1])                    # 如果一样, 把这个字母从候选里移掉(因为不能出现三个连续的字母)
            tmp = max(cand, key = lambda x: dict[x])    # 贪心，在dict候选中选择存量最大的字符
            res.append(tmp)     # 将它加到结果里.
            dict[tmp] -= 1      # 把它的剩余计数减去1. 开始下一轮.
        return ''.join(res)

if __name__ == "__main__":
    a = 1
    b = 1
    c = 7
    sol = Solution()
    result = sol.longestDiverseString(a, b, c)
    print(result)  