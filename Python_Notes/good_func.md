
计数方法的不同：
    Counter
    enumerate
    dict
    defaultdict
    defaultdict vs dict
    集合的字典，用于统计不重复的元素 defaultdict(set)
    
Counter:
words = "".join(words)      # abcaabcbc
words = Counter(words)      # {'a': 3, 'b': 3, 'c': 3}
words['a'] == 3:
相当于一个dict：
    keys是元素
    value是对应元素出现的次数



dict
get函数

zip
https://www.runoob.com/python/python-func-zip.html
统计每列的元素等作用
rows = [sum(num) for num in zip(*mat)]

# 每列的元素
mat =  [[1,0,0],
        [0,1,0],
        [0,0,1]]
cols = list(zip(*mat))

enumerate 返回下标和元素

正则表达式


位运算


chr()
返回值是当前整数对应的 ASCII 字符。


ord()
ord() 函数是 chr() 函数（对于 8 位的 ASCII 字符串）的配对函数，它以一个字符串（Unicode 字符）作为参数，返回对应的 ASCII 数值，或者 Unicode 数值。
ord("a") = 65
eg.: 'a' 用 1 替换，'b' 用 2 替换，... 'z' 用 26 替换
     (ord(c) - ord('a') + 1)

for _ in range(4):
When you are not interested in some values returned by a function we use underscore in place of variable name . 
Basically it means you are not interested in how many times the loop is run till now just that it should run some specific number of times overall.

list 变字符串：''.join(list)
字符串变 list：

整数变字符串：
int = 17
s = str(int) # 17 → ['1', '7'] → '17'

排列组合：
from itertools import permutations

生成一个m行n列的空矩阵：
res = [[0] * n for _ in range(m)]       # m 行，n 列


当题目中出现 “所有组合” 等类似字眼时，我们第一感觉就要想到用回溯。
看到 全排列，或者 枚举全部解，等类似的 搜索枚举类型题，基本就是 回溯 没跑了。