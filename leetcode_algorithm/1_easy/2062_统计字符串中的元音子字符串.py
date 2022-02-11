"""
https://leetcode-cn.com/problems/count-vowel-substrings-of-a-string/

子字符串 是字符串中的一个连续（非空）的字符序列。

元音子字符串 是 仅 由元音（'a'、'e'、'i'、'o' 和 'u'）组成的一个子字符串，且必须包含 全部五种 元音。

给你一个字符串 word ，统计并返回 word 中 元音子字符串的数目 。

示例 1：
    输入：word = "aeiouu"
    输出：2
    解释：下面列出 word 中的元音子字符串（斜体加粗部分）：
    - "aeiouu"
    - "aeiouu"

示例 2：
    输入：word = "unicornarihan"
    输出：0
    解释：word 中不含 5 种元音，所以也不会存在元音子字符串。

示例 3：
    输入：word = "cuaieuouac"
    输出：7
    解释：下面列出 word 中的元音子字符串（斜体加粗部分）：
    - "cuaieuouac"
    - "cuaieuouac"
    - "cuaieuouac"
    - "cuaieuouac"
    - "cuaieuouac"
    - "cuaieuouac"
    - "cuaieuouac"

示例 4：
    输入：word = "bbaeixoubb"
    输出：0
    解释：所有包含全部五种元音的子字符串都含有辅音，所以不存在元音子字符串。

提示：
    1 <= word.length <= 100
    word 仅由小写英文字母组成

"""

"""滑动窗口"""
class Solution:
    def countVowelSubstrings(self, word: str) -> int: 
        ans = 0
        n = len(word)
        for i in range(n - 4):          # 滑动窗口起始坐标
            for j in range(i, n + 1):   # 滑动窗口大小
                if set(word[i:j]) == set("aeiou"):
                    ans += 1
        return ans

class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        l = 0
        n = len(word)
        res = 0
        # l, r 分别记录当前元音字符串的边界
        for r in range(n):
            if word[r] not in 'aeiou': # 遇到辅音，重置左边界
                l = r + 1
                continue
            if r == n - 1 or word[r + 1] not in 'aeiou': # 已触达当前只包含元音的子字符串的最大右边界，计算该子字符串内有效的元音子字符串数目
                # 滑动窗口
                # 使用哈希记录当前窗口每个元音的出现次数
                char_count = {'a':0,'e':0,'i':0,'o':0,'u':0}
                # left, right 分别为当前窗口左右边界
                left = l
                for right in range(l, r + 1):
                    char_count[word[right]] += 1
                    while char_count[word[left]] > 1: # 收缩左边界，并保证不同元音的数量不下降
                        char_count[word[left]] -= 1
                        left += 1
                    if all(i >= 1 for i in char_count.values()): # 若当前窗口所有元音都存在，则当前窗口为有效的元音子字符串，且往左扩展的所有子字符串均为有效的元音子字符串
                        res += left - l + 1
        return res


if __name__ == "__main__":
    nums = [3,2,1,5,4]
    k = 2
    sol = Solution()
    result = sol.countKDifference(nums)
    print (result)