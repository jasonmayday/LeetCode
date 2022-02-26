"""
https://leetcode-cn.com/problems/similar-rgb-color/

RGB 颜色 "#AABBCC" 可以简写成 "#ABC" 。

    例如，"#15c" 其实是 "#1155cc" 的简写。

现在，假如我们分别定义两个颜色 "#ABCDEF" 和 "#UVWXYZ"，则他们的相似度可以通过这个表达式 -(AB - UV)^2 - (CD - WX)^2 - (EF - YZ)^2 来计算。

那么给你一个按 "#ABCDEF" 形式定义的字符串 color 表示 RGB 颜色，请你以字符串形式，返回一个与它相似度最大且可以简写的颜色。（比如，可以表示成类似 "#XYZ" 的形式）

任何 具有相同的（最大）相似度的答案都会被视为正确答案。

示例 1：
    输入：color = "#09f166"
    输出："#11ee66"
    解释：
        因为相似度计算得出 -(0x09 - 0x11)^2 -(0xf1 - 0xee)^2 - (0x66 - 0x66)^2 = -64 -9 -0 = -73
        这已经是所有可以简写的颜色中最相似的了

示例 2：
    输入：color = "#4e3fe1"
    输出："#5544dd"

提示：
    color.length == 7
    color[0] == '#'
    对于任何 i > 0，color[i] 都是一个在范围 ['0', 'f'] 内的 16 进制数

"""

"""
    比如说在十进制中，0（00），11，22，33，44，55，都是（10 + 1）的倍数，那么在16进制中，00，11，22，33，都是（16 + 1）的倍数
    0x11, 0x22, 0x33, 0x44... 都是 0x11 的倍数，0x11 就是 17
"""

""" 方法一：枚举 """
class Solution(object):
    def similarRGB(self, color):
        def similarity(hex1, hex2):
            r1, g1, b1 = hex1 >> 16, (hex1 >> 8) % 256, hex1 % 256
            r2, g2, b2 = hex2 >> 16, (hex2 >> 8) % 256, hex2 % 256
            return -(r1 - r2)**2 - (g1 - g2)**2 - (b1 - b2)**2

        hex1 = int(color[1:], 16)
        ans = 0
        for r in range(16):
            for g in range(16):
                for b in range(16):
                    hex2 = 17 * r * (1 << 16) + 17 * g * (1 << 8) + 17 * b
                    if similarity(hex1, hex2) > similarity(hex1, ans):
                        ans = hex2

        return '#{:06x}'.format(ans)

""" 方法二：独立性 + 枚举 """
class Solution(object):
    def similarRGB(self, color):
        def f(comp):
            q, r = divmod(int(comp, 16), 17)
            if r > 8: q += 1
            return '{:02x}'.format(17 * q)
        return '#' + f(color[1:3]) + f(color[3:5]) + f(color[5:])

if __name__ == "__main__":
    color = "#09f166"
    sol = Solution()
    result = sol.similarRGB(color)
    print(result)