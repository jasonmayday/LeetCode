"""
https://leetcode-cn.com/problems/reverse-string/

编写一个函数，其作用是将输入的字符串反转过来。输入字符串以字符数组 s 的形式给出。

不要给另外的数组分配额外的空间，你必须原地修改输入数组、使用 O(1) 的额外空间解决这一问题。

示例 1：
    输入：s = ["h","e","l","l","o"]
    输出：["o","l","l","e","h"]

示例 2：
    输入：s = ["H","a","n","n","a","h"]
    输出：["h","a","n","n","a","H"]
 
提示：
    1 <= s.length <= 10^5
    s[i] 都是 ASCII 码表中的可打印字符

"""
from typing import List

'''解法1：双指针'''
class Solution:
    def reverseString(self, s: List[str]) -> None:
        s = list(s)
        left = 0
        right = len(s) - 1 
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return ''.join(s)

'''解法2：位运算'''
class Solution:
    def reverseString(self, s: List[str]) -> None:
        lt = list(s)        # str类型数据无法直接查询 in 和 not in，转换为list, lt = ['h', 'e', 'l', 'l', 'o']
        h = len(lt)//2
        for i in range(h):
            lt[i],lt[~i] = lt[~i],lt[i]
        return ''.join(lt)

if __name__ == "__main__":
    s = "hello"
    sol = Solution()
    result = sol.reverseString(s)
    print (result)