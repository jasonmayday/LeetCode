# 如果用dict 实现，只需要一个“名字”-“成绩”的对照表
info = {'math': 95, 'phys': 90, 'chem': 85}
print ( info ['math'])

# 把数据放入dict 的方法，除了初始化时指定外，还可以通过key放入：
info ['chinese'] = 88
print ( info ['chinese'])

#由于一个key 只能对应一个value，所以，多次对一个key 放入value，后面的值会把前面的值冲掉：
info ['chinese'] = 94
print ( info ['chinese'])

# 如果key 不存在，dict 就会报错：
# print ( info ['history'])

# 要避免key 不存在的错误，有两种办法:
    # 通过in判断key是否存在
print ('history' in info )

    # 通过dict 提供的get()方法，如果key不存在，可以返回None，或自己指定的value:
print ( info .get ('history'))
print ( info .get ('history', -1))

# 要删除一个key，用pop(key)方法，对应的value 也会从dict 中删除：
# 请务必注意：dict 内部存放的顺序和key 放入的顺序没有关系，也就是dict 是无序的。
info .pop('chem')
print ( info )

