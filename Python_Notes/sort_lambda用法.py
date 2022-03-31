"""
https://blog.csdn.net/qq_41500249/article/details/106244810
https://blog.csdn.net/u010758410/article/details/79737498

sort在Python中存在两种形式，分别是sorted(str)，另一种是list.srot()

sort函数是针对列表的，不改变原有的列表

sorted()函数是Python的内置函数，具体形式为sorted(iterable, cmp=None, key=None, reverse=False)，
   iterable是可迭代对象，包括列表、元组、字典、字符串；
   cmp代表比较函数；
   key代表迭代对象中的某个属性，如某个元素的下标；
   reverse代表升序或者降序

"""
from functools import cmp_to_key

# 名字，成绩，年龄
students = [('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]
# 根据 年龄 升序
print ("根据年龄升序:", sorted (students, key = lambda x: x[2]))
# 根据 年龄 降序
print ("根据年龄降序:", sorted (students, key = lambda x: x[2], reverse = True))
