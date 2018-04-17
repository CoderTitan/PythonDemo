

# 字符串
"""字符串

str = 'Hello Python'

# 1. 输出完整字符串
print("完整字符串--" + str)
# 结果输出:

# 2. 输出第一个字符
print("第一个字符--" + str[0])

# 3. 输出第三到七个字符
print("第3-7个字符--" + str[2:6])

# 4. 输出低2个字符开始的所有字符
print("第2个开始的所有字符--" + str[1:])

# 5. 拼接字符串
# 像上面一样, 字符串用 `+`拼接
print("拼接--" + str)

# 6. 输出3次
# `*` 表示重复操作, 需要重复操作几次, 后面跟上次数即可
print(str * 3)

# 7. 输出最后一个字符
print("最后一个字符--" + str[-1])

# 8. 输出倒数第二个字符
print("倒数第二个字符--" + str[-2])

"""


# List 列表
"""List 列表

list1 = [12, 34, 3.14, 5.3, 'titan']
list2 = [10, 'jun']

# 1.完整列表
print(list1)

# 2.列表第一个元素
print(list1[0])

# 3.获取第2-3个元素
print(list1[1:2])

# 4.获取第三个到最后的所有元素
print(list1[2:])

# 5.获取最后一个元素
print(list1[-1])

# 6.获取倒数第二个元素
print(list1[-2])

# 7.获取最后三个元素
print(list1[-3:-1])

# 8.合并列表
print(list1 + list2)

# 9.重复操作两次
print(list2 * 2)

"""


# 元组
"""元组

tuple1 = (12, 34, 3.14, 5.3, 'titan')
tuple2 = (10, 'jun')

# 1.完整元组
print(tuple1)

# 2.元组一个元素
print(tuple1[0])

# 3.获取第2-3个元素
print(tuple1[2:3])

# 4.获取第三个到最后的所有元素
print(tuple1[2:])

# 5.获取最后一个元素
print(tuple1[-1])

# 6.获取倒数第二个元素
print(tuple1[-2])

# 7.获取最后三个元素
print(tuple1[-3:-1])

# 8.合并元组
print(tuple1 + tuple2)

# 9.重复操作两次
print(tuple2 * 2)

# 因元组的元素是只读的, 不能二次赋值, 所以请注意, 以下写法是错误的
# 运行会报错: TypeError: 'tuple' object does not support item assignment
# tuple2[0] = 20
# tuple2[1] = "titan"

"""


# 字典
'''字典

dict1 = {'name': 'jun', 'age': 18, 'score': 90.98}
dict2 = {'name': 'titan'}

# 完整字典
print(dict2)

# 1.修改或添加字典元素
dict2['name'] = 'brother'
dict2['age'] = 20
dict2[3] = '完美'
dict2[0.9] = 0.9
print(dict2)

# 2.根据键值获取value
print(dict1['score'])

# 3.获取所有的键值
print(dict1.keys())

# 4.获取所有的value值
print(dict1.values())

# 5.删除字典元素
del dict1['name']
print(dict1)

# 6.清空字典所有条目
dict1.clear()
print(dict1)

# 7.删除字典
dict3 = {2: 3}
del dict3
# print(dict3)

'''


# 集合
'''集合

s = {1, 2, 3, 4}

# 1. 输出
print(s)

# 2. 用set转化已存在的类型, 可以去重
# 集合不会存在相同的元素
myList = [1, 2, 3, 3, 4, 4, 4]
mySet = set(myList)
print(mySet)

# 3. 添加元素(已经存在的元素, 无法添加)
mySet.add(2)
print(mySet)
mySet.add(6)
print(mySet)

# 4.删除元素
mySet.remove(2)
print(mySet)

# 5.方法difference
set1 = {1, 2, 4}
set2 = {1, 2, 5, 6}
# 用set1和set2做difference
diff = set1.difference(set2)
print(diff)
# 输出: {4}

# 用set2和set1做difference
diff2 = set2.difference(set1)
print(diff2)
# 输出: {5, 6}

# 6. 返回相同的元素
inter = set1.intersection(set2)
print(inter)
# 输出: {1, 2}

# 7.合并集合
union1 = set1.union(set2)
print(union1)
# 输出: {1, 2, 4, 5, 6}

'''


# 数据类型转换
'''

# 数据类型转换
dic = {'name': 'jun', 'age': 18}
# 1.将x转换为一个整数
print(int(9.89))
print(int('9'))
# print(int('8.89')) # 这样的写法会报错

# 2.创建一个复数
print(complex(1, 2))
print(complex('3'))
print(complex(-2, -4))

# 3.转换为一个浮点型
print(float(9))
print(float('12.45'))

# 4.转换为字符串
print(str(9))
print(str(9.09))
print(str('89'))
print(str(dic))

# 5.转换为表达式字符串
print(repr(9.09))
print(repr(9 + 10))
print(repr(dic))

# 6.用来计算在字符串中的有效Python表达式,并返回一个对象
print(eval('3*9'))
print(eval("dic['age']*2"))

# 7.将序列转换为一个元组
list7 = [1, 2, 3]
print(tuple(list7))

# 8.将序列转换为一个列表
tuple8 = ('a', 's', 'd')
print(list(tuple8))

# 9.转换为可变集合
print(set(list7))

# 10.创建一个字典
dic10 = dict([('name', 'titan'), ('age', 17)])
print(dic10)

# 11.转换为不可变集合
print(frozenset({1, 2}))

# 12.将一个整数转换为一个字符
# 48对应字符'0'(参照ASCII码表)
print(chr(122))

# 13.将一个字符转换为它的整数值
print(ord('0'))

# 14.将一个整数转换为一个十六进制字符串
print(hex(10))

# 15.将一个整数转换为一个八进制字符串
print(oct(10))

'''






