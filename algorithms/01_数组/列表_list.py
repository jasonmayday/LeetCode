

courses = ['math', 'phys', 'chem']
print (courses)

# 用len()函数获取列表中元素的个数
print (len(courses))

# 用索引来访问列表中每一个位置的元素，记住索引从0 开始
print (courses[0])
print (courses[1])
print (courses[2])

# 向列表末尾追加元素，用append()方法：
courses.append ('biology')
print (courses)

# 把元素插入到指定的位置，用insert()方法：
courses.insert(1, 'history')
print (courses)

# 删除列表末尾的元素，用pop()方法：
courses.pop()
print (courses)

# 删除指定位置的元素，用pop(i)方法，其中i为索引位置：
courses.pop(1)
print (courses)

# 把某个元素替换成别的元素，可以直接赋值给对应的索引位置：
courses [1] = 'chinese'
print (courses)