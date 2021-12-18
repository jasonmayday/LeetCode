"""
https://leetcode-cn.com/problems/positions-of-large-groups/

在一个由小写字母构成的字符串 s 中，包含由一些连续的相同字符所构成的分组。

例如，在字符串 s = "abbxxxxzyy" 中，就含有 "a", "bb", "xxxx", "z" 和 "yy" 这样的一些分组。

分组可以用区间 [start, end] 表示，其中 start 和 end 分别表示该分组的起始和终止位置的下标。上例中的 "xxxx" 分组用区间表示为 [3,6] 。

我们称所有包含大于或等于三个连续字符的分组为 较大分组 。

找到每一个 较大分组 的区间，按起始位置下标递增顺序排序后，返回结果。

示例 1：
    输入：s = "abbxxxxzzy"
    输出：[[3,6]]
    解释："xxxx" 是一个起始于 3 且终止于 6 的较大分组。

示例 2：
    输入：s = "abc"
    输出：[]
    解释："a","b" 和 "c" 均不是符合要求的较大分组。

示例 3：
    输入：s = "abcdddeeeeaabbbcd"
    输出：[[3,5],[6,9],[12,14]]
    解释：较大分组为 "ddd", "eeee" 和 "bbb"

示例 4：
    输入：s = "aba"
    输出：[]
 
提示：
    1 <= s.length <= 1000
    s 仅含小写英文字母

"""
from typing import List

"""使用num记录重复字符的个数，只需要更新num就可以了。"""
class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        res = []    # 初始化答案数组
        num = 1     # 使用num记录重复字符的个数

        for i in range(len(s)):
            if i != len(s) - 1 and s[i] == s[i+1]:  # 与下一个值相同：
                num += 1                            # 记录连续相同的 num 加一
            if i == len(s) - 1 or s[i] != s[i+1]:   # 到达尾部或者与下一个值不同，判断长度
                if num >= 3:                        # 如果有三个连续的
                    res.append([i-num+1, i])        # 加一个区间 [start, end]
                num = 1                             # 然后 num 重置为 1
        return res
                

"""使用start和end更新两个指针，略显复杂。"""
class Solution:
    def largeGroupPositions(self, s):
        start, end = 0, 0
        res = []
        if len(s) < 3:
            return res
        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:    #如果与下个值相同，只更新end
                end = i + 1
                if end == len(s) - 1 and end - start + 1 >= 3:  #判断是否到达尾部
                    res.append([start, end])
                    
            else:                   #如果与下个值不同，只更新start
                if end - start + 1 >= 3:
                    res.append([start, end])
                start = i + 1
        return res

if __name__ == "__main__":
    s = "abcdddeeeeaabbbcd"
    sol = Solution()
    result = sol.largeGroupPositions(s)
    print(result)
