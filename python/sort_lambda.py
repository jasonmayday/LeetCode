# https://blog.csdn.net/qq_41500249/article/details/106244810
# https://blog.csdn.net/u010758410/article/details/79737498

# sort在Python中存在两种形式，分别是sorted(str)，另一种是list.srot()

## sorted()函数是Python的内置函数，具体形式为sorted(iterable, cmp=None, key=None, reverse=False)，
   ###  iterable是可迭代对象，包括列表、元组、字典、字符串；
   ###  cmp代表比较函数；
   ###  key代表迭代对象中的某个属性，如某个元素的下标；
   ###  reverse代表升序或者降序


from functools import cmp_to_key

students = [('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]
sorted (students, key = lambda student: student[2])


# lambda函数用法举例：
L = [('b',2),('a',1),('c',3),('d',4)]

#2 利用参数 cmp 排序
sorted(L, key = cmp_to_key(lambda x, y: (x[1], y[1])))

[('a', 1), ('b', 2), ('c', 3), ('d', 4)]
#3 利用参数 key 排序
sorted(L, key = lambda x: x[1])

[('a', 1), ('b', 2), ('c', 3), ('d', 4)]
#4 按年龄升序
students = [('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]
sorted(students, key = lambda s: s[2])

[('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]
#5 按年龄降序
sorted(students, key = lambda s: s[2], reverse = True)
# 结果：
[('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]


## sort函数是针对列表的，不改变原有的列表

## sort函数和lambda函数结合使用
## 假如a是一个由元组构成的列表，对该列表进行排序时，我们需要用到参数key，也就是关键词。
## 如下面代码所示，lambda是一个匿名函数，是固定写法；
## x表示匿名函数的输入，即列表中的一个元素，在这里，表示一个元组，x只是临时起的一个名字，你可以使用任意的名字；
## x[0]表示匿名函数的输出，即元组里的第一个元素，即key = x[0]；
## 所以这句命令的意思就是按照列表中第一个元素进行排序
a = [('b', 4), ('a', 12), ('d', 7), ('h', 6), ('j', 3)]
a.sort(key=lambda x: x[0])
print(a)