"""
https://leetcode-cn.com/problems/permutation-in-string/

给你两个字符串 s1 和 s2 ，写一个函数来判断 s2 是否包含 s1 的排列。如果是，返回 true ；否则，返回 false 。

换句话说，s1 的排列之一是 s2 的 子串 。

示例 1：
    输入：s1 = "ab" s2 = "eidbaooo"
    输出：true
    解释：s2 包含 s1 的排列之一 ("ba").

示例 2：
    输入：s1= "ab" s2 = "eidboaoo"
    输出：false

提示：
    1 <= s1.length, s2.length <= 10^4
    s1 和 s2 仅包含小写字母

"""
from collections import Counter

""" 滑动窗口 + 字典
    使用一个长度和 s1 长度相等的固定窗口大小的滑动窗口，在 s2 上面从左向右滑动,
    判断 s2 在滑动窗口内的每个字符出现的个数是否跟 s1 每个字符出现次数完全相等。"""
class Solution(object):
    def checkInclusion(self, s1, s2):
        counter1 = Counter(s1)  # 统计 s1 中每个字符出现的次数
        n = len(s2)
        left = 0                # 定义滑动窗口的范围是 [left, right]，闭区间，长度与 s1 相等
        right = len(s1) - 1
        counter2 = Counter(s2[0:right]) # 统计窗口 s2[left, right-1] 内的元素出现的次数
        while right < n:                # 不断右移滑动窗口
            counter2[s2[right]] += 1    # 把 right 位置的元素放到 counter2 中
            if counter1 == counter2:    # 如果滑动窗口内各个元素出现的次数跟 s1 的元素出现次数完全一致，返回 True
                return True
            counter2[s2[left]] -= 1     # 窗口向右移动前，把当前 left 位置的元素出现次数 - 1
            if counter2[s2[left]] == 0: # 如果当前 left 位置的元素出现次数为 0， 需要从字典中删除，否则这个出现次数为 0 的元素会影响两 counter 之间的比较
                del counter2[s2[left]]
            left += 1   # 窗口向右移动
            right += 1
        return False

if __name__ == "__main__":
    s1 = "ab"
    s2 = "eidbaooo"
    sol = Solution()
    result = sol.checkInclusion(s1, s2)
    print (result)