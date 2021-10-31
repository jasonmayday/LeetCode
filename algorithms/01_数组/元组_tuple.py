'''
元组也是Python 内置的一种数据类型，也是一种有序的集合。
tuple和list 非常类似，但tuple 一旦初始化就不能修改。
• 它不能改变，没有append(), insert()这样的方法。
• 其他获取元素的方法和list 是一样的，你可以正常地使用courses[0], courses[-1]，但不能赋值成另外的元素。
因为tuple 不可变，所以代码更安全。如果可能，能用tuple 代替list 就尽量用tuple。
'''
courses = ('math', 'phys', 'chem')

# 定义只有一个元素的tuple:
tuple4 = (1, )

# 可变的tuple
t = ('a', 'b', ['A', 'B'])
print (t)

t [2][0] = 'X'
t [2][1] = 'Y'
print (t)