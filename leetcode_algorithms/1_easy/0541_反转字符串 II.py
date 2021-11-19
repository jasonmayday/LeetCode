"""
https://leetcode-cn.com/problems/reverse-string-ii/

给定一个字符串 s 和一个整数 k，从字符串开头算起，每计数至 2k 个字符，就反转这 2k 字符中的前 k 个字符。
    如果剩余字符少于 k 个，则将剩余字符全部反转。
    如果剩余字符小于 2k 但大于或等于 k 个，则反转前 k 个字符，其余字符保持原样。

示例 1：
    输入：s = "abcdefg", k = 2
    输出："bacdfeg"

示例 2：
    输入：s = "abcd", k = 2
    输出："bacd"

提示：
    1 <= s.length <= 10^4
    s 仅由小写英文组成
    1 <= k <= 10^4

"""
# 通俗一点说，每隔k个反转k个，末尾不够k个时全部反转

class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        n = len(s)
        arr = list(s)           # 将字符串转换为list数组
        for i in range(0, n, 2*k):          # 函数range(start,stop,step)表示从索引start到stop-1，每次移动步长为step
            arr[i:(i+k)] = arr[i:(i+k)][::-1]   # 通过arr[::-1]实现反转
        return "".join(arr)

class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        left = 0
        mid = k
        right = 2 * k                  # 初始化左中右指针
        res = ''                       # 初始化结果字符串
        while len(res) < len(s):                        # 满足条件时执行
            res += s[left:mid][::-1] + s[mid:right]     # 把当前单元的结果添加到结果字符串
            left = left + 2 * k
            mid = mid + 2 * k
            right = right + 2 * k                          
        return res

if __name__ == "__main__":
    s = "01234567890123456789"
    k = 2
    sol = Solution()
    result = sol.reverseStr(s,k)
    print(result)