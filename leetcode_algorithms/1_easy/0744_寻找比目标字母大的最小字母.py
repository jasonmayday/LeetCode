"""
https://leetcode-cn.com/problems/find-smallest-letter-greater-than-target/

给你一个排序后的字符列表 letters ，列表中只包含小写英文字母。另给出一个目标字母 target，请你寻找在这一有序列表里比目标字母大的最小字母。

在比较时，字母是依序循环出现的。举个例子：
    如果目标字母 target = 'z' 并且字符列表为 letters = ['a', 'b']，则答案返回 'a'

示例：
    输入:
    letters = ["c", "f", "j"]
    target = "a"
    输出: "c"

    输入:
    letters = ["c", "f", "j"]
    target = "c"
    输出: "f"

    输入:
    letters = ["c", "f", "j"]
    target = "d"
    输出: "f"

    输入:
    letters = ["c", "f", "j"]
    target = "g"
    输出: "j"

    输入:
    letters = ["c", "f", "j"]
    target = "j"
    输出: "c"

    输入:
    letters = ["c", "f", "j"]
    target = "k"
    输出: "c"

提示：
    letters长度范围在[2, 10000]区间内。
    letters 仅由小写字母组成，最少包含两个不同的字母。
    目标字母target 是一个小写字母。

"""
from typing import List

"""二分查找"""
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        length = len(letters)
        left = 0
        right = length - 1
        while(left <= right):           # 如果left > right, 跳出循环
            mid = (left + right)//2
            if letters[mid] > target:   # 当中间值mid>target时
                right = mid - 1         # 右边界 = mid - 1
            else:
                left = mid + 1          # 否则左边界 = mid + 1
        if left == length:              # 特殊情况:即如果目标字母 target = 'z'
            return letters[0]
        else:                       # 跳出循环, 此时left为大于target的最小字母的下标,right为小于等于target的最大字母的下标,
            return letters[left]    # 所以return letters[left]

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l = [x > target for x in letters]
        return letters[l.index(max(l))]
    
if __name__ == "__main__":
    letters = ["c", "f", "j"]
    target = "d"    # 输出: "f"
    sol = Solution()
    result = sol.nextGreatestLetter(letters,target)
    print(result)