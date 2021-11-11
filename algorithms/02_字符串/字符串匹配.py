
"""BF算法，即暴力(Brute Force)算法
   BF算法的思想就是将目标串S的第一个字符与模式串T的第一个字符进行匹配。。
   若相等，则继续比较S的第二个字符和 T的第二个字符；
   若不相等，则比较S的第二个字符和T的第一个字符，依次比较下去，直到得出最后的匹配结果。
   BF算法是一种蛮力算法。"""
def naive_matching(t, p):
    m, n = len(p), len(t)
    i, j = 0, 0
    while i < m and j < n:  # i==m means a matching
        if p[i] == t[j]:  # ok! consider next char in p
            i, j = i + 1, j + 1
        else:  # no! consider next position in t
            i, j = 0, j - i + 1
    if i == m:  # find a matching, return its index
        return j - i
    return -1  # no matching, return special value

"""KMP算法（无回溯串匹配算法）
   KMP算法的核心是利用匹配失败后的信息，尽量减少模式串与主串的匹配次数以达到快速匹配的目的。
   具体实现就是通过一个next()函数实现，函数本身包含了模式串的局部匹配信息。KMP算法的时间复杂度O(m+n)。"""
def KMP_matching(t, p):
    # KMP字符串匹配的另一个版本, 稍许修改（非本质）.
    # 将gen_pnext定义为局部函数.
    def gen_pnext(p):  # p = "abbab"
        """生成p中各i的下一检查位置表，稍许优化版本."""
        i, k, m = 0, -1, len(p)  
        pnext = [-1] * m  # 初始化一个数组
        while i < m - 1:  # generate pnext[i+1]
            if k == -1 or p[i] == p[k]:
                i, k = i + 1, k + 1
                if p[i] == p[k]:
                    pnext[i] = pnext[k]
                else:
                    pnext[i] = k
            else:
                k = pnext[k]
        return pnext

    j, i = 0, 0
    n, m = len(t), len(p)
    pnext = gen_pnext(p)
    while j < n and i < m:  # i==m means a matching
        while i >= 0 and t[j] != p[i]:
            i = pnext[i]
        j, i = j + 1, i + 1
    if i == m:  # 找到匹配, 返回其下标
        return j - i
    return -1  # 不存在匹配, 返回特殊值

"""BM算法：
   Boyer-Moore字符串搜索算法是一种非常高效的字符串搜索算法。
   仅对搜索目标字符串（关键字）进行预处理，而非被搜索的字符串。
   虽然Boyer-Moore算法的执行时间同样线性依赖于被搜索字符串的大小，但是通常仅为其它算法的一小部分：
   它不需要对被搜索的字符串中的字符进行逐一比较，而会跳过其中某些部分。通常搜索关键字越长，算法速度越快。
   它的效率来自于这样的事实：对于每一次失败的匹配尝试，算法都能够使用这些信息来排除尽可能多的无法匹配的位置。"""

def getBMBC(pattern):
    BMBC = dict()   # 预生成坏字符表
    for i in range(len(pattern) - 1):
        char = pattern[i]
        # 记录坏字符最右位置（不包括模式串最右侧字符）
        BMBC[char] = i + 1
    return BMBC

def getBMGS(pattern):
    BMGS = dict()   # 预生成好后缀表
    BMGS[''] = 0    # 无后缀仅根据坏字移位符规则
    for i in range(len(pattern)):
        # 好后缀
        GS = pattern[len(pattern) - i - 1:]
        for j in range(len(pattern) - i - 1):
            NGS = pattern[j:j + i + 1]  # 匹配部分
            # 记录模式串中好后缀最靠右位置（除结尾处）
            if GS == NGS:
                BMGS[GS] = len(pattern) - j - i - 1
    return BMGS

def BM(string, pattern):    # Boyer-Moore算法实现字符串查找
    m = len(pattern)
    n = len(string)
    i = 0
    j = m
    res = 0
    BMBC = getBMBC(pattern=pattern)  # 坏字符表
    BMGS = getBMGS(pattern=pattern)  # 好后缀表
    while i < n:
        while (j > 0):
            if i + j - 1 >= n:  # 当无法继续向下搜索就返回值
                return res
            a = string[i + j - 1:i + m] # 主串判断匹配部分
            b = pattern[j - 1:]         # 模式串判断匹配部分
            if a == b:                  # 当前位匹配成功则继续匹配
                j = j - 1
            else:                       # 当前位匹配失败根据规则移位
                i = i + max(BMGS.setdefault(b[1:], m), j - BMBC.setdefault(string[i + j - 1], 0))
                j = m
            if j == 0:                  # 匹配成功返回匹配位置
                res += i
                i += 1
                j = len(pattern)

"""Sunday算法：
   其核心思想是：在匹配过程中，模式串发现不匹配时，算法能跳过尽可能多的字符以进行下一步的匹配，从而提高了匹配效率。
   目前发现的最高效且容易理解的算法。"""
def sunday_match_str(main_str, find_str):
    m, f = 0, 0
    m_len = len(main_str)   # main_str: 主串
    f_len = len(find_str)   # find_str: 模式串
    while m < m_len:
        if main_str[m] == find_str[f]:
            m, f = m + 1, f + 1
            if f == f_len:
                return m - f_len  # 此时找到了第一个匹配到的下标
            continue
        else:
            flag = m - f + f_len
            if flag > m_len - 1:  # main_str下标越界，没有找到匹配的串
                return -1
            check_exits = find_str.rfind(main_str[flag])
            if check_exits != -1:  # 在find_str中有匹配
                jump = f_len - check_exits  # 移动的步长
                m, f = m - f + jump, 0
            else:  # 在find_str中无匹配
                jump = f_len + 1  # 移动的步长
                m, f = m - f + jump, 0
    else:
        return -1


if __name__ == '__main__':
    t = "aabababababbbbaababaaaababababbab"
    p = "abbab"
    
    print(naive_matching(t, p))
    print(KMP_matching(t, p))
    print(BM(t, p))
    print(sunday_match_str(t, p))



