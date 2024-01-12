'''
set 和dict 类似，也是一组key 的集合，但不存储value。由于key不能重复，所以，在set 中，没有重复的key。

set 和 dict 的唯一区别仅在于没有存储对应的value，但是，set 的原理和dict 一样，所以，同样不可以放入可变对象.

因为无法判断两个可变对象是否相等，也就无法保证set 内部“不会有重复元素”。
'''


# 创建一个set，用花括号：
s1 = {1, 2, 3}
print (type(s1))
print (s1)

# 创建一个set，
    # 提供一个list 作为输入集合：
s2 = set ([1, 2, 3])
print (type(s2))
print (s2)

# 重复元素在set 中自动被过滤：
s3 = {1, 1, 2, 2, 3, 3}
print (s3)
{1, 2, 3}

# 通过add(key)方法可以添加元素到set 中，可以重复添加，但不会有效果：
s3.add (4)
print (s3)
s3.add (4)
print (s3)

# 通过remove(key)方法可以删除元素：
s3. remove (4)
print (s3)

# set 可以看成数学意义上的无序和无重复元素的集合，因此，两个 set 可以做数学意义上的交集、并集等操作：
s1 = {1, 2, 3}
s2 = set ([2 , 3, 4])
print (s1 & s2)
print (s1 | s2)