"""
https://leetcode-cn.com/problems/long-pressed-name/

你的朋友正在使用键盘输入他的名字 name。偶尔，在键入字符 c 时，按键可能会被长按，而字符可能被输入 1 次或多次。

你将会检查键盘输入的字符 typed。如果它对应的可能是你的朋友的名字（其中一些字符可能被长按），那么就返回 True。

示例 1：
    输入：name = "alex", typed = "aaleex"
    输出：true
    解释：'alex' 中的 'a' 和 'e' 被长按。

示例 2：
    输入：name = "saeed", typed = "ssaaedd"
    输出：false
    解释：'e' 一定需要被键入两次，但在 typed 的输出中不是这样。

示例 3：
    输入：name = "leelee", typed = "lleeelee"
    输出：true

示例 4：
    输入：name = "laiden", typed = "laiden"
    输出：true
    解释：长按名字中的字符并不是必要的。

提示：
    name.length <= 1000
    typed.length <= 1000
    name 和 typed 的字符都是小写字母。

"""

class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i = 0   # cur_name
        j = 0   # cur_typed
        while i < len(name) and j < len(typed): # 模拟同时遍历两个数组，进行对比
            if name[i] == typed[j]:             # 相同时向后匹配
                i += 1
                j += 1
            else: # 不相同
                if j == 0: return False # 如果第一位不相同，直接返回false
                while j < len(typed) - 1 and typed[j] == typed[j-1]:    # 判断边界为 n-1, 若为 n 会越界
                    j += 1  # 不是第一位不相同，就让 j 跨越重复项，移动到重复项之后的位置，再次比较name[i] 和typed[j]
                if name[i] == typed[j]: # 如果 name[i] 和 typed[j]相同，继续向后对比
                    i += 1
                    j += 1
                else: return False
        if i < len(name):
            return False                # 说明name没有匹配完
        while j < len(typed):           # 说明type没有匹配完
            if typed[j] == typed[j-1]: j += 1
            else: return False
        return True

if __name__ == "__main__":
    name = "leelee"
    typed = "lleeelee"
    sol = Solution()
    result = sol.isLongPressedName(name, typed)
    print (result)