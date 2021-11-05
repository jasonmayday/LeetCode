# Python序列的运算
'''
运算名  运算符   解释
索引    []      取序列中的某个元素
连接    +       将序列连接在一起
重复    *       重复次连接
成员    in      询问序列中是否有某元素
长度    len     询问序列的元素个数
切片    [:]     取出序列的一部分
'''
#Python列表提供的方法
'''
方法名      用法                     解释
append      alist.append(item)      在列表末尾添加一个新元素
insert      alist.insert(i,item)    在列表的第个位置插入一个元素
pop         alist.pop()             删除并返回列表中最后一个元素
pop         alist.pop(i)            删除并返回列表中第个位置的元素
sort        alist.sort()            将列表元素排序
reverse     alist.reverse()         将列表元素倒序排列
del         del alist[i]            删除列表中第个位置的元素
index       alist.index(item)       返回item第一次出现时的下标
count       alist.count(item)       返回item在列表中出现的次数
remove      alist.remove(item)      从列表中移除第一次出现的item
'''

# Python字符串提供的方法
'''
方法名       用法                    解释
center      astring.center(w)       返回一个字符串，原字符串居中，使用空格填充新字符串，使其长度为w
count       astring.count(item)     返回item出现的次数
ljust       astring.ljust(w)        返回一个字符串，将原字符串靠左放置并填充空格至长度w
rjust       astring.rjust(w)        返回一个字符串，将原字符串靠右放置并填充空格至长度w
lower       astring.lower()         返回均为小写字母的字符串
upper       astring.upper()         返回均为大写字母的字符串
find        astring.find(item)      返回item第一次出现时的下标
split       astring.split(schar)    在schar位置将字符串分割成子串
'''

# Python集支持的运算
'''
运算名      运算符                   解释
成员        in                      询问集中是否有某元素
长度        len                     获取集的元素个数
\|          aset \| otherset        返回一个包含aset与otherset所有元素的新集
&           aset & otherset         返回一个包含aset与otherset共有元素的新集
-           aset - otherset         返回一个集，其中包含只出现在aset中的元素
<=          aset <= otherset        询问aset中的所有元素是否都在otherset中
'''

# Python集提供的方法
'''
方法名          用法                             解释
union           aset.union(otherset)            返回一个包含aset和otherset所有元素的集
intersection    aset.intersection(otherset)     返回一个仅包含两个集共有元素的集
difference      aset.difference(otherset)       返回一个集，其中仅包含只出现在aset中的元素
issubset        aset.issubset(otherset)         询问aset是否为otherset的子集
add             aset.add(item)                  向aset添加一个元素
remove          aset.remove(item)               将item从aset中移除
pop             aset.pop()                      随机移除aset中的一个元素
clear           aset.clear()                    清除aset中的所有元素
'''

# Python字典支持的运算
'''
运算名          运算符                   解释
[]              myDict[k]               返回与k相关联的值，如果没有则报错
in              key in adict            如果key在字典中，返回True，否则返回False
del             del adict[key]          从字典中删除key的键–值对
'''

# Python字典提供的方法
'''
方法名           用法                    解释
keys            adict.keys()            返回包含字典中所有键的dict_keys对象
values          adict.values()          返回包含字典中所有值的dict_values对象
items           adict.items()           返回包含字典中所有键–值对的dict_items对象
get             adict.get(k)            返回k对应的值，如果没有则返回None
get             adict.get(k, alt)       返回k对应的值，如果没有则返回alt
'''

# 格式化字符串可用的类型声明
'''
字符            输出格式
d、i            整数
u               无符号整数
f               m.dddd格式的浮点数
e               m.dddde+/-xx格式的浮点数
E               m.ddddE+/-xx格式的浮点数
g               对指数小于-4或者大于5的使用%e，否则使用%f
c               单个字符
s               字符串，或者任意可以通过str函数转换成字符串的Python数据对象
%               插入一个常量%符号
'''

# 格式化修改符
'''
修改符          例子            解释
数字            %20d            将值放在20个字符宽的区域中
-               %-20d           将值放在20个字符宽的区域中，并且左对齐
+               %+20d           将值放在20个字符宽的区域中，并且右对齐
0               %020d           将值放在20个字符宽的区域中，并在前面补上0
.               %20.2f          将值放在20个字符宽的区域中，并且保留小数点后2位
(name)          %(name)d        从字典中获取name键对应的值格
'''